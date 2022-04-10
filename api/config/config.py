from dotenv import load_dotenv, dotenv_values

ENV_PATH = '.env'

load_dotenv(dotenv_path=ENV_PATH)
config = dotenv_values(dotenv_path=ENV_PATH)
