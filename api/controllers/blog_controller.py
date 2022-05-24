from .controller import Controller
from query.tables import blog
from sqlalchemy.sql import select, update, insert, delete


class BlogController(Controller):
    def __init__(self) -> None:
        super().__init__()
    
    def get_many(self):
        with self.engine.begin() as conn:
            return conn.execute(select(blog)).fetchall()
    
    def get_one(self, id: int):
        select_exp = select(blog).where(blog.c.id == id)
        
        with self.engine.begin() as conn:
            return conn.execute(select_exp).first()
    
    def update_one(self, id: int, values: dict):
        with self.engine.begin() as conn:
            return conn.execute(update(blog).where(blog.c.id == id).values(**values))
    
    def insert_one(self, values: dict):
        with self.engine.begin() as conn:
            pk = conn.execute(insert(blog), [values]).inserted_primary_key['id']
            return pk
    
    def delete_one(self, id: int):
        with self.engine.begin() as conn:
            return conn.execute(delete(blog).where(blog.c.id == id))

    