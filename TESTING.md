# Testing &mdash; BTR Directory MVP

This document outlines the **manual testing process** carried out for the BTR Directory MVP.

Testing was conducted to validate: 
- User stories
- Core functionality
- Staff workflows
- Data integrity
- Responsiveness
- Accessibility

Testing was performed incrementally throughout development and finalise prior to submission.

---

## User Story Testing

### Primary User (Renter)

| User Story | Test | Result | Evidence |
|------------|------|--------|----------|
| Browse cities | Navigate to cities index | Pass | [Cities Index (Desktop)](docs/testing/screenshots/cities-index-desktop.jpeg) |
| View developments in a city | Select city → view listings | Pass | [City Listings (Desktop)](docs/testing/screenshots/city-developments-list-desktop.jpeg) |
| View development details | Open development page | Pass | [Development Detail (Desktop)](docs/testing/screenshots/development-detail-info-desktop.jpeg) |
| View images | Check images load correctly | Pass | [Gallery Interaction (Desktop)](docs/testing/screenshots/development-detail-top-desktop.jpeg) |
| Submit enquiry | Complete and submit form | Pass | [Enquiry form submission](docs/testing/screenshots/enquiry-form-empty-desktop.jpeg) |
| Recieve confirmation | Redirect to confirmation page | Pass | [Confirmation page](docs/testing/screenshots/enquiry-confirmation-desktop.jpeg) |

### Staff User (Dashboard)

| User Story | Test | Result | Evidence |
|------------|------|--------|----------|
| View enquires | Access dashboard list | Pass |  [Dashboard list](docs/testing/screenshots/staff-enquiries-dashboard.jpeg) |
| Update status | Change status via dropdown | Pass | [Status update](docs/testing/screenshots/staff-enquiry-status-update.jpeg) |
| Forward enquiry | Click forward button | Pass | [Mailto trigger](docs/testing/screenshots/mailto.png) |
| Close enquiry | Click close button | Pass | [Closed status](docs/testing/screenshots/staff-enquiry-closed.jpeg) |
| Delete enquiry | Use delete confirmation flow | Pass | [Delete confirmation](docs/testing/screenshots/staff-enquiry-delete-confirmation.jpeg) |

---

## Feature Testing

### Homepage

| Test case | Expected result | Pass | Notes |
|-----------|-----------------|------|-------|
| Page loads | No errors      | [x]  |       |
| Search by city | Filtered results | [x] |  |
| Search by postcode | Results shown | [x] | |
| Invalid search | Empty state message | [x] | |
| Navigation links | Correct routing | [x] | |

### Cities Index

| Test case | Expected result | Pass | Notes |
|-----------|-----------------|------|-------|
| Active cities displayed | Only active records shown | [x] | |
| Cards clickable | Opens correct page | [x] | |

### Development Detail

| Test case | Expected result | Pass | Notes |
|-----------|-----------------|------|-------|
| Data accuracy | Matches database | [x] | |
| Amenities | Render correctly | [x] | |
| Images | Load via Cloudinary | [x] | |
| Alt text | Present | [x] | |

### Enquiry Form

| Test case | Expected result | Pass | Notes |
|-----------|-----------------|------|-------|
| Required fields | Validation errors | [x] | |
| Invalid email | Rejected | [x] | |
| Valid submission | Saved to DB | [x] | |
| Redirect | Confirmation page | [x] | |

### Dashboard (CRUD)

| Test case | Expected result | Pass | Notes |
|-----------|-----------------|------|-------|
| View enquiries | List displayed | [x] | |
| Update status | Persisted | [x] | |
| Forward | Mailto triggered | [x] | |
| Close | Status updated | [x] | |
| Delete | Removed after confirmation | [x] | |

---

## Accessibility Testing

Accessibility was tested using:
- Chrome Lighthouse
- WAVE (WebAIM accessibility evaluation tool)
- Keyboard navigation
- Manual semantic HTML and ARIA review

### Accessibility checks

