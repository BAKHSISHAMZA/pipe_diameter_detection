import cv2
def click_event(event, x, y, flags, param):
    """
    A callback function for handling mouse click events in an
    OpenCV window.
    Parameters:
    event (int): The type of mouse event that occurred.
    x (int): The x-coordinate of the mouse cursor.
    y (int): The y-coordinate of the mouse cursor.
    flags (int): Any special flags associated with the mouse
    event.
    param (object): Optional parameters passed to the mouse
    callback.
    Returns:
    None.
    Side Effects:
    Depending on the type of mouse event, this function may
    display text on the image window.
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        # Handle left button-down event
        print('Left button clicked at (%d, %d)' % (x, y))
        # Add text to the image window displaying the coordinates of the click
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strxy = str(x) + ', ' + str(y)
        cv2.putText(img, strxy, (x, y), font, 1, (255, 255, 0), 2)
        # Update the image window with the new text
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        # Handle right button down event
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        # Add text to the image window displaying the BGR color values of the pixel
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (0, 255, 255), 2)
        # Update the image window with the new text
        cv2.imshow('image', img)
# Display the image
img = #replace with you image path 
img = cv2.resize(img,(1080,720))
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event )
cv2.waitKey(0)
cv2.destroyAllWindows()
