Writeup 3 - OSINT II, OpSec and RE
======

Name: Michael Zheng
Section: 0101
I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Michael Zheng

## Assignment 3 Writeup

### Part 1 (100 pts)
One vulnerability Krueger must fix is his password. His password “pokemon” is too simple and can be crack down if an attacker runs a script using the word list from rockyou.txt. Fred needs to add more special characters and symbol in his password. For example, if he still wants to use the phrase pokemon he could use the password “#p0ke$M36o48n.” According to https://howsecureismypassword.net/, this password would take 34 thousand years for an average computer to crack down the password. Another way is to create a password using a secure random password generator. 
The second vulnerability is that an attacker can attempt to login without any limits.  I was able to send my code to the server over and over until I was able to gain access to the company website. Following the instruction from https://blog.emsisoft.com/en/28622/rdp-brute-force-attack/, Fred could implement a simple policy that locks users out after several failed attempts. This would prevent an attacker trying to brute force the website.
The third vulnerability would be the multiple open ports on the server. I was able to gain access to the server by using one of the multiple open ports. To prevent this from happening Fred could configure the server to listen on a specific port. Following the instruction on https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-a-server-to-listen-on-a-specific-tcp-port?view=sql-server-2017, Fred could allow only one port to be open limiting the opportunities of an attack. If Fred puts up a firewall on the specific port, this covers the port from the incoming request.
