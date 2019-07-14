# admin panel
**Points: 150**

## Forensics

## Question
>We captured some traffic logging into the admin panel, can you find the password?

### Hint
>Tools like wireshark are pretty good for analyzing pcap files.

## Solution
We open it with **Wireshark** and filter with `http.request.method == POST` and then `Follow > TCP Stream`

![alt text](https://github.com/manulqwerty/picoCTF-2018-WriteUp/blob/master/Forensics/admin%20panel/images/1.gif)

### Flag
`picoCTF{n0ts3cur3_9feedfbc}`
