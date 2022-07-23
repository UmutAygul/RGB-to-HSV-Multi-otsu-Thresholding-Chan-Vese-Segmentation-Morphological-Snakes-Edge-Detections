from skimage.color import rgb2gray,rgb2hsv 
from skimage import io
from skimage import img_as_ubyte



class Conversion:
    """! The Conversion  class.
    All Conversion functions belong this class.
    """
    
    def __init__(self):
        pass
    
    def conversiongray(self,img):
        """! The Conversion to gray function.
        @param img Reads the path of picture
        @param Make the picture HSV
        
        """
        
        img = io.imread(self.path)
        self.imgGray = rgb2gray(img)
        name="gray.png"
        io.imsave(name, (self.imgGray))
        
        self.copying(name)
    def conversionhsv(self,img):
        """! The Conversion to hsv function.
        @img name Reads the path of picture
        @imgHsv Make the picture HSV
        
        """
                
        
        img = io.imread(self.path) 
        imgHsv = rgb2hsv(img)#rgb to hsv
        io.imsave('hsv.png', img_as_ubyte(imgHsv))
        name="hsv.png"
        self.copying(name)