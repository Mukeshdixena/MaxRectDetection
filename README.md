
## Overview

This project contains a Python script that processes a grayscale image to find the largest rectangle within a binary matrix, defined by four corners (top-left, top-right, bottom-left, bottom-right). The rectangle is then visually highlighted and displayed using OpenCV and Matplotlib.

## Prerequisites

Before running the script, ensure you have the following packages installed:

- `OpenCV`: For image processing.
- `NumPy`: For numerical operations.
- `Matplotlib`: For plotting and visualization.

You can install these dependencies using pip:

```bash
pip install opencv-python numpy matplotlib
```

## Code Explanation

### 1. `convert_image_to_binary_matrix(image_path, threshold_value=128)`

**Purpose**: This function converts a grayscale image to a binary matrix using a specified threshold value.

- **Input**:
  - `image_path`: Path to the input grayscale image.
  - `threshold_value`: The threshold value for binarization (default is 128).
  
- **Output**:
  - `binary_image`: A binary matrix representation of the image where each pixel is either 0 or 1.
  - `original_image`: The original grayscale image for reference.

- **Steps**:
  1. The image is loaded using `cv2.imread`.
  2. The image is converted to a binary format where pixels above the threshold are set to 1, and those below are set to 0 using `cv2.threshold`.

### 2. `largestRectangleAreaWithCorners(heights)`

**Purpose**: Finds the largest rectangle that can be formed using histogram heights and returns its area and corner points.

- **Input**:
  - `heights`: A list of integers representing the heights of histogram bars.
  
- **Output**:
  - `max_area`: The area of the largest rectangle.
  - `top_left`: Coordinates of the top-left corner of the rectangle.
  - `bottom_right`: Coordinates of the bottom-right corner of the rectangle.

- **Steps**:
  1. The function iterates over the histogram, maintaining a stack to store indices of the bars.
  2. It calculates the area of rectangles that can be formed and updates the maximum area found.
  3. The corner points of the rectangle with the maximum area are recorded and returned.

### 3. `maximalRectangleWithCorners(matrix)`

**Purpose**: Finds the largest rectangle in a binary matrix and returns its area and corner points.

- **Input**:
  - `matrix`: A 2D binary matrix where each element is either 0 or 1.
  
- **Output**:
  - `max_area`: The area of the largest rectangle.
  - `top_left`, `top_right`, `bottom_left`, `bottom_right`: The corner points of the rectangle.

- **Steps**:
  1. The function constructs a histogram for each row of the binary matrix.
  2. It calls `largestRectangleAreaWithCorners` to find the largest rectangle that can be formed in each histogram.
  3. The largest rectangle found is returned along with its corner points.

### 4. `plot_rectangle_with_points(image_path, corners)`

**Purpose**: Draws and visualizes the largest rectangle found on the original image using the provided corner points.

- **Input**:
  - `image_path`: Path to the input image.
  - `corners`: A tuple containing the corner points of the rectangle (top-left, top-right, bottom-left, bottom-right).
  
- **Steps**:
  1. The image is loaded and the rectangle is drawn using `cv2.rectangle`.
  2. The corners are marked with red dots using `cv2.circle`.
  3. The modified image is displayed using `matplotlib.pyplot`.

### 5. Main Execution

**Process**:

1. **Convert Image to Binary Matrix**: The image is converted to a binary matrix using `convert_image_to_binary_matrix`.
2. **Find the Largest Rectangle**: The script identifies the largest rectangle in the binary matrix with `maximalRectangleWithCorners`.
3. **Visualize the Result**: If a rectangle is found, it is drawn on the original image and displayed.

**Output**:
- If a rectangle is found, the area and corner coordinates are printed, and the rectangle is visualized.
- If no rectangle is found, a message is displayed indicating that no rectangle was found.

### Example

```python
image_path = 'image-path.png' 

binary_matrix, original_image = convert_image_to_binary_matrix(image_path)

max_area, top_left, top_right, bottom_left, bottom_right = maximalRectangleWithCorners(binary_matrix)

if max_area > 0:
    print(f"Largest Rectangle Area: {max_area}")
    print(f"Top Left Corner: {top_left}")
    print(f"Top Right Corner: {top_right}")
    print(f"Bottom Left Corner: {bottom_left}")
    print(f"Bottom Right Corner: {bottom_right}")
    plot_rectangle_with_points(image_path, (top_left, top_right, bottom_left, bottom_right))
else:
    print("No rectangle found.")
```

In this example, the script will load an image, convert it to a binary matrix, find the largest rectangle within the binary matrix, and then visualize it by drawing the rectangle on the original image.
