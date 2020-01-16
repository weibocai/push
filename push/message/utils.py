import json
import requests

from datetime import datetime
from functools import lru_cache
from django.conf import settings
from hyper import tls, HTTP20Connection

from vivo.APIMessage import *
from vivo.APISender import APISender as vo_APISender
from APISender import APISender as xm_APISender
from base.APIMessage import Constants as xm_Constants
from base.APIMessage import PushMessage as xm_PushMessage


# con_type: 与表中的con_type一致
# is_all: 与表中的is_all一致


def ios_push(title, text, **kwargs):
    """
    kwargs={'product':'', 'product_id': '产品id', 'device_token': 'device_token'}
    """
    content = {
        "aps": {
            "alert": {
                "title": title,
                "body": text,
            },
        },
        "classify": kwargs['product'],
        "carousel_id": kwargs['product_id'],
    }
    conf = settings.IOS_CONF
    ssl_context_obj = tls.init_context(cert=conf['cer_path'], cert_password=conf['cer_path'])
    conn = HTTP20Connection('api.development.push.apple.com', port=443, ssl_context=ssl_context_obj)
    conn.request(method='POST', url=f"/3/device/{kwargs['device_token']}", body=json.dumps(content))
    reps = conn.get_response()

    return reps.status


@lru_cache(maxsize=124)
def get_hw_token(minute_):
    conf = settings.HW_CONF
    para = {
        'grant_type': 'client_credentials',
        'client_id': conf['app_id'],
        'client_secret': conf['client_secret']
    }
    url = 'https://oauth-login.cloud.huawei.com/oauth2/v2/token'

    data = requests.post(url, data=para).json()
    return data.get('access_token', None)


def hw_push(title, text, con_type=1, is_all=0, validate_only=False, **kwargs):
    """
    :param title:
    :param text:
    :param con_type: 自定义发送，普通发送
    :param validate_only:
    :param is_all: 全部推送，部分推送
    :param kwargs: {'product':'', '': '产品id', 'device_token': ['device_token1, device_token2']}
    :return:
    """
    context = {
        "validate_only": validate_only,
        "message": {
            "notification": {
                "title": title,
                "body": text
            },
            "android": {
                "notification": {
                    "title": title,
                    "body": text,
                    "click_action": {
                        "type": con_type,
                    }
                }
            },
            "token": [kwargs['device_token']]
        }
    }
    if is_all == 0:
        context['message']['token'] = [kwargs['device_token']]
    else:
        context['message']['topic'] = '所有用户'
    if con_type == 1:
        product = {'body_loc_key': kwargs['product_id'], 'title_loc_key': kwargs['product']}
        intent = f"intent://com.huawei.codelabpush/deeplink?#Intent;scheme=pushscheme;launchFlags=0x4000000;S.name={product};end"
        context['message']['android']['notification']['click_action']['intent'] = intent
    elif con_type == 2:
        context['message']['android']['notification']['click_action']['url'] = kwargs.get('url',
                                                                                          'https://www.getfan.cn/')
    else:
        pass

    now = datetime.now()
    minute = now.minute
    minute_ = 30 if minute > 30 else 0
    access_token = get_hw_token(minute_)
    if access_token is None:
        return False

    conf = settings.HW_CONF
    url = f"https://push-api.cloud.huawei.com/v1/{conf['app_id']}/messages:send"
    headers = {'Authorization': access_token}
    data = requests.post(url, json=context, headers=headers).json()
    return data


def xm_push(title, text, is_all=False, con_type=1, **kwargs):
    xm_Constants.use_official()
    sender = xm_APISender(settings.XM_CONF['client_secret'])
    if con_type != 1:
        raise ValueError('小米暂时只支持打开应用内项目')
    product = {'body_loc_key': kwargs['product_id'], 'title_loc_key': kwargs['product']}
    message = xm_PushMessage().restricted_package_name(settings.XM_CONF['package_name']).notify_type(-1).notify_id(
        0).collapse_key(None) \
        .title(title).description(text) \
        .pass_through(0).payload(f'{product}')
    if is_all == 0:
        return sender.send(message.message_dict(), kwargs['device_token'])
    elif is_all == 1:
        return sender.send_to_alias(kwargs['device_token'])
    else:
        return sender.broadcast_all(message.message_dict())


def vo_push(title, text, *args, **kwargs):
    sender_send = vo_APISender(settings.VO_CONF['app_secret'])
    is_all = kwargs['type']

    message = PushMessage().title(title).content(text).notify_type(2).network_type(-1).skip_type(4).time_to_live(1000) \
        .request_id('1234567890123456') \
        .client_custom_map(title_loc_key=kwargs.get('product', None), body_loc_key=kwargs.get('product_id', None)) \
        .message_dict()
    if is_all == 0:
        message['reg_id'] = kwargs['device_token']
        return sender_send.send(message)
    elif is_all == 1:
        send_to_list = TargetMessage() \
            .reg_ids(args) \
            .request_id('1234567890123456') \
            .message_dict()
        return sender_send.send_to_list(send_to_list)
    else:
        return sender_send.send_to_all(message)
