
# Objective
Create a mail protocol.

This is an exercise in creating an end-to-end protocol using TCP under the hood. 

The TCP server is already set up. You can reliabily send and recieve messages from a connected client. 

_Clients and servers using your protocol should be able to..._
1. Send mail from a mailbox to a mailbox
2. Get all mail from mailbox
3. Create a mailbox
4. Delete a mailbox
5. Clear mailbox
6. Get list of all mailboxes

*Do not worry about security*

## Steps: 
1. Define the mail protocol. 
    * What actions should you be able to do?
    * What messages should the client send / the server expect? 
    * What should the server send back (If applicable)?

    Note: A protocol is a specification! It is up to the programmer how it should be implemented!

2. Create an implementation of the mail protocol. 
    * You only need to write code in the MailProtocol class
    * You will need some sort of data structure to store all the mailboxes and their mail

## Running:
1. Run the server
```bash
python mail_server.py
```

2. Connect to the server using telnet
```bash
telnet <ip> <port>
```

3. Make requests through telnet according to your protocol

## Common issues: 
* Installing telnet
    * Windows: Install wsl (Choose ubuntu as distro) and then run *sudo apt install telnet*. Note: You will have to reload vscode and run the server using wsl as well
    * MacOS: Install brew and then run *brew install telnet*

