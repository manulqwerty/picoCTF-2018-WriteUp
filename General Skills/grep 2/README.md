# grep 2
**Points: 125**

## General Skills

## Question
>This one is a little bit harder. Can you find the flag in /problems/grep-2_2_413a577106278d0711d28a98f4f6ac28/files on the shell server? Remember, grep is your friend. 

### Hint
>grep tutorial (https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution
![alt text](https://github.com/manulqwerty/picoCTF-2018-WriteUp/blob/master/General%20Skills/grep%202/images/1.png)
```bash
grep -r 'picoCTF' /problems/grep-2_2_413a577106278d0711d28a98f4f6ac28/files
```
> /problems/grep-2_2_413a577106278d0711d28a98f4f6ac28/files/files7/file9:picoCTF{grep_r_and_you_will_find_8eb84049}

### Flag
`picoCTF{grep_r_and_you_will_find_8eb84049}`
