# QR 코드를 생성하는 프로그램이다 

# pip install qrcode
import qrcode  

qr_data = 'www.google.com'

qr_img = qrcode.make(qr_data)
save_path = 'QR_code\\' + qr_data + '.png'
qr_img.save(save_path)

