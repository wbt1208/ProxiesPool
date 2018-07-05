from flask import Flask,g
from proxies_pool.save_model import RedisClient
__all__ = ["app"]
app = Flask(__name__)

def get_conn():
    if not hasattr(g,"redis"):
        g.redis = RedisClient()
    return g.redis

@app.route("/")
def welcome():
    return "<h1>welcome to my proxies pool</h1>"

@app.route("/random")
def random():
    """
    获取可用代理ip
    :return: 代理ip
    """
    conn = get_conn()
    return conn.random()

@app.route("/count")
def count():
    """
    获取代理池总数量
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())
if __name__ == '__main__':
    app.run()