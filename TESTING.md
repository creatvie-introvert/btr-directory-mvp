# Testing Documentation

This document defines the testing approach for **BTR Directory — MVP**.  
It is intentionally set up **before testing is carried out**, so results and evidence can be added quickly and consistently during development.

## How to use this file

- Run each test case in the tables below
- Update **Result** to `Pass` / `Fail` / `Blocked`
- Add a short **Notes / Fix** summary (especially for failures)
- Add an **Evidence** link (screenshot path or URL) for anything meaningful (forms , errors, responsiveness, accessibility, bugs)

## Test environment

| Item | Planned |
|------|---------|
| Local testing URL | `http://127.0.0.1:8000/` |
| Deployed testing URL | _Add Heroku URL_ |
| Database | PostgreSQL (local + production) |
| Media storage | Cloudinary |
| Devices | Mobile, tablet, and desktop viewport emulations |
| Breakpoints tested | 390px, 768px, 1440px |
| Browsers tested | Chrome, Firefox, Safari |

## Testing Status

| Area | Status | Notes |
| Manual user story testing | Not started |   |
| Forms and validation | Not started |   |
| Responsiveness | Not started |   |
| Browser compatibility | Not started |   |
| Accessibility checks | Not started |   |
| HTML / CSS validation | Not started |   |
| Lighthouse reports | Not started |   |
| Bugs and fixes | Not started |   |

## User story coverage

The tables below map each user story defined in the README to the corresponding test cases in  this document. This provides clear traceability between **user requirements** and **testing evidence**.

### Primary user stories (Renters)

**Note:** The table below maps each user story defined in the README to the corresponding test cases in this document. This provides full traceability between **user requirements** and **testing evidence**.

R-01 (Home page loads) is treated as a baseline smoke test and is not mapped to a specific user story, as it supports all renter journeys.

| User story | Test case reference(s) | Result | Evidence | Notes / Fix |
|------------|------------------------|--------|----------|-------------|
|As a user, I want to browse cities so that I can quickly narrow my search by location | R-02, R-03 |   |   |   |
| As a user, I want to view a list of developments within a city so that I can compare available options | R-03, R-04 |   |   |   |
| As a user, I want to view detailed information about a development so that I can decide if it meets my needs | R-05 |   |   |   |
| As a user, I want to view images of a development so that I can better understand the space and environment | R-05, R-06 |   |   |   |
| As a user, I want to submit an enquiry so that I can request more information or express interest | R-07, R-08, R-09 |   |   |   |
| As a user, I want to access clear legal and trust information so that I understand the purpose and limitations of the site | R-10 |   |   |   |

### Secondary user stories (Staff workflow)

**Note:** S-02 (View enquiry detail) is treated as a supporting test case and is not mapped to a standalone user story, as it enables staff actions such as updating status, forwarding, and deletion.

| User story | Test case reference(s) | Result | Evidence | Notes / Fix |
|------------|------------------------|--------|----------|-------------|
| As a user, I want to view all enquiries in one place so that I can manage incoming leads efficiently | S-01 |   |   |   |
| As a user, I want update the status of an enquiry so that I can track and follow progress | S-03 |   |   |   |
| As a user, I want to forward enquiries to the relevant operator so that leads are delivered quickly and accurately | S-04 |   |   |   |
| As a user, I want to delete enquiries when appropriate so that data can be managed responsibly | S-05 |   |   |   |

## Manual test cases

### Renter journey test cases

| ID | Page / Feature | Steps | Expected result | Result | Evidence | Notes / Fix |
|----|----------------|-------|-----------------|--------|----------|-------------|
| R-01 | Home page loads | Navigate to `/` | Home page loads without errors |   |   |   |
| R-02 | Cities index | Navigate to Cities page | Cities index loads correctly |   |   |   |
| R-03 | City selection | Select a city | City developments page loads |   |   |   |
| R-04 | Development card | Click development card | Development detail page opens |   |   |   |
| R-05 | Development content | Review development detail | Content displays clearly |   |   |   |
| R-06 | Development images | Load image gallery | Images load from Cloudinary |   |   |   |
| R-07 | Enquiry form access | Click enquiry | Enquiry form loads |   |   |   |
| R-08 | Enquiry submission | Submit valid form | Enquiry submitted successfully |   |   |   |
| R-09 | Enquiry validation | Submit invalid form | Validation errors shown |   |   |   |
| R-10 | Legal pages | Visit trust/legal pages | Pages load correctly |   |   |   |

### Staff / admin workflow test cases

| ID | Page / Feature | Steps | Expected result | Result | Evidence | Notes / Fix |
|----|----------------|-------|-----------------|--------|----------|-------------|
| S-01 | Enquiries list | Open staff dashboard | Enquiries list displays |   |   |   |
| S-02 | Enquiry detail | Open enquiry | Enquiry detail displays |   |   |   |
| S-03 | Update status | Change enquiry status | Status persists |   |   |   |
| S-04 | Forward enquiry | Trigger mailto action | Email client opens with data |   |   |   |
| S-05 | Delete enquiry | Delete enquiry | Enquiry removed |   |   |   |

## Responsiveness testing

| Page | 390px | 768px | 1440px | Issues | Evidence | Notes / Fix |
|------|-------|-------|--------|--------|----------|-------------|
| Home |   |   |   |   |   |   |
| Cities index |   |   |   |   |   |   |
| City developments |   |   |   |   |   |   |
| Development detail |   |   |   |   |   |   |
| Enquiry form |   |   |   |   |   |   |

## Accessibility testing

| Check | Expected Outcome | Result | Evidence | Notes / Fix |
|-------|------------------|--------|----------|-------------|
| Keyboard navigation | Logical tab order |   |   |   |
| Focus visibility | Focus states visible |   |   |   |
| Form labels | Inputs have labels |   |   |   |
| Colour contrast | WCAG compliant |   |   |   |
| Heading structure | Logical hierarchy |   |   |   |

## Validation & performance

| Tool | Target | Result | Evidence | Notes |
|------|--------|--------|----------|-------|
| W3C HTML Validator | Key templates |   |   |   |
| W3C CSS Validator | Custom CSS |   |   |   |
| Lighthouse | Core pages |   |   |   |

## Bugs and fixes log

| ID  | Bug description | Steps to reproduce | Fix applied | Result | Evidence |
|-----|-----------------|--------------------|-------------|--------|----------|
| 001 |   |   |   |   |   |