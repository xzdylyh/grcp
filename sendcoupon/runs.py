import grpc,time
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
    args.bid = 2048695606
    args.aid = 11111111
    args.sid = 151299566
    args.uids.append(11610005739753862)
    #args.uids.append(61610007009398436)
    args.couponids.extend([info])

    start_time = int(time.time())

    k = 1
    for n in range(100):
        n += 1

        args.uids.extend(range(k, n * 1000 + 1))
        k = n * 1000 + 1
        if n==1:
            args.uids.pop(3)
            #args.uids.pop(4)
        #time.sleep(0.2)
        if n ==100:
            args.uids.pop()
            args.uids.append(61610007009398436)
        response = client.SendCoupon(args)
        del args.uids[:]
        print(response.errCode)
        print('已发送{}张券......'.format(n*1000))
        if response.errCode!=0:
            print('result:{}'.format(response.result))
            print('errCode:{}'.format(response.errCode))
            print('errMsg:{}'.format(response.errMsg))

    end_time = int(time.time())
    print('总共用时:{}秒'.format(end_time-start_time))

    #print(args)
    print('ok...')



if __name__ == '__main__':
    run()