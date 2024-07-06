from fastapi import FastAPI
from fastapi.responses import FileResponse, Response
from httpx import AsyncClient

app = FastAPI(redoc_url=None, docs_url=None)

@app.get("/skin/pose/{username}/{pose}")
async def skin_pose(username: str, pose: str):
    if not username.startswith("."):
        async with AsyncClient() as client:
            resp = await client.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
            if resp.status_code != 200:
                return FileResponse("img/notfound.png")
    async with AsyncClient() as client:
        resp = await client.get(f"https://starlightskins.lunareclipse.studio/render/{pose}/{username}/full")
    return Response(content=resp.content, media_type="image/png")


