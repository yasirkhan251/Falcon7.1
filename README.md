<h1 align="center">🦅 Falcon Tech World — Falcon 7.1</h1>

<p align="center">
  <strong>A Django-powered service, product and booking management platform</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-5.2.6-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/Django%20Auth-Custom%20User-092E20?style=for-the-badge">
</p>

---

<h2>🎯 What This Project Offers</h2>

<p>
<strong>Falcon 7.1</strong> is a full-stack Django platform developed for
<strong>Falcon Tech World</strong> to bring products, technical services,
customer accounts, bookings and administrative operations together in one
system.
</p>

<p>
Rather than being only a company website, the platform provides a complete
workflow for customers to:
</p>

<ul>
<li>🛍️ Explore products and categories</li>
<li>🛠️ Explore technical services</li>
<li>📅 Book a service</li>
<li>📍 Submit service location details</li>
<li>🔐 Create and manage an account</li>
<li>📱 Authenticate using phone/email credentials</li>
<li>🔑 Recover accounts using OTP</li>
<li>📋 Review previous bookings</li>
</ul>

<p>
Administrators receive a separate management environment for handling
products, service categories, clients and booking operations.
</p>

---

<h2>✨ Highlighted Features</h2>

<table>
<tr>

<td width="33%" align="center" valign="top">

<h3>🛍️ Product Catalog</h3>

<p>
Hierarchical product categories, brands, models, variants, inventory and pricing.
</p>

</td>

<td width="33%" align="center" valign="top">

<h3>🛠️ Service Catalog</h3>

<p>
Organize technical services into service categories and service offerings.
</p>

</td>

<td width="33%" align="center" valign="top">

<h3>📅 Service Booking</h3>

<p>
Customers can schedule service appointments and submit device and issue details.
</p>

</td>

</tr>

<tr>

<td align="center" valign="top">

<h3>🔐 Custom Authentication</h3>

<p>
Custom Django user model with phone/email login and password authentication.
</p>

</td>

<td align="center" valign="top">

<h3>🔢 OTP Recovery</h3>

<p>
OTP-based password recovery with five-minute session expiry.
</p>

</td>

<td align="center" valign="top">

<h3>📍 Location Capture</h3>

<p>
Booking addresses can include coordinates and can be opened directly in Google Maps.
</p>

</td>

</tr>

<tr>

<td align="center" valign="top">

<h3>👑 Admin Dashboard</h3>

<p>
Monitor bookings, clients, pending jobs and recent activity from one dashboard.
</p>

</td>

<td align="center" valign="top">

<h3>📦 Inventory Management</h3>

<p>
Manage product stock, SKU generation, categories and display ordering.
</p>

</td>

<td align="center" valign="top">

<h3>🗂️ Drag & Drop Organization</h3>

<p>
Reorder products and folders directly from the administration interface.
</p>

</td>

</tr>
</table>

---

<h2>🧠 How It Works</h2>

```text id="3b3s4p"
                         🦅 Falcon Tech World
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
        🛍️ Products          🛠️ Services         👤 Accounts
              │                   │                   │
              │                   ▼                   │
              │             Service Selection         │
              │                   │                   │
              └───────────────┐   ▼   ┌───────────────┘
                              │ Booking │
                              ▼         │
                         📅 Appointment
                              │
                              ▼
                         📍 Address
                              │
                              ▼
                     🆔 Booking Token
                              │
                              ▼
                        👑 Admin Panel
                              │
                     ┌────────┼────────┐
                     ▼        ▼        ▼
                  Pending  Assigned  Completed
```

---

<h2>🏗️ Application Architecture</h2>

<table>
<tr>
<th>Application</th>
<th>Responsibility</th>
</tr>

<tr>
<td><code>Accounts</code></td>
<td>Custom user model, authentication, registration, OTP and password recovery.</td>
</tr>

<tr>
<td><code>Falcon</code></td>
<td>Main customer-facing website and storefront pages.</td>
</tr>

