# DOM Selector Strategy Using Chrome DevTools

## Scenario
While inspecting a login/form page, I evaluated element selectors to determine automation stability.

## Investigation
Using the Elements panel, I identified:
- A dynamically generated ID that would cause flaky tests
- A stable attribute suitable for long-term automation

## Evidence
![Bad selector](screenshots/bad-selector.png)
![Good selector](screenshots/good-selector.png)

## Findings
- Dynamic IDs and index-based XPaths are brittle
- Attributes like name, aria-label, or data-* are preferred

## QA Impact
Choosing stable selectors reduces automation flakiness in Selenium and Playwright tests.


