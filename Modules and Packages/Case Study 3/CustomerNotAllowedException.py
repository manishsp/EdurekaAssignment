import Customer, Merger


class CustomerNotAllowedException(Exception):
    pass
    try:
        if Customer.Customer.isblacklisted == 0:
            print(f"Customer{Merger.customer_m.getFname()} is not blacklisted")
        else:
            raise CustomerNotAllowedException
    except CustomerNotAllowedException:
        print(f"Customer{Merger.customer_m.getFname()} is blacklisted and not allowed")
