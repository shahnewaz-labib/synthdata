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

income_columns = {
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

expense_columns = {
    "Date",
    "Purpose",
    "Item",
    "Quantity",
    "Recipient",
    "Amount",
    "Notes",
}

expense_purpose_with_probabilities = [
    ("Material Purchase", 0.3),
    ("Equipment Purchase", 0.2),
    ("Utility", 0.1),
    ("Lab Bill", 0.1),
    ("Rent", 0.1),
    ("Marketing", 0.1),
    ("Maintenance", 0.1),
    ("Staff Salary", 0.4),
]

materials_prices = {
    "Adhesive Bonding Agent": 1500,
    "Alginate Impression Material": 1800,
    "Amalgam Filling Material": 2500,
    "Articulating Paper": 600,
    "Base Plate Wax": 800,
    "Beechwood Sticks": 500,
    "Brass Wire": 400,
    "Burnishing Instrument": 1100,
    "Calcium Hydroxide Paste": 1000,
    "Carbide Burs": 1200,
    "Composites": 2500,
    "Cotton Rolls": 150,
    "Crown & Bridge Remover": 2200,
    "Curette": 800,
    "Cushioning Material": 1000,
    "Cyanoacrylate Adhesive": 150,
    "Disinfectant Spray": 500,
    "Endodontic Files": 2000,
    "Etching Gel": 1000,
    "Glass Ionomer Cement": 2500,
    "Gold Alloy": 8000,
    "Handpieces": 15000,
    "Hemostatic Agents": 700,
    "Impression Trays": 1000,
    "Lab Putty": 1800,
    "Matrix Bands": 700,
    "Melting Wax": 600,
    "Needles (Sterile)": 300,
    "Orthodontic Brackets": 2500,
    "Orthodontic Elastics": 800,
    "Patient Bibs": 100,
    "Periodontal Probes": 500,
    "Rubber Dam": 200,
    "Sodium Hypochlorite": 800,
    "Spreader (Endodontic)": 1000,
    "Sterilization Pouches": 400,
    "Surgical Sutures": 700,
    "Temporary Filling Material": 900,
    "Tooth Whitening Gel": 1500,
    "Universal Bonding Agent": 2000,
    "X-Ray Film": 250,
    "Zinc Oxide Eugenol Cement": 1500,
}

# MM/DD/YYYY
start_date = "01/01/2021"
end_date = "12/31/2024"

np.random.seed(45)

income_data = []
expense_data = []

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

        doctor_name = weighted_random_choice(doctor_name_with_probabilities)

        income_data.append(
            [
                date.strftime("%m/%d/%Y"),
                patient_id,
                service_name,
                paid_amount,
                service_price,
                discount_amount,
                payment_status,
                payment_mode,
                doctor_name,
            ]
        )

    num_expenses = np.random.randint(1, 5)
    for _ in range(num_expenses):
        purpose = weighted_random_choice(expense_purpose_with_probabilities)

        if purpose == "Material Purchase":
            # Randomly select a material without using weighted random choice
            item = np.random.choice(list(materials_prices.keys()))
            amount = materials_prices[item]
            recipient = "Material Supplier"
            notes = f"Purchase of {item}"

        elif purpose == "Staff Salary":
            # Randomly select a doctor and assign a salary
            doctor = weighted_random_choice(doctor_name_with_probabilities)
            salary = np.random.randint(
                10000, 30000
            )  # Random salary between 10k and 30k
            item = f"Salary for {doctor}"
            amount = salary
            recipient = doctor
            notes = f"Salary for {doctor}"

        elif purpose == "Utility":
            # Random utility expenses
            item = "Electricity/Water Bill"
            amount = np.random.randint(500, 2000)
            recipient = "Utility Company"
            notes = "Monthly utility bill"

        elif purpose == "Lab Bill":
            # Random lab bill
            item = "Lab Services"
            amount = np.random.randint(1000, 5000)
            recipient = "Lab Service Provider"
            notes = "Payment for lab services"

        elif purpose == "Rent":
            # Monthly rent expense
            item = "Office Rent"
            amount = np.random.randint(5000, 15000)
            recipient = "Landlord"
            notes = "Monthly office rent payment"

        elif purpose == "Marketing":
            # Marketing expense (e.g., advertising)
            item = "Advertising"
            amount = np.random.randint(1000, 5000)
            recipient = "Advertising Agency"
            notes = "Marketing campaign costs"

        elif purpose == "Maintenance":
            # Maintenance expense (e.g., office repairs)
            item = "Office Maintenance"
            amount = np.random.randint(500, 3000)
            recipient = "Maintenance Service Provider"
            notes = "Maintenance and repairs of office equipment"

        expense_data.append(
            [date.strftime("%m/%d/%Y"), purpose, item, recipient, amount, notes]
        )

income_df = pd.DataFrame(
    income_data,
    columns=[
        "Date",
        "Patient ID",
        "Service Name",
        "Paid Amount",
        "Service Price",
        "Discount Amount",
        "Payment Status",
        "Payment Mode",
        "Doctor Name",
    ],
)

expense_df = pd.DataFrame(
    expense_data,
    columns=["Date", "Purpose", "Item", "Recipient", "Amount", "Notes"],
)

with pd.ExcelWriter("income_and_expense.xlsx") as writer:
    income_df.to_excel(writer, sheet_name="Income", index=False)
    expense_df.to_excel(writer, sheet_name="Expense", index=False)

print("Excel file 'income_and_expense.xlsx' has been created.")
