# assembly-3
**Points: 400**

## Reversing

## Question
>What does asm3(0xbda42100,0xb98dd6a5,0xecded223) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/assembly-3_4_05ce5be4420bf9bd2ff37caf87e32898. 
```asm
.intel_syntax noprefix
.bits 32
	
.global asm3

asm3:
	push   	ebp
	mov    	ebp,esp
	mov	eax,0xbc
	xor	al,al
	mov	ah,BYTE PTR [ebp+0x9]
	sal	ax,0x10
	sub	al,BYTE PTR [ebp+0xc]
	add	ah,BYTE PTR [ebp+0xd]
	xor	ax,WORD PTR [ebp+0x10]
	mov	esp, ebp
	pop	ebp
	ret
```

### Hint
>more(?) registers

## Solution
We can  solve this challenge easily executing the asm.
- 1. Convert to nasm syntax
```asm
section .text
    global asm3

asm3:
	push   	ebp
	mov    	ebp,esp
	mov	eax,0xbc
	xor	al,al
	mov	ah,BYTE [ebp+0x9]
	sal	ax,0x10
	sub	al,BYTE [ebp+0xc]
	add	ah,BYTE [ebp+0xd]
	xor	ax,WORD [ebp+0x10]
	mov	esp, ebp
	pop	ebp
	ret
```
- 2. Create a solver.c:
```c
#include <stdio.h>
extern int asm3(int a, int b, int c);

int main(int argc, char *argv[]) {
    
	printf("Flag: 0x%x\n", asm3(0xbda42100,0xb98dd6a5,0xecded223));
	return 0;
}
```
- 3. Compile and run the code
```bash
~ nasm -f elf32 ass-3.asm -o asm3.o
~ gcc solver.c asm3.o -o solver -m32
~ ./solver
Flag: 0x478
```
### Flag
`0x478`
