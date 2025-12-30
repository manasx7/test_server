```markdown
# test_server
```

Run the Streamlit TCP Server Control Panel locally:

1. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and set `API_KEY` (and `API_URL` if needed):

```bash
cp .env.example .env
# edit .env to set your API_KEY
```

3. Start the app:

```bash
streamlit run streamlit_app.py
```

The app will read `API_URL` and `API_KEY` from environment variables.
# test_server