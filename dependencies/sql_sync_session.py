from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
# synchronous database URL
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create DB sync engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# session maker
SyncSessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


# Dependency to get the DB session
def get_db_sync():
    """
    Creates the database session
    :return: Yields the session
    """
    with SyncSessionLocal() as sync_session:
        yield sync_session