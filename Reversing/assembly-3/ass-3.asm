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

