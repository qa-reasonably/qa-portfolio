# Network Debugging with Chrome DevTools

## Scenario
A UI action appeared successful, but the backend response indicated a failure.

## Investigation
Using the Network tab (XHR/Fetch), I captured:
- Request method and endpoint
- Headers and payload
- Response body and status code

## Evidence
![Successful request](screenshots/network-success.png)
![Failed request](screenshots/network-failure.png)

## Findings
- UI feedback did not reflect API failure
- Error was identifiable only through Network inspection

## QA Impact
This issue could be reproduced and validated via Postman, enabling faster root-cause analysis.


