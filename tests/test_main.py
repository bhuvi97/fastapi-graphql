import pytest


@pytest.mark.asyncio
async def test_main_route(async_client):
    response = await async_client.get("http://test/")
    assert response.status_code == 200
    assert response.json() == {"Health": "OK"}
