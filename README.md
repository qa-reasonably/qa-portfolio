# QA Portfolio

This repository documents hands-on Quality Assurance work across UI investigation, API testing, and automated regression execution.

The goal of this portfolio is to demonstrate practical testing workflow, tooling familiarity, and defect analysis using real QA techniques rather than theoretical examples.

---

## Scope of Work

### UI & Network Investigation
- Chrome DevTools used for:
  - Network request inspection
  - API response validation
  - Authentication and session analysis
  - Frontend behavior investigation
- Manual validation of application behavior through browser inspection

---

### API Testing (Postman)

API testing performed against a public REST service to demonstrate realistic testing scenarios without proprietary data exposure.

#### Covered Scenarios
- API health validation
- CRUD operations
- Positive and negative test cases
- Status code verification
- Response validation
- Authentication behavior testing

#### Testing Approach
- Requests validated through:
  - Postman execution
  - Browser network inspection via Chrome DevTools
- Environment variables used for reusable test configuration
- JavaScript assertions implemented within Postman tests

ReqRes API was selected to simulate real-world REST behavior including authentication handling and error responses.

---

### Automated API Regression

Postman collections are executed headlessly using **Newman** with Python orchestration to simulate automated regression testing.

#### Execution
```bash
python api-testing/python-automation/run_with_newman.py
```

#### Output
Machine-readable regression reports are generated under:

```
api-testing/postman/reports/
```

---

## Repository Structure

```
devtools/
  UI and network investigation examples

api-testing/
  postman/
    collections
    environments
    reports
  python-automation/
    Newman execution scripts
```

---

## Tooling Used

- Postman
- Newman
- Python
- Chrome DevTools
- JavaScript (Postman test assertions)
- Node.js

---

## Running Tests Locally

Install Newman:

```bash
npm install -g newman
```

Run automated API regression:

```bash
python api-testing/python-automation/run_with_newman.py
```

---

## Tooling & Security Note

This repository is a QA learning and demonstration environment, not a production application.

Dependency vulnerability warnings (for example via `npm audit`) may originate from third-party testing tooling used locally for experimentation and do not impact production systems.

---

## Purpose

This portfolio represents applied QA workflow including:
- Test investigation
- API validation
- Regression execution
- Evidence-driven testing practices

All work shown reflects hands-on execution rather than generated examples.

## Investigations

Documented QA investigations and root-cause analyses can be found under:

investigations/