<tr>
<td><code>services</code></td>
<td>Service categories, service products and service presentation.</td>
</tr>

<tr>
<td><code>Bookings</code></td>
<td>Appointments, addresses, booking identifiers and booking history.</td>
</tr>

<tr>
<td><code>Admin</code></td>
<td>Administrative dashboards, catalog management and booking operations.</td>
</tr>

<tr>
<td><code>Core</code></td>
<td>Main Django project configuration and URL routing.</td>
</tr>
</table>

---

<h2>🛠️ Software & Technologies Used</h2>

<table>
<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>🐍 Python</td>
<td>Backend programming language</td>
</tr>

<tr>
<td>🌐 Django 5.2.6</td>
<td>Web framework</td>
</tr>

<tr>
<td>🗄️ SQLite</td>
<td>Default database</td>
</tr>

<tr>
<td>🎨 HTML5</td>
<td>Server-rendered frontend</td>
</tr>

<tr>
<td>🎨 CSS3</td>
<td>Responsive styling</td>
</tr>

<tr>
<td>⚡ JavaScript</td>
<td>Interactive frontend behaviour</td>
</tr>

<tr>
<td>🔐 Django Authentication</td>
<td>User/session authentication and authorization</td>
</tr>

<tr>
<td>📧 SMTP</td>
<td>OTP/email delivery</td>
</tr>

<tr>
<td>🗺️ Google Maps</td>
<td>Location viewing from captured booking coordinates</td>
</tr>
</table>

---

<h2>💻 System Requirements</h2>

<ul>
<li>Windows, Linux or macOS</li>
<li>Python 3.x</li>
<li>pip</li>
<li>Git</li>
<li>Modern web browser</li>
<li>Internet connection for email and map integrations</li>
<li>Sufficient storage for uploaded product/service images</li>
</ul>

<h3>Recommended Development Setup</h3>

<ul>
<li>Python 3.11+</li>
<li>8 GB RAM or more</li>
<li>Modern multi-core CPU</li>
<li>Stable internet connection</li>
</ul>

---

<h2>📦 Installation & Setup</h2>

<h3>1️⃣ Clone the Repository</h3>

```bash id="lj8c4p"
git clone https://github.com/yasirkhan251/Falcon7.1.git
cd Falcon7.1
```

<h3>2️⃣ Create a Virtual Environment</h3>

```bash id="2n92r9"
python -m venv venv
```

<p><strong>Windows:</strong></p>

```bash id="8v6e56"
venv\Scripts\activate
```

<p><strong>Linux / macOS:</strong></p>

```bash id="wmq9so"
source venv/bin/activate
```

<h3>3️⃣ Install Django</h3>

<p>
The repository does not currently provide a root <code>requirements.txt</code>,
so install Django first:
</p>

```bash id="rj7cvc"
pip install django
```

<p>
Then install any additional third-party packages required by your local
environment as they are introduced by the project.
</p>

---

<h2>🗄️ Database Setup</h2>

<p>
Falcon 7.1 currently uses SQLite:
</p>

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

<p>
Run the migrations:
</p>

```bash id="s9o2lq"
python manage.py makemigrations
python manage.py migrate
```

<p>
Create an administrator when required:
</p>

```bash id="7j5n2f"
python manage.py createsuperuser
```

---

<h2>▶️ How to Run</h2>

```bash id="dm17my"
python manage.py runserver
```

<p>
Then open:
</p>

```text id="xsw0ig"
http://127.0.0.1:8000/
```

---

<h2>🌐 Main Routes</h2>

<table>
<tr>
<th>Route</th>
<th>Purpose</th>
</tr>

<tr>
<td><code>/</code></td>
<td>Main Falcon Tech World site</td>
</tr>

<tr>
<td><code>/auth/</code></td>
<td>User authentication and registration</td>
</tr>

<tr>
<td><code>/services/</code></td>
<td>Service catalog</td>
</tr>

