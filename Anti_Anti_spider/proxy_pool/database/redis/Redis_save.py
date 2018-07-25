#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           07_25_2018  13:26
    File Name:      /proxy_pool/Redis_save
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

from database.redis.redis_connect import RedisConnect


class RedisString(RedisConnect):
    """
    redis中的String在在内存中按照一个name对应一个value来存储
    """
    def __init__(self, host=None, port=None, db=None):
        super(RedisString).__init__(host=host, port=port, db=db)
        self.pipe = self.pipeline()
        self.pool = self.connect_pool()

    def _add(self, a_type, name, *args, **kwargs):
        if a_type == "set": self.pipe.set(name, *args, **kwargs)  # 在Redis中设置值，默认不存在则创建，存在则修改
        if a_type == "setex": self.pipe.setex(name, *args, **kwargs)  # 设置过期时间（秒）
        if a_type == "psetex": self.pipe.psetex(name, *args, **kwargs)  # 设置过期时间（豪秒）
        if a_type == "mset": self.pipe.mset(**kwargs)  # 批量设置值
        if a_type == "incr": self.pipe.incr(name,
                                            **kwargs)  # 自增mount对应的值，当mount不存在时，则创建mount＝amount，否则，则自增,amount为自增数(整数)
        if a_type == "incrbyfloat": self.pipe.incrbyfloat(name, **kwargs)  # 类似 incr() 自增,amount为自增数(浮点数)
        if a_type == "decr":  # 自减name对应的值,当name不存在时,则创建name＝amount，否则，则自减，amount为自增数(整数)
            self.pipe.incrbyfloat(name, **kwargs)
        if a_type == "append": self.pipe.append(name, *args)  # 在name对应的值后面追加内容

    def _delete(self, d_type, name, *args):
        pass

    def _update(self, u_type, name, *args):
        if u_type == "setrange": self.pipe.setrange(name, *args)  # 修改字符串内容，从指定字符串索引开始向后替换，如果新值太长时，则向后添加
        if u_type == "setbit": self.pipe.setbit(name, *args)  # 对二进制表示位进行操作

    def _query(self, q_type, name, *args):
        if q_type == "get": self.pipe.get(name)  # 获取值
        if q_type == "mget": self.pipe.mget(name, *args)  # 批量获取
        if q_type == "getset": self.pipe.getset(name, *args)  # 设置新值，打印原值
        if q_type == "getrange": self.pipe.getrange(name, *args)  # 根据字节获取子序列
        if q_type == "getbit": self.pipe.getbit(name, *args)  # 获取name对应值的二进制中某位的值(0或1)
        if q_type == "bitcount": self.pipe.bitcount(name, *args)  # 获取对应二进制中1的个数
        if q_type == "strlen": self.pipe.strlen(name)  # 返回name对应值的字节长度（一个汉字3个字节）


class RedisHash(RedisConnect):
    """
    redis中的Hash 在内存中类似于一个name对应一个dic来存储
    """
    def __init__(self, host=None, port=None, db=None):
        super(RedisHash).__init__(host=host, port=port, db=db)
        self.pipe = self.pipeline()
        self.pool = self.connect_pool()

    def _add(self, a_type, name, *args, **kwargs):
        if a_type == "hset": self.pipe.hset(name, *args, **kwargs)  # name对应的hash中设置一个键值对（不存在，则创建，否则，修改）
        if a_type == "hmset": self.pipe.hmset(name, **kwargs)  # 在name对应的hash中批量设置键值对,mapping:字典
        if a_type == "hincrby": self.pipe.hincrby(name, *args, **kwargs)  # 自增hash中key对应的值，不存在则创建key=amount(amount为整数)
        if a_type == "hincrbyfloat": self.pipe.hincrbyfloat(name, *args,
                                                            **kwargs)  # 自增hash中key对应的值，不存在则创建key=amount(amount为浮点数)

    def _delete(self, d_type, name, *args):
        if d_type == "hdel": self.pipe.hdel(name, *args)  # 删除指定name对应的key所在的键值对

    def _update(self, u_type, name, to_name, *args):
        pass

    def _query(self, q_type, name, *args, **kwargs):
        if q_type == "hget": self.pipe.hget(name, *args)  # 在name对应的hash中根据key获取value
        if q_type == "hgetall": self.pipe.hgetall(name)  # 获取name对应hash的所有键值
        if q_type == "hmget": self.pipe.hmget(name, *args)  # 在name对应的hash中获取多个key的值
        if q_type == "hlen": self.pipe.hlen(name)  # hlen(name) 获取hash中键值对的个数
        if q_type == "hkeys": self.pipe.hkeys(name)  # hkeys(name) 获取hash中所有的key的值
        if q_type == "hvals": self.pipe.hvals(name)  # hvals(name) 获取hash中所有的value的值
        if q_type == "hexists": self.pipe.hexists(name, *args)  # 检查name对应的hash是否存在当前传入的key
        # self.pipe.hscan(name, *args, **kwargs)
        # self.pipe.hscan_iter(name, *args, **kwargs)


