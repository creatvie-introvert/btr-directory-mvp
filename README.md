# BTR Directory — MVP

**Live Site:** _Add Heroku URL once deployed_

**Repository:** _Add GitHub repository URL_

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?logo=django&logoColor=white)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)


![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-API-blue?logo=cloudinary&logoColor=white)

![Deployed on Heroku](https://img.shields.io/badge/Deployed-Heroku-430098?logo=heroku&logoColor=white)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## Project Overview

**BTR Directory — MVP** is a renter-first Build-to-Rent discovery platform designed to help users browse BTR developments by city, view key development details, and submit enquiries.
The MVP is intentionally scoped to validate the core renter journey while establishing a realistic operational workflow. Enquiries are managed through a **custom staff dashboard** and forwarded to the relevant operator using a **pre-filled email action (mailto workflow)**. Development listings are managed centrally by an authenticated admin user.

## Responsive Design Preview

![Am I Responsive screenshot]()
> Screenshot generated using the **Am I Responsive** tool to demonstrate the project across mobile, tablet, laptop, and desktop screens.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Responsive Design Preview](#responsive-design-preview)
- [User Goals](#user-goals)
- [User Stories](#user-stories)
- [Website Goals and Objectives](#website-goals-and-objectives)
- [Target Audience](#target-audience)
- [UX and UI](#ux-and-ui)
- [Wireframes](#wireframes)
- [Design System Summary](#design-system-summary)
- [Features](#features)
- [Future Features](#future-features)
- [Data Model](#data-model)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
- [Deployment (Heroku)](#deployment-heroku)
- [Testing](#testing)
- [Version Control](#version-control)
- [Attribution and Credits](#attribution-and-credits)
- [README Maintenance](#readme-maintenance)
- [License](#license)

---

## User Goals 

### Primary user goals (Renters)

**Who they are:** People actively searching for a long-term rental home in a Build-to-Rent development and using the site to discover, compare, and enquire.

- Discover Build-toRent developments in a specific city
- Compare developments using clear, scannable information
- View essential details such as amenities, tenancy information, and images
- Submit an enquiry with minimal friction
- Trust the platform through transparent legal and accessibility information

### Secondary user goals (Operators / Developers — indirect for MVP)

**Who they are:** BTR operators or developers who receive renter enquiries about specific developments and want leads delivered in a clear, usable format.

- Receive structured enquires containing relevant renter intent
- Reduce follow-up friction by receiving complete enquiry details in one message

---

## User Stories

User stories were defined to clearly capture the needs of each type of user interacting with the platform. These stories informed feature scope, information architecture, and tresting decisions throughout the project.

### Primary user stories (Renters)

**User type:** Renter searching for Build-to-Rent properties.

- As a user, I want to browse cities so that I can quickly narrow my search by location
- As a user, I want to view a list of developments within a city so that I can compare available options
- As a user, I want to view detailed information about a development so that I can decide if it meets my needs
- As a user, I wantview images of a development so that I can better understand the space and environment
- As a user, I want to submit an enquiry so that I can request more information or express interest
- As a user, I want to access clear legal and trust information so that I understand the purpose and limitations of the site

### Secondary user stories (Staff / Admin workflow)

**User type:** Staff users managing enquiries and content on the platform

- As a user, I want to view all enquiries in one place so that I can manage incoming leads efficiently
- As a user, I want update the status of an enquiry so that I can track and follow progress
- As a user, I want to forward enquiries to the relevant operator so that leads are delivered quickly and accurately
- As a user, I want to delete enquiries when appropiate so that data can be managed responsibly

---

## Website Goals and Objectives

The following goals define the purpose of the website and guided key design, feature, and scope decisions throughout the MVP. They balance user needs, business intent, and course assessment requirements.

- Provide a renter-focused directory of BTR developments by city
- Support a complete **browse → view → enquiries** user journey
- Maintain a centralised content management with single admin user
- Establish trust through transparency and accessibility-focused content
- Demonstrate Django relational database implmentation

---

## Target Audience

This section defines who the platform is designed for at MVP stage, as well as which users and features are intentionally out of scope. Clearly defining the target audience helped guide scope decisions and maintain focus during development.

### Primary audience

- UK-based renters seeking Build-to-Rent properties

### Secondary audience (post-MVP)

- BTR developers and operators
- Industry stakeholders seeking visibility of BTR developments

### Out of scope (MVP)

- Short-term lets as a primary product
- Renter accounts and saved searches
- Operator dashboards or accouts
- Payment features or monetisation

---

## UX and UI

This project follows a user-centred design approach guided by the **Five Planes of UX**.

### Strategy Plane

- **Problem:** BTR information is fragmented and often not renter-focused
- **Primary goal:** Enable renters to discover developments and submit enquiries
- **Future business goal:** Evolve into a go-to BTR discovery platform supporting lead-based monetisation.

### Scope Plane

**Included in MVP:**

- Cities index
- City development listings
- Development detail pages (with multiple images)
- Enquiry form
- Custom staff enquiries dashboard (CRUD)
- Admin-only content management (developments and cities)
- Trust and legal pages
- 404 error page

**Excluded from MVP:**

- Map integration
- Operator accounts
- Automated email delivery
- Monetisation features

### Structure Plane

**Public flow:**
Home → Cities → City Developments → Development Detail → Enquiry

**Staff flow:**
Enquiries List → Enquiry Detail → Status Update / Delete / Email operator (mailto)

### Skeleton Plane

- Mobile-first layouts for clarity and accesibility
- Consistent header and footer across all pages
- Scannable layouts using sections and headings
- Clearly labelled forms with logical field order

### Surface Plane

- Bootstrap-based responsive layouts
- Custom CSS applied for clariry and hierarachy
- High-contrast, accessible design decisions documented in planning notes

---

## Wireframes

Low-fidelity wireframes were created for **all MVP screens** across **three breakpoints**:

- **Mobile:** 390px
- **Tablet:** 768px
- **Desktop:** 1440px

**Wireframes directory:** `wireframes/`

**Design file:** [View wireframes in Figma](https://www.figma.com/design/DEOSptgxu5fwmNIyOT0tZS/BTR-Directory-%E2%80%94-Low-Fidelity-Wireframes--MVP-?node-id=3-229&p=f&t=wxqrYHQOPzDyOhdu-0)

### Screens included (14 total)

- Home
- Cities Index
- City Developments Listing
- Development Detail
- Enquiry Form
- What is Build-To-Rent
- About
- Disclaimer
- Accessibility
- Privacy Policy
- Terms of Use
- 404 Page
- Admin — Development List
- Admin — Add/Edit Development

---

## Design System Summary

The design system establishes visual consistency, accessibility, and scalability across the MVP while remaining lightweight and compatible with Bootstrap defaults.

### Typography

The project uses Inter as the primary typeface due to its high legibility, modern apperance, and suitability for UI-heavy applications.

The typographic scale was designed to support clear hierarchy and responsive readability across all breakpoints.

- **Font family:** Inter (Google Fonts)
- **Weights used:** 400 (Regular), 600 (Semi-bold)

|Element|Font|Size (px)|Line Height|Weight|Usage|
|-------|----|----|-----------|------|-----|
|H1|Inter|40|48|600|Primary page headings|
|H2|Inter|32|40|600|Section headings|
|H3|Inter|24|32|600|Subsection headings|
|H4|Inter|16|24|600|UI Labels & card titles|
|Body|Inter|16|24|400|Primary content text|
|Small / Metadata|Inter|14|20|400| Supporting information & helper text|

### Colour Scheme

A restrained, neutral colour palette was chosen to prioritise **readability, clarity, and trust**, which are essential for a property discovery platform.

The palette supports a calm, professional tone while maintaining sufficient contrast for accessibility.

![BTR Directory colour palette](docs/images/colours-with-names.png)

**Colour approach:**
- Deep blues and dark neutrals for primary UI elements and emphasis
- Soft light backgrounds to improve content scannability
- High-contrast text colours to meet WCAG accessibility guidelines

Colours are used consistently to indicate hierarchy, actions, and states, while avoiding unnescessary visual noise. Custom colours are applied sparingly on top of Bootstrap defaults.

### Imagery

- Development listings support **multiple images** to give renters a realistic impression of each property
- City images are used to support discovery and location context
- Images are stored externally using **Cloudinary** to comply with Heroku's ephemeral file system
- Consistent image ratios are used across cards and listings to maintain layout stability

### Responsiveness

- Mobile-first layouts were designed for clarity and ease of navigation
- Layouts adapt cleanly across mobile, tablet, and desktop
- The **Bootstrap grid system** is used extensively to ensure consistent responsive behaviour
- Spacing, typography, and image scaling were tested across breakpoints during wireframing

---

## Features

The MVP focuses on delivering a clear, renter-first discovery experience while supporting a realistic internal workflow for managing enquiries and content.

### Public-facing features (Renters)

- **Hero search**
    - A prominent search bar is positioned in the homepage hero section
    - Users can search by:
        - City name (e.g. *London, Manchester*)
        - Postcode or postcode area (e.g. SW14)
    - Postcode and area searches resolve to the relevant city results page, allowing renters to quickly access appropiate listings without complex geolocation logic

- **City-based browsing**
    - Users can browse Build-to-Rent developments grouped by city
    - Cities act as the primary discovery entry point to simplify navigation

- **Development listings**
    - Each city displays a list of available BTR developments
    - Listings present key summary information in a clear, scannable card-based layout

- **Development detail pages**
    - Dedicated pages provide detailed information for each development, including:
        - Development description
        - Amenities and key features
        - Tenancy-related information
        - Multiple development images hosted via CLoudinary
    - Content is structured to support comparison and informed decision-making

- **Enquiry Submission**
    - Users can submit an enquiry directly from a development detail page
    - The form captures essential renter intent without requiring account creation
    - Clear confirmation feedback is provided after submission

- **Trust and legal content**
    - Dedicated pages for:
        - What is Build-to-Rent
        - About
        - Disclaimer
        - Accessibility statement
        - Privacy policy
        - Terms of use
    - These pages prroote transparency and build user trust

- **Responsive design**
    - Fully responsive layouts across mobile, tablet, and desktop
    - Mobile-first approach ensures usability on smaller screens

### Staff / Admin features (MVP)

- **Custom enquiries dashboard**
    - Staff can view all enquiries in a centralised dashboard
    - Each enquiry is linked to the relevant development

- **Enquiry management (CRUD)**
    - Staff can:
        - View enquiry details
        - Update enquiry status
        - Delete enquiries when appropiate
    
- **Enquiry forwarding workflow**
    - Each development stores an operator contact email
    - Staff can forward enquiries using pre-filled email action (mailto workfllow)
    - This enables fast manual routing without requiring automated email infrastructure

- **Admin-only content management**
    - Authenticated admin users manage:
        - Cities
        - Developments
        - Development metadata and imagery
    - Content is maintained centrally to ensure consitency and data integrity

### Error handling and edge cases
- **Custom 404 page**
    - A user-friendly 404 page is displayed for invalid routes
    - Ensures a graceful experience when content cannot be found

---

## Future Features

---

## Data Model

---

## Technologies Used

---

## Project Setup

---

## Deployment (Heroku)

---

## Testing

---

## Version Control

---

## Attribution and Credits

---

## README Maintenance

---

## License

---
