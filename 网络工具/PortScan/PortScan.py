#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nmap

#按照特定端口扫描
def port_scan(target_hosts,target_port):
    nm = nmap.PortScannerYield()
    for result in nm.scan(hosts=target_hosts,ports=target_port,arguments='-T4 -A -v -Pn '):
        ip=result[0]
        host_status=result[1]['scan'][ip]['status']['state']
        if host_status!="down":
         port_status=result[1]['scan'][ip]['tcp'][int(target_port)]['state']
         if port_status!="closed":
             print(ip+",端口状态："+port_status)
         else:
            continue
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
                print("++="+ip + "：")
                for port in ports.keys():
                    print("++++++发现端口"+str(port)+",状态：" +result[1]['scan'][ip]['tcp'][port]['state'])
            except:
                continue
        else:
            continue

if __name__ == '__main__':
    #port_scan("192.168.1.0/24","22")
    ip_scan("192.168.1.1/24")


