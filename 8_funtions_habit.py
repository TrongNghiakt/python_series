# Rule 1: Snake_case names
# Rule 2: Verb_Based names
# Rule 3: Clear parameters
# Rule 4: Docstrings
# Rule 5: Return not Print
# Rule 6: Local variables
# Rule 7: Type hints
# Rule 8: Args & Returns in Docstring


# Good
def calculate_discount(price: float, rate: float) -> float:
    """
    Calculate the discounted price based on the original price and discount rate.
    Agrs:
        price (float): The original price of the item.
        rate (float): The discount rate as a percentage.
    Returns:
        final_price (float): The price after applying the discount.
    """
    final_price = price - (price*rate/100)
    return (final_price)


# Bad
# def DiscPrint(p, r):
#     print("calculating discount")
#     p = p - (p*r/100)
#     print(p)


# DiscPrint(100, 10)
# help(calculate_discount)
print("Calculating discount")
print(calculate_discount(100, 10))
