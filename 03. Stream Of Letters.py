command_or_letter = input()

pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

counter_c = 0
counter_o = 0
counter_n = 0

word = ""

while command_or_letter != "End":
    if command_or_letter in pool:

        if command_or_letter == "c":
            counter_c += 1
            if counter_c == 2:
                word += command_or_letter
        elif command_or_letter == "o":
            counter_o += 1
            if counter_o == 2:
                word += command_or_letter
        elif command_or_letter == "n":
            counter_n += 1
            if counter_n == 2:
                word += command_or_letter
        else:
            word += command_or_letter

        if counter_c > 0 and counter_o > 0 and counter_n > 0:
            print(word, end=" ")
            counter_c = 0
            counter_o = 0
            counter_n = 0
            word = ""

    command_or_letter = input()
