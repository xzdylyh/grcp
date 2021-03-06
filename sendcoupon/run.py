# -*- coding: utf-8 -*-
import grpc
from grpctest.sendcoupon import coupon_pb2_grpc,coupon_pb2

#_HOST = '60.205.215.224'
#_PORT = '28083'
_HOST = '172.17.31.198'
_PORT = '50061'

def run():

    conn = grpc.insecure_channel(_HOST + ':' + _PORT,)
    client = coupon_pb2_grpc.couponStub(channel=conn)

    info = coupon_pb2.CouponInfo()
    info.CouponId = 8891172#1 券模版id
    info.CouponNum = 5 #发券数量
    #1061693987532739
    args = coupon_pb2.SendCouponRequest()
    args.bid = 2048695606
    args.aid = 11111111
    args.sid = 151299566
    args.uids.append(11610005739753862)
    args.uids.append(61610007009398436)
    args.couponids.extend([info])


    response = client.SendCoupon(args)
    print('result:{}'.format(response.result))
    print('errCode:{}'.format(response.errCode))
    print('errMsg:{}'.format(response.errMsg))

    assert int(response.errCode)==0,'fail'


if __name__ == '__main__':
    run()