import imageio.v3 as iio

filenames = ["bild_1.png", "bild_2.png", "bild_3.png", "bild_4.png"]
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('theo.gif', images, duration = 1000, loop = 0)
