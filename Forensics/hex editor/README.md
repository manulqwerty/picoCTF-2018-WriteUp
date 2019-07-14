# hex editor
**Points: 150**

## Forensics

## Question
>This cat has a secret to teach you. You can also find the file in /problems/hex-editor_0_8c20f979e6b2740dee597871ff1a74ee on the shell server. 

### Hint
>What is a hex editor?
>Maybe google knows.
>xxd>
hexedit
>bvi

## Solution
Let's check the strings of the file given:
```bash
strings hex_editor.jpg | tail -n 1
```

### Flag
`picoCTF{and_thats_how_u_edit_hex_kittos_3E03e57d}`
