#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ..util import get
GATE_WAY = ''


def gen_error(key, html=None):
    return {
        'default': {
            'code': -1,
            'error': 'lack of params.',
            'example': GATE_WAY + '?url=http://baidu.com'
        },
        'html': {
            'code': 301,
            'html': html
        },
        'server': {
            'code': 2,
            'error': 'object server error.'
        }
    }[key]


def query(gateway, queryString):
    global GATE_WAY
    GATE_WAY = gateway
    if 'url' not in queryString:
        return gen_error('default')
    try:
        return gen_error('html', get(queryString['url']).text)
    except Exception:
        return gen_error('server')
