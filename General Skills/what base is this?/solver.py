#!/usr/bin/env python2
from pwn import *

def bin2str(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def oct2str(s):
    s = s.replace(" ", "\\")
    return s.decode('string_escape')

host = '2018shell.picoctf.com'
port = 1225

p = remote(host, port)
r = p.recv()
m = re.search('Please give me the (.+?) as a word.', r)
p.sendline(bin2str(m.group(1).replace(" ", "")))
r = p.recv()
m = re.search('Please give me the (.+?) as a word.', r)
p.sendline(m.group(1).decode('hex'))
r = p.recv()
m = re.search('Please give me the (.+?) as a word.', r)
p.sendline(oct2str(m.group(1)))
print p.recv()


