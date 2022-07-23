from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import os
import matplotlib.pyplot as plt
from skimage.filters import threshold_multiotsu
from skimage.segmentation import chan_vese
import numpy as np
from skimage import io
from skimage import img_as_ubyte
from skimage.segmentation import (morphological_chan_vese,
                                  checkerboard_level_set)

class Segmentation:
    """! The Segmentation  class.
    All segmentation functions belong this class.
    """
    def __init__(self):
        pass

    
    def MS(self,image):#Morphological Snakes function
        """! Making the edge section.
        @param image The file that comes this function as a path
        
        
        @param name The name of image to be saved
        @param self.ss Image which to be Pixmapped
        
        
        """       
        image = io.imread(self.path) #Read the file
        # Initial level set
        init_ls = checkerboard_level_set(image.shape, 6) 
        # List with intermediate results for plotting the evolution
        evolution = [] #define a list
        callback = self.store_evolution_in(evolution)
        ls = morphological_chan_vese(image, num_iter=35, init_level_set=init_ls,
                                     smoothing=15, iter_callback=callback)
        fig, axes =plt.subplots(figsize=(15,15)) #define figure points and axes.
        axes.imshow(image, cmap="gray")
        axes.set_axis_off()
        axes.contour(ls, [0.5], colors='r')
        name="snake.png"   
        plt.savefig(name)   
        plt.close()
        self.ss=QtGui.QPixmap(name) 
        self.ss = self.ss.scaled(self.pic_input.width(),self.pic_input.height(),Qt.KeepAspectRatio)
        ## this line allows the photo to be label size
        self.pic_output.setPixmap(self.ss)
        
        os.remove(name)
        self.outputcheck(True)
        
        

  
    def MOtsuThresholding(self,image):
        """! Making the edge section.
        @param image The file that comes this function as a path
        @param thresholds Applying multi-Otsu threshold for the default value, generating classes.
        @param regions Using the threshold values, we generate the three regions.
        
        
        """ 

        image = io.imread(self.path)
        thresholds = threshold_multiotsu(image, classes=5)
        regions = np.digitize(image, bins=thresholds)   
        output = img_as_ubyte(regions)
        ##Convert an image to unsigned byte format, with values in [0, 255].

        name="mot.png"
        plt.imsave("mot.png", output)
        self.copying(name)
         

    
 
    def  CVS(self,image):
        """! Making the edge section of Chan-Vese
        @param image The file that comes this function as a path
        @param cv The function for chan vese.
        @param cvs Functios' exact path to be opened directly
        
        
        """ 
        image = io.imread(self.path)
        cv = chan_vese(image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
               max_num_iter=200, dt=0.5, init_level_set="checkerboard",
               extended_output=True)#This algorithm is based on level sets that are evolved iteratively to minimize an energy
                
        cvs=cv[0] 
        ##making it np.array to be read by io functionalities
        name="cvs.png" 
        io.imsave('cvs.png', img_as_ubyte(cvs))
        self.copying(name)