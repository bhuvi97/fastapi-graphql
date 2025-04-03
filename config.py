app_config = {
    "title": "FastAPI Application",
    "version": "1.0.0",
    "docs_url": "/docs",
}

import os

DB_USERNAME = os.getenv("DB_USERNAME", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "2pMQH;O%Q-Eg$5w")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = "3306"
DB_NAME = os.getenv("DB_NAME", "Institution")

# Asynchronous database URL
SQLALCHEMY_DATABASE_URL = f"mysql+asyncmy://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:pass@localhost/mydb")

settings = Settings()