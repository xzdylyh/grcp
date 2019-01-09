# -*- coding: utf-8 -*-
import grpc,time
from grpctest.openCard import user_pb2,user_pb2_grpc

_HOST = '172.17.31.204'
_PORT = '50071'
# _HOST = '172.17.31.198'
# _PORT = '50061'

def run():

    conn = grpc.insecure_channel(_HOST + ':' + _PORT,)
    client = user_pb2_grpc.userStub(channel=conn)

    info = user_pb2.CardInfo()
    info.acNo = '1253356131606359' #实体卡卡号
    info.name = '天枢' #姓名
    info.gender = '1' #性别1男2女
    info.phone = '13718651999' #开卡电话

    args = user_pb2.BatchOpenActualCardRequest()
    args.uniqId = int(time.time())
    args.bid = '2589123516'
    args.acbId = '2002506' #模版acbid
    args.ccid = '1003299' #1003299普通会员  1005210缤纷会员
    args.sid = '2825082475'
    args.qrid = ''
    args.type = 0
    args.users.extend([info])

    res = client.batchOpenActualCard(args)
    print('result:{}'.format(res.result))
    print('errCode:{}'.format(res.errCode))
    print('errMsg:{}'.format(res.errMsg))
    assert int(res.errCode)==0


if __name__ == '__main__':
    run()