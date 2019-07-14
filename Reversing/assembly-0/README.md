# assembly-0
**Points: 150**

## Reversing

## Question
>What does asm0(0xd8,0x7a) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/assembly-0_1_fc43dbf0079fd5aab87236bf3bf4ac63.

### Hint
>basical assembly tutorial (https://www.tutorialspoint.com/assembly_programming/assembly_basic_syntax.htm) \n assembly registers (https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm)

## Solution


```asm
asm0:
        push    ebp
        mov     ebp,esp
        mov     eax,DWORD PTR [ebp+0x8]
        mov     ebx,DWORD PTR [ebp+0xc]
        mov     eax,ebx
        mov     esp,ebp
        pop     ebp
        ret
```
The returned value is _eax_. Initilly the first value (0xd8) is stored in _eax_, and the second value (0x7a) is stored in _ebx_.
On the next line (_mov     eax,ebx_) _eax_=_ebx_ , so the returned value is : 0x7a

### Flag
`0x7a`
