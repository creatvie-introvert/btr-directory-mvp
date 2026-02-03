# Testing &mdash; BTR Directory MVP

This document outlines the **manual testing process** carried out for the BTR Directory MVP.
Testing was conducted to validate user stories, core functionality, staff workflows, responsiveness, and accessibility prior to final submission.

The sections below act as a **testing template**, and were completed incrementally as testing is performed.

---


## Public User (Renter) Journey Testing

### Homepage

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Homepage loads without errors | Page renders correctly | [x] |  |
| Hero heading and text visible | Content displayed correctly | [x] |  |
| Hero search input usabe | Input accepts text | [x] |  |
| Search by city name | Displays search results filtered by city | [x] | Search results filtered on the search returns   |
| Search by postcode | Displays search results filtered by postcode | [x] | Postcode and postcode-area searches resolve to the search results page showing matching developments. |
| Invalid search input | Graceful fallback or empty state | [x] | Search page loads with user-friendly no-results message. |
| Browse cities section visible | Section displays correctly | [x] |  |
| Navigation links work | Correct pages load | [x] |  |
| Footer links work | Correct pages load | [x] |  |
| Responsive layout | Layout adapts across breakpoints | [x] | Verified across mobile (390px), tablet (768px), and desktop (1440px) using browser dev tools. |

---

### Cities index page

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Cities index loads | Page renders correctly | [x] |  |
|Active cities displayed | All expected cities visible | [x] | Only cities marked as active in the admin are displayed. |
| City card shows name and image | Correct content shown | [x] |  |
| City card is clickable | Opens correct city listing | [x] |  |
| Responsive layout | Layout adapts across breakpoints | [x] | Verified at mobile (390px), tablet(768px), and desktop (1440px). |

---

### City development listing page

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| City development list loads | Correct city title shown | [x] |  |
| Developments filtered by city | Only relevant developments shown | [x] | Filtered based on city slug in URL. |
| Development card content | Name, image,  summary visible | [x] |  |
| Empty state handling | Clear messaging if no developments | [x] | User-friendly message displayed when no developments exist for a city. |
| Responsive layout | Layout adapts across breakpoints | [x] | Verified at mobile (390px), tablet(768px), and desktop (1440px). |

---

### Development detail page

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Detail page loads | No errors | [x] | Content matches database values for selected development. |
| Development data shown | Correct content displayed | [x] |  |
| Amenities visible | Amenities listed correctly | [x] | Amenities rendered from many-to-many relationship. |
| Images load | Images served from Cloudinary | [x] | Images successfully loaded from Cloudinary URLs. |
| Image alt text | Present and meaningful | [x] | Alt text present and descriptive for all images. |
| Enquiry CTA visible | Clear call-to-action shown | [x] |  |
| Responsive layout | Layout adapts across breakpoints | [x] | Verified at mobile (390px), tablet(768px), and desktop (1440px). |

---

### Enquiry form

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Enquiry form loads | Form visible | [x] |Page loads without console errors |
| Required field validation | Errors are shown on empty submit | [x] | Inline validation errors displpayed clearly |
| Invalid email rejected | Validation error displayed | [x] | Django email validation triggered on submit |
| Valid submission | Enquiry saved successfully | [x] | Enquiry appears in staff dashboard with status "New" |
| Redirect on success | User redirected to confirmation | [x] | Confirmation message displayed |
| Responsive layout | Layout adapts across breakpoints | [x] |  |

---

### Enquiry confirmation page

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Confirmation page loads | Success message visible | [] |  |
| Clear confirmation message | User informed of submission | [] |  |
| No sensitive data shown | Safe output | [] |  |
| Responsive layout | Layout adapts across breakpoints | [] | Verified at mobile (390px), tablet(768px), and desktop (1440px). |

---


## Staff / Admin Workflow Testing

### Authentication

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Dashboard protected | Unauthenticated users blocked | [x] | Redirected to login page. |
| Login page loads | Login form visible | [x] | Django suthentication from rendered. |
| Valid login | Access granted | [x] | Authenticated user redirected to dashboard. |
| Invalid login | Error message shown | [x] | Form-level error displayed without page crashhing. |

---

### Enquiry management

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Enquiry detail loads | Full enquiry visible | [x] | All submitted fields displayed corrreclty. |
| Status update | Status persists correctly | [x] | Status change saved to database and reflected in UI. |
| Forward action | Mail client opens with pre-filled content | [x] | Mailto link opens with subject and body populated. |
| Forward metadata saved | Timestamp and email stored | [x] | forwarded_at and forwarded_to_email saved on send. |
| Close enquiry | Status updated to closed | [x] | Closed status shown with updated badge. |
| Delete enquiry | Enquiry removed | [x] | Enquiry no longer visible in the dashboard list. |

Enquiry management testing confirmed that staff users can track, forward, update, and close enquiries using the custom dashboard workflow.

---

### Responsive Testing

| Page | Mobile | Tablet | Desktop | Notes |
|------|--------|--------|---------|-------|
| Home | [x] | [x] | [x] | Hero, search, and cards stack correctly |
| Cities index | [x] | [x] | [x] | City cards flow cleanly with no overflow |
| City listings | [x] | [x] | [x] | Grid adapts across breakpoints |
| Development detail | [x] | [x] | [x] |Images, amenities, and CTA remain usable |
| Enquiry form | [x] | [x] | [x] | Form fields are readable and accessible on all screens |
| Dashboard | [x] | [x] | [x] | Tables and actions remain usable at smaller screens |

All key pages were tested across mobile, tablet, and desktop breakpoints using browser dev tools and actual devices. No layout breakage, overflow, or usability issues were observed.

---


## Data Integrity & Validation

| Check | Pass/Fail | Notes |
|-------|-----------|-------|
| Enquiries linked to development | [x] | Enquires correctly reference their associated development via foreign key. |
| Duplicate unit types prevented | [x] | Unique constraint enforces one unit type per development. |
| Required fields enforced | [x] | Model and form validation prevent incomplete submissions. |
| Cascade behaviour correct | [x] | Related enquiries are deleted when a development is removed. |
| Indexes operate correctly | [x] | Indexed fields supprort efficient querying in listings and dashboard. |

All relational data behaved as expected during testing, Foreign key constraints, unique constraints, and indexed fields ensure data integrity and consistent behaviour across development, enquiry submission, and staff management workflows.

---


## Known MVP Limitations

| Limitation | Confirmed |
|-----------|-----------|
| Mailto enquiry forwarding | [x] |
| No renter/operator accounts | [x] |
| Limited search logic | [x] |
| Default Django auth only | [x] |

---


## Testing Status

- **Manual testing started:** [x]
- **Manual testing completed:** [x]
- **Blocking issues identified:** none
- **Ready for automated testing:** [x]