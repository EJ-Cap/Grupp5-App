"""Flask application factory."""

from flask import Flask
from app.config import config


def create_app(config_name: str = "development") -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config.get(config_name, config["default"]))
    
    # Register blueprints
    from app.presentation.routes import register_routes
    register_routes(app)
    
    return app
