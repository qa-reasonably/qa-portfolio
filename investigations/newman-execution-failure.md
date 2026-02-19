# Investigation: Newman Regression Execution Failure

## Summary
Automated API regression execution failed when running Postman collections through Newman despite successful execution within Postman.

## Observed Behavior
- Collection executed successfully inside Postman
- Newman execution terminated early
- No regression reports generated
- CLI output indicated environment resolution issues

## Investigation Steps
- Verified collection functionality in Postman Collection Runner
- Executed Newman manually via CLI
- Compared runtime differences between Postman and Newman execution
- Reviewed environment variable usage within requests and tests

## Root Cause
Newman execution did not automatically inherit the Postman environment configuration used during manual execution.

Required environment variables were not explicitly passed during automated execution.

## Resolution
Updated execution command to include the required environment file during Newman runtime.

## Verification
- Newman execution completed successfully
- All assertions executed
- Regression reports generated under:
  api-testing/postman/reports/

## QA Takeaway
Validated differences between manual and headless API execution environments and ensured regression runs remain reproducible outside the UI.