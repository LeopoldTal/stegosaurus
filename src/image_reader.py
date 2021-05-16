from constants import BITS_PER_BYTE, HEADER_SIZE_IN_BITS

def image_to_bits(image):
	px = image.load()
	return [
		channel & 1
		for y in range(image.height)
		for x in range(image.width)
		for channel in px[x,y]
	]

def bits_to_int(bits):
	n = 0
	for bit in bits:
		n = n << 1 | bit
	return n

def decipher(image):
	"""decipher(image: PIL image) -> string
	reads the steganographically hidden message in an image"""
	buffer = image_to_bits(image)
	header_bits = buffer[:HEADER_SIZE_IN_BITS]
	buffer = buffer[HEADER_SIZE_IN_BITS:]
	data_size_in_bits = BITS_PER_BYTE * bits_to_int(header_bits)
	if data_size_in_bits > len(buffer):
		raise ValueError('Requested {} bits but only {} available'.format(data_size_in_bits, len(buffer)))
	message_bytes = [ bits_to_int(buffer[k:k+BITS_PER_BYTE]) for k in range(0, data_size_in_bits, BITS_PER_BYTE) ]
	return bytes(message_bytes).decode('utf-8')
