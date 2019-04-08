#!/bin/python
from pyzabbix import ZabbixAPI
import sys
import logging

stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
log = logging.getLogger('pyzabbix')
log.addHandler(stream)
log.setLevel(logging.DEBUG)

zapi = ZabbixAPI('http://localhost/zabbix')
zapi.login('zabbix user', 'zabbix password')
print('Connected to Zabbix API Version %s' % zapi.api_version() + '\n')
