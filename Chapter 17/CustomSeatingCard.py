#! python3
# Chapter 17 Project - Create a customer invitation card

import os, sys, logging
from PIL import Image, ImageDraw

image = Image.new('RGBA', (500,500), 'white')
canvas = ImageDraw.Draw(image)

canvas.text((20,20), "You're invited, Bob!", fill='pink')
canvas.line([(0,0), (499,0), (499,499), (0,499), (0,0)], fill='purple', width=20)
image.save('invitation.png')