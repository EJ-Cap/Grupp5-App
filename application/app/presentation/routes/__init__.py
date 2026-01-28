"""Application routes."""

from flask import Flask


def register_routes(app: Flask) -> None:
    """Register all route blueprints."""
    
    @app.route("/")
    def index():
        """Home route."""
        return {"message": "Welcome to Flask app!"}, 200
    
    @app.route("/health")
    def health():
        """Health check route."""
        return {"status": "healthy"}, 200
