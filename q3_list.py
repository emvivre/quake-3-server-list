#!/usr/bin/python

import socket
import struct

def get_ip_port(packet):
    p = packet[len('\xFF\xFF\xFF\xFFgetserversResponse'):]
    addr = []
    while len(p) is not 0:
        (ip_byte_0, ip_byte_1, ip_byte_2, ip_byte_3, port_byte_0, port_byte_1) = struct.unpack('BBBBBB', p[1:7])
        port = (port_byte_0 << 8) + port_byte_1
        ip = '%d.%d.%d.%d' % (ip_byte_0, ip_byte_1, ip_byte_2, ip_byte_3)
        addr.append((ip, port))
        p = p[7:]
    return addr

MASTER = 'master.ioquake3.org'
# MASTER = 'master.huxxer.de'
# MASTER = 'master3.idsoftware.com'
# MASTER = 'master.gnw.de'
# MASTER = 'masterserver.exhale.de'
# MASTER = 'master.gamershut.de'

PORT = 27950

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(3)
s.connect((MASTER, PORT))
s.send("\xFF\xFF\xFF\xFFgetservers 68 empty full demo\n")
addr = {}
d = s.recv(999999)
for (ip, port) in get_ip_port(d):
    print '%s:%s' % (ip, port)
s.close()
    
