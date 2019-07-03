#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nmap
import sys

sys.path.append('../IPSCAN/')
import IPSCAN

#按照特定端口扫描
def port_scan(target_host, target_port):
    nm = nmap.PortScannerYield()
    for result in nm.scan(hosts=target_host, ports=target_port, arguments='-T4 -A -v -Pn '):
        host_status=result[1]['scan'][target_host]['status']['state']
        if host_status!="down":
            port_status=result[1]['scan'][target_host]['tcp'][int(target_port)]['state']
            print("++++++ "+target_port+" 端口状态：" + port_status)
        else:
            continue

#按照特定IP扫描
def ip_scan(target_hosts):
    nm = nmap.PortScannerYield()
    for result in nm.scan(hosts=target_hosts,arguments='-T4 -A -v -Pn '):
        ip=result[0]
        host_status=result[1]['scan'][ip]['status']['state']
        if host_status!="down":
            try:
                ports= dict(result[1]['scan'][ip]['tcp'])
                for port in ports.keys():
                    print("++++++发现端口"+str(port)+",状态：" +result[1]['scan'][ip]['tcp'][port]['state'])
            except:
                continue
        else:
            continue

if __name__ == '__main__':
    ip_list=IPSCAN.get_ip_list("192.168.1.0")  #C段
    for ip in ip_list:
        print("检测IP:"+ip)
        port_scan(ip,"22")
        #ip_scan(ip)


