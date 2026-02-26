# 🚗 TorqueLeads – Automotive Lead Management System

TorqueLeads is a web-based Lead Management System developed for HSR Motors to streamline and automate their sales workflow. It replaces manual spreadsheet tracking with a centralized, structured, and analytics-driven solution designed for automotive dealerships.

---

## 📌 Problem Statement

HSR Motors receives leads from multiple sources such as Facebook, Google, website inquiries, and offline campaigns. Previously, these leads were managed using spreadsheets, which lacked:

* Real-time collaboration
* Structured sales workflow
* Automated follow-up tracking
* Performance analytics

TorqueLeads solves this problem by providing a unified CRM platform tailored for dealership operations.

---

## 🚀 Features

### 🔹 Lead Listing

View all leads in a structured table with status, score, and creation date.

### 🔹 Lead Details

Access complete customer information including notes and follow-up dates.

### 🔹 Lead Management

Add new leads through a structured form and move them through a defined lifecycle:
New → Contacted → Qualified → Test Drive Scheduled → Closed Won → Closed Lost

### 🔹 Automated Lead Scoring

Leads are automatically assigned scores based on source and status progression to help prioritize high-value opportunities.

### 🔹 Follow-Up Reminder System

Leads with scheduled follow-ups are automatically highlighted on the dashboard.

### 🔹 Aging Lead Detection

Leads older than 2 days and still marked as "New" are flagged for action.

### 🔹 Business Dashboard

Displays:

* Total Leads
* New Leads
* Contacted Leads
* Closed Deals
* Conversion Rate
* Today’s Follow-Ups

---

## 🛠 Tech Stack

* **Backend:** Python (Flask)
* **Database:** SQLite
* **Frontend:** HTML, Bootstrap
* **Architecture:** MVC-style structure

---

## 📂 Project Structure

```
hsr-motors-lead-manager/
│
├── app.py
├── database.db
├── templates/
│   ├── base.html
│   ├── leads.html
│   ├── lead_detail.html
│   ├── manage_lead.html
│   └── dashboard.html
```

---

## ▶️ How to Run the Project

1. Clone the repository

```
git clone <your-repo-link>
```

2. Navigate to the project folder

```
cd hsr-motors-lead-manager
```

3. Install dependencies

```
pip install flask
```

4. Run the application

```
python app.py
```

5. Open in browser

```
http://127.0.0.1:5000
```

---

## 🎯 Future Improvements

* User authentication (Sales vs Manager roles)
* Chart-based dashboard analytics
* Export to Excel
* REST API integration
* Cloud deployment

---

## 👤 Rujula S

Developed as part of a product-focused web application assignment to demonstrate workflow design, automation integration, and analytics-driven decision-making.

---
