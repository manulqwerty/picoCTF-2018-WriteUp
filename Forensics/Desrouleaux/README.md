# Desrouleaux
**Points: 150**

## Forencsics

## Question
>Our network administrator is having some trouble handling the tickets for all of of our incidents. Can you help him out by answering all the questions? Connect with nc 2018shell.picoctf.com 40952. incidents.json

### Hint
>If you need to code, python has some good libraries for it.

## Solution
The program asks us about the **incidents.json** file
#### Questions
- What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.
- How many unique destination IP addresses were targeted by the source IP address 164.209.29.191? (the ip changes)
- What is the number of unique destination ips a file is sent, on average? Needs to be correct to 2 decimal places.

I wrote a python script to resolve it.

```python
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
```

### Flag
`picoCTF{J4y_s0n_d3rUUUULo_b6cacd6c}`
