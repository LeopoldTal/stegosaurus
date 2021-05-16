from constants import BITS_PER_BYTE, HEADER_SIZE_IN_BITS

def bytes_to_bits(b):
	return [ byte >> k & 1 for byte in b for k in range(BITS_PER_BYTE - 1, -1, -1) ]

def secret_to_bits(secret):
	secret = bytes(secret, 'utf-8')
	secret_size_in_bytes = len(secret)
	header = [ secret_size_in_bytes >> k & 1 for k in range(HEADER_SIZE_IN_BITS - 1, -1, -1) ]
	return header + bytes_to_bits(secret)

def group_bits(l):
	padded = l + [0] * (-len(l) % 3)
	return [ padded[k:k+3] for k in range(0, len(padded), 3) ]

def write_lsb(orig, bit):
	return orig >> 1 << 1 | bit

def hide(clean_image, secret):
	"""hide(clean_image: PIL image, secret: string) -> PIL image
	creates an image similar to clean_image, with secret hidden in it"""
	message_image = clean_image.convert('RGB')
	bits = secret_to_bits(secret)
	bit_groups = group_bits(bits)
	if len(bit_groups) > message_image.width * message_image.height:
		raise ValueError('Cannot fit {}-bit message into {} by {} image'.format(
			len(bits), message_image.width, message_image.height))
	
	px = message_image.load()
	for ii in range(len(bit_groups)):
		x = ii % message_image.width
		y = ii // message_image.width
		r,g,b = px[x,y]
		dr,dg,db = bit_groups[ii]
		px[x,y] = write_lsb(r, dr), write_lsb(g, dg), write_lsb(b, db)
	
	return message_image
