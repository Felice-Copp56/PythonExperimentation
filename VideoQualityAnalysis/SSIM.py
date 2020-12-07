# 1. Import the necessary packages
from skimage.measure import compare_ssim
import cv2
# 2. Load the two input images
from skimage.metrics import structural_similarity


def main():

    imageA = cv2.imread("YourFolder/frame82.jpg")
    imageB = cv2.imread("YourFolder/frame86.jpg")

# 3. Convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# 4. Compute the Structural Similarity Index (SSIM) between the two
#    images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    
# 5. You can print only the score if you want
    print("SSIM: {}".format(score))
    if score==1.0:
        print("Same image")
    else:
        print("The images are not equals")
if __name__ == '__main__':
    main()
