from pytest_redis import factories


redis_ext = factories.redisdb('redis_nooproc')


def test_redis_connection(redis_ext):
    redis_ext.set('test1', 'success')
    my_test = redis_ext.get('test1')
    assert my_test == b'success'
    redis_ext.delete('test1')
