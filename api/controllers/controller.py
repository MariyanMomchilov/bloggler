from abc import ABC, abstractmethod
from query import db_engine


class Controller(ABC):
    def __init__(self, engine=db_engine) -> None:
        self.engine = engine

    #@abstractmethod
    def get_one(self, id: int):
        raise NotImplementedError()

    #@abstractmethod
    def get_many(self):
        raise NotImplementedError()

    #@abstractmethod
    def update_one(self, id: int, values: dict):
        raise NotImplementedError()

    #@abstractmethod
    def delete_one(self, id: int):
        raise NotImplementedError()

    @abstractmethod
    def insert_one(self, values: dict):
        raise NotImplementedError()
