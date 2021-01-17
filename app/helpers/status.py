import socket

def is_open():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        sock.connect(("localhost", 25565))
        print("Server is open")
        res = True
    except ConnectionRefusedError:
        print("Server is closed")
        res = False

    sock.close()
    return res