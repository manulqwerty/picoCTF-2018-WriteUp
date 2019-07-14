#include <stdio.h>
int main(int argc, char *argv[])
{
    int i, n = 1058, t1 = 0, t2 = 1, nextTerm;

    for (i = 1; i <= n; ++i)
    {
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }
    printf("[+] Paste this on Radare2:\n");
    printf("aaa\npdf @ sym.calculate_key\ndb 0x0040074b\ndc\ndr rip=0x0040075a\ndr eax=0x%x\ndc", t1);
    return 0;
}

