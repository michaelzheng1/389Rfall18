Writeup 5 - Binaries I
======

Name: Michael
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Michael Zheng

## Assignment 5 Writeup

First I split the my_memset function into 3 parts. One part that initialize the
variables. The second part for the loop that does the work and the third part
for the condition. Initially, I had trouble how to get the values from the
parameter. From the lecture slides, I know that rdi = 1st parameter,
rsi = 2nd parameter, and rdx for the 3rd parameter. For the initialization,
I used a temporary register rax and set it to 0. Then I check if rdx (strl)
greater than rdx. If it is true just let it continue to the end. Otherwise,
jump to the loop. Then I couldn't remember how to get a value from an array.
I tried looking at the slides and found out I could either use a stack pointer
or [] to compute intricate address. I decided to use [] and type down
mov [rdi], sil. However, I was getting the wrong output. Then I realized I needed
to add the index. I fixed it to mov [rdi + rax], sil.

For the my_strncpy, I basically copied over the my_memset function. The only
difference I needed to save the value src[i] to bl. Then assigned the value to
dst[i]. This time I make sure I included the index.
