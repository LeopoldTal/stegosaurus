"""stegosaurus

Very simple image steganography"""

from PIL import Image
from sys import argv, exit
from image_reader import decipher
from image_writer import hide

usage = """python stegosaurus.py write input_image_path input_message_path [out_image_path]
python stegosaurus.py read image_path"""

def write_image(image_path, message_path, out_path):
	clean_image = Image.open(image_path)
	with open(message_path) as h:
		secret = h.read()
	message_image = hide(clean_image, secret)
	if out_path:
		message_image.save(out_path)
	else:
		message_image.show()

def read_image(image_path):
	message_image = Image.open(image_path)
	message = decipher(message_image)
	print(message)

def error():
	print(usage)
	exit(1)

if __name__ == '__main__':
	if len(argv) < 3:
		error()
	if argv[1] == 'write':
		if len(argv) < 4:
			error()
		image_path = argv[2]
		message_path = argv[3]
		out_path = argv[4] if len(argv) > 4 else None
		write_image(image_path, message_path, out_path)
	elif argv[1] == 'read':
		read_image(argv[2])
	else:
		error()
