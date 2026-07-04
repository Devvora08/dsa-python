# # You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# # Find two lines that together with the x-axis form a container, such that the container contains the most water.
# # Return the maximum amount of water a container can store.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

def most_water(height):
    # brute force - find area of all the containers, return maximum area
    max_area = -100

    for i in range(0,len(height)):
        curr_area = 0
        for j in range(i, len(height)):
            max_height = min(height[i], height[j])
            length = j-i

            curr_area = max_height * length
            max_area = max(curr_area, max_area)
    
    return max_area

def container_most_water(height):
    # 2 pointer
    max_area = -100

    i = 0
    j = len(height) - 1

    while i != j:
        max_height = min(height[i], height[j])
        length = j-i

        curr_area = max_height * length
        max_area = max(max_area, curr_area)

        if height[i] > height[j]:
            j -= 1
        else: i += 1

    return max_area


height = [1,8,6,2,5,4,8,3,7]
print(container_most_water(height))