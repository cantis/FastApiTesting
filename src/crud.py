"""Contains the CRUD operations."""

from __future__ import annotations

from typing import Generator

from sqlmodel import Session, create_engine

from src.models import Character, Player

DATABASE_URL = 'sqlite:///game.db'

engine = create_engine(DATABASE_URL, echo=True)


def create_session() -> Generator[Session, None, None]:
    """Create a new session to the database."""
    with Session(engine) as session:
        yield session


async def create_player(session: Session, name: str, email: str) -> Player:
    """Create a new player in the database."""
    player = Player(name=name, email=email)
    session.add(player)
    session.commit()
    session.refresh(player)
    return player


async def get_players(session: Session) -> list[Player]:
    """Get all players from the database."""
    return session.exec(Player).all()


async def get_player(session: Session, name: str) -> Player:
    """Get a player from the database."""
    return session.get(Player, name).first()


async def create_character(session: Session, name: str, class_name: str, level: int, player_name: str) -> Character:
    """Create a new character in the database."""
    character = Character(name=name, character_class=class_name, level=level, player_name=player_name)
    session.add(character)
    session.commit()
    session.refresh(character)
    return character


async def get_characters(session: Session) -> list[Character]:
    """Get all characters from the database."""
    return session.exec(Character).all()


async def get_character(session: Session, name: str) -> Character:
    """Get a character from the database."""
    return session.get(Character, name).first()
