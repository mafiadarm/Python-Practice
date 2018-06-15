import pymongo
import redis
import json


def main():
    # 指定Redis数据库信息
    rediscli = redis.Redis(host="localhost", port=6379, db=0)
    # 指定MongoDB数据库信息
    mongocli = pymongo.MongoClient(host='127.0.0.1', port=27017)

    # 创建数据库名
    db = mongocli['tencent']
    # 创建表名
    collection = db['tencent']

    while True:
        # FIFO模式为blpop, LIFO模式为brpop, 获取键值
        source, data = rediscli.blpop(["Tencent:items"])

        item = json.loads(data.decode())
        collection.insert(item)

        try:
            print(u"Processing:%(name)s <%(link)s>" % item)
        except KeyError:
            print(u"Error procesing: %r" % item)


if __name__ == "__main__":
    main()