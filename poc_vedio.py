# Program To Read video and Extract Frames 
import cv2 
  
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
    
    print("==============>>>>>>>>>>>> ")
    print("vidObj >> ", vidObj)
    # Used as counter variable 
    count = 0
    
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        
        print("Frame ")
        print(count, image)
        # Saves the frames with frame-count 
        cv2.imwrite("/home/meetu/p_p/docs/poc/frame%d.jpg" % count, image) 
        print("Frame saved to image")
        count += 1
  
# Driver Code 
if __name__ == '__main__': 

    # Calling the function 
    FrameCapture("/home/meetu/p_p/docs/poc/nobita.mp4") 
