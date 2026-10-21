# colors = ['red', 'green', 'blue']
# sizes = ['L', 'M', 'S']
# for color in colors:
#     for size in sizes:
#         print(f"{color}, Size: {size}")


# years = [2026, 2027]
# months = ['Jan', 'Feb']
# days = range(1, 29)

# for y in years:
#     for m in months:
#         for d in days:
#             print(f"report_{y}_{m}_{d}.csv")


tables = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'name', 'price', 'quantity']
for t in tables:
    for c in columns:
        print(f"SELECT count(*) from {t} WHERE {c} IS NULL;")
