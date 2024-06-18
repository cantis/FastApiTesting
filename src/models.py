"""SQLModel classes for the database."""

from sqlmodel import Field, SQLModel


class Player(SQLModel):
    """Represents a player in the game."""

    name: str = Field(primary_key=True, Title='Player Name')
    email: str = Field(nullable=False, Title='Player Email')


class Character(SQLModel):
    """Represents a character in the game."""

    name: str = Field(nullable=False, Title='Character Name')
    class_name: str
    level: int = Field(default=1)
    player: Player = Field(backref='characters', foreign_key='player.name')