class RedisList(RedisConnect):
    """
    redis中的List在在内存中按照一个name对应一个List来存储
    """
    def __init__(self, host=None, port=None, db=None):
        super(RedisList).__init__(host=host, port=port, db=db)
        self.pipe = self.pipeline()
        self.pool = self.connect_pool()

    def _add(self, a_type, name, *args, **kwargs):
        if a_type == "lpush": self.pipe.lpush(name, *args, **kwargs)  # 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
        if a_type == "rpush": self.pipe.rpush(name, *args, **kwargs)  # 同lpush，但每个新的元素都添加到列表的最右边
        if a_type == "lpushx": self.pipe.lpushx(name, *args, **kwargs)  # 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边
        if a_type == "rpushx": self.pipe.rpushx(name, *args, **kwargs)  # 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最右边

    def _delete(self, d_type, name, *args):
        if d_type == "lrem": self.pipe.lrem(name, *args)  # 删除name对应的list中的指定值
        if d_type == "lpop": self.pipe.lpop(name, *args)  # 移除列表的左侧第一个元素，返回值则是第一个元素
        if d_type == "ltrim": self.pipe.ltrim(name, *args)  # 移除列表内没有在该索引之内的值
        if d_type == "blpop": self.pipe.blpop(name, *args)  # 将多个列表排列,按照从左到右去移除各个列表内的元素
        if d_type == "brpop": self.pipe.brpop(name, *args)  # 同blpop，将多个列表排列,按照从右像左去移除各个列表内的元素

    def _update(self, u_type, name, to_name, *args):
        if u_type == "linsert": self.pipe.linsert(name, *args)  # 在name对应的列表的某一个值前或后插入一个新值
        if u_type == "rpoplpush": self.pipe.rpoplpush(name, to_name)  # 从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
        if u_type == "brpoplpush": self.pipe.brpoplpush(name, to_name,
                                                        *args)  # 同rpoplpush，多了个timeout, timeout：取数据的列表没元素后的阻塞时间，0为一直阻塞

    def _query(self, q_type, name, *args):
        if q_type == "llen": self.pipe.llen(name, *args)  # name对应的list元素的个数
        if q_type == "lset": self.pipe.lset(name, *args)  # 对list中的某一个索引位置重新赋值
        if q_type == "lindex": self.pipe.lindex(name, *args)  # 根据索引获取列表内元素
        if q_type == "lrange": self.pipe.lrange(name, *args)  # 分片获取元素


