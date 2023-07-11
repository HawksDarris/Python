'''
This reduces directions that would send you back to your starting point on a cartesian plane. Like if directions tell you to go NORTH one unit then SOUTH one unit, they haven't told you to go anywhere.
'''
def dirReduc(arr):
    opposite_dirs = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    mostrecent = []

    for direction in arr:
        if mostrecent and opposite_dirs[direction] == mostrecent[-1]:
            mostrecent.pop()
        else:
            mostrecent.append(direction)

    return mostrecent

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
