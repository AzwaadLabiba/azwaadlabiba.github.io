from flask_frozen import Freezer
from app import app
import os
import shutil

DEST = 'docs'

app.config['FREEZER_DESTINATION'] = DEST
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_REMOVE_EXTRA_FILES'] = True   # wipe stale files on each build

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()

    # Give extension-less pages a .html extension so GitHub Pages serves them as HTML
    for filename in os.listdir(DEST):
        filepath = os.path.join(DEST, filename)
        if os.path.isfile(filepath) and '.' not in filename:
            shutil.move(filepath, filepath + '.html')
            print(f"Renamed: {filename} -> {filename}.html")

    # Stop GitHub Pages from running Jekyll on the output
    open(os.path.join(DEST, '.nojekyll'), 'w').close()

    print(f"\nSite frozen into {DEST}/")