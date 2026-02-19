# Investigation: API Response Validation Mismatch

## Summary
API tests intermittently failed due to unexpected response structure differences between successful and error responses.

## Observed Behavior
- Positive test cases passed consistently
- Negative scenarios failed assertion validation
- Response schema differed from expected structure

## Investigation Steps
- Captured failing responses using Postman console
- Inspected network responses via Chrome DevTools
- Compared successful vs error payload structures
- Reviewed assertion logic within Postman test scripts

## Root Cause
Assertions assumed a consistent response schema across both success and failure responses.

Error responses returned alternate payload structures that were not accounted for in validation logic.

## Resolution
Updated assertions to validate conditionally based on response status code rather than assuming uniform schema structure.

## Verification
- Positive and negative scenarios executed successfully
- Assertions correctly validated both response types
- Collection execution completed without false failures

## QA Takeaway
Reinforced the importance of validating API behavior rather than assuming consistent response models across execution paths.