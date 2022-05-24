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
        pk = self.controller.insert_one(model_data)
        return self.get_instance(pk)
    
    def update_instance(self, id: int, model: BaseModel):
        model_data = self.from_representation(model)
        self.controller.update_one(id, model_data)
    
    def delete_instance(self, id: int):
        self.controller.delete_one(id)

    def get_instances(self):
        return [self.to_representation(model_data) for model_data in self.controller.get_many()]