python -m venv venv
source venv/bin/activate

pip install fastapi
pip install uvicorn
pip install gitpython
pip install groq
pip install python-dotenv
pip install PyGithub

to clean cache : find . -type d -name "__pycache__" -exec rm -rf {} +
check cache : find . -name "__pycache__"

