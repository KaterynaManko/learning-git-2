def shopping():
    shopping_items = [
        "яйця",
        "булочка",
        "сир фета",
        "масло",
        "помідор"
  ]
    shopping_cart = "У кошику:"
    for item in shopping_items:
     shopping_cart += item +
     return shopping_cart

print(shopping())