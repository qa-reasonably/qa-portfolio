# Authentication Token Analysis

## Scenario
Testing login/logout behavior to confirm authentication state handling.

## Investigation
Using the Application panel, I inspected:
- Cookies
- Local storage
- Session storage

## Evidence
![Token present](screenshots/token-present.png)
![Token cleared](screenshots/token-cleared.png)

## Findings
- Auth token was correctly set on login
- Token was removed on logout (expected behavior)

## QA Impact
Improper token lifecycle handling can cause security and session-related defects.


