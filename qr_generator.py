
import qrcode


def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")


def main():
    data = input("Enter text or URL to generate QR code: ")
    generate_qr(data)


if __name__ == "__main__":
    main()