| Check | Result | Notes |
|-------|--------|-------|
|Semantic HTML | Pass | Pages structured using appropiate semantic elements such as <section>, <nav>, <article>, and headings |
| Heading hierachy | Pass | Logical order maintained |
| Alt text | Pass | All images include descriptive alt text |
| Form labels | Pass | Explicit <label> added to search input (visually hidden but accesible to screen readers) |
| Keyboard navigation | Pass | Forms and button accessible via tab |
| Colour contrast | Partial | Majority of UI elements accessible via keyboard (tab, enter, focus states visible) |
|ARIA usage | Pass | Used only where necessary |

### Lighthouse Accessibility Score

- **Mobile:** 96
- **Desktop:** 96

Lighthouse audits indicate a high level of accessibility compliance, with no critical or blocking issues identified.

### Accessibility Limitations (Known Issues)

- **7 low contrast warnings** were identified using WAVE.
- These occur primarily in:
    - Hero section over background image
    - Footer text using brand colour palette

**Cause:**

- Background image variabilty affects contrast consistency
- Brand colour palette limits contrast options
- Bootstrap utility classes may override custom styles

**Mitigation steps taken:**

- Increased hero overlay opacity to improve readability
- Applied text-shadow colours to higher contrast variants
- Ensured all critical content remains readable

**Reason not fully reloved:**

- Fully resolving these warnings would require:
    - Redesigning the brand colour system or
    - Removing/replacing the image-based hero section

**Impact:**

- No blocking accessibility issues
- Core content remains readable and usable
- High Lghthouse accessibility score maintained

### Future Improvements

In a production environment, furtherimprovements could include:
- Dynamic contrast overlays based on background brightness
- Alternative non-image hero design for guaranteed contrast compliance
- Full WCAG 2.1 AA colour audit across all components

---

## Responsive Testing

| Page | Mobile | Tablet | Desktop | Result |
|------|--------|--------|---------|--------|
| Home | [x] | [x] | [x] | Pass |
| Cities | [x] | [x] | [x] | Pass |
| Listings | [x] | [x] | [x] | Pass |
| Detail | [x] | [x] | [x] | Pass |
| Form | [x] | [x] | [x] | Pass |
| Dashboard | [x] | [x] | [x] | Pass |

All layouts tested using DevTools and real devices.

---

## Data Integrity & Validation

| Check | Result | Notes |
|-------|--------|-------|
|Foreign keys | Pass | Enquiries linked correctly |
| Unique contraints | Pass | No duplicate unit types |
| Required fields | Pass | Validated at model + form level |
| Cascade deletion | Pass | No orphaned records |
| Indexed queries | Pass | Efficient filtering |

---

## Lighthouse

Full Lighthouse reports have been generated and stored for reference:

- **Mobile report:** [Mobile Lighthouse report](testing/lighthouse/lighthouse-report-mobile.pdf)
- **Mobile report:** [Desktop Lighthouse report](testing/lighthouse/lighthouse-report-desktop.pdf)

Lighthouse audits were conducted on both **mobile** and **desktop** views using Chrome DevTools to assess performance, accessibility, best practice, and SEO.

### Mobile

- **Performance:** 73
- **Accessibility:** 96
- **Best Practice:** 100
- **SEO:** 100

### Desktop

- **Performance:** 83
- **Accessibility:** 96
- **Best Practice:** 100
- **SEO:** 100

---

## HTML & CSS Validation

### HTML

- All key templates validated via W3C
- Errors fixed:
    - Heading hierarchy
    - Section labels
    - Invalid attributes

### CSS 

- No critical issues found

---

## JavaScript Testing

- No console errors detected
- All interactions behave as expected

---

## Screenshots (Evidence)

- Screenshots stored in:

```
doc/testing/screenshots
```

Include:
- Homepage
- Listings
- Detail page
- Dashboard
- Delete confirmation

---

## Known MVP Limitations

- Mailto-based forwarding
- No user accounts
- No advancedsearch filters
- Basic authentication only

---

## Testing Status

- Manual testing completed
- No blocking issues identified
- Ready for submission