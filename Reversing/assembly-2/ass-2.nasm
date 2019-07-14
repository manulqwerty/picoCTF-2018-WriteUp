section .text
    global asm2

asm2:
	push   	ebp
	mov    	ebp,esp
	sub    	esp,0x10
	mov    	eax,DWORD [ebp+0xc]
	mov 	DWORD [ebp-0x4],eax
	mov    	eax,DWORD [ebp+0x8]
	mov	    DWORD [ebp-0x8],eax
	jmp    	part_b
part_a:	
	add    	DWORD [ebp-0x4],0x1
	add	DWORD [ebp+0x8],0x64
part_b:	
	cmp    	DWORD [ebp+0x8],0x1d89
	jle    	part_a
	mov    	eax,DWORD [ebp-0x4]
	mov	esp,ebp
	pop	ebp
	ret
