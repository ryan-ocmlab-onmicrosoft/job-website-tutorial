# My First Web Application

## How to carete favicon.ico

visit URL = https://favicon.io I try TEXT -> ICO
change the icon attributes : Text, Background, Font Family, Font Variant, Font Size to get desired result. Preview will be shown in left upper corner.

Download it as you love it. Download button is located in right upper corner.

Base on Flask requirement, download favicon.ico file MUST be stored in /static folder. Add the program statements below :

```python
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
```

## SEO; Search Engine Optimization