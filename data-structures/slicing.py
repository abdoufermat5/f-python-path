# One thing I had lean from this section is the slice() function

line_items = """
0.....6.................................40........52...55........
1909 Pimoroni PiBrella                          $17.50    3 $52.50
"""

S = slice(0, 6)

print(line_items[S])
