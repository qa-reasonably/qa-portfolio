# Console Error Investigation

## Scenario
A UI action failed without visible user feedback.

## Investigation
Using the Console panel, I observed:
- JavaScript error messages
- Correlation with a failed network request

## Evidence
![Console error](screenshots/console-error.png)
![Related network failure](screenshots/console-network.png)

## Findings
- Frontend error surfaced due to backend failure
- Stack trace pointed to failed API response handling

## QA Impact
Console errors help distinguish frontend vs backend ownership during triage.


