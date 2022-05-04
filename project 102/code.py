
import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
image_name = "img" + str(number) + ".png"
cv2.inwrite(image_name, frame)
start_time = time.time
result = False
return image_name
print("snapshot taken")

videoCaptureObject.release
cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token = 'https://www.dropbox.com/scl/fi/8wes4sx533aklgauvyhit/_-Getting-Started-with-Dropbox-Paper.paper?dl=0&rlkey=85eao7zv0e4qlrz3nj0muo2yv'
    file image_name
    file_from= file
    file_to="/newFolder1" + (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.writefode.overtrite) 
        print("file uploaded")

def main():
    while(True):
        if ((time.time() start_time) >= 3):     
            name= take_snapshot() 
            upload_file(name)
            
main()
