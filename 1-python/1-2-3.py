# write a sentinel controlled loop to input a color until quit
# add the colors to a list and print the list each time
# do not add a color if it has already been added to the list
# keep a separate list of duplicate colors and print it at the end
colors = []
duplicates = []
while True:
    color = input("Enter a color (or 'quit' to exit): ")
    if color == "quit":
        break
    if color not in colors:
        colors.append(color)
    else:
        duplicates.append(color)
    print(f"The list of colors is: {colors}")
print(f"The list of duplicate colors is: {duplicates}")