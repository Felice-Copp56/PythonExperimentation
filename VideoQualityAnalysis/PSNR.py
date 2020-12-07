from math import log10, sqrt
import cv2
import numpy as np
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
def MSE(original,compressed):
    mse = np.square(np.subtract(original, compressed)).mean()
    return mse
def main():
    original = cv2.imread("RiferimentoLocale/frame42.jpg")    #
    compressed = cv2.imread("XCloud5/frame50.jpg", 1) #
    """Confrontare locale vs cloud gaming per ogni connessione"""
    value = PSNR(original, compressed)
    mser = MSE(original,compressed)
    print(f"PSNR value is {value} dB")
    #mse = np.mean((original-compressed)**2)
    print(f"MSE value is {mser}")

if __name__ == "__main__":
    main()
