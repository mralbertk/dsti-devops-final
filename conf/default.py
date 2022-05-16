import os
from dotenv import load_dotenv


load_dotenv()
env_ip = os.environ.get("REDIS_IP")
env_port = int(os.environ.get("REDIS_PORT"))

redis_ip = env_ip if env_ip else "127.0.0.1"
redis_port = env_port if env_port else 6379
