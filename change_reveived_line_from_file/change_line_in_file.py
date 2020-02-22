inf = open('filename.txt', "r")
rec_line = inf.readline() + " "
digits_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
next_digit = ""
next_char = ""

for i in rec_line:
    if i in digits_set:
        next_digit += i
    else:
        if i != rec_line[0]:
            next_digit = int(next_digit)
            print(next_char * next_digit, end="")
            next_digit = ""
        next_char = i
