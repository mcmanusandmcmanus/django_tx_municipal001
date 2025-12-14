# Municipal Equity Lab

Hypothesis-led racial equity analytics with transparent governance. Built with Django for safe deployment on Render or similar platforms.

## Local setup
1. (Optional) `python -m venv .venv && .\\.venv\\Scripts\\activate`
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver` and open `http://localhost:8000/`

Environment variables (see `.env.example`):
- `DJANGO_SECRET_KEY` (required in prod)
- `DJANGO_DEBUG` (set to `False` in prod)
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL` (Postgres on Render)

## Deployment (Render)
- Create a Web Service pointing to this repo.
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn municipal_site.wsgi --log-file -`
- Add env vars above; set `DATABASE_URL` from the Render Postgres add-on.
- Static files served by WhiteNoise; no extra CDN config required.

## What’s inside
- Security-forward Django settings (HSTS, secure cookies, WhiteNoise, env-driven secrets).
- Core homepage showcasing hypothesis discipline and 10+ analysis playbooks spanning business stats, causal inference, and ML.
- Ready to extend with APIs, dashboards, or notebook integrations.
