"""Main module of the API."""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.crud import (
    create_character,
    create_player,
    create_session,
    get_character,
    get_characters,
    get_player,
    get_players,
)
from src.models import Character

if TYPE_CHECKING:
    from src.models import Player

app = FastAPI()

# Allow CORS for development purposes (remove for production)
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])


@app.post('/players')
async def create_new_player(name: str, email: str) -> Player:
    """Create a new player in the database."""
    return await create_player(session=next(create_session()), name=name, email=email)


@app.get('/players')
async def retrieve_all_players() -> list[Player]:
    """Retrieve all players from the database."""
    players = await get_players(session=next(create_session()))
    return list(players)


@app.get('/players/{player_name}')
async def retrieve_player(player_name: str) -> Player | dict[str, str]:
    """Retrieve a player from the database."""
    player = await get_player(session=next(create_session()), name=player_name)
    if player:
        return player
    return {'error': 'Player not found'}


@app.post('/characters')
async def create_new_character(name: str, class_name: str, level: int, player_name: str) -> Character:
    """Create a new character in the database."""
    return await create_character(
        session=next(create_session()), name=name, class_name=class_name, level=level, player_name=player_name
    )


@app.get('/characters')
async def retrieve_all_characters() -> list[Character]:
    """Retrieve all characters from the database."""
    return await get_characters(session=next(create_session()))


@app.get('/characters/{character_name}')
async def retrieve_character(character_name: str) -> Character | dict[str, str]:
    """Retrieve a character from the database."""
    character = await get_character(session=next(create_session()), name=character_name)
    if character:
        return character

    return {'error': 'Character not found'}
