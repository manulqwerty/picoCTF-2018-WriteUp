# Truly an Artist
**Points: 200**

## Forensics

## Question
>Can you help us find the flag in this Meta-Material? You can also find the file in /problems/truly-an-artist_4_cdd9e325cf9bacd265b98a7fe336e840. 

### Hint
>Try looking beyond the image.
>Who created this?

## Solution
We have to check the metainfo
```bash
exiftool 2018.png
```

### Flag
`picoCTF{look_in_image_13509d38}`
