def calculate_total_cost(price, quantity):
    subtotal = price * quantity

    # TODO: complete basic if/else discount logic
    if quantity >= 10:
        discount_rate = 0.10
    else:
        discount_rate = None

    # TODO: return final total after discount
    return subtotal
