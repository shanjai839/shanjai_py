
import json
import os
import webbrowser

BLOOD_GROUPS = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
FILE_NAME = "blood_data.json"


# Load data from file
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {"donors": [], "requests": []}


# Save data to file
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Load existing data
data = load_data()


# Register donor
def register_donor():
    print("--- REGISTER DONOR ---")

    name = input("Enter Name: ")
    print("Blood Groups:", ", ".join(BLOOD_GROUPS))

    blood = input("Enter Blood Group: ").upper().strip()
    phone = input("Enter Phone Number: ")
    city = input("Enter City: ")

    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid Age!")
        return

    if blood not in BLOOD_GROUPS:
        print("Invalid Blood Group!")
        return

    donor = {
        "name": name,
        "blood_group": blood,
        "phone": phone,
        "city": city,
        "age": age
    }

    data["donors"].append(donor)
    save_data()

    print("Donor Registered Successfully!")


# List donors
def list_donors():
    print("--- DONOR LIST ---")

    if len(data["donors"]) == 0:
        print("No donors available.")
        return

    for i, donor in enumerate(data["donors"], start=1):
        print(
            f"{i}. {donor['name']} | "
            f"{donor['blood_group']} | "
            f"{donor['city']} | "
            f"{donor['phone']}"
        )


# Add blood request
def post_request():
    print("--- BLOOD REQUEST ---")

    patient = input("Patient Name: ")
    print("Blood Groups:", ", ".join(BLOOD_GROUPS))

    blood = input("Blood Needed: ").upper().strip()
    hospital = input("Hospital Name: ")
    city = input("City: ")
    phone = input("Contact Number: ")

    if blood not in BLOOD_GROUPS:
        print("Invalid Blood Group!")
        return

    request = {
        "patient_name": patient,
        "blood_group": blood,
        "hospital": hospital,
        "city": city,
        "phone": phone
    }

    data["requests"].append(request)
    save_data()

    print("Blood Request Added Successfully!")


# List requests
def list_requests():
    print("--- BLOOD REQUESTS ---")

    if len(data["requests"]) == 0:
        print("No blood requests found.")
        return

    for i, req in enumerate(data["requests"], start=1):
        print(
            f"{i}. {req['patient_name']} needs "
            f"{req['blood_group']} blood at "
            f"{req['hospital']} ({req['city']}) "
            f"| Phone: {req['phone']}"
        )


# Find matching donors
def find_match():
    print("--- FIND MATCHING DONORS ---")

    blood = input("Enter Blood Group Needed: ").upper().strip()
    city = input("Enter City: ")

    found = False

    for donor in data["donors"]:
        if donor["blood_group"] == blood and donor["city"].lower() == city.lower():
            print(
                f"{donor['name']} | "
                f"{donor['phone']} | "
                f"{donor['city']}"
            )
            found = True

    if not found:
        print("No matching donors found.")


# tips
def blood_tips():
    print("--- BLOOD DONATION TIPS ---")

    ask = input("Do you want Blood Donation Tips video? (yes/no): ").lower()

    if ask == "yes":
        webbrowser.open("https://youtu.be/jrSJVXy7WoA?si=CUXta8EsQLMD9YtU")
        print("Opening YouTube video...")

    elif ask == "no":
        print("Okay! Showing tips only.")

    else:
        print("Invalid choice!")

    print("Blood Donation Tips:")
    print("1. Drink plenty of water before donation.")
    print("2. Eat healthy food before donating blood.")
    print("3. Sleep at least 6-8 hours.")
    print("4. Avoid smoking and alcohol.")
    print("5. Wear comfortable clothes.")
    print("6. Take rest after donation.")


# Eligibility 
def eligibility():
    print("--- ELIGIBILITY TO DONATE BLOOD ---")
    print("1. Age must be 18 to 65 years.")
    print("2. Weight must be at least 50 kg.")
    print("3. Must be healthy.")
    print("4. No fever or major illness.")
    print("5. Hemoglobin level should be normal.")
    print("6. 3 months gap after last donation.")


# # Delete donor
def delete_donor():
    print("--- DELETE DONOR ---")

    if len(data["donors"]) == 0:
        print("No donors available.")
        return

    list_donors()

    try:
        index = int(input("Enter donor number to delete: "))

        if index >= 1 and index <= len(data["donors"]):
            deleted = data["donors"].pop(index - 1)
            save_data()
            print(deleted["name"], "deleted successfully!")

        else:
            print("Invalid donor number!")

    except ValueError:
        print("Enter valid number!")


# Delete request
def delete_request():
    print("--- DELETE REQUEST ---")

    if len(data["requests"]) == 0:
        print("No requests available.")
        return

    list_requests()

    try:
        index = int(input("Enter request number to delete: "))

        if index >= 1 and index <= len(data["requests"]):
            data["requests"].pop(index - 1)
            save_data()
            print("Request deleted successfully!")

        else:
            print("Invalid request number!")

    except ValueError:
        print("Enter valid number!")



 # Main Menu
def main():
    while True:
        print("===== BLOOD DONATION APP =====")
        print("1. Register Donor")
        print("2. List Donors")
        print("3. Post Blood Request")
        print("4. List Requests")
        print("5. Find Matching Donors")
        print("6. Blood Donation Tips")
        print("7. Eligibility to Donate Blood")
        print("8. Delete Donor")
        print("9. Delete Blood Request")
        print("10. Exit")

        choice = input("Choose option (1-10): ")

        if choice == "1":
            register_donor()

        elif choice == "2":
            list_donors()

        elif choice == "3":
            post_request()

        elif choice == "4":
            list_requests()

        elif choice == "5":
            find_match()

        elif choice == "6":
            blood_tips()

        elif choice == "7":
            eligibility()

        elif choice == "8":
            delete_donor()

        elif choice == "9":
            delete_request()

        elif choice == "10":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


main()

