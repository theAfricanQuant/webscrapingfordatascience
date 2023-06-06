from random import choice
from captcha.image import ImageCaptcha
import os.path
from os import makedirs
from constants import *

makedirs(CAPTCHA_FOLDER)

image = ImageCaptcha()

for i in range(NR_CAPTCHAS):
    captcha = ''.join([choice(CHARACTERS) for _ in range(NR_CHARACTERS)])
    filename = os.path.join(CAPTCHA_FOLDER, f'{captcha}_{i}.png')
    image.write(captcha, filename)
    print('Generated:', captcha)
