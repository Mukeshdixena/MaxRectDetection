import cv2
import numpy as np
import matplotlib.pyplot as plt

def convert_image_to_binary_matrix(image_path, threshold_value=128):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if original_image is None:
        print(f"Error: Unable to load image from path: {image_path}")
        return None, None
    
    _, binary_image = cv2.threshold(original_image, threshold_value, 1, cv2.THRESH_BINARY)
    return binary_image, original_image

def largestRectangleAreaWithCorners(heights):
    stack = []
    max_area = 0
    top_left = (0, 0)
    bottom_right = (0, 0)
    index = 00

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            height = heights[top_of_stack]
            width = (index - stack[-1] - 1) if stack else index
            area = height * width

            if area > max_area:
                max_area = area
                bottom_right = (index - 1, top_of_stack)
                top_left = (bottom_right[0] - width + 1, bottom_right[1] - height + 1)

    while stack:
        top_of_stack = stack.pop()
        height = heights[top_of_stack]
        width = (index - stack[-1] - 1) if stack else index
        area = height * width

        if area > max_area:
            max_area = area
            bottom_right = (index - 1, top_of_stack)
            top_left = (bottom_right[0] - width + 1, bottom_right[1] - height + 1)

    return max_area, top_left, bottom_right

def maximalRectangleWithCorners(matrix):
    if matrix is None or not matrix.any():
        print("Error: The binary matrix is empty or invalid.")
        return 0, None, None, None, None

    max_area = 0
    top_left = (0, 0)
    top_right = (0, 0)
    bottom_left = (0, 0)
    bottom_right = (0, 0)
    histogram = [0] * matrix.shape[1]

    for row_index, row in enumerate(matrix):
        for col_index in range(len(row)):
            histogram[col_index] = histogram[col_index] + 1 if row[col_index] == 1 else 0

        area, top_left_temp, bottom_right_temp = largestRectangleAreaWithCorners(histogram)

        if area > max_area:
            max_area = area
            top_left = (top_left_temp[0], row_index - (bottom_right_temp[1] - top_left_temp[1]) + 1)
            top_right = (bottom_right_temp[0], row_index - (bottom_right_temp[1] - top_left_temp[1]) + 1)
            bottom_left = (top_left_temp[0], row_index)
            bottom_right = (bottom_right_temp[0], row_index)

    return max_area, top_left, top_right, bottom_left, bottom_right

def plot_rectangle_with_points(image_path, corners, output_path):
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Unable to load image from path: {image_path}")
        return

    top_left, top_right, bottom_left, bottom_right = corners

    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    cv2.circle(image, top_left, 5, (0, 0, 255), -1)  
    cv2.circle(image, top_right, 5, (0, 0, 255), -1)  
    cv2.circle(image, bottom_left, 5, (0, 0, 255), -1)  
    cv2.circle(image, bottom_right, 5, (0, 0, 255), -1)  

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title("Largest Rectangle with Corner Points")
    plt.show()

    if cv2.imwrite(output_path, image):
        print(f"Image saved successfully to {output_path}")
    else:
        print("Failed to save the image.")



# Example usage:
image_path = 'img/input_images/zigzag_mask.png' 
output_path = 'img/output_images/out_zigzag_mask.png'

binary_matrix, original_image = convert_image_to_binary_matrix(image_path)
max_area, top_left, top_right, bottom_left, bottom_right = maximalRectangleWithCorners(binary_matrix)

if max_area > 0:
    print(f"Largest Rectangle Area: {max_area}")
    print(f"Top Left Corner: {top_left}")
    print(f"Top Right Corner: {top_right}")
    print(f"Bottom Left Corner: {bottom_left}")
    print(f"Bottom Right Corner: {bottom_right}")
    plot_rectangle_with_points(image_path, (top_left, top_right, bottom_left, bottom_right), output_path)
else:
    print("No rectangle found.")
