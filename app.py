import asyncio

from filtering import filter_spam
from src.censore.censore_main import check_censoring
from src.grammar_correction.grammar_correction_main import print_all_necessary
from src.websocket.server import server
from utils.similarity import has_cyrillic



async def echo(websocket) -> None:
    async for message in websocket:
        string = filter_spam(message)
        await websocket.send(string)


if __name__ == "__main__":
    asyncio.run(server("0.0.0.0", 8567, echo))