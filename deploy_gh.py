#!/usr/bin/env python3
"""Skapa GitHub-repo, pusha sajten och aktivera GitHub Pages."""
import os, re, json, subprocess, urllib.request
from pathlib import Path

ROOT = Path("/home/clawd/business-breakdown")
REPO = "business-breakdown"
OWNER = "oskarhellmer-dev"

creds = Path.home() / ".git-credentials"
txt = creds.read_text()
m = re.search(r"https://[^:]+:([^@]+)@github\.com", txt)
TOKEN = m.group(1)
print("token hittad:", len(TOKEN), "tecken")

def api(method, path, data=None):
    req = urllib.request.Request(
        "https://api.github.com" + path,
        data=json.dumps(data).encode() if data else None,
        headers={"Authorization": f"token {TOKEN}",
                 "Accept": "application/vnd.github+json",
                 "User-Agent": "hermes"},
        method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode() or "{}")

# 1. skapa repo (ignorera om det finns)
st, body = api("POST", "/user/repos", {"name": REPO, "private": False,
                                       "description": "The Margin — landing page + lead magnet"})
print("skapa repo:", st, body.get("full_name") if isinstance(body, dict) else body)

# 2. git init + push
def run(cmd, **kw):
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, **kw)

(ROOT / "README.md").write_text("# The Margin\n\nLanding page + lead magnet.\n")
run(["git", "init", "-q"])
run(["git", "add", "-A"])
run(["git", "-c", "user.email=oskarhellmer-dev@users.noreply.github.com",
     "-c", "user.name=oskarhellmer-dev", "commit", "-q", "-m", "The Margin: landing page + lead magnet"])
run(["git", "branch", "-M", "main"])
run(["git", "remote", "remove", "origin"])
run(["git", "remote", "add", "origin", f"https://{TOKEN}@github.com/{OWNER}/{REPO}.git"])
p = run(["git", "push", "-u", "origin", "main", "--force"])
print("push:", p.returncode, (p.stderr or p.stdout)[-200:])

# 3. aktivera Pages (build_type=workflow kräver workflow; använd legacy branch-build)
for payload in [{"source": {"branch": "main", "path": "/"}},
                {"build_type": "legacy", "source": {"branch": "main", "path": "/"}}]:
    st, body = api("POST", f"/repos/{OWNER}/{REPO}/pages", payload)
    print("pages:", st, body.get("html_url") if isinstance(body, dict) else body)
    if st in (201, 409, 422):
        break

st, body = api("GET", f"/repos/{OWNER}/{REPO}/pages")
print("pages-status:", st, body.get("html_url") if isinstance(body, dict) else body)
print("URL: https://%s.github.io/%s/" % (OWNER, REPO))
