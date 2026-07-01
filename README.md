# Health Prediction Application

## Project Overview

This project is a Health Prediction Application developed as part of the Junior AI/ML Developer Technical Assessment.

The application allows users to:

- Add patient records
- View patient records
- Update patient records
- Delete patient records
- Predict possible health conditions using Google Gemini AI
- Store patient records in SQLite database

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Bootstrap
- SQLite
- Google Gemini API
- Flask-SQLAlchemy

---

## Features

- CRUD Operations
- AI-based Health Prediction
- Input Validation
- SQLite Database
- Responsive User Interface

---

## Project Structure

```
HealthPredictionApp
│
├── app.py
├── config.py
├── requirements.txt
├── models/
├── services/
├── templates/
├── static/
└── database/
```

---

## Installation

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## AI Integration

The application integrates with the Google Gemini API.

When patient blood test values are submitted, the application sends them to the external AI API, which analyzes the values and predicts a possible health condition. The prediction is displayed in the **Remarks** field.

---

## Developer

Vasuki Moger