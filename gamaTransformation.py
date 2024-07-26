import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image_array, gamma):
    # Normalize pixel values to range [0, 1]
    image_array = image_array / 255.0
    
    # Apply gamma transformation
    gamma_corrected = np.power(image_array, gamma)
    
    # Scale values back to range [0, 255] and convert to uint8
    gamma_corrected = (gamma_corrected * 255).astype(np.uint8)
    
    return gamma_corrected

def plot_gamma_transformed_image(image_path, gamma):
    # Read the image
    image_array = plt.imread(image_path)
    
    # Convert image to grayscale if it's not already
    if len(image_array.shape) == 3:
        # Assuming the image is RGB, convert to grayscale
        image_array = np.dot(image_array[..., :3], [0.299, 0.587, 0.114])
    
    # Perform gamma correction
    gamma_corrected = gamma_correction(image_array, gamma)
    
    # Display original and gamma corrected images
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display original image
    ax1.imshow(image_array, cmap='gray')
    ax1.set_title('Original Image')
    ax1.axis('off')
    
    # Display gamma corrected image
    ax2.imshow(gamma_corrected, cmap='gray')
    ax2.set_title(f'Gamma Corrected (Gamma: {gamma})')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.show()

# Specify the path to the image and the gamma value
image_path = "/home/parrot/Desktop/test.png"
gamma_value = 1.5  # Adjust this gamma value as needed

# Plot gamma transformed image
plot_gamma_transformed_image(image_path, gamma_value)
