import cv2

# verify installation & import
print(cv2.__version__)

# read the image
image_name = './img/cat-4753271_640'
image_extension = 'jpg'
counter = 1

cat_image = cv2.imread(image_name + '.' + image_extension)

# displays python cv2 representation of the image as an array in case of success
# displays none if image could not be opened
print(cat_image)

# show the image
cv2.imshow('PyImage',cat_image)

# Do not close the image window immediate but wait till the user closes it.
key_hit = cv2.waitKey(0)      # in milliseconds - 0: wait forever
  
if key_hit == ord('s'):
    cv2.imwrite(image_name + '-copy-'+ str(counter) + '.png', cat_image)
    counter += 1

# Exit gracefully - clear memory
cv2.destroyAllWindows()