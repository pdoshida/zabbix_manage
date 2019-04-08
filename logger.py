#!/bin/python
from pyzabbix import ZabbixAPI

import sys
import logging
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
log = logging.getLogger('pyzabbix')
log.addHandler(stream)
log.setLevel(logging.DEBUG)

zapi = ZabbixAPI("http://localhost/zabbix")
zapi.login("zabbix user", "zabbix pasword")
#print("Connected to Zabbix API Version %s" % zapi.api_version() + "\n")

host = zapi.host.get(output="host")
#host = zapi.host.get(output=["hostid", "host"], selectInterfaces=["ip"], selectGroups=["name"])
#for h in host:
#	print(h)
