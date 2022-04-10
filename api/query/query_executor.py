from typing import Dict, List
from sqlalchemy.engine import Engine
from sqlalchemy import MetaData, insert

from .tables import metadata_obj
from .engine import db_engine


class QueryExecutor:
    def __init__(self, engine: Engine, metadata: MetaData):
        self.engine = engine
        self.metadata = metadata

    def insert(self, table_name: str, values: List[Dict[str, any]]):
        table = self.metadata.tables[table_name]
        with self.engine.begin() as conn:
            conn.execute(insert(table), values)


blog_query_executor = QueryExecutor(engine=db_engine, metadata=metadata_obj)
