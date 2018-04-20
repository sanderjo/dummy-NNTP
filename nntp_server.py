# Example of simple, fake NNTP server

import socket

def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 5555))
    connection.listen(10)
    while True:
        current_connection, address = connection.accept()
        # Ah, there is an incomping connection:
        current_connection.send('200 Welcome\r\n')
        while True:
            data = current_connection.recv(2048).upper()
            print "data received:", data

            if data.find('QUIT') >= 0:
                current_connection.send('100 OK\r\n')
                current_connection.shutdown(1)
                current_connection.close()
                break

            elif data == 'STOP\r\n':
                current_connection.shutdown(1)
                current_connection.close()
                exit()

            elif data:
                # current_connection.send(data)
                print "responding with 100 OK"
                current_connection.send('100 OK\r\n')


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
