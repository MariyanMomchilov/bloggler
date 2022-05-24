from abc import ABC, abstractmethod
from query import db_engine


class Controller(ABC):
    def __init__(self, engine=db_engine) -> None:
        self.engine = engine

    @abstractmethod
    def get_one(self, id: int):
        pass

    @abstractmethod
    def get_many(self):
        pass

    @abstractmethod
    def update_one(self, id: int, values: dict):
        pass

    @abstractmethod
    def delete_one(self, id: int):
        pass

    @abstractmethod
    def insert_one(self, values: dict):
        pass
