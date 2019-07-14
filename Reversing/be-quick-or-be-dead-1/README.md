# be-quick-or-be-dead-1
**Points: 200**

## Reversing

## Question
>You find this when searching for some music, which leads you to be-quick-or-be-dead-1. Can you run it fast enough? You can also find the executable in /problems/be-quick-or-be-dead-1_4_98374389c5652d0b16055427532f098f.

### Hint
> What will the key finally be?

## Solution
A normal execution:
![alt text](https://github.com/manulqwerty/picoCTF-2018-WriteUp/blob/master/Reversing/be-quick-or-be-dead-1/images/3.png)

Let's dissamble the binary:
```c
main(void)
{
  header();
  set_timer();
  get_key();
  print_flag();
  return 0;
}
```
# Method 1
We can get the flag no calling 'set_timer()' using Radare2:
```
db 0x00400856
dr rip=0x0040084f
dc
```
![alt text](https://github.com/manulqwerty/picoCTF-2018-WriteUp/blob/master/Reversing/be-quick-or-be-dead-1/images/2.png)

# Method 2
Let's dissamble
```c
long calculate_key(void)
{
  uint local_c;
  
  local_c = 0x75c3328b;
  do {
    local_c = local_c + 1;
  } while (local_c != 0xeb866516);
  return (ulong)local_c;
}
```
The required value for the return is 0xeb866516, so we just have to set local_c as 0xeb866515:
```
pdf @ sym.calculate_key
s 0x0040070a
wa mov dwork [rbp-0x], 0xeb866515
q
```
![alt text](https://github.com/manulqwerty/picoCTF-2018-WriteUp/blob/master/Reversing/be-quick-or-be-dead-1/images/5.png)
### Flag
`picoCTF{why_bother_doing_unnecessary_computation_402ca676}`
