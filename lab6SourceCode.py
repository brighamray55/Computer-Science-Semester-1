# This code was written by: Colm Corr and Brigham Ray
# The following is a list of all the shortcut keys we used.

s1 = "    #     "
s2 = "   # #    "
s3 = "  #####   "
s4 = " #     #  "
s5 = "#       # "
s6 = "######### "
s7 = "#         "
s8 = "      #   "
s9 = "#####     "
s10 = "#    #### "
s11 = "#       # "
s12 = "#    #    "
s13 = "# #       "
s14 = "        # "
s15 = "#   #   # "

# The dictionary that holds the characters for the banner
let_dict = {"a": [s1, s2, s3, s4, s5],
            "b": [s6, s5, s6, s5, s6],
            "c": [s6, s7, s7, s7, s6],
            "d": [s6, s5, s5, s5, s6],
            "e": [s6, s7, s6, s7, s6],
            "f": [s6, s7, s9, s7, s7],
            "g": [s6, s7, s7, s10, s6],
            "h": [s5, s5, s6, s5, s5],
            "i": [s1, s1, s1, s1, s1],
            "j": [s6, s14, s14, s8, s9],
            "k": [s11, s12, s13, s12, s11],
            "l": [s7, s7, s7, s7, s6],
            "m": [s6, s15, s15, s15, s15],
            "n": [s6, s5, s5, s5, s5],
            "o": [s6, s11, s11, s11, s6],
            "p": [s6, s11, s6, s7, s7],
            "q": [s6, s11, s6, s14, s14],
            "r": [s6, s5, s7, s7, s7],
            "s": [s6, s7, s6, s14, s6],
            "t": [s1, s6, s1, s1, s1],
            "u": [s5, s5, s5, s5, s6],
            "v": [s5, s4, s3, s2, s1],
            "w": [s15, s15, s15, s15, s6],
            "x": [s5, s4, s1, s4, s5],
            "y": [s5, s6, s14, s14, s6],
            "z": [s6, s1, s7, s1, s6]}


def letter(string, position):
    # Vertical loop
    if "vertical" == position:
        for i in string:
            for j in range(0, 5):
                x = let_dict[i][j]
                print(x)
            print()
    # Horziontal loop
    elif "horizontal" == position:
        # Created dummy variabalesa
        x = ''
        h = ''
        for i in range(0, 5):
            for j in string:
                x = let_dict[j][i]
                h += x
            print(h)
            # I added line so that I could empty the string on each
            # iteration
            h = ''
# Call the function
letter('hello', "horizontal")
letter('hello', "vertical")
