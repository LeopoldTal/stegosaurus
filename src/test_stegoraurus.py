from PIL import Image
from stegosaurus import hide, decipher

def test_roundtrip():
	secret = 'My cool test'
	clean_image = Image.new('RGB', (16, 16), 'black')
	message_image = hide(clean_image, secret)
	assert decipher(message_image) == secret
