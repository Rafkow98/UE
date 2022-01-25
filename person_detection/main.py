import cv2
from Modules.person_detector import person_detect
import glob


def main():
    cv_img = []
    for img in glob.glob("*.jpg"):
        n = cv2.imread(img)
        cv_img.append(n)

    for x in cv_img:
        person_detect(x)


if __name__ == "__main__":
    main()
