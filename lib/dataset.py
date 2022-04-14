import os
from typing import List, Tuple

import aiohttp
import pandas as pd

from lib import models, aio


    
async def load_dataset(urls: List[models.Dataset]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """ Loads dataset from given Dataset, store data in folder if it's needed in future """
    if not aio.check_if_there_is_data():
        await aio.create_folders()
        