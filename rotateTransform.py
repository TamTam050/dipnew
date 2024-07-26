import numpy as np
import matplotlib.pyplot as plt
import math

def rotate_image(image_array, angle):
    # Convert angle to radians
    theta = math.radians(angle)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    
    # Define the transformation matrix for 2D rotation
    transformation_matrix = np.array([[cos_theta, -sin_theta],
                                      [sin_theta, cos_theta]])
    
    # Get the size of the original image
    height, width = image_array.shape[:2]
    
    # Calculate new image size after rotation
    new_height = int(abs(width * sin_theta) + abs(height * cos_theta))
    new_width = int(abs(height * sin_theta) + abs(width * cos_theta))
    
    # Initialize the transformed image array
    transformed_image = np.zeros((new_height, new_width, image_array.shape[2]), dtype=np.uint8)
    
    # Compute the center of the original and transformed images
    center_x, center_y = width / 2, height / 2
    new_center_x, new_center_y = new_width / 2, new_height / 2
    
    # Apply the rotation transformation
    for x in range(new_width):
        for y in range(new_height):
            # Compute the original coordinates from the new coordinates
            original_x = (x - new_center_x) * cos_theta + (y - new_center_y) * sin_theta + center_x
            original_y = -(x - new_center_x) * sin_theta + (y - new_center_y) * cos_theta + center_y
            
            # Check if the coordinates are within the bounds of the original image
            if 0 <= original_x < width and 0 <= original_y < height:
                transformed_image[y, x, :] = image_array[int(original_y), int(original_x), :]
    
    return transformed_image

# Load the original image using matplotlib
image_path = "/home/parrot/Desktop/test.png"
original_image = plt.imread(image_path)

# Ensure image is in RGB format (if it's grayscale, the shape will be 2D)
if len(original_image.shape) == 2:
    original_image = np.stack([original_image]*3, axis=-1)  # Convert grayscale to RGB

# Rotate the image by 30 degrees
rotated_image = rotate_image(original_image, 30)

# Visualizing the original and transformed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(original_image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Rotated Image (30 degrees)')
plt.imshow(rotated_image)
plt.axis('off')

plt.tight_layout()
plt.show()
