from PIL import Image
import sys

def convert(source, target, file_prefix=""):
	ifile = Image.open(source)
	ifile = ifile.convert('L')		# Convert to Black & White
	ifile.save(f"{str(file_prefix + '_') if file_prefix else ''}{target}")
	print("Complete!")

if __name__ == '__main__':
	
	subargs = sys.argv[1:]
	if subargs:
		src = subargs[0]
		dest = subargs[1] if len(subargs) > 1 else "temp_out.png"
		file_prefix = subargs[2] if len(subargs) > 2 else ""
		convert(src, dest, file_prefix)
	else:
		print("Usage: imgConvert.py [sourceFile] [destinationFile] (output_prefix)")
