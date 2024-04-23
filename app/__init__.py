from flask import Flask, render_template

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    
    # Initialize flask extensions here
    db.init_app(app)
    
    # Initialize blueprints here
    
    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')
    
    return app