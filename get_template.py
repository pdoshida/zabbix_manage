#!/bin/python
from pyzabbix import ZabbixAPI

zapi = ZabbixAPI('http://localhost/zabbix')
zapi.login('Admin', 'zabbix')
print('Connected to Zabbix API Version %s' % zapi.api_version() + '\n')

templates = zapi.template.get(
  output=['name', 'templateid'],
  selectItems=['itemid'],
  selectDiscoveries=['itemid'],
  selectHttpTests=['httptestid']
)

for tp in filter(lambda tps: not 'Template' in tps['name'], templates):
  print(tp['name'])
