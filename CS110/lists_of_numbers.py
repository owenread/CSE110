points_scored = [24, 18, 31, 42, 28]

running_total = 0
for point_amount in points_scored:
    #running_total = running_total + point_amount
    running_total += point_amount

print(f"The player has scored {running_total} points.")