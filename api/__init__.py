from flask import jsonify


def make_response_ok(data=None):
    """
    :param data:
    :return:
    """
    resp = {'code': 0, 'msg': 'success'}
    if data:
        resp['data'] = data
    return jsonify(resp)


def make_response_error(code, msg):
    """
    :param code:
    :param msg:
    :return:
    """
    resp = {'code': code, 'msg': msg}
    return jsonify(resp)