<tr>
<td><code>/bookings/</code></td>
<td>Booking workflow and booking history</td>
</tr>

<tr>
<td><code>/admin/</code></td>
<td>Custom Falcon administration interface</td>
</tr>

<tr>
<td><code>/admin_dev/</code></td>
<td>Django's built-in admin</td>
</tr>
</table>

---

<h2>👤 User Authentication</h2>

<p>
Falcon 7.1 uses a custom <code>MyUser</code> model.
</p>

<h3>Account Information</h3>

<ul>
<li>👤 Name</li>
<li>📱 Phone number</li>
<li>📧 Email</li>
<li>🆔 Falcon server ID</li>
<li>🖼️ Profile image</li>
<li>👑 Administrator flag</li>
<li>📅 Date joined</li>
</ul>

<h3>🔑 Login Flow</h3>

```text id="o9h9f5"
Phone / Email
      │
      ▼
Find User
      │
      ▼
Password Authentication
      │
      ▼
Django Login Session
      │
      ├───────────────┐
      ▼               ▼
Regular User       Administrator
      │               │
      ▼               ▼
   Store /        Admin Dashboard
   Services
```

---

<h2>🔢 OTP Password Recovery</h2>

<p>
The authentication system contains an OTP-based password recovery workflow.
</p>

```text id="6l0p4r"
Forgot Password
      │
      ▼
Phone / Email Lookup
      │
      ▼
Generate 6-digit OTP
      │
      ▼
Store OTP in Session
      │
      ▼
5-minute Expiration
      │
      ▼
Email OTP
      │
      ▼
Verify OTP
      │
      ▼
Set New Password
```

<p>
The OTP is stored in the session and the recovery session expires after five
minutes.
</p>

---

<h2>🛍️ Product Catalog</h2>

<p>
Products are organized using a hierarchical category system rather than a flat
list.
</p>

<h3>📂 Category Hierarchy</h3>

```text id="sx6kfe"
Root Category
     │
     ├── Brand
     │    │
     │    ├── Series
     │    │     │
     │    │     └── Product
     │    │
     │    └── Series
     │
     └── Brand
```

<p>
Categories support:
</p>

<ul>
<li>Nested parent/child relationships</li>
<li>Images</li>
<li>Description</li>
<li>Slug generation</li>
<li>Active/inactive state</li>
<li>Display ordering</li>
<li>Breadcrumb/path generation</li>
</ul>

---

<h3>📦 Product Information</h3>

<p>
Products currently support:
</p>

<ul>
<li>Brand</li>
<li>Model name</li>
<li>Variant</li>
<li>Product image</li>
<li>Description</li>
<li>Price</li>
<li>Stock</li>
<li>SKU</li>
<li>Active/inactive state</li>
<li>Display order</li>
</ul>

<h3>🏷️ Dynamic SKU Generation</h3>

<p>
Products automatically receive generated SKUs in the format:
</p>

```text id="u4k2d9"
FTW-BRA-MODEL-XXXXXX
```

<p>
The SKU is derived from the brand/model and supplemented with a unique
identifier.
</p>

---

<h2>🛠️ Service Catalog</h2>

<p>
Falcon 7.1 separates services from ordinary products through the
<strong>services</strong> application.
</p>

<h3>Service Categories</h3>

<p>
Service categories support:
</p>

<ul>
<li>Service name</li>
<li>Description</li>
<li>Unique slug</li>
<li>Associated product/category</li>
<li>Image</li>
<li>Display order</li>
<li>Creation/update timestamps</li>
</ul>

<h3>Service Products</h3>

<p>
A service offering can be connected to a product/model and can contain:
</p>

<ul>
<li>Service category</li>
<li>Device/product</li>
<li>Description</li>
<li>Price</li>
<li>Image</li>
<li>Active state</li>
<li>Display order</li>
</ul>

---

<h2>📅 Service Booking System</h2>

