from sqlalchemy import Table, Column, MetaData, Integer, String, Enum, ForeignKey
from .engine import db_engine
from models import BlogType, BlogVisibility

metadata_obj = MetaData()

BLOG_TABLENAME = 'blog'

blog = Table(
    BLOG_TABLENAME,
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('content', String, nullable=False),
    Column('type', Enum(BlogType), nullable=False),
    Column('visibility', Enum(BlogVisibility), nullable=False)
)

BLOG_RELATION_TABLENAME = 'blog_relation'

blog_relation = Table(
    BLOG_RELATION_TABLENAME,
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('parent', Integer, ForeignKey(f'{BLOG_TABLENAME}.id', ondelete='CASCADE'), nullable=False),
    Column('child', ForeignKey(f'{BLOG_TABLENAME}.id', ondelete='CASCADE'), nullable=False)
)

metadata_obj.create_all(db_engine)
metadata_obj.reflect(db_engine)
