import asyncio
from websockets.server import serve

async def server(host: str, port: int, func):
    async with serve(func, host, port):
        await asyncio.Future()  # run forever