class RedisSet(RedisConnect):
    def __init__(self, host=None, port=None, db=None):
        super(RedisSet).__init__(host=host, port=port, db=db)
        self.pipe = self.pipeline()
        self.pool = self.connect_pool()

    """
    Set集合就是不允许重复的列表
    可以直接用初始化里面的连接实例直接进行操作，或者查询对应方法使用私有方法进行操作
    """

    def _add(self, a_type, name, *args, **kwargs):
        if a_type == "sadd": self.pipe.sadd(name, *args, **kwargs)  # 无序
        if a_type == "zadd": self.pipe.zadd(name, *args, **kwargs)  # 有序

    def _delete(self, d_type, name, *args):
        if d_type == "srem": self.pool.srem(name, *args)  # 删除name对应的集合中的某些值
        if d_type == "zrem": self.pool.zrem(name, *args)  # 删除name对应的有序集合中值是values的成员
        if d_type == "zremrangebyrank": self.pool.zremrangebyrank(name, *args)  # 根据排行范围删除
        if d_type == "zremrangebyscore": self.pool.zremrangebyscore(name, *args)  # 根据排行范围删除
        if d_type == "smove": self.pool.smove(name, *args)  # 从集合的右侧移除一个元素，并将其返回

    def _update(self, u_type, name, to_name, *args):
        if u_type == "sinterstore": self.pool.sinterstore(to_name, name, *args)  # 获取多个name对应集合的并集，再讲其加入到dest对应的集合中
        if u_type == "sunionstore": self.pool.sunionstore(to_name, name,
                                                          *args)  # 获取多个name对应的集合的并集，并将结果保存到dest对应的集合中
        if u_type == "sdiffstore": self.pool.sdiffstore(to_name, name, *args)  # 相当于把sdiff获取的值加入到dest对应的集合中
        if u_type == "zinterstore":  # 获取两个有序集合的交集并放入dest集合，如果遇到相同值不同分数，则按照aggregate进行操作
            self.pool.zinterstore(to_name, *args, aggregate="MAX")
        if u_type == "delete": self.pool.delete(*args)  # 根据name删除redis中的任意数据类型
        if u_type == "expire": self.pool.expire(name, *args)  # 为某个name设置超时时间
        if u_type == "rename": self.pool.rename(name, *args)  # 重命名
        if u_type == "move": self.pool.move(name, to_name)  # 将redis的某个值移动到指定的db下

    def _query(self, q_type, name, *args):
        if q_type == "smembers": self.pool.smembers(name)  # 获取name对应的集合的所有成员
        if q_type == "scard": self.pool.scard(name)  # 获取name对应的集合中的元素个数
        if q_type == "sdiff": self.pool.sdiff(name, *args)  # 在第一个name对应的集合中且不在其他name对应的集合的元素集合

        if q_type == "sinter": self.pool.sinter(name, *args)  # 获取多个name对应集合的并集
        if q_type == "sismember": self.pool.sismember(name, *args)  # 检查value是否是name对应的集合内的元素
        if q_type == "srandmember": self.pool.srandmember(name, *args)  # 从name对应的集合中随机获取numbers个元素
        if q_type == "sunion": self.pool.sunion(name, *args)  # 获取多个name对应的集合的并集

        if q_type == "zcard": self.pool.zcard(name)  # 获取有序集合内元素的数量
        if q_type == "zcount": self.pool.zcount(name, *args)  # 获取有序集合中分数在[min,max]之间的个数
        if q_type == "zincrby": self.pool.zincrby(name, *args)  # 自增有序集合内value对应的分数zincrby(name, value, amount)
        if q_type == "zrange" or "zrevrange":  # 按照索引范围获取name对应的有序集合的元素
            print("手动执行 ",
                  "self.pool.zrange(name, start, end, desc=False, withscores=False, score_cast_func=float)")

        if q_type == "zrank": self.pool.zrank(name, *args)  # 获取value值在name对应的有序集合中的排行位置（从0开始）
        if q_type == "zrevrank": self.pool.zrevrank(name, *args)  # 从大到小排序
        if q_type == "zscore": self.pool.zscore(name, *args)  # 获取name对应有序集合中 value 对应的分数

        if q_type == "exists": self.pool.exists(name)  # 检测redis的name是否存在
        if q_type == "keys": self.pool.zscore(pattern=name)  # 根据* ？等通配符匹配获取redis的name
        if q_type == "randomkey": self.pool.randomkey()  # 随机获取一个redis的name（不删除）
        if q_type == "type": self.pool.type(name)  # 获取name对应值的类型
