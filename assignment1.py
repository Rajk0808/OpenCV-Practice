import cv2

def read_image(image_path):
    " Reads Images"
    image = cv2.imread(image_path)
    return image

def showimage(image):
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

def sav_image(image, name):
    "Saves image with a particular name."
    cv2.imwrite(image, name)
    print("Image Saved with name {0}".format(name))

def convert_image(image, form):
    " Converts Image to grayscale Format"
    if form.lower() == 'gray':
        cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif form.lower() == 'bgr': 
        pass
    return image

def workflow():
    "Whole Workflow of the Assignment"

    print("Hii there this is Assignment 1 Project")

    print('Please Input image file name :')

    path = input()

    image = read_image(path)

    print("✅ File Found Image readed Succesfully !!!")    

    form = input("Please Specify which form to convert current BGR Scaled Image, if you want to left it as it is then 'q' :")

    image = convert_image(image, form)

    ifprint = input('if you want to display press "yes" else "q" :')

    if ifprint.lower() == 'yes':
        showimage(image)
    
    print('Want to save image ?, if not press "q" else provide name')

    name = input()

    if name.lower() != 'q':
        sav_image(image, name)

if __name__ == '__main__':
    workflow()