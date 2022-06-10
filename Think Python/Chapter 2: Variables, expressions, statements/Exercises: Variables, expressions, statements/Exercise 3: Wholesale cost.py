"""Wholesale cost for book with cover price, discount percentage, first-, extra-copy shipping, extra-copy"""
copies = 60
cov_price = 24.95
discount = 40           # Percentage
frst = 3                # First copy
xtra = 0.75             # Extra copies

all_discount = (cov_price * ((100 - discount) / 100)) * copies
all_ship = frst + (xtra * (copies - 1))
cost = all_discount + all_ship

print("Wholesale cost for",
      (str(copies) + " copies"),
      "of", ("$" + str(cov_price) + " book"),
      "is", ("$" + "%.2f" % cost),
      "if:", "\n",
      "bookstores get", (str(discount) + "%"), "discounts", "\n",
      "first copy is", ("$" + str("%.2f" % frst)), "\n",
      "extras are", ("$" + str(xtra)), "each")