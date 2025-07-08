
def show_doors(monty_door, first):
    if first == 1:
        if monty_door == 2:
            return one_two
        elif monty_door == 3:
            return one_three
    elif first == 2:
        if monty_door == 1:
            return two_one
        elif monty_door == 3:
            return two_three
    elif first == 3:
        if monty_door == 1:
            return three_one
        elif monty_door == 2:
            return three_two

# Shows up after monty picks his door
one_two = (r"""
+-----+  +-----+  +-----+
| You |  |  X  |  |     |
+-----+  +-----+  +-----+
""")

one_three = (r"""
+-----+  +-----+  +-----+
| You |  |     |  |  X  |
+-----+  +-----+  +-----+
""")

two_one = (r"""
+-----+  +-----+  +-----+
|  X  |  | You |  |     |
+-----+  +-----+  +-----+
""")

two_tree = ("""
+-----+  +-----+  +-----+
|     |  | You |  |  X  |
+-----+  +-----+  +-----+
""")

three_one = (r"""
+-----+  +-----+  +-----+
|  X  |  |     |  | You |
+-----+  +-----+  +-----+
""")

three_two = (r"""
+-----+  +-----+  +-----+
|     |  |  X  |  | You |
+-----+  +-----+  +-----+
""")

# Final Door that you open

correct_door = (r"""
+-----+
|(=^.^)|
+-----+
""")

wrong_door = (r"""
+-----+
|  X  |
+-----+
""")