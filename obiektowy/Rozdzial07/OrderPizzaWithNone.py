def orderPizza(size, style='regular', topping=None):
    # Przeprowadzenie pewnych obliczeń na podstawie parametrów size i style.
    # Sprawdzenie, czy została podana wartość parametru topping.
    PRICE_OF_TOPPING = 1.50  # Dopłata za dodatkowe składniki.

    if size == 'mała':
        price = 10.00
    elif size == 'średnia':
        price = 14.00
    else: # Duża pizza.
        price = 18.00

    if style == 'podwójne':
        price = price + 2.00 # Dopłata za podwójne ciasto.

    line = 'Zamówiona pizza: ' + size + ' ' + style + ' ciasto, '
    if topping is None:  # Sprawdzenie, czy nie podano dodatkowych składników.
        print(line +'bez dodatków')
    else:
        print(line + topping)
        price = price + PRICE_OF_TOPPING

    print('Wartość zamówienia to', price)
    print()

# Pizzę można zamówić na takie sposoby:
orderPizza('duża')  # Duża, domyślne ciasto, brak dodatków.

orderPizza('duża', style='pojedyncze')  # Taka sama jak poprzednio.

orderPizza('średnia', style='podwójne', topping='pieczarki')

orderPizza('mała', topping='pieczarki')  # Domyślnie ciasto to pojedyncze.
