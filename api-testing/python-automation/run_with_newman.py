import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_COLLECTION_NAME = "Auth_Flows.postman_collection.json"
DEFAULT_ENV_NAME = "reqres-env.postman_environment.json"


def find_default_files(base_dir: Path):
    collections_dir = base_dir / "postman" / "collections"
    envs_dir = base_dir / "postman" / "environments"

    # Prefer explicit defaults
    environment = envs_dir / DEFAULT_ENV_NAME
    if not environment.exists():
        # Fallback environment: first matching file
        env_matches = sorted(envs_dir.glob("*.postman_environment.json"))
        environment = env_matches[0] if env_matches else None

    collection = collections_dir / DEFAULT_COLLECTION_NAME
    if not collection.exists():
        # Fallback collection: first matching file
        matches = sorted(collections_dir.glob("*.postman_collection.json"))
        collection = matches[0] if matches else None

    return collection, environment


def run_newman(collection_path: Path, environment_path: Path | None, out_dir: Path) -> Path:
    if shutil.which("newman") is None:
        raise RuntimeError(
            "Newman not found on PATH.\n"
            "Install it with: npm install -g newman\n"
            "Then open a NEW terminal and try again."
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = out_dir / f"newman_report_{timestamp}.json"

    cmd = [
        "newman", "run", str(collection_path),
        "--reporters", "json",
        "--reporter-json-export", str(report_path),
    ]

    if environment_path is not None:
        cmd.extend(["-e", str(environment_path)])

    print("Running:", " ".join(cmd))
    completed = subprocess.run(" ".join(cmd), capture_output=True, text=True, shell=True)

    if completed.stdout:
        print("\n--- newman stdout ---")
        print(completed.stdout)
    if completed.stderr:
        print("\n--- newman stderr ---")
        print(completed.stderr)

    if completed.returncode != 0:
        print(f"\nNewman exited with code {completed.returncode} (tests likely failed).")

    if not report_path.exists():
        raise RuntimeError("Newman did not produce a JSON report. Check stdout/stderr above.")

    return report_path


def summarize_report(report_path: Path) -> int:
    """Returns number of failed assertions (0 means green)."""
    with report_path.open("r", encoding="utf-8") as f:
        report = json.load(f)

    run = report.get("run", {})
    stats = run.get("stats", {})

    assertions = stats.get("assertions", {})
    requests = stats.get("requests", {})

    total_assert = assertions.get("total", 0)
    failed_assert = assertions.get("failed", 0)
    total_req = requests.get("total", 0)
    failed_req = requests.get("failed", 0)

    print("\n=== SUMMARY ===")
    print(f"Report: {report_path}")
    print(f"Requests:   {total_req} total, {failed_req} failed")
    print(f"Assertions: {total_assert} total, {failed_assert} failed")

    failures = run.get("failures", [])
    if failures:
        print("\n=== FAILURES (first 25) ===")
        for i, fail in enumerate(failures[:25], start=1):
            source = fail.get("source", {})
            request_name = source.get("name") or source.get("request", {}).get("name") or "<unknown request>"
            error = fail.get("error", {})
            message = error.get("message") or str(error) or "<no message>"
            print(f"{i:02d}. {request_name} -> {message}")

        if len(failures) > 25:
            print(f"... and {len(failures) - 25} more")
    else:
        print("\nNo failures reported. ✅")

    return failed_assert


def main():
    parser = argparse.ArgumentParser(description="Run Postman collections via Newman and print a summary.")
    parser.add_argument("--collection", help="Path to a Postman collection JSON file", default=None)
    parser.add_argument("--env", help="Path to a Postman environment JSON file (optional)", default=None)
    args = parser.parse_args()

    # Script location: .../api-testing/python-automation/run_with_newman.py
    script_dir = Path(__file__).resolve().parent

    # Base dir we want: .../api-testing
    base_dir = script_dir.parent

    # Helpful debug line (keep or delete)
    print("BASE DIR:", base_dir)

    default_collection, default_env = find_default_files(base_dir)

    collection_path = Path(args.collection).resolve() if args.collection else (default_collection.resolve() if default_collection else None)
    env_path = Path(args.env).resolve() if args.env else (default_env.resolve() if default_env else None)

    if collection_path is None or not collection_path.exists():
        raise FileNotFoundError(
            "Could not find a Postman collection.\n"
            "Either pass --collection <path> or ensure you have:\n"
            f"  {base_dir / 'postman' / 'collections'}"
        )

    out_dir = base_dir / "postman" / "reports"
    report_path = run_newman(collection_path, env_path if env_path and env_path.exists() else None, out_dir)

    failed = summarize_report(report_path)
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()