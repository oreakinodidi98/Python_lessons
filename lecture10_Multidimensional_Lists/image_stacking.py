import numpy as np
import matplotlib.pyplot as plt

# sample grayscal image (all of the same size)
image1 = np.array([[0, 255, 255, 255, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0],
                   [0, 0, 0, 0, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0]])


image2 = np.array([[0, 255, 255, 255, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0],])

image3 = np.array([[0, 255, 255, 255, 255, 0],
                   [0, 0, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0],
                   [0, 255, 255, 255, 255, 0],
                   [0, 0, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0],])

image4 = np.array([[0, 255, 0, 0, 0, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 255],
                   [0, 0, 0, 0, 255, 0],
                   [0, 0, 0, 0, 255, 0]])

image5 = np.array([[0, 255, 255, 255, 255, 0],
                   [0, 255, 0, 0, 0, 0],
                   [0, 255, 255, 255, 255, 0],
                   [0, 0, 0, 0, 255, 0],
                   [0, 0, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0]])

class ImageStacker():
    def __init__(self, img_stack):
        self.imgs = img_stack
        pass
# take all the images in the stack and stack them into a 3D tensor
    def stack_images(self):
        stacked = np.stack(self.imgs)
        return stacked
# display the image
    def display_image(self, img):
        plt.imshow(img, cmap="gray")
        plt.show()

# create an instance/object of the class
img_stack = ImageStacker([image1, image2, image3, image4, image5])

# Stack images into a 3D tensor
stacked_tensor = img_stack.stack_images()

# Display two images from the stacked tensor
img_stack.display_image(stacked_tensor[0])
img_stack.display_image(stacked_tensor[1])
img_stack.display_image(stacked_tensor[2])
img_stack.display_image(stacked_tensor[3])
img_stack.display_image(stacked_tensor[4])

# run with C:/Python311/python.exe