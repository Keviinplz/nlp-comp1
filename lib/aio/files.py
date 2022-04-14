from typing import List, Optional

import aiofiles

async def store_file(filename: str, data: str, dtype: str = "train") -> None:
    """ Store data in file """
    async with aiofiles.open(f"data/{dtype}/{filename}", 'w') as file:
        await file.write(data)

async def create_folders(name_folders: Optional[List[str]] = None) -> None:
    """ Create folder if it doesn't exist """
    if not name_folders:
        name_folders = ["train", "test"]
    
    if not await aiofiles.os.path.exists("data"):
        await aiofiles.os.makedirs("data")
        for name_folder in name_folders:
            await aiofiles.os.makedirs(f"data/{name_folder}")

async def check_if_there_is_data() -> bool:
    """ Check if there is data in folder """
    return await aiofiles.os.path.exists("data/train") and await aiofiles.os.path.exists("data/test")