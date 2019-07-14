#include <stdio.h>
extern int asm3(int a, int b, int c);

int main(int argc, char *argv[]) {
    
	printf("Flag: 0x%x\n", asm3(0xbda42100,0xb98dd6a5,0xecded223));
	return 0;
}
