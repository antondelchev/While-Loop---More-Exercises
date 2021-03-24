num_bottles = int(input())

total_liquid = num_bottles * 750

used_liquid = 0
counter = 0
num_dishes = 0
num_pots = 0

command_or_end = input()

while command_or_end != "End":
    counter += 1
    if counter % 3 == 0:
        used_liquid += 15 * int(command_or_end)
        num_pots += int(command_or_end)
    else:
        used_liquid += 5 * int(command_or_end)
        num_dishes += int(command_or_end)

    if used_liquid > total_liquid:
        needed = used_liquid - total_liquid
        print(f"Not enough detergent, {needed} ml. more necessary!")
        break
    command_or_end = input()

if used_liquid <= total_liquid:
    left = total_liquid - used_liquid
    print("Detergent was enough!")
    print(f"{num_dishes} dishes and {num_pots} pots were washed.")
    print(f"Leftover detergent {left} ml.")
