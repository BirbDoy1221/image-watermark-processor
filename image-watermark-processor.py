from PIL import Image, ImageOps, ImageDraw, ImageFont
from clear_screen import clear
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(prog='my-program', usage='%(prog)s [options]')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-t','--timestamp')
group.add_argument('-b', '--border')
group.add_argument('-w', '--watermark')

args = parser.parse_args()

# ---------------------------------------------------------- #

if args.timestamp:
    clear()
    user_choice = input('Choose option: \n1. Use current time\n2. Use custom time\n')
    if user_choice == '1':
        clear()
        img = Image.open(args.timestamp)

        img = img.convert('RGBA')

        fnt_size = img.height / 50

        fnt = ImageFont.truetype('Lexend.ttf', fnt_size)

        d = ImageDraw.Draw(img)

        # timestamp = f'{datetime.date(datetime.now())}\n + {}'
        timestamp = 'yey'

        d.multiline_text((20,img.height - (fnt_size * 2.5)), text=timestamp, font=fnt, fill=(50,50,50), features=[])

    elif user_choice == '2':
        clear()
        print('User pressed 2')
    else:
        clear()
        print('Invalid input')


    img.show()