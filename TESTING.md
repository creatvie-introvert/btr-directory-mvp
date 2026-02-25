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
| Browse cities | Navigate to cities index | Pass | [View evidence &mdash; Cities Index](docs/testing/screenshots/cities-index-desktop.jpeg) |
| View developments in a city | Select city → view listings | Pass | [View evidence &mdash; City Listings](docs/testing/screenshots/city-developments-list-desktop.jpeg) |
| View development details | Open development page | Pass | [View evidence &mdash; Development Detail ](docs/testing/screenshots/development-detail-top-desktop.jpeg) |
| View images | Check images load correctly | Pass | Cloudinary images displayed |
| Submit enquiry | Complete and submit form | Pass | Enquiry appears in dashboard |
| Recieve confirmation | Redirect to confirmation page | Pass | Confirmation screenshot |

### Staff User (Dashboard)

| User Story | Test | Result | Evidence |
|------------|------|--------|----------|
| View enquiires | Access dashboard list | Pass |  Dashboard screenshot |
| Update status | Change status via dropdown | Pass | Status updates in UI |
| Forward enquiry | Click forward button | Pass | Mail client opens |
| Close enquiry | Click close button | Pass | Status changes to closed |
| Delete enquiry | Use delete confirmation flow | Pass | Enquiry removed from DB |

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

Accessibility Testing

Accessibility was tested using:
- Chrome Lighthouse
- Keyboard navigation
- Manual semantic review

### Accessibility checks

| Check | Result | Notes |
|-------|--------|-------|
|Semantic HTML |  |  |
| Heading hierachy | Pass | Logical order maintained |
| Alt text | Pass | All images include descriptive alt text |
| Form labels | | |
| Keyboard navigation | Pass | Forms and button accessible via tab |
| Colour contrast | | |
|ARIA usage | Pass | Used only where necessary |

### Lighthouse Accessibility Score

- **Mobile:**
- **Desktop:**

---

## Responsive Testing

| Page | Mobile | Tablet | Desktop | Result |
|------|--------|--------|---------|--------|
| Home | [x] | [x] | [x] | Pass |
| Cities | [x] | [x] | [x] | Pass |
| Listings | [x] | [x] | [x] | Pass |
|Detail | [x] | [x] | [x] | Pass |
|Form | [x] | [x] | [x] | Pass |
|Dashboard | [x] | [x] | [x] | Pass |

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

- **Performance:** 
- **Accessibility:** 
- **Best Practice:** 
- **SEO:** 

### Desktop

- **Performance:** 
- **Accessibility:** 
- **Best Practice:** 
- **SEO:** 

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