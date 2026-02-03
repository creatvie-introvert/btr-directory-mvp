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
| Cities index loads | Page renders correctly | [] |  |
|Active cities displayed | All expected cities visible | [] |  |
| City card shows name and image | Correct content shown | [] |  |
| City card is clickable | Opens correct city listing | [] |  |
| Responsive layout | Layout adapts across breakpoints | [] |  |

---

### City development listing page

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| City development list loads | Correct city title shown | [] |  |
| Developments filtered by city | Only relevant developments shown | [] |  |
| Development card content | Name, image,  summary visible | [] |  |
| Empty state handling | Clear messaging if no developments | [] |  |
| Responsive layout | Layout adapts across breakpoints | [] |  |

---

### Development detail page

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Detail page loads | No errors | [] |  |
| Development data shown | Correct content displayed | [] |  |
| Amenities visible | Amenities listed correctly | [] |  |
| Images load | Images served from Cloudinary | [] |  |
| Image alt text | Present and meaningful | [] |  |
| Enquiry CTA visible | Clear call-to-action shown | [] |  |
| Responsive layout | Layout adapts across breakpoints | [] |  |

---

### Enquiry form

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Enquiry form loads | Form visible | [] |  |
| Required field validation | Errorsa shown on empty submit | [] |  |
| Invalid email rejected | Validation error displayed | [] |  |
| Valid submission | Enquiry saved successfully | [] |  |
| Redirect on success | User redirected to confirmation | [] |  |
| Responsive layout | Layout adapts across breakpoints | [] |  |

---

### Enquiry confirmation page

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Confirmation page loads | Success message visible | [] |  |
| Clear confirmation message | User informed of submission | [] |  |
| No sensitive data shown | Safe output | [] |  |
| Responsive layout | Layout adapts across breakpoints | [] |  |

---


## Staff / Admin Workflow Testing

### Authentication

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Dashboard protected | Unauthenticated users blocked | [] |  |
| Login page loads | Login form visible | [] |  |
| Valid login | Access granted | [] |  |
| Invalid login | Error message shown | [] |  |

---

### Enquiry management

| Test case | Expected result | Pass/Fail | Notes |
|-----------|-----------------|-----------|-------|
| Enquiry detail loads | Full enquiry visible | [] |  |
| Status update | Status persists correctly | [] |  |
| Forward action | Mail client opens with pre-filled content | [] |  |
| Forward metadata saved | Timestamp and email stored | [] |  |
| Close enquiry | Status updated to closed | [] |  |
| Delete enquiry | Enquiry removed | [] |  |

---

### Responsive Testing

| Page | Mobile | Tablet | Desktop | Notes |
|------|--------|--------|---------|-------|
| Home | [] | [] | [] | |
| Cities index | [] | [] | [] | |
| City listings | [] | [] | [] | |
| Development detail | [] | [] | [] | |
| Enquiry form | [] | [] | [] | |
| Dashboard | [] | [] | [] | |

---


## Data Integrity & Validation

| Check | Pass/Fail | Notes |
|-------|-----------|-------|
| Enquiries linked to development | [] | |
| Duplicate unit types prevented | [] | |
| Required fields enforced | [] | |
| Cascade behaviour correct | [] | |
| Indexes operate correctly | [] | |

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
- **Manual testing completed:** []
- **Blocking issues identified:** []
- **Ready for sutomated testing:** []