import asyncio

from src.censore.censore_main import check_censoring
from src.grammar_correction.grammar_correction_main import print_all_necessary
from src.websocket.server import server
from utils.similarity import has_cyrillic


async def echo(websocket) -> None:
    async for message in websocket:
        if has_cyrillic(message):
            grammar_result = print_all_necessary(message, 'ru-RU')
        else:
            grammar_result = print_all_necessary(message, 'ro-RO')
        censoring_result = check_censoring(message)
        string = f'{censoring_result} / {grammar_result}'
        await websocket.send(string)


async def main(func1, func2) -> None:
    await asyncio.gather(func1, func2)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(server("localhost", 8567, echo), server("localhost", 8566, echo)))
    finally:
        loop.close()