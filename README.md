# Digital-stole-POS
class Person:
    def __init__(self, name):
        self.name = name


class RetailCustomer(Person):
    def price(self, item, qty):
        prices = {"tomatoes": 3000, "onions": 2500, "matooke": 25000}
        price = prices[item]

        if item in ["tomatoes", "onions"] and qty > 5:
            return 5 * price + (qty - 5) * price * 0.95

        return qty * price


class WholesaleCustomer(Person):
    def price(self, item, qty):
        prices = {"tomatoes": 2400, "onions": 2000, "matooke": 20000}

        if item == "matooke" and qty < 3:
            return qty * 25000

        return qty * prices[item]


def quantity():
    while True:
        try:
            q = float(input("Enter quantity: "))
            if q > 0:
                return q
            print("Quantity must be greater than 0.")
        except ValueError:
            print("Enter a number.")


def main():
    customers = 0
    revenue = 0
    highest = 0
    star = ""

    print("=" * 50)
    print("       MAMA MBOGA DIGITAL STALL POS")
    print("=" * 50)

    while True:
        name = input("Customer Name: ")
        kind = input("Customer Type (retail/wholesale): ").lower()

        if kind == "retail":
            customer = RetailCustomer(name)
        else:
            customer = WholesaleCustomer(name)

        subtotal = 0

        while True:
            item = input(
                "Add Item (tomatoes/onions/matooke/done): "
            ).lower()

            if item == "done":
                break

            if item not in ["tomatoes", "onions", "matooke"]:
                print("Invalid item!")
                continue

            q = quantity()
            cost = customer.price(item, q)
            subtotal += cost

            print("Added", q, item)

        crate = input("Add reusable crate? (yes/no): ").lower()

        crate_cost = 5000 if crate == "yes" else 0
        levy = subtotal * 0.01
        total = subtotal + levy + crate_cost

        print("\n----------- RECEIPT -----------")
        print("Customer:", name, "(" + kind.upper() + ")")
        print("Subtotal:", subtotal, "UGX")
        print("Crate:", crate_cost, "UGX")
        print("Levy:", levy, "UGX")
        print("TOTAL:", total, "UGX")

        customers += 1
        revenue += total

        if total > highest:
            highest = total
            star = name

        again = input("Serve next customer? (yes/no): ").lower()

        if again == "no":
            break

    print("\n====== DAILY MARKET CLOSE ======")
    print("Customers Served:", customers)
    print("Total Revenue:", revenue, "UGX")
    print("Star Customer:", star, "(", highest, "UGX)")


main()
