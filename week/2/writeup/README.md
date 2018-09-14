Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Michael Zheng
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Michael Zheng

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. First, I search up kruegster1990 on google. I saw that he had a reddit account https://www.reddit.com/user/kruegster1990. Then I try using twitter and found his twitter account https://twitter.com/kruegster1990. 

3. His Twitter account tells me where he works. I copy the link and then paste it on the centralops and found the ip address: 142.93.118.186.

4. I use robot.txt which shows a hidden directory http://www.cornerstoneairlines.co/secret/ and got CMSC389R-{fly_th3_skles_wlth_u5}

5. When I click on the admin tab, I found 142.93.117.193.

6. Using the censys.io, I found 142.93.117.193 and 142.93.118.186 are both located at New York City. 

7. From the censys.io, the 0S is Ubuntu.

8. CMSC389R-{h1dden_fl4g_in_s0urce}

### Part 2 (55 pts)

From the nmaps on the CornerStone website, I found the ip address is 142.93.118.186. From the nmaps, I found the port number 22 was open, so I put it down on my program. Afterward, based from his email and the hint from piazza, I guess his username could be krugster. I use krugster as the username in the stub.py and tried to find the correct password by iterating through rockyou.txt. However, my program stated that the connection failed. I tried using nmap again and use port 1337. I tried running my code again. The program was about to run past the deadline, so I stop and submit.
