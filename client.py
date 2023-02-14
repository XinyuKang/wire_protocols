import os
import threading
import socket
import argparse
import pickle

# global variables
stop = False
username = "example"
password = "123"


# def check_dupname():

def login():
    client.send('LOGIN'.encode('ascii'))
    os.system("cls||clear")
    global username
    global password
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    global stop
    stop = False
    
    


def signup():  
    os.system('cls||clear')
    # check if username is unique
    global username
    global password
    while True:
        try:
            username = input("Create your username: ")
            # send the username to server for duplicate check
            client.send(('SIGNUP '+username).encode('ascii'))
            dup_message = client.recv(1024).decode('ascii')
            if dup_message == "DUPNAME":
                print("Username already exists! Change to another one.")
            elif dup_message == "NONDUPNAME":
                client.send(id.encode('ascii'))
                password = input("Create your password: ")
                client.send(password.encode('ascii'))
                break

        except Exception as e:
            print('Error Occurred: ', e)
            client.close()
        

    
def listAccounts():
    os.system('cls||clear')
    # list all or a subset of the accounts by text wildcard
    while True:
        option = input("(1)List all \n(2)List by wildcard\n")
        if option == "1":
            client.send('LIST ALL'.encode('ascii'))
            break
        elif option == "2":
            pattern = input("Input your search pattern: ")
            client.send(('LIST '+pattern).encode('ascii'))
            break
        else: 
            print("Invalid option, choose again")
    
    response = client.recv(1024).decode('ascii')
    if response == "NOMATCHED":
        print("No matched account found")
    elif response == "MATCHED":
        client.send("SENDMATCHED".encode('ascii'))
        list_bytes = client.recv(4096)
        list_accounts = pickle.loads(list_bytes)
        for a in list_accounts:
            print(a)
        

def receive():
    print("in receive")
    try:
        while True:
            global stop
            if stop: break
        
            message = client.recv(1024).decode('ascii')
            # print("message is ", message)
            if message == "USERNAME":
                # print("client trying to send username")
                client.send(username.encode('ascii'))
                next_message = client.recv(1024).decode('ascii')
                if next_message == 'PASSWORD':
                    client.send(password.encode('ascii'))
                    check_state = client.recv(1024).decode('ascii')
                    if check_state == "REJECT":
                        print("Wrong password! Try again")
                        stop = True
                    elif check_state == "NOUSER":
                        print("No such user")
                        stop = True
                    else:
                        #print(s)
                        print("Successfully logged in as ", username)

                        # retry = input("Retry ? y/n ")
                        # if retry is "y":
                        #     client.send('RESTART'.encode('ascii'))
                        #     choose_operations()
                        # else:
                        #     #TODO 
                        #     client.send('BREAK'.encode('ascii'))
                        #     return
                # elif next_message == 'DUPNAME':
            elif message == "FAIL":
                print("You've reach the attemp limit, connection failed.")
            else: 
                print(" the message is not on the list")
                print(message)
        print("out of while loop")
    except Exception as e:
        print('Error Occurred: ', e)
        client.close()

    #client.send('RESTART'.encode('ascii'))
    choose_operations()

def choose_operations():
    while True:
        option = input("(1)Sign in\n(2)Sign up\n(3)List existing accounts\n")
        if option == "1":
            login()
            break
        elif option == "2":
            signup()
        elif option == "3":
            listAccounts()
        else: 
            print("Invalid option, choose again")
    recieve_thread = threading.Thread(target=receive)
    recieve_thread.start()
    recieve_thread.join()

def choose_talkto():
    choose_talk_to_stop = False
    while True:
        if choose_talk_to_stop: 
            break
        global talkto
        talkto = input("Who do you want to talk to? (specify the username) ")
        client.send(("TALKTO "+talkto).encode('ascii'))
        next_message = client.recv(1024).decode('ascii')
        if next_message == "VALTALKTO":
            print("Start your conversation with "+talkto + "!")
            choose_talk_to_stop = True
        else:
            print("The username you were trying to talk to doesn't exist, please try another one. The available users are: \n")
            list_accounts = pickle.loads(next_message)
            for a in list_accounts:
                print(a)

def start_conversation():
    os.system('cls||clear')
    client.send('STARTHIST'.encode('ascii'))
    # receive all the queued messages
    list_bytes = client.recv(4096)
    list_messages = pickle.loads(list_bytes)
    for m in list_messages:
        print(m)
    # after receive the history, start to chat
    client.send('STARTCHAT'.encode('ascii'))
    next_message = client.recv(1024).decode('ascii')
    # talk to someone online
    # what if the other online user logout when chatting and the user still wants to leave messages
    if next_message == "CHATNOW":
        try:
            while True:
                global stop
                if stop: break

                

        except Exception as e:
            print('Error Occurred: ', e)
            client.close()
    # Same Queston :what if the other user login when leaving offline message
    elif next_message == "CHATLATER":
        try:
            print("The user you are trying to reach is not online now, please leave a message")
            while True:
                global stop
                if stop: break

        
        except Exception as e:
            print('Error Occurred: ', e)
            client.close()




    

    





def main():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the host
    client.connect((host, port))
    os.system("cls||clear")
    choose_operations()  # finished login here
    # choose who to talk to
    choose_talkto()
    # now start conversation
    recieve_thread = threading.Thread(target=start_conversation)
    recieve_thread.start()
    # recieve_thread.join()



if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-u', dest = 'host' , help = '127.0.0.1')
    parse.add_argument('-p', dest = 'port' ,type=int,help = '9999')
    args = parse.parse_args()
    global host
    global port
    host = args.host
    port = args.port
    main()


