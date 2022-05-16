import os
from dotenv import load_dotenv


load_dotenv()
env_ip = os.environ.get("REDIS_IP")
env_port = os.environ.get("REDIS_PORT")
env_port = int(env_port) if env_port else None

redis_ip = env_ip if env_ip else "127.0.0.1"
redis_port = env_port if env_port else 6379
