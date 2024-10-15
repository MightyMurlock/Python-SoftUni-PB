#workspace = 120 * 70 / w * h
#corridor = 100 / h

WORKSPACE_WIDTH = 120
WORKSPACE_HEIGHT = 70
CORRIDOR_HEIGHT = 100

width = float(input()) * 100
height = float(input()) * 100

workspaces_width = int(width // WORKSPACE_WIDTH)

height -= CORRIDOR_HEIGHT
workspaces_height = int(height // WORKSPACE_HEIGHT)

seats = (workspaces_height * workspaces_width) - 3
print(seats)