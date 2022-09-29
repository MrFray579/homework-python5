with open('RLE.txt', 'r') as file:
   my_text = file.readline()
   text_compression = my_text.split()

print(my_text)

def compresing(file):
    compres = ''
    prev_char = ''
    count = 1
    if not file: return ''
    for char in file:
        if char != prev_char:
            if prev_char: 
                compres += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else: 
        compres += str(count) + prev_char
        return compres

text_compression = compresing(my_text)

with open('text_compression_RLE_024.txt', 'w', encoding='UTF-8') as file:
      file.write(f'{text_compression}')
print(text_compression)