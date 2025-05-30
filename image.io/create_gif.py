import imageio.v3 as iio

filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
imagens = []

for filename in filenames:
    imagens.append(iio.imread(filename))


iio.imwrite('nyan-cat.gif', imagens, duration = 500, loop=0)


