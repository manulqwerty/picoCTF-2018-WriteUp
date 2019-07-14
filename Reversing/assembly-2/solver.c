#include <stdio.h>
extern int asm2(int a, int b);

int main(int argc, char *argv[]) {

	printf("Flag: 0x%x\n", asm2(0x4,0x2d));
	return 0;
}
