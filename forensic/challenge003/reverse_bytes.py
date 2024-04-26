def reverse_bytes(filename):
    try:
        with open(filename, 'rb') as file:
            bytes_list = file.read()
            reversed_bytes = bytes_list[::-1]
            with open('reversed_' + filename, 'wb') as output_file:
                output_file.write(reversed_bytes)
            print("Reversed bytes saved to 'reversed_" + filename + "'.")
    except FileNotFoundError:
        print("File not found.")

# Replace 'filename.txt' with the path to your file
reverse_bytes('flag.png')
