import time

TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True
API_HOSTS = "0.0.0.0"
API_PORT = 5000
from multiprocessing import Process
from proxies_pool.api_model import app
from getter.getter import Getter
from proxies_pool.inspect_model import Tester
class Scheduler():
    def schedule_tester(self,cycle=TESTER_CYCLE):
        """
        定时测试代理
        :param cycle:
        :return:
        """
        tester = Tester()
        while True:
            print("测试器开始运行")
            tester.run()
            time.sleep(cycle)
    def schedule_getter(self,cycle=GETTER_CYCLE):
        """
        定时获取ip
        :param cycle: 睡眠时间
        :return: None
        """
        getter = Getter()
        while True:
            print("抓取器开始运行")
            getter.run()
            time.sleep(cycle)
    def schedule_api(self):
        """
        开启app服务器
        :return:
        """
        app.run(API_HOSTS,API_PORT)
    def run(self):
        print("代理池开始运行")
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
