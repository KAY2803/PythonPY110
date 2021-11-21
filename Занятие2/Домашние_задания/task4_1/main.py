if __name__ == "__main__":

    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

def pairwise(arg: list):
    pair = ((pts[x], pts[x+1]) for x in range(len(pts)-1))
    return pair

coordinates = pairwise(pts)
length = sum(map(lambda x: (((x[1][0] - x[0][0]) ** 2) + ((x[1][1] - x[0][1]) ** 2)) ** 0.5, coordinates))
print(length)

# AB = √(xb - xa)2 + (yb - ya)2