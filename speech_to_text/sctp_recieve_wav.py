# sctp_receive_wav.py
import sctp
import socket

HOST = '0.0.0.0'
PORT = 5000
OUTPUT_PATH = 'audio.wav'

s = sctp.sctpsocket_tcp(socket.AF_INET)
s.bind((HOST, PORT))
s.listen(1)

print(f"Listening on {HOST}:{PORT}...")
conn, addr = s.accept()
print(f"Connected by {addr}")

# Receive size first
size_data = b""
while not size_data.endswith(b'\n'):
    size_data += conn.recv(1)
file_size = int(size_data.strip())

# Receive the WAV file data
received_data = b""
while len(received_data) < file_size:
    chunk = conn.recv(min(4096, file_size - len(received_data)))
    if not chunk:
        break
    received_data += chunk

# Save the file
with open(OUTPUT_PATH, 'wb') as f:
    f.write(received_data)

conn.close()
s.close()
print(f"Received {len(received_data)} bytes. File saved as {OUTPUT_PATH}.")

