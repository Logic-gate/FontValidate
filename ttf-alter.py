

from fontTools.ttLib import TTFont
import sys


def original(file_name, properties, new_value, out_file):
    name = TTFont(file_name)
    OS2 = name['OS/2'].__dict__
    OS2[properties] = int(new_value)
    name.save(out_file)


def main():
	argv = sys.argv[1:]
	file_name, properties, new_value, out_file = argv
	[original(f, p, n, o) for f, p, n, o in [argv]]


if __name__=='__main__':
	main()





