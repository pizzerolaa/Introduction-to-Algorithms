# A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of 
# these three possible types of commands:
# -2: Turn left 90 degrees.
# -1: Turn right 90 degrees.
# 1 <= k <= 9: Move forward k units, one unit at a time.
# Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). 
# If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.
# Return the maximum Euclidean distance that the robot ever gets from the origin squared 
# (i.e. if the distance is 5, return 25).
# Note:
# North means +Y direction.
# East means +X direction.
# South means -Y direction.
# West means -X direction.
# There can be obstacle in [0,0].

def robotSim(commands: list[int], obstacles: list[list[int]]) -> int:
    directions = ((0,1), (1, 0), (0, -1), (-1, 0))
    x = 0
    y = 0
    d = 0
    out = 0
    obstacles = {tuple(j) for j in obstacles}
    for i in commands:
        if i == -1:
            d = (d + 1) % 4
        elif i == -2:
            d = (d - 1) % 4
        else:
            dx, dy = directions[d]
            for _ in range(i): 
                if (x + dx, y + dy) in obstacles:
                    break
                x, y = x + dx, y + dy
        out = max(out, x**2 + y**2)
    return out
com = [4,-1,4,-2,4]
obs = [[2,4]]
print(robotSim(com, obs))