import time
from zapv2 import ZAPv2
from pprint import pprint

target = 'http://clubgeny.com'
apikey = 'kke8ia95g2117bodtr1ts418vd'
zap = ZAPv2(apikey=apikey)

zap.urlopen(target)
time.sleep(2)

scanid = zap.spider.scan(target)

while (int(zap.spider.status(scanid)) < 100):
    print('Spider progress %: ' + zap.spider.status(scanid))
    time.sleep(2)

print('Spider completed')
time.sleep(5)

print('Scanning target %s' % target)
scanid = zap.ascan.scan(target)

while (int(zap.ascan.status(scanid)) < 100):
    print('Scan progress %: ' + zap.ascan.status(scanid))
    time.sleep(5)

print('Scan completed')

print('Hosts: ' + ', '.join(zap.core.hosts))
print('Alerts: ')
pprint(zap.core.alerts())
