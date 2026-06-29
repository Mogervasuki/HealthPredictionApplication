from flask import Flask, render_template, request, redirect
from config import Config
from models.patient import db, Patient
from services.ai_service import get_health_prediction

import re
from datetime import datetime

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


# ---------------- HOME ---------------- #

@app.route("/")
def home():

    patients = Patient.query.all()

    return render_template(
        "index.html",
        patients=patients
    )


# ---------------- CREATE ---------------- #

@app.route("/add_patient", methods=["POST"])
def add_patient():

    full_name = request.form["full_name"].strip()
    dob = request.form["dob"]
    email = request.form["email"].strip()

    # Email Validation
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(email_pattern, email):
        return "Invalid Email Address"

    # Date Validation
    if dob > datetime.today().strftime("%Y-%m-%d"):
        return "Date of Birth cannot be a future date."

    # Numeric Validation
    try:

        glucose = float(request.form["glucose"])
        haemoglobin = float(request.form["haemoglobin"])
        cholesterol = float(request.form["cholesterol"])

    except ValueError:

        return "Blood test values must be numeric."

    # AI Prediction
    prediction = get_health_prediction(
        glucose,
        haemoglobin,
        cholesterol
    )

    patient = Patient(
        full_name=full_name,
        dob=dob,
        email=email,
        glucose=glucose,
        haemoglobin=haemoglobin,
        cholesterol=cholesterol,
        remarks=prediction
    )

    db.session.add(patient)
    db.session.commit()

    return redirect("/")


# ---------------- DELETE ---------------- #

@app.route("/delete/<int:id>")
def delete_patient(id):

    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)

    db.session.commit()

    return redirect("/")


# ---------------- EDIT ---------------- #

@app.route("/edit/<int:id>")
def edit_patient(id):

    patient = Patient.query.get_or_404(id)

    return render_template(
        "edit.html",
        patient=patient
    )


# ---------------- UPDATE ---------------- #

@app.route("/update/<int:id>", methods=["POST"])
def update_patient(id):

    patient = Patient.query.get_or_404(id)

    patient.full_name = request.form["full_name"].strip()
    patient.dob = request.form["dob"]
    patient.email = request.form["email"].strip()

    # Email Validation
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(email_pattern, patient.email):
        return "Invalid Email Address"

    # DOB Validation
    if patient.dob > datetime.today().strftime("%Y-%m-%d"):
        return "Date of Birth cannot be a future date."

    # Numeric Validation
    try:

        patient.glucose = float(request.form["glucose"])
        patient.haemoglobin = float(request.form["haemoglobin"])
        patient.cholesterol = float(request.form["cholesterol"])

    except ValueError:

        return "Blood test values must be numeric."

    # AI Prediction
    patient.remarks = get_health_prediction(
        patient.glucose,
        patient.haemoglobin,
        patient.cholesterol
    )

    db.session.commit()

    return redirect("/")


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)