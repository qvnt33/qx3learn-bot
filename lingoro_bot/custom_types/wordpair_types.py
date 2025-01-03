from typing import TypedDict

from sqlalchemy import Column


class BaseWordpairWordType(TypedDict):
    word: str
    transcription: str | None


class BaseWordpairTranslationType(TypedDict):
    translation: str
    transcription: str | None


class WordpairComponentsType(TypedDict):
    words: list[BaseWordpairWordType]
    translations: list[BaseWordpairTranslationType]
    annotation: str | None


class WordpairWordType(TypedDict):
    word: Column[str]
    transcription: Column[str] | None


class WordpairTranslationType(TypedDict):
    translation: Column[str]
    transcription: Column[str] | None


class WordpairType(TypedDict):
    words: list[WordpairWordType]
    translations: list[WordpairTranslationType]
    annotation: Column[str] | None


class WordpairInfoType(TypedDict):
    id: Column[int]
    words: list[WordpairWordType]
    translations: list[WordpairTranslationType]
    annotation: Column[str] | None
    number_errors: Column[int]
