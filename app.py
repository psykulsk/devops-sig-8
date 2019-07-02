#!/usr/bin/env python
import falcon
import threading
import time
import yaml


try:
    with open('/etc/app/config.yml', 'r') as f:
        print("Reading from config")
        new_magic_word = yaml.load(f.read())['MAGIC']
except FileNotFoundError:
    print("FileNotFound")
    new_magic_word = 'filenotfound'
except KeyError:
    print("KeyError")
    new_magic_word = 'config key error'


class VarResource:
    def on_get(self, req, resp):
            resp.media = {'magic_word': new_magic_word}


class ConstResource:
    def on_get(self, req, resp):
        resp.media = {'devops_sig_no': 8}


class TimeResource:
    def on_get(self, req, resp):
        resp.media = int(time.time())


api = falcon.API()
api.add_route('/var', VarResource())
api.add_route('/const', ConstResource())
api.add_route('/time', TimeResource())
