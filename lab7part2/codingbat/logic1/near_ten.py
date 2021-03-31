def near_ten(num):
    within = num % ((num / 10) * 10) if num >= 10 else num
    return within in [8, 9, 0, 1, 2]
