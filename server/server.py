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


def receive_readings(connection, address, reading_received_callback):
    reading_json_accumulator = ""
    is_first_received_reading = True

    while True:
        received = connection.recv(1)

        if received == b'':
            log_error(client_name(address) + " disconnected")
            connection.close()
            break

        received_text = received.decode('utf-8')
        if received_text == "{":
            reading_json_accumulator = "{"
        elif received_text == "}":
            reading_json = reading_json_accumulator + "}"
            reading_json_accumulator = ""

            print("-> " + reading_json)
            reading_properties = json.loads(reading_json)

            if is_first_received_reading:
                is_first_received_reading = False
                reading_properties["measured"] = None

            reading_received_callback(reading_properties["measured"], reading_properties["timestamp"])
        else:
            reading_json_accumulator = reading_json_accumulator + received_text


def start_server(server_port):
    s = create_socket()
    bind_socket(s, server_port)

    log_info("start listening")
    s.listen()

    while True:
        log_info("waiting for client")
        connection, address = s.accept()
        log_info("client connected: " + client_name(address))
        receive_readings(connection, address, insert_reading)


start_server(port)
