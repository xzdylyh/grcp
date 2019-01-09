# -*- coding: utf-8 -*-
import grpc,time
from grpctest.sendcoupon import coupon_pb2_grpc,coupon_pb2

_HOST = '60.205.215.224'
_PORT = '28083'
# _HOST = '172.17.31.198'
# _PORT = '50061'

def run():

    conn = grpc.insecure_channel(_HOST + ':' + _PORT,)
    client = coupon_pb2_grpc.couponStub(channel=conn)

    info = coupon_pb2.CouponInfo()
    info.CouponId = 12345692#1 券模版id
    info.CouponNum = 1 #发券数量
    #1061693987532739
    args = coupon_pb2.SendCouponRequest()
    args.bid = 1991243684#2589123516
    args.aid = 11111111
    args.sid = 3691394527#222
    args.couponids.extend([info])
    args.uids.append(31609394374409511)
    args.uids.append(61610007009398436)

    ######################每次发送1000张#########################
    # k = 1
    # # 发券，一次最多发1000，range为次数 400*1000 ＝40W
    # for n in range(2):
    #     n += 1
    #     args.uids.extend(range(k, n * 1000 + 1))
    #     k = n * 1000 + 1
    #     if n==1:
    #         args.uids.pop(3)
    #         args.uids.pop(4)
    #     print(args.uids)
    #     response = client.SendCoupon(args)
    #     del args.uids[:]
    #     print(args.uids)
    #
    #     if response.errCode!=0:
    #         print('result:{}'.format(response.result))
    #         print('errCode:{}'.format(response.errCode))
    #         print('errMsg:{}'.format(response.errMsg))


    response = client.SendCoupon(args)
    print('result:{}'.format(response.result))
    print('errCode:{}'.format(response.errCode))
    print('errMsg:{}'.format(response.errMsg))
    assert int(response.errCode)==0


if __name__ == '__main__':
    run()