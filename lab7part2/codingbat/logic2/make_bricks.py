def make_bricks(small, big, goal):
    a = goal
    a -= 5 * min(big,goal / 5)
    return a - small <= 0
