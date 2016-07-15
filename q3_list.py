#!/usr/bin/python

import socket
import struct
import sys

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

if len(sys.argv) > 1:
    if sys.argv[1] == '-h':
        print('Usage: %s [<SERVER>:<PORT>]' % sys.argv[0])
        quit(1)    
    (ip, port) = sys.argv[1].split(':')
    port = int(port)
    ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ss.settimeout(10)
    ss.connect((ip, port))
    ss.send(b'\xFF\xFF\xFF\xFFgetstatus')
    dd = ss.recv(999999)
    i = 0
    status = {}
    for e in dd.replace(b'\n',b'').split(b'\\')[1:]:
        e = e.decode('utf-8')
        if i % 2 == 0:
            k = e
        else:
            status[k] = e
        i += 1
    for (k,v) in status.items():
        print('  %s : %s' % (k, v))
    ss.close()
    quit(0)
    
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(3)
s.connect((MASTER, PORT))
s.send(b'\xFF\xFF\xFF\xFFgetservers 68 empty full demo')
addr = {}
d = s.recv(999999)
for (ip, port) in get_ip_port(d):
    print('%s:%s' % (ip, port))
s.close()
    
