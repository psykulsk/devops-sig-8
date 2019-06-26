#!/usr/bin/env python
import falcon
import threading
import time
import yaml

global_config_lock = threading.Lock()
config = { 'magic_word': 'abc' }


def dummy_config_changer():

    while True:
        time.sleep(1)
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

        try:
            print('GCL locking')
            with global_config_lock:
                config['magic_word'] = new_magic_word
                print('GCL unlocking')
        except Exception as e:
            print('exc')
    print("Thread %s: finishing")


config_changers = {
    'dummy_config_changer': dummy_config_changer
}


class VarResource:
    def on_get(self, req, resp):
        with global_config_lock:
            obj = {'todays_magic_word': config['magic_word']}
            resp.media = obj


class ConstResource:
    def on_get(self, req, resp):
        resp.media = { 'devops_sig_no': 8 }


class TimeResource:
    def on_get(self, req, resp):
        resp.media = int(time.time())

config_changer = 'dummy_config_changer'
config_changer_thread = threading.Thread(target=config_changers[config_changer])
config_changer_thread.start()
api = falcon.API()
api.add_route('/var', VarResource())
api.add_route('/const', ConstResource())
api.add_route('/time', TimeResource())


