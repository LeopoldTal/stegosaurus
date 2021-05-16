from PIL import Image
from image_reader import bits_to_int, image_to_bits

def test_image_to_bits():
	image = Image.new('RGB', (2, 1), 'yellow')
	assert image_to_bits(image) == [ 1, 1, 0, 1, 1, 0 ]

def test_bits_to_int():
	assert bits_to_int([ 1, 0, 1, 0 ]) == 10
