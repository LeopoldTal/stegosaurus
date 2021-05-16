import pytest
from PIL import Image
from image_writer import bytes_to_bits, group_bits, hide

class TestBytesToBits:
	def test_single_byte(self):
		assert bytes_to_bits([ 10 ]) == [ 0, 0, 0, 0, 1, 0, 1, 0 ]
	
	def test_order(self):
		assert bytes_to_bits([ 255, 0 ]) == [ 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]

class TestGroupBits:
	def test_group(self):
		assert(group_bits([ 0, 1, 0, 1, 0, 1 ])) == [ [ 0, 1, 0 ], [ 1, 0, 1 ] ]
	
	def test_pad(self):
		assert(group_bits([ 1 ])) == [ [ 1, 0, 0 ] ]

def test_message_too_long():
	with pytest.raises(ValueError):
		secret = 'My cool test'
		clean_image = Image.new('RGB', (1, 1), 'black')
		hide(clean_image, secret)
