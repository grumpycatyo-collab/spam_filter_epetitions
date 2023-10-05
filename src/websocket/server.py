import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def server(host: str, port: int):
    async with serve(echo, host, port):
        await asyncio.Future()  # run forever

def RunServer(host: str, port: int):
    asyncio.run(server(host, port))