<p>
The booking module is one of the core features of Falcon 7.1.
Authenticated customers can schedule a technical service and provide detailed
information about the device/problem.
</p>

<h3>Booking Information</h3>

<ul>
<li>Service type</li>
<li>Service name</li>
<li>Device/model</li>
<li>Purpose</li>
<li>Description</li>
<li>Phone number</li>
<li>Appointment date/time</li>
<li>Customer</li>
</ul>

---

<h3>📍 Booking Address</h3>

<p>
The booking system stores a separate address record with fields such as:
</p>

<ul>
<li>House number</li>
<li>Building</li>
<li>Street</li>
<li>Landmark</li>
<li>City</li>
<li>State</li>
<li>Pincode</li>
<li>Country</li>
<li>Coordinates</li>
</ul>

---

<h3>🗺️ Location Integration</h3>

<p>
Captured coordinates can be converted into a Google Maps link from the
administrative interface.
</p>

```text id="st9t6n"
Booking Address
      │
      ▼
GPS Coordinates
      │
      ▼
Google Maps URL
      │
      ▼
📍 Open Precise Location
```

---

<h2>🆔 Booking Tracking</h2>

<p>
Every booking receives generated tracking identifiers.
</p>

<h3>Sequence Number</h3>

<p>
Bookings receive a unique incremental sequence.
</p>

<h3>Order ID</h3>

```text id="z6ew31"
#0001
#0002
#0003
...
```

<h3>Booking Token</h3>

<p>
A token is generated from service information, model information and the
booking sequence.
</p>

<p>
This provides a human-readable reference for individual bookings.
</p>

---

<h2>🚦 Booking Status Workflow</h2>

```text id="h6vwjd"
🟠 Pending
    │
    ▼
🔵 Technician Assigned
    │
    ▼
🟣 In Progress
    │
    ▼
🟢 Completed

        OR

🟠 Pending ─────► 🔴 Cancelled
```

<p>
The booking model currently defines:
</p>

<table>
<tr>
<th>Status</th>
<th>Meaning</th>
</tr>

<tr>
<td>Pending</td>
<td>Booking has been submitted and is awaiting processing.</td>
</tr>

<tr>
<td>Assigned</td>
<td>A technician has been assigned.</td>
</tr>

<tr>
<td>In Progress</td>
<td>The service operation is underway.</td>
</tr>

<tr>
<td>Completed</td>
<td>The service request has been completed.</td>
</tr>

<tr>
<td>Cancelled</td>
<td>The booking has been cancelled.</td>
</tr>
</table>

---

<h2>📋 My Bookings</h2>

<p>
Logged-in customers can access their previous bookings through:
</p>

```text id="3tdnjm"
/bookings/my-bookings/
```

<p>
Bookings are displayed in reverse chronological order, allowing customers to
review their service history.
</p>

---

<h2>👑 Admin Dashboard</h2>

<p>
The custom administrator dashboard is designed as an operational overview of
Falcon Tech World.
</p>

<h3>📊 Dashboard Statistics</h3>

<table>
<tr>
<th>Metric</th>
<th>Purpose</th>
</tr>

<tr>
<td>📅 Total Bookings</td>
<td>Total service bookings in the system.</td>
</tr>

<tr>
<td>👥 Clients</td>
<td>Total non-admin users.</td>
</tr>

<tr>
<td>📆 Today</td>
<td>Bookings created today.</td>
</tr>

<tr>
<td>⏳ Pending</td>
<td>Bookings awaiting processing.</td>
</tr>
</table>

---

<h3>🛠️ Admin Operations</h3>

<ul>
<li>View recent bookings</li>
<li>View complete booking reports</li>
<li>Edit booking status</li>
<li>Delete bookings</li>
<li>Inspect customer details</li>
<li>View submitted booking addresses</li>
<li>Open customer coordinates in Google Maps</li>
</ul>

---

<h2>🗂️ Admin Catalog Management</h2>

