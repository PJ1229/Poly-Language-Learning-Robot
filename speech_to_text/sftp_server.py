import paramiko

host = "192.168.68.116"  # Mac's IP
port = 22
username = "pjkim"
password = "Quiggle4_23_24!"
local_path = "audio.wav"
remote_path = "/Users/pjkim/repos/Poly-Language-Learning-Robot/speech_to_text"  # Full path with file name

# Establish connection
transport = paramiko.Transport((host, port))
transport.connect(username=username, password=password)

# Start SFTP session
sftp = paramiko.SFTPClient.from_transport(transport)

# Upload the file
sftp.put(local_path, remote_path)

# Close the connection
sftp.close()
transport.close()

print("File sent via SFTP!")
