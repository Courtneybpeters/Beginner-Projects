"""
To access data from constants, use the following indexes:

[0] Penny
[1] Nickel
[2] Dime
[3] Quarter

"""

DENOM = ["Pennies", "Nickels", "Dimes", "Quarters"]
WEIGHT = [2.5, 5, 2.268, 5.67]
WRAP_QTY = [50, 40, 50, 40]
VALUE = [.01, .05, .1, .25]

def main():
    coins = [0, 0, 0, 0]
    qty = [0, 0, 0, 0]

    # Gets weight of all coins
    for coin in range(len(coins)):
        print "Weight of ", DENOM[coin], ": "
        coins.append(float(raw_input()))

    for coin in range(len(coins)):
        # TODO: Do I need to round and then int? Am I using Round wrong?
        quantity = int(round(coins[coin] /  WEIGHT[coin]))
        qty[coin] = quantity

    print 'Weights: ', coins
    print 'Est. Qty: ', qty

    wrappers(qty)
    coin_value(qty)

# Calculates how many wrappers needed based off weights
def wrappers(quantity):
    print "Wrappers needed for: "

    # Calculate number of wrappers
    for coin in range(len(quantity)):
        wrap_need = quantity[coin] / WRAP_QTY[coin]

        # Determine if will totally fit
        if quantity[coin] % WRAP_QTY[coin] != 0:
            wrap_need += 1

        # Display result
        print DENOM[coin], ": ", wrap_need

def coin_value(coins):

    for i in range(len(coins)):
        value = coins[i] * VALUE[i]
        value = round(value, 2)
        print DENOM[i], "value: $", value


if __name__ == "__main__":
    main()
