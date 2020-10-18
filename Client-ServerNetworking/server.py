#Author: Jeanette Eldredge

import socket
import threading

computers=[]
names = []
host = ''
port = 0

# This is the first function called in the program. This asks the user for the computer
# IP address and the port the user would like to use.
def beginningSetUp():
    global host
    global port
    host = input("Please enter computer IP address to begin server: ")
    period = 0
    for letters in host:
        if letters == '.':
            period +=1
    while period != 3:
        period = 0
        host = input( "Invalid IP address. Please try again: ")
        for letters in host:
            if letters == '.':
                period +=1

    port = int(input("Please enter port number to begin server: "))
    while port < 1000:
        port = input( "It is suggested to use a high number port to avoid interference with other programs. Please enter a number above 1000: ")

# This function is the threading function that handles multiple computers connected to the server.
# Without this function the server could only host one computer.
def chatHandle(client, address):
    global computers
    while True:
        if len(names) != 1:
            client.send(bytes("\nWho would you like to send a message to?","utf-8"))
            for name in names:
                client.send(bytes("\n", "utf-8"))
                client.send(bytes(name))
                client.send(bytes("\n","utf-8"))
            client.send(bytes("Type their name or 'all' to send to all machines. Hit 'enter' to quit: ","utf-8"))
            choice = client.recv(1024)
            client.send(bytes("Enter message: ","utf-8"))
            msg = client.recv(1024)
            if str(choice) != "all" and len(names)>1:
                match = 0
                for name in names:
                    if str(choice) == name:
                        computers[match].send(bytes(msg, "utf-8"))
                    else:
                        match +=1
            if str(choice)=="all" or len(names)==1:
                sending(msg)
            if msg == '':
                client.send(bytes("Thank you for Joining the Chat!", "utf-8"))
                computers.remove(client)
                return
        else:
            client.send(bytes("Enter message: ","utf-8"))
            msg = client.recv(1024)
            sending(msg)

# This function handles sending texts to all computers on the server. This is called when the user selects all computers 
# or when there is only one computer on the server.
def sending(msg):
    if len(msg) == 0:
        computers.remove(client)
        client.close()
        return
    else:
        for computer in computers:
            computer.send(bytes(msg))
        if len(msg) == 0:
            computers.remove(client)
            client.close()
            return
    if len(names) == 1:
        print(msg.decode("utf-8"))

    if msg == '':
        client.send(bytes("Thank you for Joining the Chat!", "utf-8"))
        computers.remove(client)
        return

# This is the set up of the server and the program.
beginningSetUp()
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind((host, port))
print(socket.gethostname(), "server has been started! Waiting for connection...")
serversock.listen(1)

# Main code that runs the server and who connects to them.
while True:
    client, address = serversock.accept()
    computers.append(client)
    client.send(bytes("Welcome to ", socket.gethostname()," server! \n", "utf-8"))
    client.send(bytes("Please enter name: ", "utf-8"))
    name = client.recv(1024)
    print("Connected to (" ,name, ")!")
    names.append(name)
    chatThread = threading.Thread(target = chatHandle, args=(client, address))
    #chatThread = threading.Thread(target = sending, args=(client, address))
    chatThread.daemon = True
    chatThread.start()

    