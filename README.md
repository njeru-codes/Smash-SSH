# SMASH SSH
A Python script designed to brute-force SSH credentials using a customizable wordlist.

```
        ███████╗███╗   ███╗ █████╗ ███████╗██╗  ██╗        ███████╗███████╗██╗  ██╗
        ██╔════╝████╗ ████║██╔══██╗██╔════╝██║  ██║        ██╔════╝██╔════╝██║  ██║
        ███████╗██╔████╔██║███████║███████╗███████║        ███████╗███████╗███████║
        ╚════██║██║╚██╔╝██║██╔══██║╚════██║██╔══██║        ╚════██║╚════██║██╔══██║
        ███████║██║ ╚═╝ ██║██║  ██║███████║██║  ██║        ███████║███████║██║  ██║
        ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝        ╚══════╝╚══════╝╚═╝  ╚═╝

```
## installation
```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    
```
## usage
```python
    python3 smash.py -h 192.168.0.13 -u admin -w wordlist.txt
```