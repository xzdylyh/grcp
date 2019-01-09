import time
import grpc
from grpctest.snowid import snowid_pb2,snowid_pb2_grpc
from locust import (TaskSet,task,events,Locust)
from gevent._semaphore import Semaphore

all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()

events.hatch_complete += on_hatch_complete

class GrpcClient(object):
    """重写self.client"""
    def __init__(self):
        self.ht = '172.17.31.220'
        self.pt = '50073'

    def connect(self):
        """grpc实例"""
        all_locusts_spawned.wait()
        try:
            #记录开始时间
            start_time = int(time.time())

            #创建链接
            self.conn = grpc.insecure_channel(self.ht +':'+self.pt)
            self.cl = snowid_pb2_grpc.snowidStub(channel=self.conn)
            #参数实例
            args = snowid_pb2.GenerateSnowidRequest()
            args.uniqId = 10000 #此参数现在未起作用，可以为任意数字

            #调用
            res = self.cl.generateSnowid(args)
            total_time = int((time.time() - start_time) * 1000)
            if res.errCode != 0:
                raise Exception
            events.request_success.fire(
                request_type='grpc',
                name=r'/generateSnowid',
                response_time=total_time,
                response_length=0
            )
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type='grpc',
                name='/generateSnowid',
                response_time=total_time,
                exception=e
            )

        return res


class GrpcLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GrpcLocust, self).__init__(*args, **kwargs)
        self.client = GrpcClient()



class GrpcTask(TaskSet):
    """压测任务"""


    @task
    def generateSnowid(self):
        #grpc接口响应数据
        res = self.client.connect()
        # print('errCode:{}'.format(res.errCode))
        # print('result:{}'.format(res.result))
        # print('errMsg:{}'.format(res.errMsg))


class WebsiteUser(GrpcLocust):
    task_set = GrpcTask
    min_wait = 5000
    max_wait = 9000