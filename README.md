# BTR Directory — MVP

**Live Site:** _Add Heroku URL once deployed_

**Repository:** [View on GitHub](https://github.com/creatvie-introvert/btr-directory-mvp)

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white) ![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?logo=django&logoColor=white)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black) ![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)


![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white) ![Cloudinary](https://img.shields.io/badge/Cloudinary-API-blue?logo=cloudinary&logoColor=white)

![Deployed on Heroku](https://img.shields.io/badge/Deployed-Heroku-430098?logo=heroku&logoColor=white)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## Project Overview

**BTR Directory — MVP** is a renter-first Build-to-Rent discovery platform designed to help users browse BTR developments by city, view key development details, and submit enquiries.
The MVP is intentionally scoped to validate the core renter journey while establishing a realistic operational workflow. Enquiries are managed through a **custom staff dashboard** and forwarded to the relevant operator using a **pre-filled email action (mailto workflow)**. Development listings are managed centrally by an authenticated admin user.

## Responsive Design Preview

![Responsive homepage showing mobile, tablet, and desktop layouts](docs/images/homepage-responsive.png)

> Composite screenshot showing the homepage hero and key sections across **mobile, tablet, and desktop** breakpoints.
> Screens were captured using browser developer tools and combined into a single composite image to demonstrate responsive behaviour across breakpoints.

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

- Discover Build-to-Rent developments in a specific city
- Compare developments using clear, scannable information
- View essential details such as amenities, tenancy information, and images
- Submit an enquiry with minimal friction
- Trust the platform through transparent legal and accessibility information

### Secondary user goals (Operators / Developers — indirect for MVP)

**Who they are:** BTR operators or developers who receive renter enquiries about specific developments and want leads delivered in a clear, usable format.

- Receive structured enquiries containing relevant renter intent
- Reduce follow-up friction by receiving complete enquiry details in one message

---

## User Stories

User stories were defined to clearly capture the needs of each user type interacting with the platform. These stories informed feature scope, information architecture, and testing decisions throughout the project.

### Primary user stories (Renters)

**User type:** Renter searching for Build-to-Rent properties.

- As a user, I want to browse cities so that I can quickly narrow my search by location
- As a user, I want to view a list of developments within a city so that I can compare available options
- As a user, I want to view detailed information about a development so that I can decide if it meets my needs
- As a user, I want view images of a development so that I can better understand the space and environment
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
- Maintain a centralised content management using Django's admin authentication
- Establish trust through transparency and accessibility-focused content
- Demonstrate Django relational database implementation

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
- Operator dashboards or accounts
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

- Mobile-first layouts for clarity and accessibility
- Consistent header and footer across all pages
- Scannable layouts using sections and headings
- Clearly labelled forms with logical field order

### Surface Plane

- Bootstrap-based responsive layouts
- Custom CSS applied for clarity and hierarchy
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

The project uses Inter as the primary typeface due to its high legibility, modern appearance, and suitability for UI-heavy applications.

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

Colours are used consistently to indicate hierarchy, actions, and states, while avoiding unnecessary visual noise. Custom colours are applied sparingly on top of Bootstrap defaults.

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
    - Prominent search bar is positioned in the homepage hero section
    - Search by:
        - City name (e.g. *London, Manchester*)
        - Postcode or postcode area (e.g. SW14)
    - Postcode and area searches resolve to the relevant city results page, allowing renters to quickly access appropiate listings without complex geolocation logic

- **City-based browsing**
    - Browse Build-to-Rent developments grouped by city
    - Cities used as the primary discovery entry point to simplify navigation

- **Development listings**
    - List of available BTR developments shown per city
    - Key summary information presented in a clear, scannable card-based layout

- **Development detail pages**
    - Detailed information for each development, including:
        - Development description
        - Amenities and key features
        - Tenancy-related information
        - Multiple development images hosted via Cloudinary
    - Content structured to support comparison and informed decision-making

- **Enquiry submission**
    - Enquiry submitted directly from a development detail page
    - Essential renter intent captured without requiring account creation
    - Clear confirmation feedback provided after submission

- **Trust and legal content**
    - Dedicated pages for:
        - What is Build-to-Rent
        - About
        - Disclaimer
        - Accessibility statement
        - Privacy policy
        - Terms of use
    - Pages promote transparency and build user trust

- **Responsive design**
    - Fully responsive layouts across mobile, tablet, and desktop
    - Mobile-first approach ensures usability on smaller screens

### Staff / Admin features (MVP)

- **Custom enquiries dashboard**
    - Staff can view all enquiries in a centralised dashboard
    - Each enquiry is linked to the relevant development
    - Staff can update enquiry status
    - Staff can close enquiries when appropriate
    
- **Enquiry forwarding workflow**
    - Each development stores an operator contact email
    - Staff can forward enquiries using pre-filled email action (mailto workflow)
    - This enables fast manual routing without requiring automated email infrastructure
    - Forwarding actions are logged with timestamp
    - A visual "Forwarded" badge is shown in the staff dashboard for audit clarity

- **Admin-only content management**
    - Authenticated admin users manage:
        - Cities
        - Developments
        - Development metadata and imagery
    - Content is maintained centrally to ensure consistency and data integrity

### Error handling and edge cases
- **Custom 404 page**
    - A user-friendly 404 page is displayed for invalid routes
    - Ensures a graceful experience when content cannot be found

---

## Feature Screenshots

The screenshots below show the implemented MVP features after development. They demonstrate the core renter journey and the internal staff workflow as delivered in the final application.

### Home — Hero search
![Home page showing the hero search bar used to search by city or postcode](docs/images/home-hero-responsive.png)

### Cities index
![Cities index page showing available Build-to-Rent locations](docs/images/cities-index-responsive.png)

### City development listing
![List of Build-to-Rent developments within a selected city](docs/images/city-developments-list-responsive.png)

### Development detail
![Development detail page showing images, amenities, tenancy information, and enquiry call-to-action](docs/images/development-detail-responsive.png)

### Enquiry form
![Enquiry form allowing renters to submit interest in a specific development](docs/images/enquiry-form-responsive.png)

### Enquiry confirmation
![Confirmation mesage displayed after a successful enquiry submission](docs/images/enquiry-confirmation-responsive.png)

### Staff enquiries dashboard
![Custom staff dashboard showing enquiries list and management overview](docs/images/staff-enquiries-dashboard-responsive.png)

### Enquiry management (detail view)
![Enquiry detail view showing status updates, forwarding, and close actions](docs/images/enquiry-detail-management-responsive.png)

---

## Future Features

The following features were intentionally excluded from the MVP to maintain focus, reduce technical risk, and ensure delivery within project constraints. They represent logical next steps if the platform were to be developed beyond the initial MVP.

### Enhanced search and discovery

- **Postcode radius search**
    - Allow users to search for developments within a specified distance of a postcode
    - Requires geocoding and latitude/longitude data for developments

- **Map-based browsing**
    - Interactive map view showing developments by location
    - Enables visual discovery and spatial filtering

- **Advanced filtering**
    - Filter developments by amenities, price range, tenancy length, or furnishing options
    - Improves comparison for users with specific requirements

### User accounts and personalisation

- **Renter accounts**
    - Save favourite developments
    - Track submitted enquiries
    - Receive updates on new developments in selected cities

- **Saved searches**
    - Allow users to store and revisit common search criteria

### Operator / Developer features

- **Operator dashboard**
    - Secure login for operators to manage their own developments
    - View and respond to enquiries within the platform

- **Automated enquiry delivery**
    - Replace manual mailto workflow with server-side email delivery
    - Add email templates and tracking

### Monetisation and platform search

- **Pay-per-lead model**
    - Charge operators for qualified enquiries
    - Provide basic lead analytics and reporting

- **Featured listings**
    - Allow operators to promote developments within city listings

- **Analytics ad insights**
    - Track user interactions, popular cities, and enquiry trends
    - Support data-driven platform improvements

### Accessibility and performance enhancements

- **Expanded accessibility testing**
    - Conduct user testing with assistive technologies
    - Further refine keyboard and screen reader support

- **Performance optimisation**
    - Improve image delivery and caching
    - Introduce pagination or lazy loading for large datasets

---

## Known MVP limitations

- Enquiry forwarding uses a mailto workflow rather than server-side delivery
- No renter or operator authentication is implemented
- Search functionality is limited to city and postcode resolution
- Admin and dashboard access is restricted to authenticated staff and superusers using Django's built-in authentication system.
- No role-based permission levels are implemented beyond Django's default auth

---

## Data Model

The application uses a relational database to store and manage structured data related to Build-to-Rent developments and user enquiries. The data model was designed to support the core renter journey while remaining simple, scalable, and aligned with MVP scope.

Each model uses Django's default auto-generated primary key (`id`) unless otherwise specified. Relationships between entities are implemented using foreign keys to enforce referential integrity across the data model.

### Overview

**ERD:** [View database diagram](https://dbdiagram.io/d/BTR-Directory-—-MVP-ERD-69430c0ee4bb1dd3a97ac8de)

The MVP data model consists of three primary entities:

- **City**
- **Development**
- **Enquiry**

These entities are related in a one-to-many structure to support city-based browsing and enquiry management.

### Data model updates

During development, the data model was expanded beyond the initial MVP ERD to support renter expectation and improve listing completedness.

**Additions:**
- **Pricing**
    - Added optional pricing fields to `Development`:
        - `rent_from_pcm` (integer)
        - `deposit_from` (integer, optional)
        - `pricing_note` (short text, optional)
- **Unit types**
    - Added a `UnitType` model linked to `Development` 
    - Represents bedroom-level pricing and availability (e.g. Studio, 1-bed, 2-bed, etc.)
    - Enforces a unique bedroom type per development

    These changes are documented in the updated ERD (`dbdiagram.io` script) and should be treated as the current source of truth for the MVP database structure.


### Entity relationships

- A **City** can have **many Developments**
- A **Development** belongs to **one City**
- A **Development** can have **many Enquiries**
- A **Enquiry** belongs to **one Development**

This structure allows users to browse developments by city and submit enquiries for individual developments, while enabling staff  to manage enquiries centrally.

### City model

Stores information about each city used as a primary discovery entry point.

**Key fields include:**
- City name
- Slug (used for clean URLs)
- Optional description or introduction text
- City image and alt text (used for visual discovery and accessibility)
- Active status flag (controls public visibility)
- Homepage feature flag(used to highlight key cities on the homepage)
- Timestamps (created / updated)

### Development model

Stores detailed information about each Build-to-Rent development.

**Key fields include:**
- Development name and slug
- Associated city (foreign key)
- Area name, address line, and postcode
- Short summary and full description
- Pricing information (rent and deposit from)
- Tenancy options and typical tenancy length
- Property type and furnishing options
- Pet policy and bills inclusion
- Number of homes within the development
- Operator name and contact email (used for enquiry forwarding)
- Amenities (many-to-many relationship)
- Unit types and bedroom-level pricing
- Development images (stored via Cloudinary)
- Active status flag
- Timestamps (created / updated)

Each development belongs to a single city and can receive multiple enquiries.

### Amenity model

Represents reusable amenities that can be linked to multiple developments.

**Key fields include:**
- Amenity name
- Optional icon reference
- Active status flag
- Timestamps (created / updated)

Amenities are linked to developments using a many-to-many relationship, allowing consistent reuse and filtering across listings.

### Enquiry model

Stores renter enquiries submitted through the platform.

**Key fields: include:**
- Renter name and email address
- Optional enquiry message
- Associated development (foreign key)
- Enquiry status (e.g. new, in progress, closed)
- Move timeframe (optional)
- Forwarding metadata (email forwarded to and timestamp)
- Timestamp of submission

Enquiries  are managed through a custom staff dashboard and can be forwarded to the relevant operator using a pre-filled email action.

### Data integrity and validation

- Foreign key relationships enforce data integrity between cities, developments, and enquiries
- Unique constraints prevent duplicate unit types per development
- Indexes are applied to frequently queried fields (status, created date, relationships)
- Required fields are validated at both model and form level
- Cascade deletion rules prevent orphaned records

### Future data model extensions

The current data model was intentionally kept minimal for MVP. Future enhancements could include:

- User account models for renters and operators
- Location data (latitude / longitude) to support radius search maps
- Analytics models for tracking engagement and enquiry performance

---

## Technologies Used

This project adopts a well-documented full-stack architecture to ensure clarity, scalability, and ease of collaboration.

### Core languages

- **HTML**  
Used to structure all templates and page content.

- **CSS**  
Used for layout refinement, spacing, and light visual customisation on top of Bootstrap styling.

- **JavaScript**  
Used for minor interactive behaviour and progressive enhancement where required.

- **Python**  
Primary backend language used with the Django framework.

### Frameworks & libraries

- **Django**  
A high-level web framework used to build the backend application, manage routing, models, forms, authentication, and templating.

- **Bootstrap**  
Used for the responsive grid system, layout structure, and UI components. Bootstrap defaults were used wherever possible, with minimal customisation to support accessibility and visual hierarchy.

### Database

- **PostgreSQL**
Used as the relational database for both local development and production to ensure consistency across environments.
The database stores structured data for cities, developments, and enquiries, with enforced relationships via foreign keys.

### Media storage

- **Cloudinary**  
Used to store and serve images for developments and city pages. This avoids reliance on Heroku's ephemeral filesystem and supports responsive image delivery.

### Deployment & hosting

- **Heroku**  
Used to deploy and host the live application.
Heroku Postgres is used for the production database, and environment variables are used to manage configuration securely.

### Version control

- **Git**  
Used for local version control throughout development.

- **GitHub**  
Used to host the project repository and manage commits and documentation.

### Design & Planning tools

- **Figma**  
Used to create low- and high-fidelity wireframes across mobile, tablet, and desktop breakpoints.

- **FigJam**  
Used for sitemap creation, navigation planning, and early UX structure.

- **Airtable**  
Used for project planning, task tracking, decision logging, and scope control.

---

## Project Setup

This section explains how to set up and run the project locally. It is intended to allow another developer to clone the repository, configure the environment, and run the application successfully.

### Prerequisites

Ensure the following are installed on your system:
- Python 3.11+
- PostgreSQL
- Git
- pip (Python package manager)
- Virtual environment support (e.g. venv)

### Clone the repository

```bash
git clone https://github.com/creatvie-introvert/btr-directory-mvp?tab=readme-ov-file
cd btr-directory-mvp
```

### Create and activate a virtual environment

``` bash
python -m venv venv
```

Activate the virtual environment:

**macOS/Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Environment variables

The project uses environment variables to store sensitive configuration values.

Create a `.env` file in the project root and add the following:

```bash
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/btr_directory
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
```

**Notes:**
- `SECRET_KEY` should be a unique, random string
- `DEBUG` must be set to False in production
- `DATABASE_URL` should point to your local PostgreSQL database
- `CLOUDINARY_URL` is provided by Cloudinary

**Important:**
The `.env` file is included in `.gitignore` and must never be committed to version control.

### Database setup

Create a PostgreSQL database locally:

```sql
CREATE DATABASE btr_directory;
```

Run migrations:

```bash
python manage.py migrate
```

### Create a superuser

```bash
python manage.py createsuperuser
```

This account is used to:
- Manage cities and developments
- Access the Django admin panel
- Support internal content management

### Run the development server

```bash
python manage.py runserver
```

The site will be available at:
```code
http://127.0.0.1:8000/
```

### Admin access

The Django admin panel is available at:

```code
http://127.0.0.1:8000/admin
```
Admin access is restricted to authenticated users and is used solely for content and enquiry management.

### Setup rationale

- PostgreSQL is used in both development and production to ensure consistency across environments
- Environment variables protect sensitive credentials
- Django's built-in tooling supports rapid local setup and testing
- The setup aligns with Heroku deployment requirements 

---

## Deployment (Heroku)

The project is deployed to **Heroku**, providing a publicly accessible live version of the application. This section documents the steps required to deploy the project and configure the production environment.

### Create a Heroku app

1. Log in to your Heroku account
2. From the dashboard, click **New → Create new** app
3. Enter a unique app name
4. Select the appropriate region
5. Click **Create app**

### Configure environment variables

In the Heroku dashboard:
1. Navigate to **Settings → Config Vars**
2. Add the following variables:
```code
SECRET_KEY=your_django_secret_key
DATABASE_URL=your_heroku_postgres_url
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
DEBUG=False
```

**Important:** Do not set DEBUG=True in production.

### Add postgreSQL database

1. In the Heroku dashboard, go to the **Resources tab**
2. Add the **Heroku Postgres** add-on
3. Select the free or low-tier plan
4. Heroku will automatically set the DATABASE_URL

### Update Django settings for production

Ensure the following are configured in `settings.py`:
- `ALLOWED_HOSTS` includes the Heroku app URL
- `DEBUG` is set via environment variable
- Static and media files are configured correctly
- Cloudinary is used for media storage

### Prepare the project for deployment

Ensure the following files are present and correctly configured:
- requirements.txt
- Procfile

**Collect static files**
```bash
python manage.py collectstatic
```

**Deploy to Heroku**
- Save and commit all changes and push to Heroku

**Verify deployment**
- Visit the live site using the Heroku app URL
- Confirm pages load correctly
- Test form submissions
Confirm admin access via /admin
- Verify Cloudinary images load correctly

**Deployment rationale**
- Heroku provides a simple deployment workflow suitable for MVPs
- Environment variables ensure credentials remain secure
- PostgreSQL ensures reliable relational data storage
- Cloudinary avoids Heroku filesystem limitations

**Known deployment limitations**
- Free/low-tier dynos may sleep after inactivity
- Cold starts can increase initial load time
- Suitable for MVP 

---

## Security considerations

- Django CSRF protection enabled on all forms
- Admin and staff routes protected by authentication
- No sensitive credentials stored in version control
- Environment variables used for all secrets

---

## Testing

Testing focused on validating user stories, form validation, staff workflows, and responsive behaviour across breakpoints.

Manual testing was conducted using Chrome DevTools responsive modes and real browser resizing to validate layout behaviour across breakpoints.

Detailed testing documentation, including user story testing, form validation, responsiveness checks, accessibility checks, and bug fixes, can be found in the separate testing file:
[View full testing documentation](TESTING.md)

---

## Version Control

This project uses **Git** for version control and is hosted on **GitHub**.

**Version control workflow**
- Changes were made locally within the VS Code workspace
- Updates were staged and committed regularly using conventional commits
- Work was pushed to the remote GitHub repository to maintain a clear development history

**Common Git commands used**
```bash
git status
git add .
git commit
git push
```

**Repository**
- **GitHub Repository:** [View on Github](https://github.com/creatvie-introvert/btr-directory-mvp?tab=readme-ov-file)
- **Main branch:** main

**Rationale**  
Using Git and GitHub supports:
- Clear tracking of progress and feature development
- Easier debugging through commit history
- Safe experimentation without losing working versions
- A professional workflow aligned with industry standards

---

## Attribution and Credits

This project was developed solely by the author as an early-stage **Minimum Viable Product (MVP)** intended to evolve into a larger Build-to-Rent discovery platform. The current implementation prioritises core functionality, clean architecture, and scalability, with future features planned beyond MVP. All custom code, layouts, and content structure were written specifically for this project unless otherwise stated below.

### Frameworks, libraries, and tools

The following third-party tools and libraries were used as part of the development process:

- **Django** — Python web framework used for backend development   
https://www.djangoproject.com/

- **Bootstrap** — Used for responsive grid layout and UI components   
https://getbootstrap.com/

- **PostgreSQL** – Relational database used in both development and production   
https://www.postgresql.org/

- **Cloudinary** – Used for external image storage and delivery
https://cloudinary.com/

- **Gunicorn** WSGI HTTP server for running Django in production
https://gunicorn.org/

- **Heroku** – Hosting and deployment platform
https://www.heroku.com/

### Design and planning tools
- **Figma & FigJam** – Used for wireframes, sitemap, navigation planning, and high-fidelity wireframes   
https://www.figma.com/   

- **Airtable** – Used for early project planning, task tracking, and decision logging   
https://www.airtable.com/   

### Images and media

- City and hero images used in wireframes and UI design were sourced from royalty-free stock or AI-generated imagery during the design phase
- Production images for developments are intended to be provided by operators or sourced with appropriate permissions
- All images are served via Cloudinary

Where third-party images are used in the final implementation, the original source and creator will be credited accordingly.

### Code references and learning resources

During development, official documentation and learning resources were consulted, including:

- Django Documentation   
https://docs.djangoproject.com/
- Bootstrap Documentation   
https://getbootstrap.com/docs/
- MDN Web Docs (HTML, CSS, JavaScript reference)
https://developer.mozilla.org/

No code was copied directly from tutorials or third-party repositories. where small snippets or patterns were inspired by documentation examples, they were adapted and written specifically for this project.

### Acknowledgements

- Course materials and guidance provided by the training programme
- Tutor feedback during project planning and review stages

### Attribution statement

All third-party tools and resources used have been credited appropiately. Any future additions of external code, assets or media will be documented here and within the codebase where applicable.

---

## README Maintenance

This README is treated as a **living document** and was updated throughout the planning and development of the MVP.

Key sections such as **UX decisions, features, data model, testing, and deployment** were documented incrementally to ensure accuracy and traceability.   
Any significant changes to scope, architecture, or implementation were reflected in the README as they occurred.

This approach ensures that the documentation remains reliable for future development, collaboration, and project handover.

---

## License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project, including for commercial purposes, provided that the original copyright and license notice are included.

See the [LICENSE](LICENSE) file for full details.

---
