"""
===========================
Object Oriented Lab Project
===========================


*In this project I've used some image sementation....... button implementation,
communating with classes and functualities are used.

Methods used in this Project:
#RGB to grayscale (converts a picture with RGB channels to a picture 
    with a single grayscale photo (2D))[1]

#RGB to HSV (Hue, Saturation, Value):
    Separating distinct colors (hues) and luminosities to different areas of the image.[2]
    
#Multi-Otsu Thresholding:
    It's used to divide an image's pixels into multiple different classes, each
    determined by the strength of the gray levels inside the image.[3]

#Chan-Vese Segmentation:
    The Chan-Vese segmentation algorithm is designed to segment objects without
    clearly defined boundaries in white.

#Morphological Snakes:
    Using morphological operators over a binary array, the standard approach for active contours.

#Edge Detections:
    In image processing, edge operators are employed in edge detection techniques.
    They're discrete differentiation operators that compute an approximation of the
    picture intensity function's gradient. The Scharr filter has a lower rotational 
    variance than the Sobel filter, which is superior than the Prewitt filter. [4][5][6]_.
    

****
Since I don't know whether you mean doxygen or report when you say 'add your new st uides' in Documentations,
 I wanted to put it here too, don't get me wrong sir.
 Differences after presentation After pressing save as, we can save the png file with the same extension by changing its name.
 Added save button for exit functionality. The save button in the exit menu works for output.
 After the presentation, I severely segmented the code and divided it into parts. I created a separate class from main for each function see in figure 6. I used lambda method to call specific function inside function.
****



[1] http://poynton.ca/PDFs/ColorFAQ.pdf
[2] https://en.wikipedia.org/wiki/HSL_and_HSV
[3] https://ftp.iis.sinica.edu.tw/JISE/2001/200109_01.pdf
[4] https://en.wikipedia.org/wiki/Sobel_operator#Alternative_operators
[5] B. Jaehne, H. Scharr, and S. Koerkel. Principles of filter design.
In Handbook of Computer Vision and Applications. Academic Press,1999.
[6] https://en.wikipedia.org/wiki/Prewitt_operator


"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QPixmap
import sys,os
from skimage import io
from skimage import img_as_ubyte
from edge_class import Edge
from segmentation_class import Segmentation
from conversion_class import Conversion
import numpy as np


class Ui_MainWindow(object):
    """! The Main class.
    """
    def setupUi(self, MainWindow):
        """! Main interface generating.
        and creating icons
        """

        MainWindow.setObjectName("OOP Lab Project")
        MainWindow.resize(1032, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico/newfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ico/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cvsi=QtGui.QIcon()
        cvsi.addPixmap(QtGui.QPixmap("ico/csv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ms = QtGui.QIcon()
        ms.addPixmap(QtGui.QPixmap("ico/mor2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        moti=QtGui.QIcon()
        moti.addPixmap(QtGui.QPixmap("ico/mot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        grayi=QtGui.QIcon()
        grayi.addPixmap(QtGui.QPixmap("ico/grayscale.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        redo=QtGui.QIcon()
        redo.addPixmap(QtGui.QPixmap("ico/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5=QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ico/exportas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4=QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ico/saveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ico/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3=QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ico/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        undo=QtGui.QIcon()
        undo.addPixmap(QtGui.QPixmap("ico/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hsvi=QtGui.QIcon()
        hsvi.addPixmap(QtGui.QPixmap("ico/hsv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconsch = QtGui.QIcon()
        iconsch.addPixmap(QtGui.QPixmap("ico/p.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconsch = QtGui.QIcon()
        iconsch.addPixmap(QtGui.QPixmap("ico/sc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconsobel = QtGui.QIcon()
        iconsobel.addPixmap(QtGui.QPixmap("ico/so.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.gSource = QtWidgets.QGroupBox(self.centralwidget)
        self.gSource.setObjectName("gSource")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.gSource)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_fOpen_Source = QtWidgets.QPushButton(self.gSource)
        self.button_fOpen_Source.setMaximumSize(QtCore.QSize(38, 33))
        self.button_fOpen_Source.setText("")
        self.button_fOpen_Source.setIcon(icon)
        self.button_fOpen_Source.setIconSize(QtCore.QSize(25, 25))
        self.button_fOpen_Source.setCheckable(False)
        self.button_fOpen_Source.setChecked(False)
        self.button_fOpen_Source.setAutoRepeat(False)
        self.button_fOpen_Source.setAutoExclusive(False)
        self.button_fOpen_Source.setAutoDefault(False)
        self.button_fOpen_Source.setObjectName("button_fOpen_Source")
        self.horizontalLayout_3.addWidget(self.button_fOpen_Source)
        self.button_Edit_Clear_Source = QtWidgets.QPushButton(self.gSource)
        self.button_Edit_Clear_Source.setEnabled(False)
        self.button_Edit_Clear_Source.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Edit_Clear_Source.setText("")
        self.button_Edit_Clear_Source.setIcon(icon1)
        self.button_Edit_Clear_Source.setIconSize(QtCore.QSize(25, 25))
        self.button_Edit_Clear_Source.setCheckable(False)
        self.button_Edit_Clear_Source.setObjectName("button_Edit_Clear_Source")
        self.horizontalLayout_3.addWidget(self.button_Edit_Clear_Source)
        self.button_fExport_As_Source = QtWidgets.QPushButton(self.gSource)
        self.button_fExport_As_Source.setEnabled(False)
        self.button_fExport_As_Source.setMaximumSize(QtCore.QSize(38, 33))
        self.button_fExport_As_Source.setText("")
        self.button_fExport_As_Source.setIcon(icon2)
        self.button_fExport_As_Source.setIconSize(QtCore.QSize(25, 25))
        self.button_fExport_As_Source.setCheckable(False)
        self.button_fExport_As_Source.setObjectName("button_fExport_As_Source")
        self.horizontalLayout_3.addWidget(self.button_fExport_As_Source)
        self.horizontalLayout_16.addWidget(self.gSource)
        self.gOutput = QtWidgets.QGroupBox(self.centralwidget)
        self.gOutput.setObjectName("gOutput")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.gOutput)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.button_file_save_output = QtWidgets.QPushButton(self.gOutput)
        self.button_file_save_output.setEnabled(False)
        self.button_file_save_output.setMaximumSize(QtCore.QSize(38, 33))
        self.button_file_save_output.setText("")
        self.button_file_save_output.setIcon(icon3)
        self.button_file_save_output.setIconSize(QtCore.QSize(25, 25))
        self.button_file_save_output.setCheckable(False)
        self.button_file_save_output.setObjectName("button_file_save_output")
        self.horizontalLayout_11.addWidget(self.button_file_save_output)
        self.button_file_saveas_output = QtWidgets.QPushButton(self.gOutput)
        self.button_file_saveas_output.setEnabled(False)
        self.button_file_saveas_output.setMaximumSize(QtCore.QSize(38, 33))
        self.button_file_saveas_output.setText("")
        self.button_file_saveas_output.setIcon(icon4)
        self.button_file_saveas_output.setIconSize(QtCore.QSize(25, 25))
        self.button_file_saveas_output.setCheckable(False)
        self.button_file_saveas_output.setObjectName("button_file_saveas_output")
        self.horizontalLayout_11.addWidget(self.button_file_saveas_output)
        self.button_file_exportas_output = QtWidgets.QPushButton(self.gOutput)
        self.button_file_exportas_output.setEnabled(False)
        self.button_file_exportas_output.setMaximumSize(QtCore.QSize(38, 33))
        self.button_file_exportas_output.setText("")
        self.button_file_exportas_output.setIcon(icon5)
        self.button_file_exportas_output.setIconSize(QtCore.QSize(25, 25))
        self.button_file_exportas_output.setCheckable(False)
        self.button_file_exportas_output.setObjectName("button_file_exportas_output")
        self.horizontalLayout_11.addWidget(self.button_file_exportas_output)
        self.button_Edit_Clear_output = QtWidgets.QPushButton(self.gOutput)
        self.button_Edit_Clear_output.setEnabled(False)
        self.button_Edit_Clear_output.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Edit_Clear_output.setText("")
        self.button_Edit_Clear_output.setIcon(icon1)
        self.button_Edit_Clear_output.setIconSize(QtCore.QSize(25, 25))
        self.button_Edit_Clear_output.setCheckable(False)
        self.button_Edit_Clear_output.setObjectName("button_Edit_Clear_output")
        self.horizontalLayout_11.addWidget(self.button_Edit_Clear_output)
        self.button_Edit_undo_output = QtWidgets.QPushButton(self.gOutput)
        self.button_Edit_undo_output.setEnabled(False)
        self.button_Edit_undo_output.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Edit_undo_output.setText("")
        self.button_Edit_undo_output.setIcon(undo)
        self.button_Edit_undo_output.setIconSize(QtCore.QSize(25, 25))
        self.button_Edit_undo_output.setCheckable(False)
        self.button_Edit_undo_output.setObjectName("button_Edit_undo_output")
        self.horizontalLayout_11.addWidget(self.button_Edit_undo_output)
        self.button_Edit_redo_output = QtWidgets.QPushButton(self.gOutput)
        self.button_Edit_redo_output.setEnabled(False)
        self.button_Edit_redo_output.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Edit_redo_output.setText("")
        self.button_Edit_redo_output.setIcon(redo)
        self.button_Edit_redo_output.setIconSize(QtCore.QSize(25, 25))
        self.button_Edit_redo_output.setCheckable(False)
        self.button_Edit_redo_output.setObjectName("button_Edit_redo_output")
        self.horizontalLayout_11.addWidget(self.button_Edit_redo_output)
        self.horizontalLayout_16.addWidget(self.gOutput)
        self.gConversion = QtWidgets.QGroupBox(self.centralwidget)
        self.gConversion.setObjectName("gConversion")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.gConversion)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.button_Conversion_RGB_to_Grayscale = QtWidgets.QPushButton(self.gConversion)
        self.button_Conversion_RGB_to_Grayscale.setEnabled(False)
        self.button_Conversion_RGB_to_Grayscale.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Conversion_RGB_to_Grayscale.setText("")
        self.button_Conversion_RGB_to_Grayscale.setIcon(grayi)
        self.button_Conversion_RGB_to_Grayscale.setIconSize(QtCore.QSize(25, 25))
        self.button_Conversion_RGB_to_Grayscale.setCheckable(False)
        self.button_Conversion_RGB_to_Grayscale.setObjectName("button_Conversion_RGB_to_Grayscale")
        self.horizontalLayout_22.addWidget(self.button_Conversion_RGB_to_Grayscale)
        self.button_Conversion_RGB_to_HSV = QtWidgets.QPushButton(self.gConversion)
        self.button_Conversion_RGB_to_HSV.setEnabled(False)
        self.button_Conversion_RGB_to_HSV.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Conversion_RGB_to_HSV.setText("")
        self.button_Conversion_RGB_to_HSV.setIcon(hsvi)
        self.button_Conversion_RGB_to_HSV.setIconSize(QtCore.QSize(25, 25))
        self.button_Conversion_RGB_to_HSV.setCheckable(False)
        self.button_Conversion_RGB_to_HSV.setObjectName("button_Conversion_RGB_to_HSV")
        self.horizontalLayout_22.addWidget(self.button_Conversion_RGB_to_HSV)
        self.horizontalLayout_16.addWidget(self.gConversion)
        self.gSegmentation = QtWidgets.QGroupBox(self.centralwidget)
        self.gSegmentation.setObjectName("gSegmentation")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.gSegmentation)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.button_Segmentation_MOT = QtWidgets.QPushButton(self.gSegmentation)
        self.button_Segmentation_MOT.setEnabled(False)
        self.button_Segmentation_MOT.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Segmentation_MOT.setText("")
        self.button_Segmentation_MOT.setIcon(moti)
        self.button_Segmentation_MOT.setIconSize(QtCore.QSize(25, 25))
        self.button_Segmentation_MOT.setCheckable(False)
        self.button_Segmentation_MOT.setObjectName("button_Segmentation_MOT")
        self.horizontalLayout_10.addWidget(self.button_Segmentation_MOT)
        self.button_Segmentation_MS = QtWidgets.QPushButton(self.gSegmentation)
        self.button_Segmentation_MS.setEnabled(False)
        self.button_Segmentation_MS.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Segmentation_MS.setText("")
        self.button_Segmentation_MS.setIcon(ms)
        self.button_Segmentation_MS.setIconSize(QtCore.QSize(25, 25))
        self.button_Segmentation_MS.setCheckable(False)
        self.button_Segmentation_MS.setChecked(False)
        self.button_Segmentation_MS.setAutoRepeat(False)
        self.button_Segmentation_MS.setAutoExclusive(False)
        self.button_Segmentation_MS.setAutoDefault(False)
        self.button_Segmentation_MS.setObjectName("button_Segmentation_MS")
        self.horizontalLayout_10.addWidget(self.button_Segmentation_MS)
        self.button_Segmentation_CVS = QtWidgets.QPushButton(self.gSegmentation)
        self.button_Segmentation_CVS.setEnabled(False)
        self.button_Segmentation_CVS.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Segmentation_CVS.setText("")
        self.button_Segmentation_CVS.setIcon(cvsi)
        self.button_Segmentation_CVS.setIconSize(QtCore.QSize(25, 25))
        self.button_Segmentation_CVS.setCheckable(False)
        self.button_Segmentation_CVS.setObjectName("button_Segmentation_CVS")
        self.horizontalLayout_10.addWidget(self.button_Segmentation_CVS)
        self.horizontalLayout_16.addWidget(self.gSegmentation)
        self.gEdge_Detection = QtWidgets.QGroupBox(self.centralwidget)
        self.gEdge_Detection.setObjectName("gEdge_Detection")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.gEdge_Detection)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_Edge_Detection_Robert = QtWidgets.QPushButton(self.gEdge_Detection)
        self.button_Edge_Detection_Robert.setEnabled(False)
        self.button_Edge_Detection_Robert.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Edge_Detection_Robert.setText("")
        self.button_Edge_Detection_Robert.setIcon(icon1)
        self.button_Edge_Detection_Robert.setIconSize(QtCore.QSize(25, 25))
        self.button_Edge_Detection_Robert.setCheckable(False)
        self.button_Edge_Detection_Robert.setObjectName("button_Edge_Detection_Robert")
        self.horizontalLayout_9.addWidget(self.button_Edge_Detection_Robert)
        self.button_Edge_Detection_Sobel = QtWidgets.QPushButton(self.gEdge_Detection)
        self.button_Edge_Detection_Sobel.setEnabled(False)
        self.button_Edge_Detection_Sobel.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Edge_Detection_Sobel.setText("")
        self.button_Edge_Detection_Sobel.setIcon(icon1)
        self.button_Edge_Detection_Sobel.setIconSize(QtCore.QSize(25, 25))
        self.button_Edge_Detection_Sobel.setCheckable(False)
        self.button_Edge_Detection_Sobel.setObjectName("button_Edge_Detection_Sobel")
        self.horizontalLayout_9.addWidget(self.button_Edge_Detection_Sobel)
        self.button_Edge_Detection_Scharr = QtWidgets.QPushButton(self.gEdge_Detection)
        self.button_Edge_Detection_Scharr.setEnabled(False)
        self.button_Edge_Detection_Scharr.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Edge_Detection_Scharr.setText("")
        self.button_Edge_Detection_Scharr.setIcon(icon1)
        self.button_Edge_Detection_Scharr.setIconSize(QtCore.QSize(25, 25))
        self.button_Edge_Detection_Scharr.setCheckable(False)
        self.button_Edge_Detection_Scharr.setObjectName("button_Edge_Detection_Scharr")
        self.horizontalLayout_9.addWidget(self.button_Edge_Detection_Scharr)
        self.button_Edge_Detection_Prewitt = QtWidgets.QPushButton(self.gEdge_Detection)
        self.button_Edge_Detection_Prewitt.setEnabled(False)
        self.button_Edge_Detection_Prewitt.setMaximumSize(QtCore.QSize(38, 33))
        self.button_Edge_Detection_Prewitt.setText("")
        self.button_Edge_Detection_Prewitt.setIcon(icon2)
        self.button_Edge_Detection_Prewitt.setIconSize(QtCore.QSize(25, 25))
        self.button_Edge_Detection_Prewitt.setCheckable(False)
        self.button_Edge_Detection_Prewitt.setObjectName("button_Edge_Detection_Prewitt")
        self.horizontalLayout_9.addWidget(self.button_Edge_Detection_Prewitt)
        self.horizontalLayout_16.addWidget(self.gEdge_Detection)
        self.gridLayout_4.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.gphoto1 = QtWidgets.QGroupBox(self.centralwidget)
        self.gphoto1.setTitle("")
        self.gphoto1.setObjectName("gphoto1")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.gphoto1)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pic_input = QtWidgets.QLabel(self.gphoto1)
        self.pic_input.setText("")
        self.pic_input.setObjectName("pic_input")
        self.horizontalLayout_20.addWidget(self.pic_input)
        
        self.horizontalLayout_19.addWidget(self.gphoto1)
        self.gphoto2 = QtWidgets.QGroupBox(self.centralwidget)
        self.gphoto2.setTitle("")
        self.gphoto2.setObjectName("gphoto2")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.gphoto2)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pic_output = QtWidgets.QLabel(self.gphoto2)
        self.pic_output.setText("")
        self.pic_output.setObjectName("pic_output")
        self.horizontalLayout_21.addWidget(self.pic_output)
        self.horizontalLayout_19.addWidget(self.gphoto2)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        self.gridLayout_4.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_4.setRowStretch(0, 3)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 19)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_As = QtWidgets.QMenu(self.menuFile)
        self.menuExport_As.setEnabled(True)
        self.menuExport_As.setObjectName("menuExport_As")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setEnabled(False)
        self.menuEdit.setObjectName("menuEdit")
        self.eClear = QtWidgets.QMenu(self.menuEdit)
        self.eClear.setObjectName("eClear")
        self.menuConversion = QtWidgets.QMenu(self.menubar)
        self.menuConversion.setEnabled(False)
        self.menuConversion.setObjectName("menuConversion")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setEnabled(False)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setEnabled(False)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fOpen_Source = QtWidgets.QAction(MainWindow)
        self.fOpen_Source.setCheckable(False)
        self.fOpen_Source.setObjectName("fOpen_Source")
        self.fSave_Output = QtWidgets.QAction(MainWindow)
        self.fSave_Output.setCheckable(False)
        self.fSave_Output.setEnabled(False)
        self.fSave_Output.setObjectName("fSave_Output")
        self.fSave_As_Output = QtWidgets.QAction(MainWindow)
        self.fSave_As_Output.setCheckable(False)
        self.fSave_As_Output.setEnabled(False)
        self.fSave_As_Output.setObjectName("fSave_As_Output")
        self.fExportasSource = QtWidgets.QAction(MainWindow)
        self.fExportasSource.setEnabled(False)
        self.fExportasSource.setObjectName("fExportasSource")
        self.fExportasOutput = QtWidgets.QAction(MainWindow)
        self.fExportasOutput.setEnabled(False)
        self.fExportasOutput.setObjectName("fExportasOutput")
        self.fExit = QtWidgets.QAction(MainWindow)
        self.fExit.setObjectName("fExit")
        self.eUndo_Output = QtWidgets.QAction(MainWindow)
        self.eUndo_Output.setObjectName("eUndo_Output")
        self.eReundo_Output = QtWidgets.QAction(MainWindow)
        self.eReundo_Output.setObjectName("eReundo_Output")
        self.eSource = QtWidgets.QAction(MainWindow)
        self.eSource.setObjectName("eSource")
        self.eOutput = QtWidgets.QAction(MainWindow)
        self.eOutput.setObjectName("eOutput")
        self.cRGB_to_GrayScale = QtWidgets.QAction(MainWindow)
        self.cRGB_to_GrayScale.setObjectName("cRGB_to_GrayScale")
        self.cRGB_to_HSV = QtWidgets.QAction(MainWindow)
        self.cRGB_to_HSV.setObjectName("cRGB_to_HSV")
        self.sMulti_Otsu_Thresholding = QtWidgets.QAction(MainWindow)
        self.sMulti_Otsu_Thresholding.setObjectName("sMulti_Otsu_Thresholding")
        self.sMorphological_Snakes = QtWidgets.QAction(MainWindow)
        self.sMorphological_Snakes.setObjectName("sMorphological_Snakes")
        self.sChan_Vese_Segmentation = QtWidgets.QAction(MainWindow)
        self.sChan_Vese_Segmentation.setObjectName("sChan_Vese_Segmentation")
        self.edRoberts = QtWidgets.QAction(MainWindow)
        self.edRoberts.setObjectName("edRoberts")
        iconrobert = QtGui.QIcon()
        iconrobert.addPixmap(QtGui.QPixmap("ico/R.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_Edge_Detection_Robert.setIcon(iconrobert)
        self.button_Edge_Detection_Robert.setIconSize(QtCore.QSize(30, 30))
        self.button_Edge_Detection_Robert.setCheckable(False)
        self.button_Edge_Detection_Robert.setChecked(False)
        self.button_Edge_Detection_Robert.setAutoRepeat(False)
        self.button_Edge_Detection_Robert.setAutoExclusive(False)
        self.button_Edge_Detection_Robert.setAutoDefault(False)     
        self.edSobel = QtWidgets.QAction(MainWindow)
        self.edSobel.setObjectName("edSobel")
        self.button_Edge_Detection_Sobel.setIcon(iconsobel)
        self.button_Edge_Detection_Sobel.setIconSize(QtCore.QSize(25, 25))
        self.edScharr = QtWidgets.QAction(MainWindow)
        self.edScharr.setObjectName("edScharr")
        self.button_Edge_Detection_Scharr.setIcon(iconsch)
        self.button_Edge_Detection_Scharr.setIconSize(QtCore.QSize(35, 35))   
        self.edPrewitt = QtWidgets.QAction(MainWindow)
        self.edPrewitt.setObjectName("edPrewitt")
        self.button_Edge_Detection_Prewitt.setIcon(iconsch)
        self.button_Edge_Detection_Prewitt.setIconSize(QtCore.QSize(25, 25))
        self.menuExport_As.addAction(self.fExportasSource)
        self.menuExport_As.addAction(self.fExportasOutput)
        self.menuFile.addAction(self.fOpen_Source)
        self.menuFile.addAction(self.fSave_Output)
        self.menuFile.addAction(self.fSave_As_Output)
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addAction(self.fExit)
        self.eClear.addAction(self.eSource)
        self.eClear.addAction(self.eOutput)
        self.menuEdit.addAction(self.eClear.menuAction())
        self.menuEdit.addAction(self.eUndo_Output)
        self.menuEdit.addAction(self.eReundo_Output)
        self.menuConversion.addAction(self.cRGB_to_GrayScale)
        self.menuConversion.addAction(self.cRGB_to_HSV)
        self.menuSegmentation.addAction(self.sMulti_Otsu_Thresholding)
        self.menuSegmentation.addAction(self.sChan_Vese_Segmentation)
        self.menuSegmentation.addAction(self.sMorphological_Snakes)
        self.menuEdge_Detection.addAction(self.edRoberts)
        self.menuEdge_Detection.addAction(self.edSobel)
        self.menuEdge_Detection.addAction(self.edScharr)
        self.menuEdge_Detection.addAction(self.edPrewitt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConversion.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.button_fOpen_Source, self.button_fExport_As_Source)
        MainWindow.setTabOrder(self.button_fExport_As_Source, self.button_file_save_output)
        MainWindow.setTabOrder(self.button_file_save_output, self.button_file_saveas_output)
        MainWindow.setTabOrder(self.button_file_saveas_output, self.button_file_exportas_output)
        MainWindow.setTabOrder(self.button_file_exportas_output, self.button_Edit_Clear_output)
        MainWindow.setTabOrder(self.button_Edit_Clear_output, self.button_Edit_undo_output)
        MainWindow.setTabOrder(self.button_Edit_undo_output, self.button_Edit_redo_output)
        MainWindow.setTabOrder(self.button_Edit_redo_output, self.button_Conversion_RGB_to_Grayscale)
        MainWindow.setTabOrder(self.button_Conversion_RGB_to_Grayscale, self.button_Conversion_RGB_to_HSV)
        MainWindow.setTabOrder(self.button_Conversion_RGB_to_HSV, self.button_Segmentation_MOT)
        MainWindow.setTabOrder(self.button_Segmentation_MOT, self.button_Segmentation_MS)
        MainWindow.setTabOrder(self.button_Segmentation_MS, self.button_Segmentation_CVS)
        MainWindow.setTabOrder(self.button_Segmentation_CVS, self.button_Edge_Detection_Robert)
        MainWindow.setTabOrder(self.button_Edge_Detection_Robert, self.button_Edge_Detection_Sobel)
        MainWindow.setTabOrder(self.button_Edge_Detection_Sobel, self.button_Edge_Detection_Scharr)
        MainWindow.setTabOrder(self.button_Edge_Detection_Scharr, self.button_Edge_Detection_Prewitt)


        
    

    def retranslateUi(self, MainWindow):
        """! The button base functualities.
        Defines the functions utilized by all button.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OOP Lab Project"))
        self.gSource.setTitle(_translate("MainWindow", "Source"))
        self.gOutput.setTitle(_translate("MainWindow", "Output"))
        self.gConversion.setTitle(_translate("MainWindow", "Conversion"))
        self.gSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.gEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_As.setTitle(_translate("MainWindow", "Export As"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.eClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuConversion.setTitle(_translate("MainWindow", "Conversion"))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.fOpen_Source.setText(_translate("MainWindow", "Open Source"))
        self.fOpen_Source.setShortcut(_translate("MainWindow", "F5"))
        
        self.fSave_Output.setText(_translate("MainWindow", "Save Output"))
        self.fSave_Output.setShortcut(_translate("MainWindow", "Ctrl+S"))
        
        self.fSave_As_Output.setText(_translate("MainWindow", "Save As Output"))
        self.fSave_As_Output.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        
        self.fExportasSource.setText(_translate("MainWindow", "Source"))
        self.fExportasSource.setShortcut(_translate("MainWindow", "Ctrl+Alt+ß"))
        
        self.fExportasOutput.setText(_translate("MainWindow", "Output"))
        self.fExportasOutput.setShortcut(_translate("MainWindow", "Ctrl+Alt+O"))
        
        self.fExit.setText(_translate("MainWindow", "Exit"))
        self.fExit.setShortcut(_translate("MainWindow", "Del"))
        
        self.eUndo_Output.setText(_translate("MainWindow", "Undo Output"))
        self.eUndo_Output.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        
        self.eReundo_Output.setText(_translate("MainWindow", "Redo Output"))
        self.eReundo_Output.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        
        self.eSource.setText(_translate("MainWindow", "Source"))
        self.eSource.setShortcut(_translate("MainWindow", "Ctrl+R"))
        
        self.eOutput.setText(_translate("MainWindow", "Output"))
        self.eOutput.setShortcut(_translate("MainWindow", "Ctrl+T"))
        
        self.cRGB_to_GrayScale.setText(_translate("MainWindow", "RGB to GrayScale"))
        self.cRGB_to_GrayScale.setShortcut(_translate("MainWindow", "Ctrl+1"))
        
        self.cRGB_to_HSV.setText(_translate("MainWindow", "RGB to HSV"))
        self.cRGB_to_HSV.setShortcut(_translate("MainWindow", "Ctrl+2"))
        
        self.sMulti_Otsu_Thresholding.setText(_translate("MainWindow", "Multi-Otsu Thresholding"))
        self.sMulti_Otsu_Thresholding.setShortcut(_translate("MainWindow", "Ctrl+^"))
        
        self.sMorphological_Snakes.setText(_translate("MainWindow", "Morphological Snakes"))
        self.sMorphological_Snakes.setShortcut(_translate("MainWindow", "Ctrl+4"))
        
        self.sChan_Vese_Segmentation.setText(_translate("MainWindow", "Chan-Vese Segmentation"))
        self.sChan_Vese_Segmentation.setShortcut(_translate("MainWindow", "Ctrl+5"))
        
        self.edRoberts.setText(_translate("MainWindow", "Roberts"))
        self.edRoberts.setShortcut(_translate("MainWindow", "Ctrl+F1"))
        
        self.edSobel.setText(_translate("MainWindow", "Sobel"))
        self.edSobel.setShortcut(_translate("MainWindow", "Ctrl+F2"))
        
        self.edScharr.setText(_translate("MainWindow", "Scharr"))
        self.edScharr.setShortcut(_translate("MainWindow", "Ctrl+F3"))
        
        self.edPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.edPrewitt.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        
        
        
        self.button_fOpen_Source.setToolTip(_translate("MainWindow", "Open a File"))
        self.button_Conversion_RGB_to_Grayscale.setToolTip(_translate("MainWindow", "Click to convert RGB to Grayscale"))
        self.button_Conversion_RGB_to_HSV.setToolTip(_translate("MainWindow", "Click to convert RGB to HSV"))
        self.button_Edge_Detection_Prewitt.setToolTip(_translate("MainWindow", "Click to detect edge Prewitt"))
        self.button_Edge_Detection_Robert.setToolTip(_translate("MainWindow", "Click to detect edge Robert"))
        self.button_Edge_Detection_Scharr.setToolTip(_translate("MainWindow", "Click to detect edge Scharr"))
        self.button_Edge_Detection_Sobel.setToolTip(_translate("MainWindow", "Click to detect edge Sobell"))
        self.button_Edit_Clear_Source.setToolTip(_translate("MainWindow", "Click to clear source"))
        self.button_Edit_Clear_output.setToolTip(_translate("MainWindow", "Click to clear output"))
        self.button_Edit_undo_output.setToolTip(_translate("MainWindow", "Click to undo output"))
        self.button_Edit_redo_output.setToolTip(_translate("MainWindow", "Click to redo output"))
        self.button_Segmentation_CVS.setToolTip(_translate("MainWindow", "Click to segmentation Chan-Vese Segmentation"))
        self.button_Segmentation_MOT.setToolTip(_translate("MainWindow", "Click to segmentation Multi-Otsu Thresholding"))
        self.button_Segmentation_MS.setToolTip(_translate("MainWindow", "Click to segmentation Morphological Snake"))
        self.button_fExport_As_Source.setToolTip(_translate("MainWindow", "Click to export as source"))
        self.button_file_exportas_output.setToolTip(_translate("MainWindow", "Click to export as output"))
        self.button_file_save_output.setToolTip(_translate("MainWindow", "Click to save output"))
        self.button_file_saveas_output.setToolTip(_translate("MainWindow", "Click to save as output"))
        

        self.fOpen_Source.triggered.connect(self.choosefile)
        self.button_fOpen_Source.clicked.connect(self.choosefile)
 
        self.button_file_save_output.clicked.connect(self.saveoutput)
        self.fSave_Output.triggered.connect(self.saveoutput)
        
        self.button_file_saveas_output.clicked.connect(self.saveas)
        self.fSave_As_Output.triggered.connect(self.saveas)
        
        self.button_file_exportas_output.clicked.connect(self.export)
        self.menuExport_As.triggered.connect(self.export)
        
        self.button_Edit_Clear_Source.clicked.connect(self.clearsource)        
        self.eSource.triggered.connect(self.clearsource)
            
        self.button_Edit_Clear_output.clicked.connect(self.clearoutput)
        self.eOutput.triggered.connect(self.clearoutput)
        
        self.button_Conversion_RGB_to_Grayscale.clicked.connect(lambda: self.conversion("gray"))
        self.cRGB_to_GrayScale.triggered.connect(lambda: self.conversion("gray"))
        self.button_Conversion_RGB_to_HSV.clicked.connect(lambda: self.conversion("hsv"))
        self.cRGB_to_HSV.triggered.connect(lambda: self.conversion("hsv"))
        
        self.button_Edge_Detection_Prewitt.clicked.connect(lambda: self.edgedetection("prewitt"))
        self.button_Edge_Detection_Prewitt.clicked.connect(lambda: self.edgedetection("prewitt"))
        self.button_Edge_Detection_Robert.clicked.connect(lambda: self.edgedetection("robert"))
        self.edRoberts.triggered.connect(lambda: self.edgedetection("robert"))
        self.button_Edge_Detection_Sobel.clicked.connect(lambda: self.edgedetection("sobel"))
        self.edSobel.triggered.connect(lambda: self.edgedetection("sobel"))
        self.button_Edge_Detection_Scharr.clicked.connect(lambda: self.edgedetection("scharr"))
        self.edScharr.triggered.connect(lambda: self.edgedetection("scharr"))
        
        self.button_Segmentation_MOT.clicked.connect(lambda: self.segmentation("mt"))
        self.sMulti_Otsu_Thresholding.triggered.connect(lambda: self.segmentation("mt"))
        self.button_Segmentation_CVS.clicked.connect(lambda: self.segmentation("cvs"))
        self.sChan_Vese_Segmentation.triggered.connect(lambda: self.segmentation("cvs"))
        self.button_Segmentation_MS.clicked.connect(lambda: self.segmentation("ms"))
        self.sMorphological_Snakes.triggered.connect(lambda: self.segmentation("ms"))

        self.fExit.triggered.connect(self.closeevent)
        

    def segmentation(self,s):
        """! Segmentation functualities
        @param s   The parameter that brings the function exactly which button is activated by triggering
        
        this function can apply image a multi-otsu thresholding,Chan-vese,and morphological snake segmentations.
        """
        if s=="ms":
            Segmentation.MS(self,self.path)
        elif s=="cvs":
            Segmentation.CVS(self, self.path)
        elif s=="mt":
            Segmentation.MOtsuThresholding(self, self.path)
    
    def edgedetection(self,ed):
        """! The edgedetection  functualities.
        @param ed   The parameter that brings the function exactly which button is activated by triggering
        
        this function can apply image a robert, sobell,scharr,and prewitt edge detections.
        """
        if ed=="prewitt":
            Edge.prewitt(self,self.path)
        elif ed=="scharr":
            Edge.scharr(self,self.path)
        elif ed=="sobel":
            Edge.sobel(self,self.path)
        elif ed=="robert":
            Edge.robert(self,self.path)

    def conversion(self,cvs):
        """! The conversion functualities.
        @param cvs   The parameter that brings the function exactly which button is activated by triggering
        
        this function can make the image gray and hsv
        """
        
        if cvs=="gray":
            Conversion.conversiongray(self,self.path)
        elif cvs=="hsv":
            Conversion.conversionhsv(self, self.path)
            
            
            
    def choosefile(self):
        """! To open a file and choosing exact files.
        @param self.filename   Takes the path of the chosen file
       
        
        this function can apply image a robert, sobell,scharr,and prewitt edge detections.
        """

        self.filename = QFileDialog.getOpenFileName(filter="jpg & png files (*.jpg *.png)")
        self.clearoutput()
        ## Clearing output unit.
        self.path = self.filename[0]
        self.foti = QPixmap(self.path)
        if self.filename != ('', ''):
            self.pic_input.setPixmap(self.foti)
            self.enabling(True)
        else:
            print("Choose an image!!")



    def closeevent(self):
        """! Closing the executed system.
        If close button pressed, ask the user to really want to exit.
        """

        ret = QMessageBox.question(MainWindow, 'Quit form', " You really want to quit?", QMessageBox.Yes | QMessageBox.Cancel |QMessageBox.Save, QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
        
            MainWindow.close()
        elif ret==QMessageBox.Cancel:
            pass
        elif ret==QMessageBox.Save:
            self.saveoutput()
        
        
        
    def store_evolution_in(self,lst):#Store function for Morphological Snakes
        """! Returns a callback function to keep track of the changes to the level sets
        in the given list.
        """
    
        def _store(x):
            lst.append(np.copy(x))
    
        return _store

        

    def output(self,isim,name):  
        """! Saves the photo to read later.
        This function saves Edge detectioned pictures to use later in output.
        Function calls the copying functions.
        """
        io.imsave(isim, img_as_ubyte(name))
        name=str(isim)
        self.copying(name)


        
    def clearoutput(self):
        """! Clearing the output section.
        It just clears the output label.
        
        """
        self.pic_output.clear()
        self.outputcheck(False)
        
        
   
    def clearsource(self):
        """! Clearing the source section.
        It clears the input label. Also
            
        """
        
        
        self.pic_input.clear()
        self.clearoutput()
        self.path=("") #bunu yapmamın sebebi clear diyip ekran gittikten sonra, conversion edge detection gibi
                                # fonksiyonlara basınca, önceki path'i algılayıp input olmadan output veriyor !!
        self.enabling(False)
        
        
        
    def export(self):
        """! Export the output function.
        You can change the extension and save somewhere else
        """
        self.option=QFileDialog.Options()
        if self.path.endswith(".png"):
            # extension=".png"
            self.file=QFileDialog.getSaveFileName(self.centralwidget,"Save As..","","All Files except png (\n *.jpg \n *.pdf \n *.csv) ",options=self.option)
        elif self.path.endswith(".jpg"):
            # extension=".jpg"
            self.file=QFileDialog.getSaveFileName(self.centralwidget,"Save As..","","All Files except png (\n *.png \n *.pdf \n *.csv) ",options=self.option)
        
        self.filesave = self.file[0]
        image=Image.fromqimage(self.pic_output.pixmap())
        image.save(self.filesave)



    def saveas(self):
        """!Save as function.
        You can change extension of an image as saving, png to jpg or jpg to png
        
        """
       
        self.option=QFileDialog.Options()

        if self.path.endswith(".png"):
            # extension=".png"
            self.file=QFileDialog.getSaveFileName(self.centralwidget,"Save As..","","png Files (*.png)",options=self.option)
        elif self.path.endswith(".jpg"):
            # extension=".jpg"
            self.file=QFileDialog.getSaveFileName(self.centralwidget,"Save As..","","jpg Files (*.jpg)",options=self.option)

        self.filesave = self.file[0]

        image=Image.fromqimage(self.pic_output.pixmap())
        image.save(self.filesave)



    def saveoutput(self):
        """!Save output function.
        @param image saves the output image
        
        """
        image=Image.fromqimage(self.pic_output.pixmap())
        image.save(self.path)
       

        
    def copying(self,n):
        """! This function is much used.
        So its basic goal is making image from the path and
        remove it from data.
        @param n has the path of the photo
        
        """
        self.ss=QtGui.QPixmap(n) 
        self.pic_output.setPixmap(self.ss)
        ## Removes the picture from data
        os.remove(n)
        self.outputcheck(True)
         
        
    
    def outputcheck(self,flag):
        """! This function is called after an image 
        operation happens.
        
        """
        self.button_file_save_output.setEnabled(flag)
        self.button_file_saveas_output.setEnabled(flag)
        self.button_file_exportas_output.setEnabled(flag)
        self.button_Edit_Clear_output.setEnabled(flag)
        self.button_Edit_redo_output.setEnabled(flag)
        self.button_Edit_undo_output.setEnabled(flag)
        self.menuEdit.setEnabled(flag)
        self.fSave_Output.setEnabled(flag)
        self.fSave_As_Output.setEnabled(flag)



    def enabling(self,check):
        """! enabling variables after loading a picture 
        fron open source
        
        """
        self.menuConversion.setEnabled(check)
        self.menuSegmentation.setEnabled(check)
        self.menuEdge_Detection.setEnabled(check)
        self.fExportasSource.setEnabled(check)
        self.button_Conversion_RGB_to_Grayscale.setEnabled(check)
        self.button_Conversion_RGB_to_HSV.setEnabled(check)
        self.button_Edge_Detection_Prewitt.setEnabled(check)
        self.button_Edge_Detection_Robert.setEnabled(check)
        self.button_Edge_Detection_Scharr.setEnabled(check)
        self.button_Edge_Detection_Sobel.setEnabled(check)
        self.button_Segmentation_CVS.setEnabled(check)
        self.button_Segmentation_MOT.setEnabled(check)
        self.button_Segmentation_MS.setEnabled(check)
        self.button_fExport_As_Source.setEnabled(check)
        self.button_Edit_Clear_Source.setEnabled(check)
        
        

        
        
        
        
        
        
        



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())