import logging
import time
import json
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse

from vivo.APIConstants import Constants
from vivo.APIError import APIError

_MAX_BACKOFF_DELAY = 1024000


class JsonDict(dict):
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'JsonDict' object has no attribute %s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


def _parse_json(body):
    """
    convert json object to python object
    :param body: response data
    """

    def _obj_hook(pairs):
        o = JsonDict()
        for k, v in pairs.items():
            o[str(k)] = v
        return o

    return json.loads(body, object_hook=_obj_hook)


def _build_request_url(request_path):
    return Constants.http_server + request_path[0]


def _http_call(url, method, token, **message):
    """
    :param url: http request url
    :param method: http request method
    :param message: params
    """
    params = _encode_params(message) if method == Constants.__HTTP_GET__ else ''
    http_url = '%s?%s' % (url, params) if method == Constants.__HTTP_GET__ else url
    http_body = None if method == Constants.__HTTP_GET__ else message
    req = urllib.request.Request(http_url, data=json.dumps(http_body).encode("utf-8"))
    if token:
        req.add_header('authToken', token)
    req.add_header('Content-Type', 'application/json;charset=UTF-8')
    try:
        resp = urllib.request.urlopen(req, timeout=5)
        r = _parse_json(resp.read().decode())
        return r
    except urllib.error.URLError as e:
        raise APIError('-5', e.reason, 'http error ' + str(e.code))
    except BaseException as e:
        raise e


def _encode_params(kw):
    """
    splic get request url
    :param kw: params
    """
    args = ''
    s = '['
    for k, v in kw.items():
        for t in v:
            s = s + str(t) + ','
        args = '%s=%s' % (k, s[:-1])
    return args


class Base(object):
    def __init__(self, secret, token=None):
        self.secret = secret
        self.token = token

    def set_token(self, token):
        self.token = token

    def _http_request(self, request_path, method, **message):
        """
        :param request_path: http interface
        :param method: GET|POST
        :param message: params
        """
        request_url = _build_request_url(request_path)
        try:
            ret = _http_call(request_url, method, self.token, **message)
            return ret
        except APIError as ex:
            logging.error("%s request: [%s] error [%s]" % (Constants.http_server, request_url, ex))
            raise ex

    def http_post(self, request_path, **message):
        logging.info("POST %s" % request_path[0])
        return self._http_request(request_path, Constants.__HTTP_POST__, **message)

    def http_get(self, request_path, **message):
        logging.info("GET %s" % request_path[0])
        return self._http_request(request_path, Constants.__HTTP_GET__, **message)

    def _try_http_request(self, request_path, retry_times, method=Constants.__HTTP_POST__, **message):
        is_fail, try_time, result, sleep_time = True, 0, None, 1
        while is_fail and try_time < retry_times:
            try:
                if method == Constants.__HTTP_POST__:
                    result = self.http_post(request_path, **message)
                elif method == Constants.__HTTP_GET__:
                    result = self.http_get(request_path, **message)
                else:
                    raise APIError('-2', 'not support %s http request' % method, 'http error')
                is_fail = False
            except APIError as ex:
                '''
                    failure retry
                '''
                if ex.error_code == '-5':
                    is_fail = True
                try_time += 1
                logging.error('code:[%s] - description:[%s] - reason:[%s] - try_time:[%s]' % (
                ex.error_code, ex.error, ex.request, try_time))
                time.sleep(sleep_time)
                if 2 * sleep_time < _MAX_BACKOFF_DELAY:
                    sleep_time *= 2
        if not result:
            raise APIError('-3', 'retry %s time failure' % retry_times, 'request error')
        return result
