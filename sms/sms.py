import time
import grpc
from grpctest.sms import sms_pb2,sms_pb2_grpc

class SmsClass(object):
    def __init__(self):
        self._host = '39.97.9.78'
        self._port = '9000'
        self.conn = grpc.insecure_channel(self._host + self._port)
        self.sms = sms_pb2_grpc.SmsInterfaceStub(channel=self.conn)

    def tpl_sms(self):
        """模版短信"""

        #用户信息
        info = sms_pb2.UserInfo()
        info.Phone = '13718651998' #手机号
        info.AreaCode = '86' #手机号区域码
        info.TradeSid = '2450366156' #交易门店id
        info.CreateSid = '1318679496' #创建门店id
        info.OpenCardSid = '3522920644' #开卡门店id
        info.SendCouponSid = '1747862319' #发券门店id
        info.MessageVar.extend([{"name":'test',"phone":"123456"}]) #替换模板用的变量

        #发送模版短信
        tpl_req = sms_pb2.TplSMSRequest()
        tpl_req.BatchID = int(time.time()) #批次id
        tpl_req.Bid = '1991243684' #商家id
        tpl_req.BizId = 2 #业务类型 1生日赠券；2开卡关怀；3填资料赠券
        tpl_req.Operator ='10001' #短信发送触发人
        tpl_req.Users.extend([info])
        tpl_req.Template ='模版发送:$$name#$你好，这是一个测试短信,您的电话是:$$phone#$,请核对。' #如果不为空，优先使用这个模板

        res = self.sms.SendTemplateSMS(tpl_req)
        print(res)
        assert res.ErrorCode ==0,res.ErrorMsg

    def normal_sms(self):
        """普通短信"""
        #用户信息
        info = sms_pb2.UserInfo()
        info.Phone = '13718651998' #手机号
        info.AreaCode = '86' #手机号区域码
        info.TradeSid = '2450366156' #交易门店id
        info.CreateSid = '1318679496' #创建门店id
        info.OpenCardSid = '3522920644' #开卡门店id
        info.SendCouponSid = '1747862319' #发券门店id

        #发送普通短信请求
        req = sms_pb2.SMSRequest()
        req.BatchID = int(time.time()) #批次id
        req.Bid = '1991243684' #商家id
        req.BizId = 2 #业务类型 1生日赠券；2开卡关怀；3填资料赠券
        req.Message = 'rpc普通短信内容' #短信内容
        req.Users.extend([info])

        res = self.sms.SendNormalSMS(req)
        print(res)
        assert res.ErrorCode ==0,res.ErrorMsg



if __name__ == "__main__":
    sms = SmsClass()
    sms.normal_sms() #普通短信
    # sms.tpl_sms() #模版短信
