import matplotlib.pyplot as plt
import qrcode
from PIL import Image

def display_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    url = "https://github.com/sahanahn74/python-mini-projects"  
    display_qr_code(url)
