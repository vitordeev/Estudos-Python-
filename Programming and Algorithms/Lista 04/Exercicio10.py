# Example using break, continue, and else
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # Skips printing 3
    if i == 5:
        break     # Stops the loop entirely at 5
    print(i)
else:
    print("Loop finished successfully!")  # Will NOT run because of the 'break'
