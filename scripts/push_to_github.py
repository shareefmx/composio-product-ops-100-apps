"""
Uploads all assignment files to GitHub repository shareefmx/composio-product-ops-100-apps
using the GitHub Contents REST API (handles empty repositories automatically).
"""

import os
import json
import base64
import urllib.request
import urllib.error
import time

TOKEN = os.popen("gh auth token").read().strip()
REPO = "shareefmx/composio-product-ops-100-apps"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "User-Agent": "Composio-ProductOps-Uploader"
}

def put_file(rel_path, full_path):
    url = f"https://api.github.com/repos/{REPO}/contents/{rel_path}"
    with open(full_path, "rb") as fp:
        content = fp.read()
    b64_content = base64.b64encode(content).decode('utf-8')

    data = {
        "message": f"Add {rel_path}",
        "content": b64_content,
        "branch": "main"
    }

    # Check if file exists to get sha if updating
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            existing = json.loads(resp.read().decode('utf-8'))
            data["sha"] = existing["sha"]
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise

    req_data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=req_data, headers=HEADERS, method="PUT")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def upload_all():
    print(f"[*] Uploading files to https://github.com/{REPO}...")
    files_to_upload = []

    # Map files
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(('.pyc', '.DS_Store', '.git')):
                continue
            if '__pycache__' in root:
                continue
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            files_to_upload.append((rel_path, full_path))

    # Add root index.html copied from web/index.html
    web_index = os.path.join(BASE_DIR, "web", "index.html")
    files_to_upload.append(("index.html", web_index))

    # Sort so README and small files go first
    files_to_upload.sort(key=lambda x: os.path.getsize(x[1]))

    for rel_path, full_path in files_to_upload:
        print(f"  -> Uploading: {rel_path} ({os.path.getsize(full_path)} bytes)...")
        put_file(rel_path, full_path)
        time.sleep(0.3)

    print(f"\n[✓] All {len(files_to_upload)} files committed successfully!")

    # Enable GitHub Pages
    pages_url = f"https://api.github.com/repos/{REPO}/pages"
    pages_data = json.dumps({"source": {"branch": "main", "path": "/"}}).encode('utf-8')
    req = urllib.request.Request(pages_url, data=pages_data, headers=HEADERS, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            p_res = json.loads(resp.read().decode('utf-8'))
            print(f"[✓] GitHub Pages active: {p_res.get('html_url')}")
    except urllib.error.HTTPError as e:
        if e.code == 409:
            print("[*] GitHub Pages already configured.")
        else:
            print(f"[!] GitHub Pages note: {e}")

    print(f"\n=======================================================")
    print(f"  LIVE LINKS READY FOR SUBMISSION:")
    print(f"  1. Live Case Study: https://shareefmx.github.io/composio-product-ops-100-apps/")
    print(f"  2. Source Code Repo: https://github.com/{REPO}")
    print(f"=======================================================\n")

if __name__ == "__main__":
    upload_all()
