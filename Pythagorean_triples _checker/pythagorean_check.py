# Checks if a triangle is a Pythagorean Triplet

def main():
    triangle = [0] * 3

    for i in range(len(triangle)):
        message = "Side" + str(i + 1) + ": "
        triangle[i] = int(raw_input(message))

    triangle.sort()

    a, b, c = triangle[0], triangle[1], triangle[2]

    if c**2 == a**2 + b**2:
        print "This triangle is a Pythagorean Triplet."
    else:
        print "This triangle is not a Pythagorean Triplet."

if __name__ == "__main__":
    main()
