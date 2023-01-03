import numpy as np
import cv2


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """

        left = image_left[0:350, 0:column]
        right = image_right[0:350, column:340]
        merged_image = np.zeros((350, 340), dtype=int)
        merged_image[0:350, 0:column] = left
        merged_image[0:350, column:340] = right








        # Please do not change the structure
        return merged_image  # Currently the original image is returned, please replace this with the merged image

    def intensity_scaling(self, input_image, column, alpha, beta):
        """
        Scale your image intensity.

        input_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """

        output_image = np.zeros((350, 340), dtype=int)
        output_image[0:350, 0:column] = input_image[0:350, 0:column] * alpha
        output_image[0:350, column:340] = input_image[0:350, column:340] * beta



        # Please do not change the structure
        return output_image  # Currently the input image is returned, please replace this with the intensity scaled image

    def centralize_pixel(self, input_image, column):
        """
        Centralize your pixels (do not use np.mean)

        input_image: the input image
        column: image column at which left section ends

        return: output_image
        """
        l_intensity = 0
        r_intensity = 0
        rows = len(input_image)

        centralized_image = np.zeros((350, 340), dtype=int)
        left = input_image[0:350, 0:column]
        right = input_image[0:350, column:340]
        for x in range(column):
            for y in range(rows):
                l_intensity += left[y, x]

        l_intensity = l_intensity/(350*column)

        l_offset = 128 - l_intensity
        for x in range(column):
            for y in range(rows):
                left[y, x] += l_offset
                if left[y, x] > 255:
                    left[y, x] = 255
                if left[y, x] < 0:
                    left[y, x] = 0
        for x in range(340-column):
            for y in range(rows):
                r_intensity += right[y, x]

        r_intensity = r_intensity/(350*(340-column))
        r_offset = 128 - r_intensity
        for x in range(340-column):
            for y in range(rows):
                right[y, x] += r_offset
                if right[y, x] > 255:
                    right[y, x] = 255
                if right[y, x] < 0:
                    right[y, x] = 0
        centralized_image[0:350, 0:column] = left
        centralized_image[0:350, column:340] = right


        return centralized_image   # Currently the input image is returned, please replace this with the centralized image
