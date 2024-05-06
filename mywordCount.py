from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from PIL import Image
import numpy as np

def plt_imshow(x, ax = None, show = True):
    if ax is None:
    fig, ax = plt.subplots()
    ax.imshow(x)
    ax.axis('off')
    #if show: plt.show()
    return ax
if __name__ == '__main__':
freq = dict()
f = open('frequent.txt', 'r', encoding = 'utf-8')
for line in f.readlines():
word, w_fre = line.split()
w_fre = int(w_fre) #频率由字符转为 int
freq[word] = w_fre
im_mask = np.array(Image.open('perfume.jpg'))
im_colors = ImageColorGenerator(im_mask)
wcd = WordCloud(font_path='C:/Windows/Fonts/HGYT_CNKI.ttf',
background_color='white', mask = im_mask)
wcd.generate_from_frequencies(freq)
wcd.recolor(color_func=im_colors)
ax = plt_imshow(wcd,)
ax.figure.savefig(f'single_wcd.png',bbox_inches='tight',
dpi=100 )