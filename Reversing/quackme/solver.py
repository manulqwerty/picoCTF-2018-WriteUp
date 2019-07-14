sekrutBuffer = ')\x06\x16O+50\x1eQ\x1b[\x14K\b]+R\x17\x01W\x16\x11\\\a]'
greetingMessage = 'You have now entered the Duck Web, and you\'re in for a honkin\' good time.'
flag = ''

for i in range(0x19):
    flag += chr(ord(sekrutBuffer[i]) ^ ord(greetingMessage[i]))
    
print flag
