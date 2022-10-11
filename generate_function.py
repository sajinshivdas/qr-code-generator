#----------------------------------------------------------------------------------------------------------------------------
# Imports
from pyqrcode import QRCode
import pyqrcode
import png
from io import BytesIO
import base64
from PIL import Image
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Generate QR Code with content
def generate_qr(content, size, logo=False):
	if logo == False:
		qr = pyqrcode.create(content)
		qr_image = './assets/QR.png'
		with open(qr_image, 'wb') as qr_file:
			qr.png(qr_file, scale=size)

		qr_code = Image.open(qr_image)
		return qr_code
	else:
        # (2.1) QR code first
		qr_image = Image.open('./assets/QR.png')
		width, height = qr_image.size
		qr_image = qr_image.convert("RGBA")   # keep the logo's colors


        # (2.2) Open the logo image
		logo_image = Image.open("./assets/logo.png")

        #how big the logo we want to put in the qr code (20% by 20%)
		logo_w, logo_h =  width/5, height/5

        # Calculate xmin, ymin, xmax, ymax to put the logo
		xmin = int((width / 2) - (logo_w / 2))
		xmax = int((width / 2) + (logo_w / 2))
		ymin = int((height/ 2) - (logo_h / 2))
		ymax = int((height/ 2) + (logo_h / 2))

        # resize the logo as calculated
		logo_image = logo_image.resize((xmax - xmin, ymax - ymin))

        # (2.3) put the logo in the qr code
		qr_image.paste(logo_image, (xmin, ymin, xmax, ymax))

        # (2.4) save to disk
		qr_code = './assets/QR-logo.png'
		qr_image.save(qr_code)
		return qr_code
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# QR Code Image Download Link
def image_download(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="qr.png">Download QR Code as .png</a>'
    return href
#----------------------------------------------------------------------------------------------------------------------------