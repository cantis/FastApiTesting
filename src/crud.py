"""Contains the CRUD operations."""

from typing import Generator, List

from sqlmodel import Session, create_engine

from src.models import Player

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

async def get_players(session: Session) -> List[Player]:
    """Get all players from the database."""
    return session.query(Player).all()    