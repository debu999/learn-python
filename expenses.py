from pprint import pp


expenses = [10.5, 8, 5, 15, 20, 4, 37]
total = 0
for e in expenses: 
    total += e

pp(f"you spent total of ${total}")
pp(f"you spent total of ${sum(expenses)}")