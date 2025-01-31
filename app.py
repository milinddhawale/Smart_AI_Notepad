from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Basic Config
    app.config['SECRET_KEY'] = 'Milind@03'  # Change this!
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notepad.db'
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Register blueprints (we'll create these next)
    from routes.auth import auth_bp
    from routes.notes import notes_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)