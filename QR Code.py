import qrcode
from qrcode import QRCode
 

qr=qrcode.QRCode()
qr.add_data("Enter Your Text")
qr.make()
img=qr.make_image(fill_color="red",back_color="white")
img.save('qr.png')

# import qrcode
# img = qrcode.make('Tanmay')
# img.save('test.png')