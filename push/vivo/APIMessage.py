# coding=utf-8
from vivo.APIConstants import Constants


class MessageDict(dict):
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'message' object has no attribute %s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


class TaskMessage(object):
    def __init__(self):
        self.__message_dict = MessageDict()

    def task_ids(self, task_ids):
        task_ids_set = set(task_ids)
        self.__message_dict[Constants.http_param_task_ids] = task_ids_set
        return self

    '''
        message params build method
    '''

    def message_dict(self):
        return self.__message_dict


class TargetMessage(object):
    def __init__(self):
        self.__message_dict = MessageDict()

    def reg_ids(self, reg_ids):
        self.__message_dict[Constants.http_param_reg_ids] = reg_ids
        return self

    def aliases(self, aliases):
        self.__message_dict[Constants.http_param_aliases] = aliases
        return self

    def task_id(self, task_id):
        self.__message_dict[Constants.http_param_task_id] = task_id
        return self

    def request_id(self, request_id):
        self.__message_dict[Constants.http_param_request_id] = request_id
        return self

    '''
        message params build method
    '''

    def message_dict(self):
        return self.__message_dict


class PushMessage(object):
    def __init__(self):
        self.__message_dict = MessageDict()

    def reg_id(self, reg_id):
        self.__message_dict[Constants.http_param_reg_id] = reg_id
        return self

    def ali_as(self, ali_as):
        self.__message_dict[Constants.http_param_ali_as] = ali_as
        return self

    def content(self, content):
        self.__message_dict[Constants.http_param_content] = content
        return self

    def title(self, title):
        self.__message_dict[Constants.http_param_title] = title
        return self

    def notify_type(self, notify_type):
        self.__message_dict[Constants.http_param_notify_type] = notify_type
        return self

    def time_to_live(self, time_to_live):
        self.__message_dict[Constants.http_param_time_to_live] = time_to_live
        return self

    def skip_type(self, skip_type):
        self.__message_dict[Constants.http_param_skip_type] = skip_type
        return self

    def skip_content(self, skip_content):
        self.__message_dict[Constants.http_param_skip_content] = skip_content
        return self

    def network_type(self, network_type=-1):
        self.__message_dict[Constants.http_param_network_type] = network_type
        return self

    def request_id(self, request_id):
        self.__message_dict[Constants.http_param_request_id] = request_id
        return self

    def client_custom_map(self, **client_custom_map):
        self.__message_dict[Constants.http_param_client_custom_map] = client_custom_map
        return self

    def extra(self, value1, value2):
        extra = {'callback': value1, 'callback.param': value2}
        self.__message_dict[Constants.http_param_extra] = extra
        return self

    '''
        message params build method
    '''

    def message_dict(self):
        return self.__message_dict
