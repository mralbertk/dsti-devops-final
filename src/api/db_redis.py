import redis
import conf.default as cfg

r = redis.Redis(
    host=cfg.redis_ip,
    port=cfg.redis_port
)
