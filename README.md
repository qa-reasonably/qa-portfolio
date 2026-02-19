# QA Portfolio

This repository showcases hands-on QA practice across manual testing, API testing, and test automation.

## Focus Areas
- Chrome DevTools investigation and defect analysis
- API testing with Postman
- UI automation with Playwright
- Learning visual testing with Applitools (TAU course)

## Contents
- `devtools/` - UI, API, and auth investigation using Chrome DevTools
- `api-testing/postman/` - API collections, environments, and assertions
- `automation/` - automation examples
- `playwright-tests/` - Playwright test specs and related assets

## Tooling Note (Security Audit)
This repo is a learning portfolio, not a production application.

`npm audit` may report vulnerabilities from transitive dev dependencies pulled in by `@applitools/eyes-playwright` (used for TAU visual testing exercises). These packages are used only for local/CI test tooling in this project.

## Run Tests
```bash
npm install
npm test
```
