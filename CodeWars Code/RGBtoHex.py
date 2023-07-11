def rgb(r, g, b):
    r, g, b = min(r, 255), min(g, 255), min(b, 255)
    r, g, b = max(r, 0), max(g, 0), max(b, 0)
    return '{:02x}{:02x}{:02x}'.upper().format(r, g, b)

print(rgb(300,255,1))
