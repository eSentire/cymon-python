from copy import copy
import json
import logging

import requests

class Cymon(object):

    def __init__(self, auth_token, endpoint='https://cymon.io/api/nexus/v1'):
        self.endpoint = endpoint
        self.session = requests.Session()
        self.session.headers = {
            'content-type': 'application/json',
            'accept': 'application/json',
            'Authorization': 'Token %s' %auth_token
        }

    def get(self, method, params=None):
        r = self.session.get(self.endpoint + method, params=params)
        r.raise_for_status()
        return r

    def post(self, method, params, headers=None):
        r = self.session.post(self.endpoint + method, data=json.dumps(params), headers=headers)
        r.raise_for_status()
        return r

    def ip_lookup(self, ip_addr):
        r = self.get('/ip/' + ip_addr)
        return json.loads(r.text)

    def ip_events(self, ip_addr):
        r = self.get('/ip/' + ip_addr + '/events')
        return json.loads(r.text)

    def ip_domains(self, ip_addr):
        r = self.get('/ip/' + ip_addr + '/domains')
        return json.loads(r.text)

    def ip_url(self, ip_addr):
        r = self.get('/ip/' + ip_addr + '/urls')
        return json.loads(r.text)

    def ip_timeline(self, ip_addr):
        r = self.get('/ip/' + ip_addr + '/timeline')
        return json.loads(r.text)

    def domain_lookup(self, name):
        r = self.get('/domain/' + name)
        return json.loads(r.text)

    def domain_events(self, name):
        r = self.get('/domain/' + name + '/events')
        return json.loads(r.text)

    def url_lookup(self, url):
        r = self.get('/url/' + url)
        return json.loads(r.text)

    def url_location(self, location):
        r = self.get('/url/' + location)
        return json.loads(r.text)

    def blacklist_ip(self, tag):
        r = self.get('/blacklist/ip/' + tag)
        return json.loads(r.text)
         
     def blacklist_domain(self, tag):
        r = self.get('/blacklist/domain/' + tag)
        return json.loads(r.text)















