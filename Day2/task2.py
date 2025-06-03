def over_and_balls(ball):
    over = ball // 6
    remaining_ball = ball % 6
    return f"{over}.{remaining_ball}"

print(over_and_balls(26))
print(over_and_balls(12))
print(over_and_balls(15))
print(over_and_balls(120))