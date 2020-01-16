# coding=utf-8
import time

from vivo.APIConstants import Constants
from vivo.APISenderBase import Base
from vivo.APISignUtil import SignUtil

_BROADCAST_TOPIC_MAX = 5
_TOPIC_SPLITTER = ';$;'


class APISender(Base):
    """
    发送消息API(send push message class)
    构造方法接收两个参数:
    @:param secret 必填 - APP_SECRET
    @:param token 可选 - authToken,发送消息时需带该参数以进行鉴权操作，调用鉴权接口获得
    """

    def get_token(self, app_id, app_key):
        timestamp = int(round(time.time() * 1000))
        sign = SignUtil(app_id, app_key, self.secret).sign_util(timestamp)
        get_token = {'appId': app_id, 'appKey': app_key, 'timestamp': timestamp, 'sign': sign}
        return self._try_http_request(Constants.request_path.GET_TOKEN, retry_times=3, **get_token)

    def send(self, push_message, retry_times=3):
        """
        发送单推消息
        :param push_message: 消息体(请求参数对象)
        :param retry_times: 重试次数
        """
        return self._try_http_request(Constants.request_path.PUSH_TO_SINGLE, retry_times, **push_message)

    def save_list_payload(self, push_message, retry_times=3):
        """
        保存群推消息
        :param push_message: 消息体(请求参数对象)
        :param retry_times: 重试次数
        """
        return self._try_http_request(Constants.request_path.SAVE_LIST_PAYLOAD, retry_times, **push_message)

    def send_to_list(self, target_push_message, retry_times=3):
        """
        推送群推消息
        :param target_push_message: 消息体(请求参数对象)
        :param retry_times: 重试次数
        """
        return self._try_http_request(Constants.request_path.PUSH_TO_LIST, retry_times, **target_push_message)

    def send_to_all(self, push_message, retry_times=3):
        """
        发送全推消息
        :param push_message: 消息体(请求参数对象)
        :param retry_times: 重试次数
        """
        return self._try_http_request(Constants.request_path.PUSH_TO_ALL, retry_times, **push_message)

    def get_statistics(self, taskids_message, retry_times=3):
        """
        发送全推消息
        :param taskids_message: 消息体(请求参数对象)
        :param retry_times: 重试次数
        """
        return self._try_http_request(Constants.request_path.GET_STATISTICS, retry_times, Constants.__HTTP_GET__,
                                      **taskids_message)
