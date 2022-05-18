import socket

HOST = "127.0.0.1"
PORT = 1234


def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(sendable_data("134"))
        s.sendall(sendable_data("73"))

        data = s.recv(1024)
    print(f'Received:\n{data.decode("utf-8").strip()}')