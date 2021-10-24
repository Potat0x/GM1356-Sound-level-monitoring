import socket
import sys
from socket import SOL_SOCKET, SO_REUSEADDR
import json
from db_inserter import insert_reading
from logger import log_info, log_error

port = 2389


def client_name(addr):
    return addr[0] + ":" + str(addr[1])


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


def receive_readings(connection, address, callback):
    tmp_json = ""
    while True:
        received = connection.recv(1)

        if received == b'':
            log_error(client_name(address) + " disconnected")
            connection.close()
            break

        received_text = received.decode('utf-8')
        if received_text == "{":
            tmp_json = "{"
        elif received_text == "}":
            tmp_json = tmp_json + "}"
            print("-> " + tmp_json)
            jp = json.loads(tmp_json)
            callback(jp["measured"], jp["timestamp"])
            tmp_json = ""
        else:
            tmp_json = tmp_json + received_text


def start_server(port):
    s = create_socket()
    bind_socket(s, port)

    log_info("start listening")
    s.listen()

    while True:
        log_info("waiting for client")
        connection, address = s.accept()
        log_info("client connected: " + client_name(address))
        receive_readings(connection, address, insert_reading)


start_server(port)
