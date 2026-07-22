## Overview

This repository contains an end-to-end UI automation framework for the Automation Exercise web application using **Playwright (Python)** and **Pytest**.

The project is designed following industry-standard automation practices with a focus on maintainability, scalability, code reusability, and reliable test execution.

---

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Git & GitHub

---

## Framework Features

- Page Object Model (POM)
- Reusable Page Classes
- Reusable Utility Methods
- Explicit Assertions
- Stable Locators
- Modular Test Structure
- Easy Test Maintenance
- Cross-browser Support
- Headless & Headed Execution
- Screenshot Support (Failure Ready)
- Pytest Test Discovery

---

## Project Structure

```
project/
│
├── pages/
├── tests/
├── utils/
├── fixtures/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Automated Test Scenarios

Examples include:

- User Login
- Invalid Login Validation
- Logout
- Register New User
- Product Search
- Product Details Verification
- Add Product to Cart
- Remove Product from Cart
- Update Cart Quantity
- Checkout Flow
- Order Placement
- Contact Us Form
- Subscription Verification

---

## Design Principles

- Maintainable Architecture
- Clean Code
- Reusable Components
- Minimal Code Duplication
- Readable Test Cases
- Easy Future Scalability

---

## Getting Started

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

### Run Tests

```bash
pytest
```

### Run in Headed Mode

```bash
pytest --headed
```

---

## Future Improvements

- HTML Reporting
- Allure Reporting
- CI/CD Integration (GitHub Actions)
- Parallel Execution
- Data-driven Testing
- API + UI Integration Testing

---

## Author

**Iffat Jahan Suchi**

Software Quality Assurance Engineer

Playwright | Python | Pytest | UI Automation | Manual Testing
