if __name__ =="__main__":
    YEARS = 15
    AMOUNT = 20000
    RATE = 0.1

    total_amount = 40000
    for i in range(YEARS):
        total_amount += AMOUNT
        total_amount *= 1 + RATE

    print(total_amount)

