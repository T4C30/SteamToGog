python -m venv .venv
# En terminal bash
source .venv/bin/activate
pip install -r requirements.txt
pyinstaller --onefile main.py
deactivate
cd dist