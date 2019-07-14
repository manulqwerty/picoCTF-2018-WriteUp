#!/usr/bin/env python3
from pwn import *
import re
import json
import collections


def getMaxOcurrences(L):
    d = collections.defaultdict(int)
    for i in L:
        d[i] += 1
    result = max(d.items(), key=lambda x: x[1])
    return result[0]
    
def getUniqueCount(L):
    unique= [item for item, count in collections.Counter(L).items() if count == 1]
    return len(unique)


with open("files/incidents.json","r") as f:
    data = json.load(f)

length = len(data["tickets"])
srcIps = []
dstIps = []
filesSent = [] 
for i in range(0,length):
	srcIps.append(data["tickets"][i]["src_ip"])
for i in range(0,length):
	dstIps.append(data["tickets"][i]["dst_ip"])
for i in range(0,length):
	filesSent.append(data["tickets"][i]["file_hash"])

p = remote("2018shell.picoctf.com", 40952)
p.recvuntil("ones.\n")
p.sendline(getMaxOcurrences(srcIps))
output = p.recvuntil("?")
ip = re.findall('[0-9]+(?:\.[0-9]+){3}', output.decode('utf-8'))

p.sendline(str(srcIps.count(ip[0])))
p.recvuntil("places.\n")
p.sendline(str(length/len(set(filesSent))))
p.recvuntil("flag: ")
print (p.recvline().decode('utf-8'))
p.close()

