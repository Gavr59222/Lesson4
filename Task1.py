from sys import argv

file_name, worked_hour, rate, benefit = argv

calculation = (int(worked_hour) * int(rate)) + int(benefit)
print(f"Заработная плата составит {calculation}")
