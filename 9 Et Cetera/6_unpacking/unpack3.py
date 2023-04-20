# Passes positional arguments as usual
# https://harrypotter.fandom.com/wiki/Wizarding_currency

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins=[100, 50, 25]

print(total(*coins), "Knuts") #unpacking