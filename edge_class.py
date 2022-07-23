from skimage import io,filters




class Edge:
    """! The Edge  class.
    All Edge functions belong this class.
    """
    def __init__(self):
        pass

    def prewitt(self,image): #of of edge detection functions is Prewitt
        """!
        This function applies the Prewitt edge detection to the picture
        It takes path of input, make it image then make it Edge detection for Prewitt.
        After that sends to the output function
        
        """
        image = io.imread(self.path)
        edge_prewitt = filters.prewitt(image)
        self.prewitt="prewitt.png"    
        self.output(self.prewitt,edge_prewitt)
   
    
   
    def scharr(self,image):#of of edge detection function is Scharr
        """!
        This function applies the Scharr edge detection to the picture.
        It follows the same system as Prewitt.
        
        """
        image = io.imread(self.path)
        edge_scharr = filters.scharr(image)
        self.scharr="scharr.png"
        self.output(self.scharr,edge_scharr)
    
    
    
    def robert(self,image):#of of edge detection function is Roberts
        """!
        This function applies the Roberts edge detection to the picture.
        It follows the same system as Prewitt.
        
        """
    
        self.robert="robert.png"
        image = io.imread(self.path)
        edge_roberts = filters.roberts(image)
        self.output(self.robert,edge_roberts)
        

        
        
    def sobel(self,image):
        """!
        This function applies the Sobel edge detection to the picture.
        It follows the same system as Prewitt.
        """
        
        self.sobel="sobel.png"
        image = io.imread(self.path)
        edge_sobel = filters.sobel(image)
        self.output(self.sobel,edge_sobel)