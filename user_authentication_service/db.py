#!/usr/bin/env python3
""" create user
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User

Base = declarative_base()


class DB:
    """ Database
    """

    def __init__(self):
        """ Init method
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__Session = sessionmaker(bind=self._engine)  # Create a session factory

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user
        """
        session = self.__Session()  # Create an actual session object
        user = User(email=email, hashed_password=hashed_password)
        session.add(user)  # Add the user to the session
        session.commit()  # Commit the transaction
        session.close()  # Close the session after the transaction
        return user
