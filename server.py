import socket
import sys
from socket import SOL_SOCKET, SO_REUSEADDR


def client_name(addr):
    return addr[0] + ":" + str(addr[1])


def log_info(message):
    print("[info] " + message)


def log_error(message):
    print("[error] " + message)


def create_socket():
    log_info("creating socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    log_info("socket created")
    return s


def bind_socket(s, port):
    log_info("binding socket")
    try:
        s.bind(("localhost", port))
    except Exception as e:
        log_error("bind failed: " + str(e))
        sys.exit()


def start_server(port):
    s = create_socket()
    bind_socket(s, port)

    log_info("start listening")
    s.listen()

    while True:
        log_info("waiting for client")
        connection, address = s.accept()
        log_info("client connected: " + client_name(address))
        while True:
            r = connection.recv(256)
            if r == b'':
                log_error(client_name(address) + " disconnected")
                connection.close()
                break

            print("-> " + r.decode('utf-8').strip())


start_server(2389)
