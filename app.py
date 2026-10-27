import json
from datetime import date, datetime
from pathlib import Path

from flask import Flask, render_template

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)


def load_updates():
    """Read data/updates.json and return entries newest-first.

    Each entry: {"date": "YYYY-MM", "title": str, "tag": str, "body": str,
                 "icon": "fa-..." (optional), "link": url (optional),
                 "link_label": str (optional), "highlight": bool (optional)}
    """
    with open(BASE_DIR / "data" / "updates.json", encoding="utf-8") as f:
        items = json.load(f)
    for it in items:
        d = datetime.strptime(it["date"], "%Y-%m")
        it["year"] = d.year
        it["month"] = d.strftime("%b")
        it["display_date"] = d.strftime("%B %Y")
    return sorted(items, key=lambda x: x["date"], reverse=True)


@app.context_processor
def inject_globals():
    return {"current_year": date.today().year}


@app.route("/")
def index():
    return render_template("index.html", title="Home", updates=load_updates()[:3])


@app.route("/education")
@app.route("/education.html")
def education():
    return render_template("education.html", title="Education")


@app.route("/experience")
@app.route("/experience.html")
def experience():
    return render_template("experience.html", title="Experience")


@app.route("/publications")
@app.route("/publications.html")
def publications():
    return render_template("publications.html", title="Publications")


@app.route("/achievements")
@app.route("/achievements.html")
def achievements():
    return render_template("achievements.html", title="Achievements")


@app.route("/updates")
@app.route("/updates.html")
def updates():
    return render_template("updates.html", title="Life Updates", updates=load_updates())


if __name__ == "__main__":
    app.run(debug=True, port=8000)
