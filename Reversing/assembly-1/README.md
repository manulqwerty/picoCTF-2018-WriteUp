# assembly-1
**Points: 200**

## Reversing

## Question
>What does asm1(0xcd) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/assembly-1_2_ac6a59ca77a2d619ddabb3c3ffedb9a8. 

### Hint
>assembly conditions (https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solution
asm1(0xcd)
```asm
.intel_syntax noprefix
.bits 32
	
.global asm1

asm1:
	push	ebp
	mov	ebp,esp
	cmp	DWORD PTR [ebp+0x8],0xde ; cmp 0xcd and 0xde
	jg 	part_a	                 ; not jump to part_a (0xcd < 0xde)
	cmp	DWORD PTR [ebp+0x8],0x8  ; cmp 0xcd and 0x8
	jne	part_b                   ; jump to part_b (0xcd != 0x8)
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x4e
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3                 ; 0xcd - 0x3 = 0xca
	jmp	part_d
	cmp	DWORD PTR [ebp+0x8],0xee
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
part_d:
	pop	ebp
	ret                         ; ret 0xca
```
Following the comments on the previus asm:
```
asm1:
    DWORD PTR [ebp+0x8] == 0xcd
    compare 0xcd and 0xde
    if 0xcd > 0xde : jmp part_a  ;  so the jump is not taken (0xcd < 0xde)
    compare 0xcd and 0x8
    if 0x8 != 0xcd : jmp part_b  ;  so the jump is taken (0xcd != 0x8)
    
part_b:
    sub	eax,0x3 ; 0xcd - 0x3 = 0xca
    jmp	part_d

part_d:
    ret 0xca
```
### Flag
`0xca`







