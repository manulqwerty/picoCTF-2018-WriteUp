# HEEEEEEERE'S Johnny!
**Points: 100**

## Cryptography

## Question
>Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with nc 2018shell.picoctf.com 38860. Files can be found here: passwd shadow. 

### Hint
>If at first you don't succeed, try, try again. And again. And again.

## Solution

`hashcat -a 0 -m 1800 root.hash /usr/share/wordlists/rockyou.txt`
>\$6$HRMJoyGA$26FIgg6CU0bGUOfqFB0Qo9AE2LRZxG8N3H.3BK8t49wGlYbkFbxVFtGOZqVIq3qQ6k0oetDbn2aVzdhuVQ6US.:hellokitty

```
# nc 2018shell.picoctf.com 38860
Username: root
Password: hellokitty
picoCTF{J0hn_1$_R1pp3d_4e5aa29e}
```

### Flag
`picoCTF{J0hn_1$_R1pp3d_4e5aa29e}`
