from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Emotions:
    angry: str
    fear: str
    joy: str
    sadness: str

    def asdict(self) -> Dict[str, str]:
        return {
            "angry": self.angry,
            "fear": self.fear,
            "joy": self.joy,
            "sadness": self.sadness
        }

@dataclass
class Dataset:
    dtype: str
    emotions: Emotions
    