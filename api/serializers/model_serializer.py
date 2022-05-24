from abc import ABC, abstractmethod
from typing import Dict, Any
from pydantic import BaseModel

from controllers.controller import Controller


class ModelSerializer(ABC):

    def __init__(self, controller: Controller) -> None:
        self.controller = controller

    @abstractmethod
    def from_representation(self, model: BaseModel):
        pass

    @abstractmethod
    def to_representation(self, data: Dict[str, Any]) -> BaseModel:
        pass
    
    def get_instance(self, id: int):
        instance_data = self.controller.get_one(id)
        return self.to_representation(instance_data)
    
    def create_instance(self, model: BaseModel):
        model_data = self.from_representation(model)
        instance_data = self.controller.insert_one(model_data)

    def get_instances(self):
        return [self.to_representation(model_data) for model_data in self.controller.get_many()]