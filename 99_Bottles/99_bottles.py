# Prints out the lyrics to 99 Bottles of Beer on the Wall.

def main():
    bottles = 99

    while bottles > 0:
        if bottles == 2:
            print bottles, "bottles of beer on the wall,", bottles, "bottles of beer."
            print "Take one down and pass it around,", bottles - 1, "bottle of beer on the wall."
            print

        elif bottles == 1:
            print bottles, "bottle of beer on the wall,", bottles, "bottle of beer."
            print "Take one down and pass it around,", bottles - 1, "bottle of beer on the wall."
            print



        else:
            print bottles, "bottles of beer on the wall,", bottles, "bottles of beer."
            print "Take one down and pass it around,", bottles - 1, "bottles of beer on the wall."
            print

        bottles -= 1

main()
