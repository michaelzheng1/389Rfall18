Writeup 10 - Crypto II
=====

Name: Michael Zheng
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Michael Zheg

## Assignment 10 Writeup

### Part 1 (70 Pts)
I found out the id in the url changes when I click on a different item. I know this is a sql injection based on the highlighted letters of Part 1 description.  I assumed the url is passed through the format of SELECT * FROM table WHERE id=.  I tried 1' OR '1' = '1 and different variations. Eventually I ended up with 1' or '1'=1' and got the flag CMSC38R-{y0U-are_the_5ql_n1nja}
http://cornerstoneairlines.co:8080/item?id=1' or '1'='1



### Part 2 (30 Pts)
1.    From the lecture notes, I reused <script>alert('this is Xss');</script> and it works.

2.    First, I tried to use the same input from the first problem. However, this doesn't work. Then I realized the website might be using JavaScript, so I search online how to perform an XSS attack with JavaScript. I would have to use an img tag and oneerror attribute to perform the XSS attack. I enter in
<img src='blank' onerror=alert(1) />

3.    This problem is almost the same as the previous one. Instead of injecting into a prompt, I have to inject the url.  I tried to enter the same injection, but it doesn't work. I noticed the frame number changes as I selected different images, so I decided to remove the first part of the injection leaving ='blank' onerror=alert(1) />
The overall url is :
 https://xss-game.appspot.com/level3/frame#1='blank' onerror=alert(1) />
 
4.    While looking through the code, it seems the user input is placed in timer in startTimer('{{ timer }}');" />. I need to close the function with a }}') and add the onerror=alert. Then I need to add ('{{ to close the matching set. The overall injection is }}'); onerror =alert('{{

5.    I was planning to inject a command to the email input, but the target code completely ignores the email. So I decided to see if I could do something to the url. When I clicked  the sign-up link, the url changed to
https://xss-game.appspot.com/level5/frame/signup?next=confirm
I tried to replace confirm to alert(1), but it didn't work. I clicked for hints and found out I need to execute Javascipt. I replaced the confirm to javascript:alert('1') and it works.
https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('1')

6.    The mission objective stated I would need to make the application to request an external file. I wasn't sure how to host my own JS file, so Iook at the hints. The hints tell me to use google.com/jsapi?callback=foo. I tried to add
 https:// google.com/jsapi?callback=foo after frame#, but the webpage tells me I cannot load a url containing "http". Looking at the target code I found out there is a regex that prevents any "https" inputs. So I decide to change https to HTTPs and it works.
https://xss-game.appspot.com/level6/frame#HTTPs://google.com/jsapi?callback=alert
