import cv2
from Modules.person_detector import person_detect
import glob


def main():
    for img in glob.glob("*.jpg"):
        n = cv2.imread(img)
        person_detect(n)


if __name__ == "__main__":
    main()
