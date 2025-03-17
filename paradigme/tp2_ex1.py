euros = [50, 20, 35, 100, 80]

dollars = list(map(lambda x: f"${x * 1.4:.2f}", euros))

print(dollars)