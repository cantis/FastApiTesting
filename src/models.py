"""SQLModel classes for the database."""

from sqlmodel import Field, Relationship, SQLModel


class Player(SQLModel):
    """Represents a player in the game."""

    name: str = Field(primary_key=True)
    email: str = Field(nullable=False)
    characters: Relationship = Relationship(back_populates='player')


class Character(SQLModel):
    """Represents a character in the game."""

    name: str = Field(nullable=False, primary_key=True)
    character_class: str
    level: int = Field(default=1)
    player: Player = Field(foreign_key='name')
