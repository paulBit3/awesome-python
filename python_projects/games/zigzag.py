import sys, time

"""This program creates a back-and-forth, zigzag pattern until the user stops by pressing CTRL-C"""

# let's define the number space to indent
indent = 0
# decide whether the indentation is increasing or not
indentIncreasing = True

try:
    while True:  # The main program loop
        print('' * indent, end='')
        print('**********')
        time.sleep(0.1)  # Pause the program for 1/10 of a second

        if indentIncreasing:  # Increase the number of space
            indent = indent + 1  # we can also do this indent += 1
            if indent == 20:  # change direction
                indentIncreasing = False
        else:  # Decrease the number of spaces
            indent = indent - 1
            if indent == 0:  # change direction
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()  # exiting the program

    # **********
    # **********
# **********
# **********
# **********
# **********
# **********
    # **********
    # **********
    # **********
    # **********
    # **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********