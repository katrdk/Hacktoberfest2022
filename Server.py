import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 4001

def client(conn, addr):
    print("[NEW CONNECTION] ",addr,"connected.")

    connected = True
    while connected:
        msg = conn.recv(1024).decode()
        print(msg)
        if msg.endswith("quit"):
            print("Client ",addr," got disconnected")
            connected=False
            
        

    conn.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(4)
    print("[LISTENING] Server is listening on IP : ",host," Port : ",port)

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
