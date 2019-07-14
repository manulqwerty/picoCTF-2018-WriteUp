# pipe
**Points: 110**

## General Skills

## Question
>During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file. Can you find a way to save the output from this program and search for the flag? Connect with 2018shell.picoctf.com 2015.

### Hint
>Remember the flag format is picoCTF{XXXX}
>Ever heard of a pipe? No not that kind of pipe... This kind

## Solution
`nc 2018shell.picoctf.com 2015| grep picoCTF`
>picoCTF{almost_like_mario_8861411c}


### Flag
`picoCTF{almost_like_mario_8861411c}`
