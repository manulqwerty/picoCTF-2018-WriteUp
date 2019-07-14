import string
from pwn import *

text_in = string.printable
p = process('./main')
p.recvline()
p.sendline(text_in)
ciphertext = p.recvline()
m = re.search('Here\'s your ciphertext: (.*)', ciphertext)
ciphertext = m.group(1)
cipher = ciphertext.split(' ')
p.recvuntil('Now quack it! : ')
flag = p.recvline().strip().split(' ')
p.close()  

cipher_dicc = {}
for a, b in zip(cipher, text_in):
    cipher_dicc[a] = b

print ('[+] Flag: %s' % (''.join( cipher_dicc[i] for i in flag)))
