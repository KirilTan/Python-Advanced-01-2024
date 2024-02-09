def grocery_store(**products) -> str:
    """
    This function takes a variable number of keyword arguments and returns a sorted list of items in the form of a string.

    Parameters:
        products: a dictionary of items and their quantities

    Returns:
        str: a sorted list of items and their quantities

    """
    organized_products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return '\n'.join(f'{product}: {quantity}' for product, quantity in organized_products)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
