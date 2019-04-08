#!/bin/python
from pyzabbix import ZabbixAPI
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

tri=[]
tmp=[]

zapi = ZabbixAPI('http://localhost/zabbix')
zapi.login('Admin', 'zabbix')

for template in zapi.template.get(selectTriggers='triggerid'):
  #print (template['name'])
  if 'Template' in template['name']:
    continue
  for trigger in template['triggers']:
    id = trigger['triggerid']
    for t in zapi.trigger.get(filter={'triggerid':id}):
      tmp.append(template['name'])
      tri.append(t['description'])


data=pd.DataFrame({'Template Name':tmp,'Trigger':tri})
data.to_csv('triggers_templates.csv',index=False)
