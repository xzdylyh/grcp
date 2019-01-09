# -*- coding: utf-8 -*-
import grpc,time
import random
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
    info.CouponNum = 1 #发券数量
    #1061693987532739
    args = coupon_pb2.SendCouponRequest()
    #args.bid = 2048695606
    #args.aid = 11111111
    #args.sid = 151299566
    args.uids.append(11610005739753862)
    args.uids.append(61610007009398436)
    args.couponids.extend([info])
    bid_arr = [2048695606,2589123516]
    sid_arr = [1512995661,3164832681]
    aid_arr = [11111111,3033146]

    #bid_arr = [2048695606,2048695606]
    #sid_arr = [1512995661,1512995661]
    #aid_arr = [11111111,11111111]



    start_time = time.time()

    k = 1
    for n in range(10):
        n += 1
        args.uids.extend(range(k, n * 1000 + 1))
        k = n * 1000 + 1
        if n == 1:
            args.uids.pop(3)
            args.uids.pop(4)
        # time.sleep(0.2)

        renum = random.randint(0, 1)
        args.aid = aid_arr[renum]
        args.bid = bid_arr[renum]
        args.sid = sid_arr[renum]
        response = client.SendCoupon(args)
        del args.uids[:]
        print(response.errCode)
        print(n)
        if response.errCode != 0:
            print('result:{}'.format(response.result))
            print('errCode:{}'.format(response.errCode))
            print('errMsg:{}'.format(response.errMsg))
    end_time = time.time()
    print('共用时:{}s'.format(end_time - start_time))

    # print(args)
    print('ok...')
