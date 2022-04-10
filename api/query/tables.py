from sqlalchemy import Table, Column, MetaData, Integer, String

from .engine import db_engine

metadata_obj = MetaData()

BLOG_TABLENAME = 'blog'
blog = Table(
    BLOG_TABLENAME,
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('content', String)
)

metadata_obj.create_all(db_engine)
metadata_obj.reflect(db_engine)
