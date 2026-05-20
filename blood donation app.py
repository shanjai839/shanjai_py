

"""Blood  Donation App - Console version (pure Python, no Flask)
Run: py blood_app_console.py"""


import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "blood_bank.db"
BLOOD_GROUPS = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.executescript(
            
           ''' CREATE TABLE IF NOT EXISTS donors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                blood_group TEXT NOT NULL,
                phone TEXT NOT NULL,
                city TEXT NOT NULL,
                age INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                blood_group TEXT NOT NULL,
                hospital TEXT NOT NULL,
                city TEXT NOT NULL,
                contact_phone TEXT NOT NULL,
                status TEXT DEFAULT 'open'
            );'''
        
        )


def register_donor():
    print("\n--- Register Donor ---")
    name = input("Name: ").strip()
    print("Blood groups:", ", ".join(BLOOD_GROUPS))
    blood = input("Blood group: ").strip().upper().replace(" ", "")
    phone = input("Phone: ").strip()
    city = input("City: ").strip()
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        return
    if blood not in BLOOD_GROUPS:
        print("Invalid blood group.")
        return
    if age < 18 or age > 65:
        print("Age must be 18-65.")
        return
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO donors (name, blood_group, phone, city, age) VALUES (?,?,?,?,?)",
            (name, blood, phone, city, age),
        )
    print(f"Thank you {name}! Registered as donor.")


def list_donors():
    print("\n--- All Donors ---")
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM donors ORDER BY id").fetchall()
    if not rows:
        print("No donors yet.")
        return
    for d in rows:
        print(f"  [{d['id']}] {d['name']} | {d['blood_group']} | {d['city']} | {d['phone']}")


def post_request():
    print("\n--- Post Blood Request ---")
    patient = input("Patient name: ").strip()
    print("Blood groups:", ", ".join(BLOOD_GROUPS))
    blood = input("Blood needed: ").strip().upper().replace(" ", "")
    hospital = input("Hospital: ").strip()
    city = input("City: ").strip()
    phone = input("Contact phone: ").strip()
    if blood not in BLOOD_GROUPS:
        print("Invalid blood group.")
        return
    with get_connection() as conn:
        conn.execute(
           ''' INSERT INTO requests (patient_name, blood_group, hospital, city, contact_phone)
               VALUES (?,?,?,?,?),
            (patient, blood, hospital, city, phone),'''
        )
    print("Request posted.")


def list_requests():
    print("\n--- Open Requests ---")
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM requests WHERE status='open' ORDER BY id"
        ).fetchall()
    if not rows:
        print("No open requests.")
        return
    for r in rows:
        print(
            f"  [{r['id']}] {r['patient_name']} needs {r['blood_group']} "
            f"at {r['hospital']}, {r['city']} | {r['contact_phone']}"
        )


def find_match():
    try:
        req_id = int(input("\nEnter request ID to find donors: "))
    except ValueError:
        print("Invalid ID.")
        return
    with get_connection() as conn:
        req = conn.execute("SELECT * FROM requests WHERE id=?", (req_id,)).fetchone()
        if not req:
            print("Request not found.")
            return
        donors = conn.execute(
            "SELECT * FROM donors WHERE blood_group=? AND city=?",
            (req["blood_group"], req["city"]),
        ).fetchall()
    print(f"\nMatching donors for {req['blood_group']} in {req['city']}:")
    if not donors:
        print("  No match in same city. Check all donors with same blood group.")
        with get_connection() as conn:
            donors = conn.execute(
                "SELECT * FROM donors WHERE blood_group=?", (req["blood_group"],)
            ).fetchall()
    for d in donors:
        print(f"  {d['name']} | {d['phone']} | {d['city']}")


def main():
    init_db()
    while True:
        print("\n===== BLOOD DONATION APP =====")
        print("1. Register donor")
        print("2. List donors")
        print("3. Post blood request")
        print("4. List open requests")
        print("5. Find matching donors")
        print("6. Exit")
        choice = input("Choose (1-6): ").strip()
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()






