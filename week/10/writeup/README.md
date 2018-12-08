Writeup 10 - Crypto II
=====

Name: Michael Zheng
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Michael Zheng

## Assignment 10 Writeup

### Part 1 (70 Pts)
For Part I, I entered nc 142.93.118.186 1234 to see the output of the prompt. 
![Alt text](https://github.com/michaelzheng1/389Rfall18/blob/master/week/10/writeup/Screen(1).png)

Based from the output of the prompt, the first message I would send to server would be 1. Afterward I send my sample message to recieve a legit message from the server. Then I would use the legit message from the server to create the fake_hash. For Part II,  I created a for loop to iterated through the potential length for the secret message. Then I used potential length of the secret message and the length of the actual message to create the padding. With the padding, I created the payload with the malicious message and send it to the server. This is one of the output after sending the payload.

![Alt text](https://github.com/michaelzheng1/389Rfall18/blob/master/week/10/writeup/Screen(2).png)

I decided to create a checkpoint that would print out the message if it contains the word "CMSC" otherwise print out a fail message. After running the program I recieved the flag CMSC389R-{i_still_put_the_M_between_the_DV}

### Part 2 (30 Pts)
1. Entered "pgp --gen-key"

![Alt text](https://github.com/michaelzheng1/389Rfall18/blob/master/week/10/writeup/Screen(3).png)

2. Entered "gpg --import pgpassignment.key"

![Alt text](https://github.com/michaelzheng1/389Rfall18/blob/master/week/10/writeup/Screen(4).png)

3. Using the my name and the name "UMD Cybersecurity Club", I entered "gpg -e -u "Michael" -r "UMD Cybersecurity Club" message.private
 