<p>
The admin interface provides a folder-like approach to catalog management.
</p>

<h3>📁 Product Organization</h3>

```text id="7l2wgd"
Category
   │
   ├── Subcategory
   │      │
   │      ├── Product
   │      ├── Product
   │      └── Product
   │
   └── Subcategory
```

<p>
Administrators can:
</p>

<ul>
<li>➕ Create folders/categories</li>
<li>✏️ Edit categories</li>
<li>🗑️ Delete categories</li>
<li>➕ Add products</li>
<li>✏️ Edit products</li>
<li>🗑️ Delete products</li>
<li>↕️ Change display ordering</li>
<li>🖱️ Move products between folders</li>
</ul>

---

<h2>🖱️ Drag & Drop Ordering</h2>

<p>
The administration interface includes backend endpoints designed to persist
display ordering.
</p>

```text id="6br50k"
Drag Item
   │
   ▼
New Position
   │
   ▼
JavaScript Request
   │
   ▼
Django Update
   │
   ▼
display_order
```

<p>
This is implemented for both product/category organization and service
organization.
</p>

---

<h2>🧪 Advanced Admin SQL Console</h2>

<p>
The Admin application also contains an advanced SQL-console-style management
view restricted with Django's <code>user_passes_test</code>.
</p>

<p>
It supports:
</p>

<ul>
<li>▶️ Execute SQL statements</li>
<li>🔎 Display SELECT results</li>
<li>✏️ Execute UPDATE/INSERT statements</li>
<li>🗑️ Delete selected rows</li>
<li>🔄 Refresh query results</li>
<li>💾 Atomic transactions for multi-statement operations</li>
</ul>

<p>
This feature is intended for administrator/developer operations and should be
treated as a powerful internal tool.
</p>

---

<h2>📂 Project Structure</h2>

```text id="4x5y8f"
Falcon7.1/
│
├── Accounts/
│   ├── models.py
│   ├── views.py
│   ├── otp.py
│   ├── urls.py
│   └── migrations/
│
├── Admin/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── Bookings/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── services/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── Falcon/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── Core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── templates/
│   ├── Auth/
│   ├── Bookings/
│   ├── Falcon/
│   ├── admin/
│   └── service/
│
├── static/
│   ├── Falcon/
│   ├── base/
│   ├── fonts/
│   └── images/
│
├── media/
│
├── manage.py
└── db.sqlite3
```

---

<h2>📸 Screenshots</h2>

<p>
Falcon 7.1 contains dedicated frontend assets and branded imagery, making it
well suited for visual documentation.
</p>

<p align="center">
  <img src="docs/images/homepage.png" width="900" alt="Falcon Tech World Homepage">
</p>

<p align="center">
  <em>🦅 Falcon Tech World homepage</em>
</p>

<p align="center">
  <img src="docs/images/services.png" width="900" alt="Falcon Services">
</p>

<p align="center">
  <em>🛠️ Service catalog</em>
</p>

<p align="center">
  <img src="docs/images/booking.png" width="900" alt="Falcon Booking">
</p>

<p align="center">
  <em>📅 Service booking workflow</em>
</p>

<p align="center">
  <img src="docs/images/admin-dashboard.png" width="900" alt="Falcon Admin Dashboard">
</p>

<p align="center">
  <em>👑 Administration dashboard</em>
</p>

---

<h2>🎞️ GIF Demonstrations</h2>

<p>
Recommended demonstrations for the project README:
</p>

```text id="n2kn5e"
docs/
└── demo/
    ├── product-browse.gif
    ├── service-selection.gif
    ├── booking-flow.gif
    ├── otp-login.gif
    └── admin-management.gif
```

<p align="center">
  <img src="docs/demo/booking-flow.gif" width="900" alt="Falcon Booking Demo">
</p>

---

<h2>🎥 Video Demonstration</h2>

<p align="center">
  <a href="YOUR-YOUTUBE-VIDEO-LINK">
    <img src="docs/images/video-thumbnail.png" width="900" alt="Falcon Tech World Demonstration">
  </a>
