python -m venv venv
source venv/bin/activate

pip install fastapi
pip install uvicorn
pip install gitpython
pip install groq
pip install python-dotenv
pip install PyGithub
brew install ngrok/ngrok/ngrok
ngrok config add-authtoken 3G4uP34dGupi4jUv1zLOGBdQqNF_4fXeezuKXcKHe3X7oYBhm

uvicorn server:server --reload
webhook on github : https://unhealthy-pried-evaluate.ngrok-free.dev/ 

to clean cache : find . -type d -name "__pycache__" -exec rm -rf {} +
check cache : find . -name "__pycache__"

