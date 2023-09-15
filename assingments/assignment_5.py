height = [179, 154,167,163,159]
total = 0

for num in range(len(height)):
    total = total + height[num]

average = total/len(height)

print(average)