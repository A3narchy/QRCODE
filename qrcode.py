import qrcode

img = qrcode.make('YOU TEXT')
type(img)
img.save("some_file.png")
