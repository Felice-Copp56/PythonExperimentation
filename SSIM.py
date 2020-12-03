# 1. Import the necessary packages
from skimage.measure import compare_ssim
import cv2
# 2. Load the two input images
from skimage.metrics import structural_similarity

#localevs5-5, 34 e 37,114,117,72,74,116 e 119
#localevs10-10, 113 e115,38 e40,33e35,116 e 118
#localevs30-20,114 e 107,116 e 109,68 e 61
#localevs5-5Geforce 111 e114,116 e 113, 82 e 79,100 e 97
#localevs3020GeForce 116 e 114,83 e 81,126 e 124,74 e 72
#localevs1010GeForce 114 e 113,116 e 114,126e125,76 e 74,125 e 124

#localevsXCLOUD5 114 e 122,116 e 124,124 e 132,82 e 90
#localevsXCLOUD10 114 e 121,116 e 123,124 e 131,113 e 120
#localevsXCLOUD30 114 e 118,124 e 128,113 e 117,116 e 120
def main():

    imageA = cv2.imread("RiferimentoLocale/frame82.jpg")
    imageB = cv2.imread("XCloud30/frame86.jpg")

# 3. Convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# 4. Compute the Structural Similarity Index (SSIM) between the two
#    images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    structural=structural_similarity(grayA, grayB, multichannel=True, gaussian_weights=True, sigma=1.5,
                          use_sample_covariance=False, data_range=255)
    print("Strut",structural)
# 5. You can print only the score if you want
    print("SSIM: {}".format(score))
    if score==1.0:
        print("Same image")
    else:
        print("The images are not equals")
if __name__ == '__main__':
    main()