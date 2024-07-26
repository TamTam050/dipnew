import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image_array):
    # Initialize an array to store histogram values (bins range 0-255)
    histogram = np.zeros(256, dtype=int)

    # Iterate through each pixel value in the image array and count occurrences
    for pixel_value in image_array.flatten():
        histogram[pixel_value] += 1

    return histogram

def plot_image_and_histogram(image_path):
    # Read the image
    image_array = plt.imread(image_path)
    
    # Convert image to grayscale if it's not already
    if len(image_array.shape) == 3:
        # Assuming the image is RGB, convert to grayscale
        image_array = np.dot(image_array[..., :3], [0.299, 0.587, 0.114])
    
    # Convert to 8-bit image (0-255 range) if necessary
    if image_array.max() > 1:
        image_array = (image_array / image_array.max() * 255).astype(np.uint8)
    else:
        image_array = (image_array * 255).astype(np.uint8)
    
    # Calculate the histogram
    hist_values = calculate_histogram(image_array)

    # Display the image and its histogram
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display the image
    ax1.imshow(image_array, cmap='gray')
    ax1.set_title('Image')
    ax1.axis('off')

    # Plot the histogram
    ax2.plot(hist_values, color='blue')
    ax2.set_title('Image Histogram')
    ax2.set_xlabel('Pixel Value')
    ax2.set_ylabel('Frequency')

    # Display plot
    plt.tight_layout()
    plt.show()

# Specify the path to the image
image_path = "/home/parrot/Desktop/test.png"

# Plot image and histogram
plot_image_and_histogram(image_path)
