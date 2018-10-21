Writeup 7 - Forensics I
======

Name: Michael Zheng
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Michael Zheng

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG

2. Chicago, Illinois.John Hancock Center

3. August 22, 2018 11:33:24

4. IPhone 8

5. 539.5 m above sea level

6. Using strings -n 15 image, I got CMSC389R-{look_I_f0und_a_string}

### Part 2 (55 pts)


First I ran ./binary and received the message “Where is your flag?”  That wasn't really help so I tried string -n binary to get the glimpse what could be inside of the binary file. I decided to use gdb to look at the assembly code for the binary file. I entered “gdb binary” and then “disas main” to dump the assembler code. I noticed there was a lot of calls to movb with hexdecimals.

![Alt text](https://github.com/michaelzheng1/389Rfall18/blob/master/week/7/writeup/Screenshot%20from%202018-10-20%2021-55-15.png)

I decided to gather the values 0x2f, 0x74, 0x6d, 0x70, 0x2f, 0x2e, 0x73, 0x74, 0x65, 0x67, 0x6f, and 0x0. Using the website https://www.rapidtables.com/convert/number/hex-to-ascii.html, I convert the hexadecimal values to /tmp/.stego.I was kind of stump of what to do with the /tmp/.stego. I review the Forensics I slides and decided to try using binwalk. I entered binwalk .stego.

![Alt text](https://github.com/michaelzheng1/389Rfall18/blob/master/week/7/writeup/Screenshot%20from%202018-10-20%2021-58-20.png)

Now I know the .stego file is a jpeg. I extracted the .stego file by using
binwalk --dd="jpeg:jpeg" .stego.I open the _.stego.extracted file and received a picture of a stegosaurus. I assumed the flag would be within the jpeg. I review the Forensic I slides on steganography. I decided I would use steghide to extract the jpg. The terminal asks me for a password. Before I reuse the stub.py and brute force to find the password, I decided to make some educated guesses. I don’t want to wait for 30 minutes. I entered multiple attempts for the password. The first attempt I entered dinosaur, but it was incorrect. Then I tried stego before entering stegosaurs. Finally, I found the flag CMSC389R-{dropping_files_is_fun}
