import qrcode

print("=== QR Code Generator ===")
print("Made by Md Faruque Hosain")

# User input
data = input("Enter link or text for QR Code: ")
filename = input("Enter file name (ex: myqr.png): ")

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)

print(f"\nQR Code Saved Successfully! ✅")
print(f"File Name: {filename}")
print("Now scan it with your phone camera!")
