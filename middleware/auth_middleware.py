from fastapi import Request
from fastapi.responses import JSONResponse

async def auth_middleware(request: Request, call_next):

    if request.url.path == "/graphql":
        token = request.headers.get("authorization")
        if not (token and token.startswith("Bearer")):
            return JSONResponse(status_code=403, content={"error": "unauthorized"})
    response = await call_next(request)
    return response