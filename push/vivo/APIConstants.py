# coding=utf-8
class Constants(object):
    def __init__(self):
        pass

    def enum(**self):
        return type('Enum', (), self)


    __VERSION__ = '1.0'
    __HTTP_GET__ = 0
    __HTTP_POST__ = 1

    _METHOD_MAP = {'GET': __HTTP_GET__, 'POST': __HTTP_POST__}

    http_server = "https://api-push.vivo.com.cn"

    '''
        targetMessage parameter name
    '''

    http_param_reg_ids = "regIds"
    http_param_aliases = "aliases"
    http_param_task_id = "taskId"

    '''
        pushMessage parameter name
    '''
    http_param_reg_id = "regId"
    http_param_content = "content"
    http_param_title = "title"
    http_param_ali_as = "alias"
    http_param_notify_type = "notifyType"
    http_param_time_to_live = "timeToLive"
    http_param_skip_type = "skipType"
    http_param_skip_content = "skipContent"
    http_param_network_type = "networkType"
    http_param_client_custom_map = "clientCustomMap"
    http_param_extra = "extra"


    http_param_request_id = "requestId"

    http_param_task_ids = "taskIds"


    request_path = enum(
        GET_TOKEN=["/message/auth"],
        PUSH_TO_SINGLE=['/message/send'],
        SAVE_LIST_PAYLOAD=['/message/saveListPayload '],
        PUSH_TO_LIST=['/message/pushToList'],
        PUSH_TO_ALL=['/message/all'],
        GET_STATISTICS=['/report/getStatistics'],
    )


