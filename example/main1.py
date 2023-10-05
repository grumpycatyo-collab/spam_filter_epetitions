import asyncio
from src.websocket.server import server

async def echo(websocket):
    async for message in websocket:
        await websocket.send(censoring(message))

def censoring(msg: str) -> str:
    if msg == "bai":
        return "censored"
    return msg

if __name__ == "__main__":
    asyncio.run("localhost", 8567, echo)