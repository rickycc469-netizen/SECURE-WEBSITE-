# Optional local preview server for the SECURE website.
# GitHub Pages does not run Python; it serves index.html, style.css, and script.js.
# To preview locally with Python installed, run: python main.py
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)
address = ("0.0.0.0", 8000)
print("SECURE website preview: http://localhost:8000")
ThreadingHTTPServer(address, SimpleHTTPRequestHandler).serve_forever()
