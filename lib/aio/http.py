import asyncio
from typing import List, Dict

import aiohttp

from lib import models
from .files import store_file

async def download_file(*, emotion: str, url: str, dtype: str, session: aiohttp.ClientSession) -> None:
    """ Download and store file in disk """
    async with session.get(url) as response:
        data = await response.read()
        await store_file(f"{emotion}.txt", data.decode('utf-8'), dtype=dtype)


async def download_all(session: aiohttp.ClientSession, data: models.Dataset) -> None:
    """ Download and store dataset in disk """
    emotion_url: Dict[str, str] = data.emotions.asdict()

    tasks: List[asyncio.Task] = [None] * len(emotion_url)
    for i, emotion in enumerate(emotion_url):
        task = asyncio.create_task(download_file(emotion=emotion, url=emotion_url[emotion], dtype=data.dtype, session=session))
        tasks[i] = task
    await asyncio.gather(*tasks)