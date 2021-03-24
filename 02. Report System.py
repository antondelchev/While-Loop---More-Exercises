sum_needed = int(input())

money_collected = 0

pay_cash = 0
pay_card = 0
cash_sum = 0
card_sum = 0

command_or_end = input()

counter = 1

while command_or_end != "End":
    if counter % 2 != 0:
        if int(command_or_end) <= 100:
            pay_cash += 1
            cash_sum += int(command_or_end)
            money_collected += int(command_or_end)
            print("Product sold!")
        else:
            print("Error in transaction!")

    if counter % 2 == 0:
        if int(command_or_end) >= 10:
            pay_card += 1
            card_sum += int(command_or_end)
            money_collected += int(command_or_end)
            print("Product sold!")
        else:
            print("Error in transaction!")

    counter += 1

    if money_collected >= sum_needed:
        print(f"Average CS: {cash_sum / pay_cash:.2f}")
        print(f"Average CC: {card_sum / pay_card:.2f}")
        break

    command_or_end = input()

    if command_or_end == "End":
        print("Failed to collect required money for charity.")
