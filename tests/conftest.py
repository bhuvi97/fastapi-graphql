import pytest_asyncio
from httpx import AsyncClient
from main import app


@pytest_asyncio.fixture(scope="module")
async def async_client():
    # initialize and yield the AsyncClient
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
