# Portfolio (Flask + Frozen-Flask)

## Run / build
pip install flask frozen-flask
python app.py        # dev server at http://localhost:8000
python freeze.py     # static site in build/ → push its contents to your github.io repo

## Add a life update
Edit data/updates.json (newest is sorted to the top automatically; home page shows latest 3):
{
  "date": "2026-11",            // YYYY-MM
  "title": "Paper accepted at …",
  "tag": "Paper",               // any short label
  "icon": "fa-trophy",          // optional Font Awesome solid icon
  "body": "One or two sentences.",
  "link": "https://…",          // optional
  "link_label": "Read paper",   // optional
  "highlight": true             // optional: terracotta outline + "Latest"
}

Keep your photo at static/uploads/azwaad.png.
