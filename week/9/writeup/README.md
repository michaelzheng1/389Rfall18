Writeup 9 - Crypto I
=====

Name: Michael Zheng
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Michael Zheng

## Assignment 9 Writeup

### Part 1 (60 Pts)
Since I have the password list and the hashes, I can brute force the password 
combinations. First, I iterated the hashes and then the wordlist. While iterating
through the all the salt options, I appended the salt and the word from wordlist
with hashlib.256() function. Then I check if the hashed output matches the hash
value. Below is the output after running "python part1.py".

![Alt text](https://github.com/michaelzheng1/389Rfall18/blob/master/week/9/writeup/Part1.png)


### Part 2 (40 Pts)
First I added the IP and the port. The specification doesn't tell much what I
should implement for part2.py so I decided to run the program to see the output.

![Alt text](https://github.com/michaelzheng1/389Rfall18/blob/master/week/9/writeup/Part2(2).png)

From the output, I have to find the hash by using the given word and crypto
function. This was similar to the interactive shell where I have to parse the
output. The word "the" is before the given crypto function and the word "of" is
before the given word. I decided to use the index of the word "the" and "of",
to store the word and crypto function. After modifying and running the code, the
program asks me to find another hash. I placed my code inside a loop and modified
along the way until I get the flag CMSC389R-{H4sh-5l!ngInG-h@sH3r}.

![Alt text](https://github.com/michaelzheng1/389Rfall18/blob/master/week/9/writeup/Part2.png)
![Alt text](https://github.com/michaelzheng1/389Rfall18/blob/master/week/9/writeup/Part2(1).png)
