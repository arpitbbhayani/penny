import os
from app import app

BIN_PATH = os.path.join(os.getcwd(), 'bin')
os.environ["PATH"] += os.pathsep + BIN_PATH

# Start the server
app.run(debug=True, port=10101)
