import ftplib
from helper_functions import *
# Define a file called `password.txt` and include only one line with your password in plaintext.
# Do not commit this file, use a .gitignore. Ask me if you need help setting this up.
user = 'brian'
password = open(
    "~/Documents/GitHub/bc/zmq-telemetry/upload/password.txt").read()

ftp = connect()

# Show files in home directory
ftp.retrlines('LIST home')

# Upload big file
input_filepath = "/Applications/0ad_macbook.zip"
destination_filepath = "home/brian_scratch/0ad.zip"
tx_with_progress(ftp, input_filepath, destination_filepath,
                 block_size_bytes=12500000)

# Download that file back to local
filepath_pensieve = "home/brian_scratch/0ad.zip"
filepath_local = "~/Downloads/0ad_from_pe.zip"
receive(ftp, filepath_pensieve, filepath_local, 
        block_size_bytes=12500000)

#Close out the connection
ftp.quit()
ftp = None
