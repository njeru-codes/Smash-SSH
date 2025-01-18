'''


'''
import os
import threading
import logging
from paramiko import SSHClient

port=22
def send_payload(host, username, password):
    global port
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        client.connect(host, port=port, username=username, password=password, banner_timeout=300)
    except AuthenticationException:
        pass 
    except ssh_exception.SSHException:
        pass #rate limiting on server
    except Exception as error:
        pass

def help_docs():
    pass

def print_banner():
    print ("SMASH SSH")


def main():
    # TODO read params passed to file
    #file username and password wordlist file and host and optional port() default 22

    #confirm file can be reached and exists
    # validate if correct host is provided
    print_banner()


if __name__=="__main__":
    main()

