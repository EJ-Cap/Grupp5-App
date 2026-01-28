"""Flask application entry point."""

import os
from app import create_app

app = create_app(config_name=os.environ.get("FLASK_ENV", "development"))

if __name__ == "__main__":
    app.run()
