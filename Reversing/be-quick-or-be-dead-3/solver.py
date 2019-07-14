import ctypes
inp = 0x19965
mem = {}

def calc(init_value):
    if init_value in mem:
        return mem[init_value]
        
    if init_value < 5:
        final = init_value * init_value + 0x2345
    else:
        var1 = calc(init_value - 1)
        var2 = calc(init_value - 2)
        var3 = calc(init_value - 3)
        var4 = calc(init_value - 4)
        var5 = calc(init_value - 5)
        final = var5 * 0x1234 + (var1 - var2) + (var3 - var4)
    
    mem[init_value] = final    
    return final

for i in range (inp):
    calc(i)
print ('[+] Paste this on Radare2:')
print ('aaa')
print ('pdf @  sym.calculate_key')
print ('db 0x00400792')
print ('dc')
print ('dr rip=0x004007a1')
print ('dr eax=0x%x' % ctypes.c_uint32(calc(inp)).value)
print ('dc')
