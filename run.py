from app import create_app
from dotenv import load_dotenv
from flask_session import Session

load_dotenv()
app = create_app()
app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"     # Store session data in files

# Initialize Flask-Session
Session(app)

if __name__ == "__main__":
    app.run(debug=True)
