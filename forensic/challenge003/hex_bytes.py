def print_hex_byte(filename):
    try:
        with open(filename, 'rb') as file:
            byte = file.read(1)
            while byte:
                print(hex(byte[0]), end=' ')
                byte = file.read(1)
    except FileNotFoundError:
        print("File not found.")

# Replace 'filename.txt' with the path to your file
print_hex_byte('flag.png')
