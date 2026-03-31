import socket

host = '127.0.0.1'
port = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((host, port))

# Set a timeout of 5 seconds
UDPServerSocket.settimeout(5.0)

print(f"Server listening on {host}:{port} with a 5s timeout...")

while True:
    try:
        # This will now only wait for 5 seconds
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        
        message = bytesAddressPair[0].decode()
        address = bytesAddressPair[1]
        
        print(f"Received: {message} from {address}")
        
        # Echo back
        UDPServerSocket.sendto(str.encode("ACK: " + message), address)

    except socket.timeout:
        # This code runs if 5 seconds pass with no data
        print("No data received for 5 seconds. Still waiting...")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        break