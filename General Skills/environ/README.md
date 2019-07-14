# environ
**Points: 150**

## General Skills

## Question
> Sometimes you have to configure environment variables before executing a program. Can you find the flag we've hidden in an environment variable on the shell server?

### Hint
>unix env (https://www.tutorialspoint.com/unix/unix-environment.htm)

## Solution
```bash
$ env | grep -i flag                                                      
SECRET_FLAG=picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}                                                 
FLAG=Finding the flag wont be that easy...
PICOCTF_FLAG=Nice try... Keep looking!
```

### Flag
>picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492} 
