from flask_frozen import Freezer
from app import app
import os
import shutil

# Configure freezer
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    
    # Rename files without extensions to .html
    build_dir = 'build'
    for filename in os.listdir(build_dir):
        filepath = os.path.join(build_dir, filename)
        # If it's a file with no extension (not a directory, not index.html)
        if os.path.isfile(filepath) and '.' not in filename:
            new_filepath = filepath + '.html'
            shutil.move(filepath, new_filepath)
            print(f"Renamed: {filename} -> {filename}.html")
    
    print("\n" + "="*60)
    print("Site frozen successfully!")
    print("Output directory: build/")
    print("="*60)