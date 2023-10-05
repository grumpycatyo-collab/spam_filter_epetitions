import asyncio
from src.websocket.server import server

async def echo(websocket) -> None:
    async for message in websocket:
        await websocket.send(message)


async def main(func1, func2) -> None:
    await asyncio.gather(func1, func2)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(server("localhost", 8567, echo), server("localhost", 8566, echo)))
    finally:
        loop.close()