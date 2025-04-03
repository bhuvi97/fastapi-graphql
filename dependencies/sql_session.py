from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
# Asynchronous database URL
SQLALCHEMY_DATABASE_URL = f"mysql+asyncmy://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create async engine
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Async session maker
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)


# Dependency to get the async session
async def get_db() -> AsyncSession:
    """
    Creates the database session
    :return: Yields the session
    """
    async with AsyncSessionLocal() as session:
        yield session
