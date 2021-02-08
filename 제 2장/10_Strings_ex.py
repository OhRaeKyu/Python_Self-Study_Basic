str = "X-DSpAM-Confidence: 0.8475 "
num_1 = str.find(":")

str_1 = str[num_1 + 2 :]
str_2 = str_1.strip()

str_piece = float(str_2)
print(str_piece)