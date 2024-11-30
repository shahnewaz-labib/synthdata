import numpy as np
import pandas as pd


def weighted_random_choice(items_with_probabilities):
    items, probabilities = zip(*items_with_probabilities)

    probabilities = np.array(probabilities)
    probabilities /= probabilities.sum()

    return np.random.choice(items, p=probabilities)


service_name_with_probabilities = [
    ("Bite Registration", 0.05),
    ("Bite Registration for Complete Denture", 0.03),
    ("Cancer Pt Followup", 0.01),
    ("Consultation", 0.10),
    ("Core Build Up", 0.02),
    ("Crown Re-Fit", 0.02),
    ("Crown Supply", 0.09),
    ("Crown Supply Implant", 0.09),
    ("Deep Curatage", 0.01),
    ("Dental Implant- Fixture Placement", 0.09),
    ("Dental Implant- Impression", 0.01),
    ("Dental Implant- Healing Abutment Placement", 0.09),
    ("Denture Adjustment", 0.02),
    ("Denture Supply", 0.02),
    ("Denture Trial", 0.02),
    ("Dressing", 0.01),
    ("Excisional Biopsy", 0.01),
    ("Extraction", 0.03),
    ("Final Impression for Complete Denture", 0.02),
    ("Follow-Up", 0.02),
    ("Gingivectomy", 0.02),
    ("Impression for Crown", 0.02),
    ("Impression for RPD", 0.02),
    ("Impression for Study Model", 0.01),
    ("Interim Denture over Implant", 0.01),
    ("Light Cured Filling", 0.03),
    ("Metal Post Core Supply", 0.02),
    ("Partial Removal Of Broken Tooth", 0.01),
    ("Polishing", 0.02),
    ("Root Canal Treatment", 0.2),
    ("Scaling", 0.08),
    ("Sharp Tooth Grinding", 0.01),
    ("Stitch Off", 0.01),
    ("Surgical Extraction", 0.1),
    ("Vital Pulp Therapy", 0.02),
]

service_name_with_actual_service_price = {
    "Bite Registration": 1500,
    "Bite Registration for Complete Denture": 6000,
    "Cancer Pt Followup": 1200,
    "Consultation": 5000,
    "Core Build Up": 3500,
    "Crown Re-Fit": 5500,
    "Crown Supply": 7000,
    "Crown Supply Implant": 18000,
    "Deep Curatage": 2000,
    "Dental Implant- Fixture Placement": 18000,
    "Dental Implant- Impression": 2500,
    "Dental Implant- Healing Abutment Placement": 12000,
    "Denture Adjustment": 3000,
    "Denture Supply": 5000,
    "Denture Trial": 4500,
    "Dressing": 1500,
    "Excisional Biopsy": 2500,
    "Extraction": 3000,
    "Final Impression for Complete Denture": 5000,
    "Follow-Up": 2500,
    "Gingivectomy": 4000,
    "Impression for Crown": 4000,
    "Impression for RPD": 4500,
    "Impression for Study Model": 2000,
    "Interim Denture over Implant": 5500,
    "Light Cured Filling": 4000,
    "Metal Post Core Supply": 3000,
    "Partial Removal Of Broken Tooth": 2500,
    "Polishing": 1200,
    "Root Canal Treatment": 15000,
    "Scaling": 2500,
    "Sharp Tooth Grinding": 1500,
    "Stitch Off": 2000,
    "Surgical Extraction": 8000,
    "Vital Pulp Therapy": 3500,
}

payment_status_with_probabilities = [("Full Paid", 0.7), ("Due", 0.25), ("Free", 0.05)]
payment_mode_with_probabilities = [
    ("Cash", 0.6),
    ("Bank", 0.1),
    ("Bkash", 0.2),
    ("Nagad", 0.1),
]
doctor_name_with_probabilities = [
    ("Dr. Susan", 0.4),
    ("Dr. John", 0.2),
    ("Dr. Smith", 0.2),
    ("Dr. Alex", 0.2),
]

columns = {
    "Date",
    "Patient ID",
    "Service Name",
    "Paid Amount",
    "Service Price",
    "Discount Amount",
    "Payment Status",
    "Payment Mode",
    "Doctor Name",
}

# MM/DD/YYYY
start_date = "01/01/2021"
end_date = "12/31/2024"

# add a seed for reproducibility
np.random.seed(45)

# print header
print(",".join(columns))

# for each day, generate a random number of records
for date in pd.date_range(start=start_date, end=end_date):
    num_records = np.random.randint(3, 10)
    for _ in range(num_records):
        patient_id = np.random.randint(1000, 9999)
        service_name = weighted_random_choice(service_name_with_probabilities)

        payment_status = weighted_random_choice(payment_status_with_probabilities)
        actual_service_price = service_name_with_actual_service_price[service_name]
        discount_amount = round(np.random.randint(100, actual_service_price // 2), -2)
        payment_mode = weighted_random_choice(payment_mode_with_probabilities)

        if payment_status == "Full Paid":
            service_price = actual_service_price - discount_amount
            paid_amount = service_price
        elif payment_status == "Due":
            service_price = actual_service_price - discount_amount
            paid_amount = round(np.random.randint(100, service_price), -2)
        else:  # Free
            discount_amount = actual_service_price
            service_price = 0
            paid_amount = 0
            payment_mode = "None"

        # doctor_name = np.random.choice(doctor_name_with_probabilities)
        doctor_name = weighted_random_choice(doctor_name_with_probabilities)

        # print in CSV format
        print(
            f"{date.strftime('%m/%d/%Y')},{patient_id},{service_name},{paid_amount},{service_price},{discount_amount},{payment_status},{payment_mode},{doctor_name}"
        )
