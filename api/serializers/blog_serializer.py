from lib2to3.pytree import Base
from typing import Any, Dict
from .model_serializer import ModelSerializer
from models import Blog, BaseModel
from controllers import BlogController


class BlogSerializer(ModelSerializer):
    def __init__(self) -> None:
        super().__init__(BlogController())

    def from_representation(self, model: Blog):
        dict_repr = dict(model)
        if model.id is None:
            dict_repr.pop('id')
        dict_repr.pop('author', None)
        dict_repr.pop('parents', None)
        dict_repr.pop('children', None)
        return dict_repr

    def to_representation(self, data: Dict[str, Any]) -> BaseModel:
        return Blog(**data)
