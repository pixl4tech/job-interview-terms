from __future__ import annotations
from bson import ObjectId
from typing import List, Optional
from pydantic import BaseModel


class Phonetic(BaseModel):
    text: Optional[str] = None
    audio: str = None
    sourceUrl: Optional[str] = None


class Definition(BaseModel):
    definition: str = None
    synonyms: List[str] | None = None
    antonyms: List[str] | None = None
    example: Optional[str] = None


class Meaning(BaseModel):
    partOfSpeech: str = None
    definitions: List[Definition] | None = None
    synonyms: List[str] | None = None
    antonyms: List[str] | None = None


class Dictionary(BaseModel):
    phonetic: Optional[str] = None
    phonetics: List[Phonetic] | None = None
    meanings: List[Meaning] | None = None
    sourceUrls: List[str] | None = None
    context: str


class Term(BaseModel):
    name: str
    dictionary: Dictionary
    likeCounter: int
    dislikeCounter: int

    class Config:
        arbitrary_types_allowed = True
