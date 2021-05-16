# stegosaurus

Very simple image steganography. Written to annoy BizarroLand personally, neener neener.

## Usage

### Hiding a message into an image

```
python stegosaurus.py write input_image_path input_message_path [out_image_path]
```

Creates an image similar to `input_image_path`, with the contents of `input_message_path` hidden in it. Writes the message image to `out_image_path`, or displays it if omitted.

## Reading a hidden message

```
python stegosaurus.py read image_path
```

Reads the steganographic message in `image_path` and prints it to standard input.

## Example

|               Original image               |                      With message                      |
|:------------------------------------------:|:------------------------------------------------------:|
| ![BizarroLand's avatar](example/clean.png) | ![visually identical to original](example/message.png) |

## Limitations

This is just a simple demo and isn't realistically usable:

- Uses many colours not present in the original palette
- Pixel noise will show in any tool for detecting doctored images
- The message is concentrated in the top left of the image, making this region stand out
- Will not resist compression
