from flask import Flask
from flask_cors import CORS
from models import db
import config
import os

app = Flask(__name__)
app.config.from_object(config)

CORS(app)
db.init_app(app)

@app.route("/")
def home():
    return "Backend Working 👍"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    port = int(os.environ.get("PORT", 5000))  # 👈 important for Render
    app.run(host="0.0.0.0", port=port)
