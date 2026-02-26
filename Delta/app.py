from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date, datetime

print("THIS IS THE CORRECT APP FILE")

app = Flask(__name__, template_folder="templates")


# -----------------------------
# DATABASE CONNECTION FUNCTION
# -----------------------------
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# -----------------------------
# INITIALIZE DATABASE
# -----------------------------
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            source TEXT,
            status TEXT,
            notes TEXT,
            follow_up_date TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            score INTEGER
        )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# SCREEN 1 — LEAD LISTING
# -----------------------------
@app.route("/")
def home():
    conn = get_db_connection()
    leads = conn.execute("SELECT * FROM leads").fetchall()
    conn.close()

    enriched_leads = []

    for lead in leads:
        lead_dict = dict(lead)

        # Aging logic (older than 2 days and still New)
        created_date = datetime.strptime(lead_dict["created_at"], "%Y-%m-%d %H:%M:%S")
        days_old = (datetime.now() - created_date).days

        lead_dict["is_aging"] = True if days_old > 2 and lead_dict["status"] == "New" else False

        enriched_leads.append(lead_dict)

    return render_template("leads.html", leads=enriched_leads)


# -----------------------------
# SCREEN 2 — LEAD DETAILS
# -----------------------------
@app.route("/lead/<int:lead_id>")
def lead_detail(lead_id):
    conn = get_db_connection()
    lead = conn.execute(
        "SELECT * FROM leads WHERE id = ?",
        (lead_id,)
    ).fetchone()
    conn.close()

    return render_template("lead_detail.html", lead=lead)


# -----------------------------
# SCREEN 3 — LEAD MANAGEMENT
# -----------------------------
@app.route("/manage", methods=["GET", "POST"])
def manage_lead():

    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        source = request.form["source"]
        status = request.form["status"]
        notes = request.form["notes"]
        follow_up_date = request.form["follow_up_date"]

        # -----------------------
        # LEAD SCORING AUTOMATION
        # -----------------------
        score = 0

        if source == "Facebook":
            score += 5
        elif source == "Google":
            score += 8
        elif source == "Website":
            score += 10

        if status == "Test Drive Scheduled":
            score += 20

        if status == "Closed Won":
            score += 30

        conn = get_db_connection()

        conn.execute("""
            INSERT INTO leads 
            (name, phone, email, source, status, notes, follow_up_date, score)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, phone, email, source, status, notes, follow_up_date, score))

        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    return render_template("manage_lead.html")


# -----------------------------
# SCREEN 4 — DASHBOARD
# -----------------------------
@app.route("/dashboard")
def dashboard():
    conn = get_db_connection()

    total = conn.execute("SELECT COUNT(*) FROM leads").fetchone()[0]
    new = conn.execute("SELECT COUNT(*) FROM leads WHERE status='New'").fetchone()[0]
    contacted = conn.execute("SELECT COUNT(*) FROM leads WHERE status='Contacted'").fetchone()[0]
    closed_won = conn.execute("SELECT COUNT(*) FROM leads WHERE status='Closed Won'").fetchone()[0]

    # Conversion rate automation
    conversion_rate = 0
    if total > 0:
        conversion_rate = round((closed_won / total) * 100, 2)

    # Follow-up automation (today’s follow-ups)
    today = date.today().isoformat()

    follow_ups = conn.execute(
        "SELECT * FROM leads WHERE follow_up_date = ?",
        (today,)
    ).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total=total,
        new=new,
        contacted=contacted,
        closed_won=closed_won,
        conversion_rate=conversion_rate,
        follow_ups=follow_ups
    )


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)