#1- This compares to doing the same task in Excel because Python can do it a lot quicker and make it a lot less complicated. Python can easily add or delete data with a code squence, while in Excel you would have to go in and redo things if you wanted to make a change. However, Excel is better at visually showing you data in a simpler format. 
#2- The append mode showed the total revenue for certain dates and times. A business process that could use the append tool could be when a business needs to know what day and what time of the day they make the most sales. They could use the same code that I have completed in this activity to combine the sales of each different item. They can then append it to see when the most revenue is made. 

#Exercise 2

import csv

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        print(row)

#Exercise 3

print("Header:")
print(header)

print("\nRows:")

#Exercise 4

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        revenue = price * quantity
        total_revenue += revenue
        print(f"{product}: {quantity} units x ${price:.2f} = ${revenue:.2f}")

print(f"\nTotal Revenue: ${total_revenue:.2f}")

#Exercise 5

total_rows = 0
written_rows = 0

with open("data/sales.csv", "r") as infile, \
     open("data/cleaned.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        total_rows += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        if total > 100:
            writer.writerow([product, price, quantity, total])
            written_rows += 1
        print(f"Rows in original file: {total_rows}")
        print(f"Rows written to cleaned.csv: {written_rows}")

#Exercise 6

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")
#The csv.reader is good for when you know the order of your data and want to access it by index which makes it simple. I would use this if I wanted fast access.
#The csv.DictReader is good for when you want to access the data by column names, which makes the code more readable and cause less errors. I would use this if I wanted to focus on header names for each row. 

#Exercise 7

summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity

        if product in summary:
            summary[product] += revenue
        else:
            summary[product] = revenue

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")


#Exercise 8

from datetime import datetime

print(f"Total Revenue: ${total_revenue:.2f}")

timestamp = datetime.now()

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{timestamp}, Total Revenue: ${total_revenue:.2f}\n")

print(open("data/run_log.txt").read())

