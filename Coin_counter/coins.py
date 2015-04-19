"""
To access data from constants, use the following indexes:

[0] Penny
[1] Nickel
[2] Dime
[3] Quarter

"""

NAMES = ["Pennies", "Nickels", "Dimes", "Quarters"]
WEIGHT = [2.5, 5, 2.268, 5.67]
WRAP_QTY = [50, 40, 50, 40]
VALUE = [.01, .05, .1, .25]

def main():
    coins = [0, 0, 0, 0]
    qty = [0, 0, 0, 0]

    print
    print "Coin Calculator by Weight"
    print

    # Gets weight of all coins
    for i in range(len(coins)):
        print "Weight of ", NAMES[i], ": "
        coins[i] = float(raw_input())

    for i in range(len(coins)):
        qty[i] = int(round(coins[i] /  WEIGHT[i]))

    print
    print 'Weights: ', coins
    print 'Est. Qty: ', qty

    wrappers(qty)
    coin_value(qty)

# Calculates how many wrappers needed based off weights
def wrappers(quantity):
    print '=' * 80
    print "Wrappers needed for: "

    # Calculate number of wrappers
    for coin in range(len(quantity)):
        wrap_need = quantity[coin] / WRAP_QTY[coin]

        # Determine if will totally fit
        if quantity[coin] % WRAP_QTY[coin] != 0:
            wrap_need += 1

        # Display result
        print NAMES[coin], ": ", wrap_need

def coin_value(coins):
    print '=' * 80
    for i in range(len(coins)):
        value = round(coins[i] * VALUE[i], 2)
        print NAMES[i], "value:\t$", '{:,.2f}'.format(value)


if __name__ == "__main__":
    main()
