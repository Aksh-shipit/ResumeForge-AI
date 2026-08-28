from flask import Flask
from config import Config
from extensions import db, bcrypt, login_manager

from models.user import User
from models.resume import Resume
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "main.login"   


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from routes.main import main
app.register_blueprint(main)


with app.app_context():
    db.create_all()

@app.context_processor
def inject_current_year():
    return {
        "current_year": datetime.now().year
    }
if __name__ == "__main__":
    app.run(debug=True)