</p>

<p align="center">
  ▶️ <strong>Watch the complete Falcon 7.1 walkthrough</strong>
</p>

---

<h2>⚠️ Limitations & Development Notes</h2>

<ul>
<li>The repository currently uses SQLite for development.</li>
<li>The project does not currently provide a root <code>requirements.txt</code>.</li>
<li>The development settings currently have <code>DEBUG = True</code>.</li>
<li>The Django secret key is currently stored directly in <code>Core/settings.py</code>.</li>
<li>OTP email credentials are loaded from a local <code>cred.json</code> file and therefore need secure secret handling.</li>
<li>The admin SQL console is a powerful internal feature and should not be exposed to untrusted users.</li>
<li>The current media/static setup is development-oriented.</li>
<li>The repository contains many generated <code>__pycache__</code> files that should ideally be ignored.</li>
</ul>

---

<h2>🔒 Security Notes</h2>

<p>
Before deploying Falcon 7.1 publicly, move secrets and environment-specific
configuration outside the source tree.
</p>

<p>
In particular, the current project contains:
</p>

<ul>
<li>🔑 Django secret key in <code>Core/settings.py</code></li>
<li>📧 Email application credentials loaded by <code>Accounts/otp.py</code></li>
<li>🌐 Production host/domain configuration inside settings</li>
</ul>

<p>
Use environment variables or a dedicated secret manager instead.
</p>

<p>Recommended pattern:</p>

```python id="pfjjtc"
import os

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
```

<p>
Any credentials previously committed to a public repository should be rotated.
</p>

---

<h2>🔮 Future Improvements / Roadmap</h2>

<table>
<tr>
<td>📦 Dependency Management</td>
<td>Add and maintain a proper requirements.txt or pyproject.toml.</td>
</tr>

<tr>
<td>🔐 Environment Configuration</td>
<td>Move secrets, host configuration and email credentials to environment variables.</td>
</tr>

<tr>
<td>📱 Mobile Experience</td>
<td>Further optimize the customer booking and service experience for mobile devices.</td>
</tr>

<tr>
<td>💳 Payments</td>
<td>Add integrated online payments for service and product workflows where required.</td>
</tr>

<tr>
<td>👨‍🔧 Technician Management</td>
<td>Add technician accounts, assignment and field-service workflows.</td>
</tr>

<tr>
<td>📍 Live Tracking</td>
<td>Extend the current coordinate functionality into technician/customer tracking.</td>
</tr>

<tr>
<td>📊 Analytics</td>
<td>Add sales, service, booking and customer analytics.</td>
</tr>

<tr>
<td>🔔 Notifications</td>
<td>Add automated booking-status notifications through email/SMS/WhatsApp.</td>
</tr>

<tr>
<td>🐘 PostgreSQL</td>
<td>Move to a production database backend.</td>
</tr>

<tr>
<td>🚀 Production Deployment</td>
<td>Add Gunicorn, reverse proxy, HTTPS and deployment configuration.</td>
</tr>
</table>

---

<h2>👨‍💻 Author</h2>

<p align="center">

<strong>Yasir Khan</strong><br>
Full Stack Developer • Django Developer • E-commerce & Service Platform Developer

<br><br>

<a href="https://github.com/yasirkhan251">
  <img src="https://img.shields.io/badge/GitHub-yasirkhan251-181717?style=for-the-badge&logo=github">
</a>

<a href="https://yasirkhan.in">
  <img src="https://img.shields.io/badge/Portfolio-yasirkhan.in-0A66C2?style=for-the-badge">
</a>

</p>

---

<h2>📜 License</h2>

<p>
Add a dedicated license file before distributing Falcon 7.1 for external use.
</p>

---

<p align="center">
  <strong>🦅 Falcon 7.1 — Connecting customers, products, services and bookings in one platform.</strong>
</p>