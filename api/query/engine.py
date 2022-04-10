from sqlalchemy import text
from sqlalchemy.engine import create_engine

from config.config import config

db_engine = create_engine(
    f'''postgresql+psycopg2://{config["USER"]}:{config["PASSWORD"]}@{config["HOST"]}/{config["DB_NAME"]}'''
)
