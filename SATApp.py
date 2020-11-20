from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets, QtGui
import sys
import os
from os import path
import webbrowser
from PyQt5.QtWidgets import QMessageBox
import resource_rc
#######################################################################################################

marks = 0
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('sat (1).ui', self)
        self.setup_ui()
        self.show()
        self.pdf_buttons ()
    
#######################################################################################################
        
    def setup_ui (self):
        self.setWindowTitle ('SAT App')
        self.setFixedSize(1279, 591)
        
#######################################################################################################
        
    def pdf_buttons (self):
        self.pushButton_9.clicked.connect(self.book1)
        self.pushButton_10.clicked.connect(self.book2)
        self.pushButton_12.clicked.connect(self.book4)
        self.pushButton_13.clicked.connect(self.book5)
        self.pushButton_15.clicked.connect(self.book7)
        self.pushButton_17.clicked.connect(self.book8)
        self.pushButton_18.clicked.connect(self.book9)
        self.pushButton_19.clicked.connect(self.book10)
        self.pushButton_14.clicked.connect(self.book11)
        self.pushButton_85.clicked.connect(self.book12)
        self.pushButton_6.clicked.connect(self.writebut1)
        self.pushButton_8.clicked.connect(self.writebut2)
        self.pushButton_16.clicked.connect(self.writebut3)
        self.pushButton_21.clicked.connect(self.writebut4)
        self.pushButton_22.clicked.connect(self.writebut5)
        self.pushButton_23.clicked.connect(self.writebut6)
        self.pushButton_25.clicked.connect(self.writebut7)
        self.pushButton_26.clicked.connect(self.writebut8)
        self.pushButton_27.clicked.connect(self.writebut9)
        self.pushButton_28.clicked.connect(self.writebut10)
        self.pushButton_29.clicked.connect(self.writebut11)
        self.pushButton_30.clicked.connect(self.writebut12)
        self.pushButton_31.clicked.connect(self.writebut13)
        self.pushButton_33.clicked.connect(self.writebut14)
        self.pushButton_34.clicked.connect(self.writebut15)
        self.pushButton_35.clicked.connect(self.writebut16)
        self.pushButton_36.clicked.connect(self.writebut17)
        self.pushButton_37.clicked.connect(self.writebut18)
        self.pushButton_38.clicked.connect(self.writebut19) 
        self.pushButton_39.clicked.connect(self.writebut20) 
        self.pushButton_20.clicked.connect(self.readbut1) 
        self.pushButton_32.clicked.connect(self.readbut2)
        self.pushButton_40.clicked.connect(self.readbut3)
        self.pushButton_41.clicked.connect(self.readbut4)
        self.pushButton_42.clicked.connect(self.readbut5)
        self.pushButton_44.clicked.connect(self.readbut6)
        self.pushButton_45.clicked.connect(self.readbut7)
        self.pushButton_46.clicked.connect(self.readbut8)
        self.pushButton_48.clicked.connect(self.readbut9)
        self.pushButton_49.clicked.connect(self.readbut10)
        self.pushButton_50.clicked.connect(self.readbut11)
        self.pushButton_51.clicked.connect(self.readbut12)
        self.pushButton_52.clicked.connect(self.readbut13)
        self.pushButton_53.clicked.connect(self.readbut14)
        self.pushButton_54.clicked.connect(self.readbut15)
        self.pushButton_55.clicked.connect(self.readbut16)
        self.pushButton_56.clicked.connect(self.readbut17)
        self.pushButton_57.clicked.connect(self.readbut18)
        self.pushButton_58.clicked.connect(self.readbut19)
        self.pushButton_59.clicked.connect(self.readbut20)
        self.pushButton_60.clicked.connect(self.test1read1)
        self.pushButton_61.clicked.connect(self.test1read2)
        self.pushButton_62.clicked.connect(self.test1read3)
        self.pushButton_63.clicked.connect(self.test1read4)
        self.pushButton_64.clicked.connect(self.test1read5)
        self.pushButton_43.clicked.connect(self.test1write1)
        self.pushButton_47.clicked.connect(self.test1write2)
        self.pushButton_65.clicked.connect(self.test1write3)
        self.pushButton_66.clicked.connect(self.test1write4)
        self.pushButton_98.clicked.connect(self.test2read1)
        self.pushButton_99.clicked.connect(self.test2read2)
        self.pushButton_100.clicked.connect(self.test2read3)
        self.pushButton_101.clicked.connect(self.test2read4)
        self.pushButton_102.clicked.connect(self.test2read5)
        self.pushButton_103.clicked.connect(self.test2write1)
        self.pushButton_104.clicked.connect(self.test2write2)
        self.pushButton_105.clicked.connect(self.test2write3)
        self.pushButton_106.clicked.connect(self.test2write4)
        self.pushButton_67.clicked.connect(self.test1mathnocalc)
        self.pushButton_74.clicked.connect(self.test1mathcalc1)
        self.pushButton_75.clicked.connect(self.test1mathcalc2) 
        self.pushButton_76.clicked.connect(self.test1mathcalc3)
        self.pushButton_112.clicked.connect(self.test2mathnocalc)
        self.pushButton_109.clicked.connect(self.test2mathcalc)
        self.pushButton_110.clicked.connect(self.test2mathcalc2) 
        self.pushButton_70.clicked.connect(self.test3read1) 
        self.pushButton_77.clicked.connect(self.test3read2) 
        self.pushButton_81.clicked.connect(self.test3read3)
        self.pushButton_113.clicked.connect(self.test3read4)
        self.pushButton_114.clicked.connect(self.test3read5)
        self.pushButton_86.clicked.connect(self.test3write1)
        self.pushButton_87.clicked.connect(self.test3write2)
        self.pushButton_88.clicked.connect(self.test3write3)
        self.pushButton_89.clicked.connect(self.test3write4)
        self.pushButton_92.clicked.connect(self.test3mathnocalc)
        self.pushButton_96.clicked.connect(self.test3mathcalc)
        self.pushButton_97.clicked.connect(self.test3mathcalc2)
        self.pushButton_111.clicked.connect(self.test3mathcalc3)
        self.pushButton_1117.clicked.connect(self.mathnocalc)
        self.pushButton_1128.clicked.connect(self.mathnocalc2)
        self.pushButton_107.clicked.connect(self.test4read1)
        self.pushButton_108.clicked.connect(self.test4read2)
        self.pushButton_115.clicked.connect(self.test4read3)
        self.pushButton_116.clicked.connect(self.test4read4)
        self.pushButton_117.clicked.connect(self.test4read5)
        self.pushButton_118.clicked.connect(self.test4write1)
        self.pushButton_119.clicked.connect(self.test4write2)
        self.pushButton_120.clicked.connect(self.test4write3)
        self.pushButton_121.clicked.connect(self.test4write4)
        self.pushButton_127.clicked.connect(self.test5read1)
        self.pushButton_128.clicked.connect(self.test5read2)
        self.pushButton_129.clicked.connect(self.test5read3)
        self.pushButton_134.clicked.connect(self.test5read4)
        self.pushButton_135.clicked.connect(self.test5read5)
        self.pushButton_136.clicked.connect(self.test5write1)
        self.pushButton_137.clicked.connect(self.test5write2)
        self.pushButton_138.clicked.connect(self.test5write3)
        self.pushButton_139.clicked.connect(self.test5write4)
        self.pushButton_170.clicked.connect(self.test4mathnocalc)
        self.pushButton_148.clicked.connect(self.test4mathcalc)
        self.pushButton_172.clicked.connect(self.test4mathcalc2)
        self.pushButton_173.clicked.connect(self.test5mathnocalc)
        self.pushButton_174.clicked.connect(self.test5mathcalc)
        self.pushButton_176.clicked.connect(self.test5mathcalc2)
        self.pushButton_143.clicked.connect(self.test6read1)
        self.pushButton_144.clicked.connect(self.test6read2)
        self.pushButton_145.clicked.connect(self.test6read3)
        self.pushButton_146.clicked.connect(self.test6read4)
        self.pushButton_149.clicked.connect(self.test6read5)
        self.pushButton_150.clicked.connect(self.test6write1)
        self.pushButton_151.clicked.connect(self.test6write2)
        self.pushButton_152.clicked.connect(self.test6write3)
        self.pushButton_153.clicked.connect(self.test6write4)
        self.pushButton_24.clicked.connect(self.test6mathnocalc)
        self.pushButton_78.clicked.connect(self.test6mathcalc)
        self.pushButton_84.clicked.connect(self.test6mathcalc2)
        self.pushButton_1129.clicked.connect(self.mathnocalc3)
        self.pushButton_1130.clicked.connect(self.mathcalc)
        self.pushButton_1131.clicked.connect(self.mathcalc2)
        self.pushButton_1132.clicked.connect(self.mathcalc3)
        self.pushButton_1133.clicked.connect(self.mathcalc4)


#######################################################################################################
      
    def book1 (self):
        webbrowser.open('McGraw-Hill_s SAT, 2009 Edition (Mcgraw Hill_s Sat) ( PDFDrive.com ).pdf')
        
    def book2 (self):
        webbrowser.open('Official_SAT_2018.pdf')
        
    def book4 (self):
        webbrowser.open('R Barrons Reading Workbook.pdf')
        
    def book5 (self):
        webbrowser.open('011_Barron_s How to Prepare for the SAT 2007-2008_All_AK_7 EXAMS.pdf')

    def book7 (self):
        webbrowser.open('W Barrons Writing Workbook.pdf')
        
    def book8 (self):
        webbrowser.open('011_Barron_s How to Prepare for the SAT 2007-2008_All_7 EXAMS.pdf')  
        
    def book9 (self):
        webbrowser.open('001_McGraw-Hill_s 12 SAT Practice Tests with PSAT 2ed.PDF')
        
    def book10 (self):
        webbrowser.open('pdf_sat-student-guide.pdf')
        
    def book11 (self):
        webbrowser.open('SAT Erica.pdf')
        
    def book12 (self):
        webbrowser.open('The Critical Reader - The Comlete Guide to SAT Reading (2nd Ed)(gnv64).pdf')

#######################################################################################################
            
    def writebut1(self):
        global marks
        if self.radioButton_4.isChecked():
            marks += 1
        if self.radioButton_6.isChecked():
            marks += 1
        if self.radioButton_12.isChecked():
            marks += 1
        if self.radioButton_13.isChecked():
            marks += 1
        if self.radioButton_18.isChecked():
            marks += 1
        if self.radioButton_21.isChecked():
            marks += 1
        if self.radioButton_27.isChecked():
            marks += 1
        if self.radioButton_32.isChecked():
            marks += 1
        if self.radioButton_33.isChecked():
            marks += 1
        if self.radioButton_40.isChecked():
            marks += 1
        if self.radioButton_43.isChecked():
            marks += 1
        self.pushButton_6.setEnabled(False)
        model = '1 = D, 2 = B \n 3 = C, 4 = A \n 5 = B, 6 = A \n 7 = C, 8 = D \n 9 = A , 10 = D \n 11 = C'
        self.message(11, model)
        
    def writebut2(self):
        global marks
        if self.radioButton_46.isChecked():
            marks += 1
        if self.radioButton_52.isChecked():
            marks += 1
        if self.radioButton_54.isChecked():
            marks += 1
        if self.radioButton_72.isChecked():
            marks += 1
        if self.radioButton_77.isChecked():
            marks += 1
        if self.radioButton_81.isChecked():
            marks += 1
        if self.radioButton_83.isChecked():
            marks += 1
        if self.radioButton_86.isChecked():
            marks += 1
        if self.radioButton_93.isChecked():
            marks += 1
        if self.radioButton_96.isChecked():
            marks += 1
        if self.radioButton_102.isChecked():
            marks += 1
        self.pushButton_8.setEnabled(False)
        model = '1 = B, 2 = D \n 3 = B, 4 = C \n 5 = D, 6 = D \n 7 = B, 8 = A \n 9 = D , 10 = C \n 11 = B'
        self.message(11, model)
        
    def writebut3(self):
        global marks
        if self.radioButton_61.isChecked():
            marks += 1
        if self.radioButton_63.isChecked():
            marks += 1
        if self.radioButton_171.isChecked():
            marks += 1
        if self.radioButton_70.isChecked():
            marks += 1
        if self.radioButton_107.isChecked():
            marks += 1
        if self.radioButton_111.isChecked():
            marks += 1
        if self.radioButton_115.isChecked():
            marks += 1
        if self.radioButton_117.isChecked():
            marks += 1
        if self.radioButton_124.isChecked():
            marks += 1
        if self.radioButton_128.isChecked():
            marks += 1
        if self.radioButton_130.isChecked():
            marks += 1
        self.pushButton_16.setEnabled(False)
        model = '1 = D, 2 = B \n 3 = B, 4 = A \n 5 = C, 6 = C \n 7 = C, 8 = A \n 9 = D , 10 = D \n 11 = B'
        self.message(11, model)
        
    def writebut4(self):
        global marks
        if self.radioButton_175.isChecked():
            marks += 1
        if self.radioButton_178.isChecked():
            marks += 1
        if self.radioButton_183.isChecked():
            marks += 1
        if self.radioButton_187.isChecked():
            marks += 1
        if self.radioButton_193.isChecked():
            marks += 1
        if self.radioButton_196.isChecked():
            marks += 1
        if self.radioButton_200.isChecked():
            marks += 1
        if self.radioButton_202.isChecked():
            marks += 1
        if self.radioButton_206.isChecked():
            marks += 1
        if self.radioButton_211.isChecked():
            marks += 1
        if self.radioButton_216.isChecked():
            marks += 1
        self.pushButton_21.setEnabled(False)
        model = '1 = B, 2 = A \n 3 = B, 4 = B \n 5 = D, 6 = C \n 7 = C, 8 = A \n 9 = A , 10 = B \n 11 = C'
        self.message(11, model)
        
    def writebut5(self):
        global marks
        if self.radioButton_221.isChecked():
            marks += 1
        if self.radioButton_224.isChecked():
            marks += 1
        if self.radioButton_227.isChecked():
            marks += 1
        if self.radioButton_231.isChecked():
            marks += 1
        if self.radioButton_234.isChecked():
            marks += 1
        if self.radioButton_239.isChecked():
            marks += 1
        if self.radioButton_244.isChecked():
            marks += 1
        if self.radioButton_246.isChecked():
            marks += 1
        if self.radioButton_303.isChecked():
            marks += 1
        if self.radioButton_254.isChecked():
            marks += 1
        if self.radioButton_259.isChecked():
            marks += 1
        self.pushButton_22.setEnabled(False)
        model = '1 = D, 2 = C \n 3 = B, 4 = B \n 5 = A, 6 = C \n 7 = C, 8 = A \n 9 = D , 10 = A \n 11 = B'
        self.message(11, model)
        
    def writebut6(self):
        global marks
        if self.radioButton_262.isChecked():
            marks += 1
        if self.radioButton_267.isChecked():
            marks += 1
        if self.radioButton_270.isChecked():
            marks += 1
        if self.radioButton_272.isChecked():
            marks += 1
        if self.radioButton_277.isChecked():
            marks += 1
        if self.radioButton_280.isChecked():
            marks += 1
        if self.radioButton_286.isChecked():
            marks += 1
        if self.radioButton_350.isChecked():
            marks += 1
        if self.radioButton_292.isChecked():
            marks += 1
        if self.radioButton_294.isChecked():
            marks += 1
        if self.radioButton_291.isChecked():
            marks += 1
        self.pushButton_23.setEnabled(False)
        model = '1 = C, 2 = D \n 3 = C, 4 = A \n 5 = B, 6 = D \n 7 = B, 8 = C \n 9 = A , 10 = A \n 11 = C'
        self.message(11, model)
    
    def writebut7(self):
        global marks
        if self.radioButton_396.isChecked():
            marks += 1
        if self.radioButton_399.isChecked():
            marks += 1
        if self.radioButton_358.isChecked():
            marks += 1
        if self.radioButton_363.isChecked():
            marks += 1
        if self.radioButton_368.isChecked():
            marks += 1
        if self.radioButton_405.isChecked():
            marks += 1
        if self.radioButton_376.isChecked():
            marks += 1
        if self.radioButton_381.isChecked():
            marks += 1
        if self.radioButton_382.isChecked():
            marks += 1
        if self.radioButton_386.isChecked():
            marks += 1
        if self.radioButton_392.isChecked():
            marks += 1
        self.pushButton_25.setEnabled(False)
        model = '1 = D, 2 = B \n 3 = A, 4 = C \n 5 = C, 6 = D \n 7 = B, 8 = C \n 9 = A , 10 = A \n 11 = B'
        self.message(11, model)
    
    def writebut8(self):
        global marks
        if self.radioButton_408.isChecked():
            marks += 1
        if self.radioButton_410.isChecked():
            marks += 1
        if self.radioButton_371.isChecked():
            marks += 1
        if self.radioButton_415.isChecked():
            marks += 1
        if self.radioButton_420.isChecked():
            marks += 1
        if self.radioButton_423.isChecked():
            marks += 1
        if self.radioButton_427.isChecked():
            marks += 1
        if self.radioButton_432.isChecked():
            marks += 1
        if self.radioButton_437.isChecked():
            marks += 1
        if self.radioButton_439.isChecked():
            marks += 1
        if self.radioButton_443.isChecked():
            marks += 1
        self.pushButton_26.setEnabled(False)
        model = '1 = B, 2 = A \n 3 = B, 4 = C \n 5 = C, 6 = C \n 7 = A, 8 = D \n 9 = D , 10 = B \n 11 = D'
        self.message(11, model)
        
    def writebut9(self):
        global marks
        if self.radioButton_493.isChecked():
            marks += 1
        if self.radioButton_496.isChecked():
            marks += 1
        if self.radioButton_455.isChecked():
            marks += 1
        if self.radioButton_460.isChecked():
            marks += 1
        if self.radioButton_463.isChecked():
            marks += 1
        if self.radioButton_467.isChecked():
            marks += 1
        if self.radioButton_408.isChecked():
            marks += 1
        if self.radioButton_476.isChecked():
            marks += 1
        if self.radioButton_480.isChecked():
            marks += 1
        if self.radioButton_482.isChecked():
            marks += 1
        if self.radioButton_486.isChecked():
            marks += 1
        self.pushButton_27.setEnabled(False)
        model = '1 = D, 2 = D \n 3 = B, 4 = A \n 5 = B, 6 = C \n 7 = B, 8 = D \n 9 = C , 10 = A \n 11 = A'
        self.message(11, model)

    def writebut10(self):
        global marks
        if self.radioButton_500.isChecked():
            marks += 1
        if self.radioButton_505.isChecked():
            marks += 1
        if self.radioButton_471.isChecked():
            marks += 1
        if self.radioButton_537.isChecked():
            marks += 1
        if self.radioButton_512.isChecked():
            marks += 1
        if self.radioButton_506.isChecked():
            marks += 1
        if self.radioButton_519.isChecked():
            marks += 1
        if self.radioButton_516.isChecked():
            marks += 1
        if self.radioButton_538.isChecked():
            marks += 1
        if self.radioButton_529.isChecked():
            marks += 1
        if self.radioButton_533.isChecked():
            marks += 1
        self.pushButton_28.setEnabled(False)
        model = '1 = A, 2 = A \n 3 = B, 4 = D \n 5 = C, 6 = A \n 7 = B, 8 = B \n 9 = C , 10 = D \n 11 = D'
        self.message(11, model)
        
    def writebut11(self):
        global marks
        if self.radioButton_524.isChecked():
            marks += 1
        if self.radioButton_543.isChecked():
            marks += 1
        if self.radioButton_583.isChecked():
            marks += 1
        if self.radioButton_547.isChecked():
            marks += 1
        if self.radioButton_554.isChecked():
            marks += 1
        if self.radioButton_561.isChecked():
            marks += 1
        if self.radioButton_588.isChecked():
            marks += 1
        if self.radioButton_566.isChecked():
            marks += 1
        if self.radioButton_562.isChecked():
            marks += 1
        if self.radioButton_576.isChecked():
            marks += 1
        if self.radioButton_579.isChecked():
            marks += 1
            
        self.pushButton_29.setEnabled(False)
        model = '1 = A, 2 = B \n 3 = C, 4 = C \n 5 = A, 6 = B \n 7 = A, 8 = D \n 9 = C , 10 = C \n 11 = B'
        self.message(11, model)     
    
    def writebut12(self):
        global marks
        if self.radioButton_552.isChecked():
            marks += 1
        if self.radioButton_570.isChecked():
            marks += 1
        if self.radioButton_593.isChecked():
            marks += 1
        if self.radioButton_597.isChecked():
            marks += 1
        if self.radioButton_601.isChecked():
            marks += 1
        if self.radioButton_603.isChecked():
            marks += 1
        if self.radioButton_607.isChecked():
            marks += 1
        if self.radioButton_610.isChecked():
            marks += 1
        if self.radioButton_617.isChecked():
            marks += 1
        if self.radioButton_621.isChecked():
            marks += 1
        if self.radioButton_623.isChecked():
            marks += 1
            
        self.pushButton_30.setEnabled(False)
        model = '1 = A, 2 = C \n 3 = D, 4 = B \n 5 = C, 6 = C \n 7 = B, 8 = D \n 9 = C , 10 = D \n 11 = A'
        self.message(11, model)
    
    def writebut13(self):
        global marks
        if self.radioButton_670.isChecked():
            marks += 1
        if self.radioButton_632.isChecked():
            marks += 1
        if self.radioButton_635.isChecked():
            marks += 1
        if self.radioButton_635.isChecked():
            marks += 1
        if self.radioButton_642.isChecked():
            marks += 1
        if self.radioButton_649.isChecked():
            marks += 1
        if self.radioButton_651.isChecked():
            marks += 1
        if self.radioButton_655.isChecked():
            marks += 1
        if self.radioButton_659.isChecked():
            marks += 1
        if self.radioButton_712.isChecked():
            marks += 1
        if self.radioButton_669.isChecked():
            marks += 1
            
        self.pushButton_31.setEnabled(False)
        model = '1 = A, 2 = D \n 3 = B, 4 = A \n 5 = D, 6 = B \n 7 = B, 8 = B \n 9 = D , 10 = B \n 11 = C'
        self.message(11, model)
        
    def writebut14(self):
        global marks
        if self.radioButton_758.isChecked():
            marks += 1
        if self.radioButton_719.isChecked():
            marks += 1
        if self.radioButton_724.isChecked():
            marks += 1
        if self.radioButton_765.isChecked():
            marks += 1
        if self.radioButton_733.isChecked():
            marks += 1
        if self.radioButton_768.isChecked():
            marks += 1
        if self.radioButton_739.isChecked():
            marks += 1
        if self.radioButton_743.isChecked():
            marks += 1
        if self.radioButton_746.isChecked():
            marks += 1
        if self.radioButton_753.isChecked():
            marks += 1
        if self.radioButton_754.isChecked():
            marks += 1
            
        self.pushButton_33.setEnabled(False)
        model = '1 = D, 2 = B \n 3 = C, 4 = D \n 5 = C, 6 = C \n 7 = B, 8 = D\n 9 = A , 10 = D \n 11 = D'
        self.message(11, model)
        
    def writebut15(self):
        global marks
        if self.radioButton_773.isChecked():
            marks += 1
        if self.radioButton_810.isChecked():
            marks += 1
        if self.radioButton_806.isChecked():
            marks += 1
        if self.radioButton_776.isChecked():
            marks += 1
        if self.radioButton_778.isChecked():
            marks += 1
        if self.radioButton_784.isChecked():
            marks += 1
        if self.radioButton_815.isChecked():
            marks += 1
        if self.radioButton_819.isChecked():
            marks += 1
        if self.radioButton_788.isChecked():
            marks += 1
        if self.radioButton_790.isChecked():
            marks += 1
        if self.radioButton_823.isChecked():
            marks += 1
            
        self.pushButton_34.setEnabled(False)
        model = '1 = B, 2 = B \n 3 = A, 4 = C \n 5 = D, 6 = C \n 7 = D, 8 = A\n 9 = D, 10 = C \n 11 = A'
        self.message(11, model)
        
    def writebut16(self):
        global marks
        if self.radioButton_796.isChecked():
            marks += 1
        if self.radioButton_826.isChecked():
            marks += 1
        if self.radioButton_831.isChecked():
            marks += 1
        if self.radioButton_799.isChecked():
            marks += 1
        if self.radioButton_860.isChecked():
            marks += 1
        if self.radioButton_836.isChecked():
            marks += 1
        if self.radioButton_838.isChecked():
            marks += 1
        if self.radioButton_845.isChecked():
            marks += 1
        if self.radioButton_846.isChecked():
            marks += 1
        if self.radioButton_851.isChecked():
            marks += 1
        if self.radioButton_854.isChecked():
            marks += 1
            
        self.pushButton_35.setEnabled(False)
        model = '1 = C, 2 = B \n 3 = B, 4 = D \n 5 = A, 6 = C \n 7 = D, 8 = C\n 9 = C, 10 = B \n 11 = D'
        self.message(11, model)
        
    def writebut17(self):
        global marks
        if self.radioButton_805.isChecked():
            marks += 1
        if self.radioButton_862.isChecked():
            marks += 1
        if self.radioButton_902.isChecked():
            marks += 1
        if self.radioButton_871.isChecked():
            marks += 1
        if self.radioButton_875.isChecked():
            marks += 1
        if self.radioButton_907.isChecked():
            marks += 1
        if self.radioButton_883.isChecked():
            marks += 1
        if self.radioButton_887.isChecked():
            marks += 1
        if self.radioButton_893.isChecked():
            marks += 1
        if self.radioButton_897.isChecked():
            marks += 1
        if self.radioButton_899.isChecked():
            marks += 1
            
        self.pushButton_36.setEnabled(False)
        model = '1 = B, 2 = B \n 3 = B, 4 = D \n 5 = A, 6 = D \n 7 = B, 8 = D\n 9 = A, 10 = D \n 11 = A'
        self.message(11, model)
        
    def writebut18(self):
        global marks
        if self.radioButton_948.isChecked():
            marks += 1
        if self.radioButton_879.isChecked():
            marks += 1
        if self.radioButton_913.isChecked():
            marks += 1
        if self.radioButton_917.isChecked():
            marks += 1
        if self.radioButton_921.isChecked():
            marks += 1
        if self.radioButton_925.isChecked():
            marks += 1
        if self.radioButton_928.isChecked():
            marks += 1
        if self.radioButton_952.isChecked():
            marks += 1
        if self.radioButton_954.isChecked():
            marks += 1
        if self.radioButton_931.isChecked():
            marks += 1
        if self.radioButton_945.isChecked():
            marks += 1
            
        self.pushButton_37.setEnabled(False)
        model = '1 = A, 2 = C \n 3 = D, 4 = B \n 5 = D, 6 = C \n 7 = C, 8 = C\n 9 = A, 10 = D \n 11 = C'
        self.message(11, model)
    
    def writebut19(self):
        global marks
        if self.radioButton_959.isChecked():
            marks += 1
        if self.radioButton_995.isChecked():
            marks += 1
        if self.radioButton_938.isChecked():
            marks += 1
        if self.radioButton_965.isChecked():
            marks += 1
        if self.radioButton_1000.isChecked():
            marks += 1
        if self.radioButton_1003.isChecked():
            marks += 1
        if self.radioButton_975.isChecked():
            marks += 1
        if self.radioButton_978.isChecked():
            marks += 1
        if self.radioButton_985.isChecked():
            marks += 1
        if self.radioButton_1008.isChecked():
            marks += 1
        if self.radioButton_1035.isChecked():
            marks += 1
            
        self.pushButton_38.setEnabled(False)
        model = '1 = D, 2 = B \n 3 = C, 4 = B \n 5 = D, 6 = C \n 7 = B, 8 = C\n 9 = A, 10 = C \n 11 = A'
        self.message(11, model)
    
    def writebut20(self):
        global marks
        if self.radioButton_1039.isChecked():
            marks += 1
        if self.radioButton_1045.isChecked():
            marks += 1
        if self.radioButton_1085.isChecked():
            marks += 1
        if self.radioButton_1053.isChecked():
            marks += 1
        if self.radioButton_1054.isChecked():
            marks += 1
        if self.radioButton_1058.isChecked():
            marks += 1
        if self.radioButton_1065.isChecked():
            marks += 1
        if self.radioButton_1066.isChecked():
            marks += 1
        if self.radioButton_1072.isChecked():
            marks += 1
        if self.radioButton_1074.isChecked():
            marks += 1
        if self.radioButton_1078.isChecked():
            marks += 1
            
        self.pushButton_39.setEnabled(False)
        model = '1 = D, 2 = A \n 3 = D, 4 = B \n 5 = C, 6 = B \n 7 = A, 8 = C\n 9 = D, 10 = B \n 11 = C'
        self.message(11, model)
        
#######################################################################################################
        
    def readbut1(self):
        global marks
        if self.radioButton_301.isChecked():
            marks += 1
        if self.radioButton_450.isChecked():
            marks += 1
        if self.radioButton_628.isChecked():
            marks += 1
        if self.radioButton_664.isChecked():
            marks += 1
        if self.radioButton_146.isChecked():
            marks += 1
        if self.radioButton_151.isChecked():
            marks += 1
        if self.radioButton_154.isChecked():
            marks += 1
        if self.radioButton_161.isChecked():
            marks += 1
        if self.radioButton_165.isChecked():
            marks += 1
        if self.radioButton_169.isChecked():
            marks += 1
            
        self.pushButton_20.setEnabled(False)
        model = '1 = B, 2 = A \n 3 = D, 4 = D \n 5 = A, 6 = D \n 7 = C, 8 = C\n 9 = B, 10 = D'
        self.message(10, model)
        
    def readbut2(self):
        global marks
        if self.radioButton_675.isChecked():
            marks += 1
        if self.radioButton_677.isChecked():
            marks += 1
        if self.radioButton_684.isChecked():
            marks += 1
        if self.radioButton_687.isChecked():
            marks += 1
        if self.radioButton_298.isChecked():
            marks += 1
        if self.radioButton_690.isChecked():
            marks += 1
        if self.radioButton_694.isChecked():
            marks += 1
        if self.radioButton_699.isChecked():
            marks += 1
        if self.radioButton_702.isChecked():
            marks += 1
        if self.radioButton_708.isChecked():
            marks += 1
            
        self.pushButton_32.setEnabled(False)
        model = '1 = C, 2 = B \n 3 = D, 4 = A \n 5 = C, 6 = D \n 7 = B, 8 = B\n 9 = A, 10 = D'
        self.message(10, model)
        
    def readbut3(self):
        global marks
        if self.radioButton_709.isChecked():
            marks += 1
        if self.radioButton_728.isChecked():
            marks += 1
        if self.radioButton_729.isChecked():
            marks += 1
        if self.radioButton_737.isChecked():
            marks += 1
        if self.radioButton_935.isChecked():
            marks += 1
        if self.radioButton_968.isChecked():
            marks += 1
        if self.radioButton_972.isChecked():
            marks += 1
        if self.radioButton_986.isChecked():
            marks += 1
        if self.radioButton_990.isChecked():
            marks += 1
        if self.radioButton_1011.isChecked():
            marks += 1
            
        self.pushButton_40.setEnabled(False)
        model = '1 = B, 2 = D \n 3 = C, 4 = C \n 5 = B, 6 = A \n 7 = D, 8 = A\n 9 = A, 10 = C'
        self.message(10, model)
        
    def readbut4(self):
        global marks
        if self.radioButton_1013.isChecked():
            marks += 1
        if self.radioButton_1018.isChecked():
            marks += 1
        if self.radioButton_1024.isChecked():
            marks += 1
        if self.radioButton_1025.isChecked():
            marks += 1
        if self.radioButton_1029.isChecked():
            marks += 1
        if self.radioButton_1046.isChecked():
            marks += 1
        if self.radioButton_1087.isChecked():
            marks += 1
        if self.radioButton_1090.isChecked():
            marks += 1
        if self.radioButton_1093.isChecked():
            marks += 1
        if self.radioButton_1098.isChecked():
            marks += 1
            
        self.pushButton_41.setEnabled(False)
        model = '1 = B, 2 = A \n 3 = D, 4 = C \n 5 = A, 6 = D \n 7 = A, 8 = A\n 9 = B, 10 = B'
        self.message(10, model)
        
    def readbut5(self):
        global marks
        if self.radioButton_1103.isChecked():
            marks += 1
        if self.radioButton_1106.isChecked():
            marks += 1
        if self.radioButton_1109.isChecked():
            marks += 1
        if self.radioButton_1116.isChecked():
            marks += 1
        if self.radioButton_1118.isChecked():
            marks += 1
        if self.radioButton_1121.isChecked():
            marks += 1
        if self.radioButton_1128.isChecked():
            marks += 1
        if self.radioButton_1131.isChecked():
            marks += 1
        if self.radioButton_1135.isChecked():
            marks += 1
        if self.radioButton_1138.isChecked():
            marks += 1
            
        self.pushButton_42.setEnabled(False)
        model = '1 = C, 2 = A \n 3 = C, 4 = D \n 5 = B, 6 = B \n 7 = D, 8 = B\n 9 = D, 10 = B'
        self.message(10, model)
        
    def readbut6(self):
        global marks
        if self.radioButton_1181.isChecked():
            marks += 1
        if self.radioButton_1188.isChecked():
            marks += 1
        if self.radioButton_1192.isChecked():
            marks += 1
        if self.radioButton_1195.isChecked():
            marks += 1
        if self.radioButton_1200.isChecked():
            marks += 1
        if self.radioButton_1201.isChecked():
            marks += 1
        if self.radioButton_1205.isChecked():
            marks += 1
        if self.radioButton_1211.isChecked():
            marks += 1
        if self.radioButton_1216.isChecked():
            marks += 1
        if self.radioButton_1217.isChecked():
            marks += 1
            
        self.pushButton_44.setEnabled(False)
        model = '1 = B, 2 = D \n 3 = D, 4 = A \n 5 = D, 6 = B \n 7 = C, 8 = B\n 9 = C, 10 = A'
        self.message(10, model)
        
    def readbut7(self):
        global marks
        if self.radioButton_1224.isChecked():
            marks += 1
        if self.radioButton_1228.isChecked():
            marks += 1
        if self.radioButton_1231.isChecked():
            marks += 1
        if self.radioButton_1234.isChecked():
            marks += 1
        if self.radioButton_1240.isChecked():
            marks += 1
        if self.radioButton_1241.isChecked():
            marks += 1
        if self.radioButton_1247.isChecked():
            marks += 1
        if self.radioButton_1249.isChecked():
            marks += 1
        if self.radioButton_1253.isChecked():
            marks += 1
        if self.radioButton_1260.isChecked():
            marks += 1
            
        self.pushButton_45.setEnabled(False)
        model = '1 = A, 2 = D \n 3 = A, 4 = B \n 5 = D, 6 = B \n 7 = A, 8 = D\n 9 = C, 10 = D'
        self.message(10, model)
        
    def readbut8(self):
        global marks
        if self.radioButton_1261.isChecked():
            marks += 1
        if self.radioButton_1267.isChecked():
            marks += 1
        if self.radioButton_1270.isChecked():
            marks += 1
        if self.radioButton_1273.isChecked():
            marks += 1
        if self.radioButton_1278.isChecked():
            marks += 1
        if self.radioButton_1283.isChecked():
            marks += 1
        if self.radioButton_1288.isChecked():
            marks += 1
        if self.radioButton_1292.isChecked():
            marks += 1
        if self.radioButton_1294.isChecked():
            marks += 1
        if self.radioButton_1300.isChecked():
            marks += 1
            
        self.pushButton_46.setEnabled(False)
        model = '1 = B, 2 = C \n 3 = B, 4 = C \n 5 = B, 6 = C \n 7 = D, 8 = C\n 9 = A, 10 = D'
        self.message(10, model)
        
    def readbut9(self):
        global marks
        if self.radioButton_1344.isChecked():
            marks += 1
        if self.radioButton_1347.isChecked():
            marks += 1
        if self.radioButton_1351.isChecked():
            marks += 1
        if self.radioButton_1353.isChecked():
            marks += 1
        if self.radioButton_1357.isChecked():
            marks += 1
        if self.radioButton_1362.isChecked():
            marks += 1
        if self.radioButton_1366.isChecked():
            marks += 1
        if self.radioButton_1371.isChecked():
            marks += 1
        if self.radioButton_1376.isChecked():
            marks += 1
        if self.radioButton_1379.isChecked():
            marks += 1
            
        self.pushButton_48.setEnabled(False)
        model = '1 = A, 2 = C \n 3 = A, 4 = C \n 5 = A, 6 = D \n 7 = B, 8 = C\n 9 = B, 10 = C'
        self.message(10, model)
        
    def readbut10(self):
        global marks
        if self.radioButton_1382.isChecked():
            marks += 1
        if self.radioButton_1386.isChecked():
            marks += 1
        if self.radioButton_1391.isChecked():
            marks += 1
        if self.radioButton_1394.isChecked():
            marks += 1
        if self.radioButton_1400.isChecked():
            marks += 1
        if self.radioButton_1401.isChecked():
            marks += 1
        if self.radioButton_1405.isChecked():
            marks += 1
        if self.radioButton_1411.isChecked():
            marks += 1
        if self.radioButton_1415.isChecked():
            marks += 1
        if self.radioButton_1420.isChecked():
            marks += 1
            
        self.pushButton_49.setEnabled(False)
        model = '1 = D, 2 = A \n 3 = A, 4 = B \n 5 = D, 6 = B \n 7 = C, 8 = B\n 9 = D, 10 = D'
        self.message(10, model)
        
    def readbut11(self):
        global marks
        if self.radioButton_1422.isChecked():
            marks += 1
        if self.radioButton_1425.isChecked():
            marks += 1
        if self.radioButton_1429.isChecked():
            marks += 1
        if self.radioButton_1434.isChecked():
            marks += 1
        if self.radioButton_1438.isChecked():
            marks += 1
        if self.radioButton_1443.isChecked():
            marks += 1
        if self.radioButton_1447.isChecked():
            marks += 1
        if self.radioButton_1452.isChecked():
            marks += 1
        if self.radioButton_1454.isChecked():
            marks += 1
        if self.radioButton_1457.isChecked():
            marks += 1
            
        self.pushButton_50.setEnabled(False)
        model = '1 = D, 2 = B \n 3 = C, 4 = B \n 5 = B, 6 = C \n 7 = A, 8 = C\n 9 = A, 10 = A'
        self.message(10, model)
        
    def readbut12(self):
        global marks
        if self.radioButton_1463.isChecked():
            marks += 1
        if self.radioButton_1468.isChecked():
            marks += 1
        if self.radioButton_1472.isChecked():
            marks += 1
        if self.radioButton_1473.isChecked():
            marks += 1
        if self.radioButton_1477.isChecked():
            marks += 1
        if self.radioButton_1483.isChecked():
            marks += 1
        if self.radioButton_1487.isChecked():
            marks += 1
        if self.radioButton_1490.isChecked():
            marks += 1
        if self.radioButton_1496.isChecked():
            marks += 1
        if self.radioButton_1497.isChecked():
            marks += 1
            
        self.pushButton_51.setEnabled(False)
        model = '1 = C, 2 = D \n 3 = D, 4 = C \n 5 = A, 6 = C \n 7 = A, 8 = A\n 9 = B, 10 = A'
        self.message(10, model)
        
    def readbut13(self):
        global marks
        if self.radioButton_1501.isChecked():
            marks += 1
        if self.radioButton_1505.isChecked():
            marks += 1
        if self.radioButton_1511.isChecked():
            marks += 1
        if self.radioButton_1515.isChecked():
            marks += 1
        if self.radioButton_1519.isChecked():
            marks += 1
        if self.radioButton_1524.isChecked():
            marks += 1
        if self.radioButton_1527.isChecked():
            marks += 1
        if self.radioButton_1531.isChecked():
            marks += 1
        if self.radioButton_1536.isChecked():
            marks += 1
        if self.radioButton_1540.isChecked():
            marks += 1
            
        self.pushButton_52.setEnabled(False)
        model = '1 = B, 2 = C \n 3 = A, 4 = A \n 5 = C, 6 = A \n 7 = A, 8 = B\n 9 = B, 10 = D'
        self.message(10, model)
        
    def readbut14(self):
        global marks
        if self.radioButton_1544.isChecked():
            marks += 1
        if self.radioButton_1547.isChecked():
            marks += 1
        if self.radioButton_1552.isChecked():
            marks += 1
        if self.radioButton_1554.isChecked():
            marks += 1
        if self.radioButton_1558.isChecked():
            marks += 1
        if self.radioButton_1563.isChecked():
            marks += 1
        if self.radioButton_1566.isChecked():
            marks += 1
        if self.radioButton_1571.isChecked():
            marks += 1
        if self.radioButton_1574.isChecked():
            marks += 1
        if self.radioButton_1577.isChecked():
            marks += 1
            
        self.pushButton_53.setEnabled(False)
        model = '1 = A, 2 = C \n 3 = D, 4 = B \n 5 = B, 6 = C \n 7 = B, 8 = B\n 9 = A, 10 = A'
        self.message(10, model)
        
    def readbut15(self):
        global marks
        if self.radioButton_1582.isChecked():
            marks += 1
        if self.radioButton_1586.isChecked():
            marks += 1
        if self.radioButton_1591.isChecked():
            marks += 1
        if self.radioButton_1594.isChecked():
            marks += 1
        if self.radioButton_1599.isChecked():
            marks += 1
        if self.radioButton_1603.isChecked():
            marks += 1
        if self.radioButton_1606.isChecked():
            marks += 1
        if self.radioButton_1611.isChecked():
            marks += 1
        if self.radioButton_1615.isChecked():
            marks += 1
        if self.radioButton_1620.isChecked():
            marks += 1
            
        self.pushButton_54.setEnabled(False)
        model = '1 = D, 2 = A \n 3 = A, 4 = B \n 5 = C, 6 = C \n 7 = B, 8 = B\n 9 = D, 10 = D'
        self.message(10, model)
        
    def readbut16(self):
        global marks
        if self.radioButton_1621.isChecked():
            marks += 1
        if self.radioButton_1627.isChecked():
            marks += 1
        if self.radioButton_1629.isChecked():
            marks += 1
        if self.radioButton_1636.isChecked():
            marks += 1
        if self.radioButton_1639.isChecked():
            marks += 1
        if self.radioButton_1644.isChecked():
            marks += 1
        if self.radioButton_1648.isChecked():
            marks += 1
        if self.radioButton_1652.isChecked():
            marks += 1
        if self.radioButton_1654.isChecked():
            marks += 1
        if self.radioButton_1660.isChecked():
            marks += 1
            
        self.pushButton_55.setEnabled(False)
        model = '1 = B, 2 = C \n 3 = C, 4 = D \n 5 = C, 6 = A \n 7 = D, 8 = C\n 9 = A, 10 = D'
        self.message(10, model)
        
    def readbut17(self):
        global marks
        if self.radioButton_1663.isChecked():
            marks += 1
        if self.radioButton_1667.isChecked():
            marks += 1
        if self.radioButton_1672.isChecked():
            marks += 1
        if self.radioButton_1676.isChecked():
            marks += 1
        if self.radioButton_1679.isChecked():
            marks += 1
        if self.radioButton_1681.isChecked():
            marks += 1
        if self.radioButton_1686.isChecked():
            marks += 1
        if self.radioButton_1690.isChecked():
            marks += 1
        if self.radioButton_1696.isChecked():
            marks += 1
        if self.radioButton_1700.isChecked():
            marks += 1
            
        self.pushButton_56.setEnabled(False)
        model = '1 = C, 2 = C \n 3 = D, 4 = D \n 5 = C, 6 = B \n 7 = B, 8 = A\n 9 = B, 10 = D'
        self.message(10, model)
        
    def readbut18(self):
        global marks
        if self.radioButton_1704.isChecked():
            marks += 1
        if self.radioButton_1707.isChecked():
            marks += 1
        if self.radioButton_1709.isChecked():
            marks += 1
        if self.radioButton_1716.isChecked():
            marks += 1
        if self.radioButton_1717.isChecked():
            marks += 1
        if self.radioButton_1722.isChecked():
            marks += 1
        if self.radioButton_1728.isChecked():
            marks += 1
        if self.radioButton_1731.isChecked():
            marks += 1
        if self.radioButton_1733.isChecked():
            marks += 1
        if self.radioButton_1739.isChecked():
            marks += 1
            
        self.pushButton_57.setEnabled(False)
        model = '1 = A, 2 = C \n 3 = C, 4 = D \n 5 = A, 6 = D \n 7 = D, 8 = B\n 9 = C, 10 = B'
        self.message(10, model)
        
    def readbut19(self):
        global marks
        if self.radioButton_1742.isChecked():
            marks += 1
        if self.radioButton_1746.isChecked():
            marks += 1
        if self.radioButton_1751.isChecked():
            marks += 1
        if self.radioButton_1756.isChecked():
            marks += 1
        if self.radioButton_1760.isChecked():
            marks += 1
        if self.radioButton_1763.isChecked():
            marks += 1
        if self.radioButton_1768.isChecked():
            marks += 1
        if self.radioButton_1771.isChecked():
            marks += 1
        if self.radioButton_1775.isChecked():
            marks += 1
        if self.radioButton_1778.isChecked():
            marks += 1
            
        self.pushButton_58.setEnabled(False)
        model = '1 = D, 2 = A \n 3 = A, 4 = D \n 5 = D, 6 = C \n 7 = D, 8 = B\n 9 = D, 10 = C'
        self.message(10, model)
        
    def readbut20(self):
        global marks
        if self.radioButton_1783.isChecked():
            marks += 1
        if self.radioButton_1786.isChecked():
            marks += 1
        if self.radioButton_1792.isChecked():
            marks += 1
        if self.radioButton_1793.isChecked():
            marks += 1
        if self.radioButton_1797.isChecked():
            marks += 1
        if self.radioButton_1803.isChecked():
            marks += 1
        if self.radioButton_1806.isChecked():
            marks += 1
        if self.radioButton_1812.isChecked():
            marks += 1
        if self.radioButton_1815.isChecked():
            marks += 1
        if self.radioButton_1819.isChecked():
            marks += 1
            
        self.pushButton_59.setEnabled(False)
        model = '1 = C, 2 = A \n 3 = D, 4 = C \n 5 = A, 6 = C \n 7 = B, 8 = C\n 9 = D, 10 = B'
        self.message(10, model)
        
#########################################################################################

    def mathnocalc(self):
        global marks
        if self.radioButton_4963.isChecked():
            marks += 1
        if self.radioButton_4972.isChecked():
            marks += 1
        if self.radioButton_4979.isChecked():
            marks += 1
        if self.radioButton_4989.isChecked():
            marks += 1
        if self.radioButton_4997.isChecked():
            marks += 1
        if self.radioButton_5005.isChecked():
            marks += 1
        if self.radioButton_5013.isChecked():
            marks += 1
        if self.radioButton_5020.isChecked():
            marks += 1
        if self.radioButton_5030.isChecked():
            marks += 1
        if self.radioButton_5037.isChecked():
            marks += 1
    
        if self.radioButton_5042.isChecked():
            marks += 1
        if self.radioButton_5048.isChecked():
            marks += 1
        if self.radioButton_5057.isChecked():
            marks += 1
        if self.radioButton_5065.isChecked():
            marks += 1
        if self.radioButton_5073.isChecked():
            marks += 1
        if self.radioButton_5079.isChecked():
            marks += 1
        if self.radioButton_5090.isChecked():
            marks += 1
        if self.radioButton_5096.isChecked():
            marks += 1
        if self.radioButton_5104.isChecked():
            marks += 1
        if self.radioButton_5113.isChecked():
            marks += 1

        self.pushButton_1117.setEnabled(False)
        model = '1 = A, 2 = D \n 3 = C, 4 = B\n 5 = B, 6 = D \n 7 = B, 8 = C\n 9 = A, 10 = B \n 11 = D, 12 = D \n 13 = B, 14 = B \n 15 = B, 16 = C \n 17 = A, 18 = C \n 19 = C, 20 = B'
        self.message(20, model)
        
        
    def mathnocalc2(self):
        global marks
        if self.radioButton_5118.isChecked():
            marks += 1
        if self.radioButton_5125.isChecked():
            marks += 1
        if self.radioButton_5131.isChecked():
            marks += 1
        if self.radioButton_5140.isChecked():
            marks += 1
        if self.radioButton_5149.isChecked():
            marks += 1
        if self.radioButton_5158.isChecked():
            marks += 1
        if self.radioButton_5166.isChecked():
            marks += 1
        if self.radioButton_5173.isChecked():
            marks += 1
        if self.radioButton_5179.isChecked():
            marks += 1
        if self.radioButton_5190.isChecked():
            marks += 1
    
        if self.radioButton_5192.isChecked():
            marks += 1
        if self.radioButton_5199.isChecked():
            marks += 1
        if self.radioButton_5207.isChecked():
            marks += 1
        if self.radioButton_5217.isChecked():
            marks += 1
        if self.radioButton_5224.isChecked():
            marks += 1
        if self.radioButton_5232.isChecked():
            marks += 1
        if self.radioButton_5239.isChecked():
            marks += 1
        if self.radioButton_5247.isChecked():
            marks += 1
        if self.radioButton_5258.isChecked():
            marks += 1
        if self.radioButton_5265.isChecked():
            marks += 1

        self.pushButton_1128.setEnabled(False)
        model = '21 = D, 22 = C \n 23 = C, 24 = C\n 25 = B, 26 = A \n 27 = A, 28 = B\n 29 = D, 30 = A \n 31 = C, 32 = B \n 33 = C, 34 = B \n 35 = C, 36 = B \n 37 = D, 38 = D \n 39 = A, 40 = B'
        self.message(20, model)
#######################################################################################################

    def test1read1(self):
        global marks
        if self.radioButton_1824.isChecked():
            marks += 1
        if self.radioButton_1825.isChecked():
            marks += 1
        if self.radioButton_1832.isChecked():
            marks += 1
        if self.radioButton_1834.isChecked():
            marks += 1
        if self.radioButton_1837.isChecked():
            marks += 1
        if self.radioButton_1844.isChecked():
            marks += 1
        if self.radioButton_1848.isChecked():
            marks += 1
        if self.radioButton_1852.isChecked():
            marks += 1
        if self.radioButton_1853.isChecked():
            marks += 1
        if self.radioButton_1859.isChecked():
            marks += 1
            
        self.pushButton_60.setEnabled(False)
        model = '1 = A, 2 = B \n 3 = D, 4 = B \n 5 = A, 6 = A \n 7 = D, 8 = C\n 9 = C, 10 = B'
        self.message(10, model)
        
    def test1read2(self):
        global marks
        if self.radioButton_1862.isChecked():
            marks += 1
        if self.radioButton_1866.isChecked():
            marks += 1
        if self.radioButton_1871.isChecked():
            marks += 1
        if self.radioButton_1874.isChecked():
            marks += 1
        if self.radioButton_1879.isChecked():
            marks += 1
        if self.radioButton_1883.isChecked():
            marks += 1
        if self.radioButton_1888.isChecked():
            marks += 1
        if self.radioButton_1892.isChecked():
            marks += 1
        if self.radioButton_1896.isChecked():
            marks += 1
        if self.radioButton_1899.isChecked():
            marks += 1
            
        self.pushButton_61.setEnabled(False)
        model = '1 = D, 2 = A \n 3 = A, 4 = B \n 5 = C, 6 = C \n 7 = D, 8 = C\n 9 = B, 10 = B'
        self.message(10, model)
        
    def test1read3(self):
        global marks
        if self.radioButton_1902.isChecked():
            marks += 1
        if self.radioButton_1905.isChecked():
            marks += 1
        if self.radioButton_1911.isChecked():
            marks += 1
        if self.radioButton_1913.isChecked():
            marks += 1
        if self.radioButton_1919.isChecked():
            marks += 1
        if self.radioButton_1921.isChecked():
            marks += 1
        if self.radioButton_1928.isChecked():
            marks += 1
        if self.radioButton_1930.isChecked():
            marks += 1
        if self.radioButton_1935.isChecked():
            marks += 1
        if self.radioButton_1937.isChecked():
            marks += 1
        if self.radioButton_1942.isChecked():
            marks += 1
            
        self.pushButton_62.setEnabled(False)
        model = '1 = D, 2 = B \n 3 = A, 4 = C \n 5 = C, 6 = B \n 7 = D, 8 = A\n 9 = D, 10 = A\n 11 = B'
        self.message(11, model)
        
    def test1read4(self):
        global marks
        if self.radioButton_1947.isChecked():
            marks += 1
        if self.radioButton_1949.isChecked():
            marks += 1
        if self.radioButton_1954.isChecked():
            marks += 1
        if self.radioButton_1960.isChecked():
            marks += 1
        if self.radioButton_1963.isChecked():
            marks += 1
        if self.radioButton_1968.isChecked():
            marks += 1
        if self.radioButton_1971.isChecked():
            marks += 1
        if self.radioButton_1975.isChecked():
            marks += 1
        if self.radioButton_1979.isChecked():
            marks += 1
        if self.radioButton_1981.isChecked():
            marks += 1
            
        self.pushButton_63.setEnabled(False)
        model = '1 = C, 2 = B \n 3 = B, 4 = D \n 5 = C, 6 = A \n 7 = A, 8 = B\n 9 = D, 10 = A'
        self.message(10, model)
        
    def test1read5(self):
        global marks
        if self.radioButton_1988.isChecked():
            marks += 1
        if self.radioButton_1989.isChecked():
            marks += 1
        if self.radioButton_2023.isChecked():
            marks += 1
        if self.radioButton_1993.isChecked():
            marks += 1
        if self.radioButton_1999.isChecked():
            marks += 1
        if self.radioButton_2002.isChecked():
            marks += 1
        if self.radioButton_2007.isChecked():
            marks += 1
        if self.radioButton_2011.isChecked():
            marks += 1
        if self.radioButton_2016.isChecked():
            marks += 1
        if self.radioButton_2019.isChecked():
            marks += 1
            
        self.pushButton_64.setEnabled(False)
        model = '1 = A, 2 = B \n 3 = D, 4 = C \n 5 = A, 6 = B \n 7 = C, 8 = A\n 9 = C, 10 = D'
        self.message(10, model)
        
    def test1write1(self):
        global marks
        if self.radioButton_67.isChecked():
            marks += 1
        if self.radioButton_1171.isChecked():
            marks += 1
        if self.radioButton_138.isChecked():
            marks += 1
        if self.radioButton_1173.isChecked():
            marks += 1
        if self.radioButton_1144.isChecked():
            marks += 1
        if self.radioButton_1145.isChecked():
            marks += 1
        if self.radioButton_1151.isChecked():
            marks += 1
        if self.radioButton_1156.isChecked():
            marks += 1
        if self.radioButton_1160.isChecked():
            marks += 1
        if self.radioButton_1163.isChecked():
            marks += 1
        if self.radioButton_1167.isChecked():
            marks += 1
            
        self.pushButton_43.setEnabled(False)
        model = '1 = A, 2 = D \n 3 = A, 4 = A \n 5 = D, 6 = A \n 7 = C, 8 = D \n 9 = D , 10 = C \n 11 = C'
        self.message(11, model)
        
    def test1write2(self):
        global marks
        if self.radioButton_137.isChecked():
            marks += 1
        if self.radioButton_1177.isChecked():
            marks += 1
        if self.radioButton_145.isChecked():
            marks += 1
        if self.radioButton_1302.isChecked():
            marks += 1
        if self.radioButton_1306.isChecked():
            marks += 1
        if self.radioButton_1310.isChecked():
            marks += 1
        if self.radioButton_1313.isChecked():
            marks += 1
        if self.radioButton_1320.isChecked():
            marks += 1
        if self.radioButton_1322.isChecked():
            marks += 1
        if self.radioButton_1336.isChecked():
            marks += 1
        if self.radioButton_1330.isChecked():
            marks += 1
            
        self.pushButton_47.setEnabled(False)
        model = '12 = D, 13 = A \n 14 = D, 15 = C \n 16 = B, 17 = B \n 18 = A, 19 = D \n 20 = B , 21 = C \n 22 = B'
        self.message(11, model)
        
    def test1write3(self):
        global marks
        if self.radioButton_1327.isChecked():
            marks += 1
        if self.radioButton_1337.isChecked():
            marks += 1
        if self.radioButton_2025.isChecked():
            marks += 1
        if self.radioButton_2032.isChecked():
            marks += 1
        if self.radioButton_2036.isChecked():
            marks += 1
        if self.radioButton_2038.isChecked():
            marks += 1
        if self.radioButton_2043.isChecked():
            marks += 1
        if self.radioButton_2045.isChecked():
            marks += 1
        if self.radioButton_2052.isChecked():
            marks += 1
        if self.radioButton_2056.isChecked():
            marks += 1
        if self.radioButton_2057.isChecked():
            marks += 1
            
        self.pushButton_65.setEnabled(False)
        model = '23 = C, 24 = A \n 25 = A, 26 = B \n 27 = B, 28 = B \n 29 = C, 30 = C \n 31 = B , 32 = B \n 33 = A'
        self.message(11, model)
        
    def test1write4(self):
        global marks
        if self.radioButton_2106.isChecked():
            marks += 1
        if self.radioButton_2111.isChecked():
            marks += 1
        if self.radioButton_2071.isChecked():
            marks += 1
        if self.radioButton_2076.isChecked():
            marks += 1
        if self.radioButton_2079.isChecked():
            marks += 1
        if self.radioButton_2083.isChecked():
            marks += 1
        if self.radioButton_2086.isChecked():
            marks += 1
        if self.radioButton_2090.isChecked():
            marks += 1
        if self.radioButton_2093.isChecked():
            marks += 1
        if self.radioButton_2098.isChecked():
            marks += 1
        if self.radioButton_2103.isChecked():
            marks += 1
            
        self.pushButton_66.setEnabled(False)
        model = '34 = C, 35 = D \n 36 = C, 37 = B \n 38 = C, 39 = C \n 40 = D, 41 = A \n 42 = D , 43 = A \n 44 = D'
        self.message(11, model)
        
#######################################################################################################
    def test1mathnocalc(self):
        global marks
        if self.radioButton_2149.isChecked():
            marks += 1
        if self.radioButton_2270.isChecked():
            marks += 1
        if self.radioButton_2274.isChecked():
            marks += 1
        if self.radioButton_2277.isChecked():
            marks += 1
        if self.radioButton_2283.isChecked():
            marks += 1
        if self.radioButton_2287.isChecked():
            marks += 1
        if self.radioButton_2288.isChecked():
            marks += 1
        if self.radioButton_2293.isChecked():
            marks += 1
        if self.radioButton_2297.isChecked():
            marks += 1
        if self.radioButton_2301.isChecked():
            marks += 1 
        if self.radioButton_2300.isChecked():
            marks += 1
        if self.radioButton_2312.isChecked():
            marks += 1
        if self.radioButton_2320.isChecked():
            marks += 1
        if self.radioButton_2330.isChecked():
            marks += 1
        if self.radioButton_2339.isChecked():
            marks += 1
        if self.lineEdit_71.text() == "2200":
            marks += 1
        if self.lineEdit_70.text() == "5":
            marks += 1
        if self.lineEdit_69.text() == "1.21" :
            marks += 1
        if self.lineEdit_68.text() == "2500" :
            marks += 1
        if self.lineEdit_67.text() == "20" :
            marks += 1

        self.pushButton_67.setEnabled(False)
        model = '1 = B, 2 = c \n 3 = B, 4 = C \n 5 = A, 6 = A \n 7 = D, 8 = C \n 9 = C, 10 = D \n 11 = A, 12 = B \n 13 = C, 14 = b \n 15 = A, 16 = 2200 \n 17 = 5, 18 = 1.21 \n 19 = 2500 , 20 = 20'
        self.message(20, model)
#######################################################################################################        
    def test1mathcalc1(self):
        global marks
        if self.radioButton_2346.isChecked():
            marks += 1
        if self.radioButton_2352.isChecked():
            marks += 1
        if self.radioButton_2361.isChecked():
            marks += 1
        if self.radioButton_2371.isChecked():
            marks += 1
        if self.radioButton_2283.isChecked():
            marks += 1
        if self.radioButton_2530.isChecked():
            marks += 1
        if self.radioButton_2537.isChecked():
            marks += 1
        if self.radioButton_2546.isChecked():
            marks += 1
        if self.radioButton_2553.isChecked():
            marks += 1
        if self.radioButton_2561.isChecked():
            marks += 1    
        if self.radioButton_2570.isChecked():
            marks += 1
        if self.radioButton_2579.isChecked():
            marks += 1
        if self.radioButton_2585.isChecked():
            marks += 1
            
        self.pushButton_74.setEnabled(False)
        model = '1 = B, 2 = A \n 3 = B, 4 = C \n 5 = C, 6 = D \n 7 = B, 8 = C\n 9 = C, 10 = D \n 11 = A, 12 = C'
        self.message(12, model) 
#######################################################################################################        
    def test1mathcalc2(self):
        global marks
        if self.radioButton_2626.isChecked():
            marks += 1
        if self.radioButton_2631.isChecked():
            marks += 1
        if self.radioButton_2634.isChecked():
            marks += 1
        if self.radioButton_2637.isChecked():
            marks += 1
        if self.radioButton_2642.isChecked():
            marks += 1
        if self.radioButton_2645.isChecked():
            marks += 1
        if self.radioButton_2648.isChecked():
            marks += 1
        if self.radioButton_2653.isChecked():
            marks += 1
        if self.radioButton_2658.isChecked():
            marks += 1

        if self.radioButton_2698.isChecked():
            marks += 1
        if self.radioButton_2663.isChecked():
            marks += 1
        if self.radioButton_2666.isChecked():
            marks += 1
        if self.radioButton_2671.isChecked():
            marks += 1
        if self.radioButton_2672.isChecked():
            marks += 1
        if self.radioButton_2679.isChecked():
            marks += 1
        if self.radioButton_2680.isChecked():
            marks += 1
        if self.radioButton_2687.isChecked():
            marks += 1
        if self.radioButton_2689.isChecked():
            marks += 1 
        if self.lineEdit_72.text() == "6" :
            marks += 1
        self.pushButton_75.setEnabled(False)
        model = '13 = C, 14 = A \n 15 = B, 16 = C \n 17 = D, 18 = C \n 19 = D, 20 = C\n 21 = B, 22 = D \n 23 = A, 24 = B \n 25 = A, 26 = D \n 27 = A, 28 = D \n 29 = A, 30 = B \n 31 = 6'
        self.message(19, model)  
########################################################################################################################################################
    def test1mathcalc3(self):
        global marks
        if self.lineEdit_73.text() == "146":
            marks += 1
        if self.lineEdit_74.text() == "2500":
            marks += 1
        if self.lineEdit_75.text() == "34" :
            marks += 1
        if self.lineEdit_76.text() == "5/2 or 2.5" :
            marks += 1
        if self.lineEdit_76.text() == "2.5" :
            marks += 1
        if self.lineEdit_76.text() == "5/2" :
            marks += 1
        if self.lineEdit_77.text() == "25/4 or 6.25" :
            marks += 1
        if self.lineEdit_77.text() == "6.25" :
            marks += 1
        if self.lineEdit_77.text() == "25/4" :
            marks += 1
        if self.lineEdit_79.text() == "293":
            marks += 1
        if self.lineEdit_80.text() == "9" :
            marks += 1

        self.pushButton_76.setEnabled(False)
        model = '32 = 146, 33 = 2500 \n 34 = 34, 35 = 5/2 or 2.5 \n 36 = 25/4 or 6.25, 37 = 293 \n 38 = 9'
        self.message(7, model)
#########################################################################################         
    def test2read1(self):
        global marks
        if self.radioButton_3405.isChecked():
            marks += 1
        if self.radioButton_3411.isChecked():
            marks += 1
        if self.radioButton_3415.isChecked():
            marks += 1
        if self.radioButton_3418.isChecked():
            marks += 1
        if self.radioButton_3422.isChecked():
            marks += 1
        if self.radioButton_3427.isChecked():
            marks += 1
        if self.radioButton_3431.isChecked():
            marks += 1
        if self.radioButton_3433.isChecked():
            marks += 1
        if self.radioButton_3439.isChecked():
            marks += 1
        if self.radioButton_3442.isChecked():
            marks += 1
            
        self.pushButton_98.setEnabled(False)
        model = '1 = B, 2 = C \n 3 = A, 4 = B \n 5 = B, 6 = C \n 7 = A, 8 = D\n 9 = D, 10 = C'
        self.message(10, model)
        
    def test2read2(self):
        global marks
        if self.radioButton_3447.isChecked():
            marks += 1
        if self.radioButton_3452.isChecked():
            marks += 1
        if self.radioButton_3453.isChecked():
            marks += 1
        if self.radioButton_3459.isChecked():
            marks += 1
        if self.radioButton_3463.isChecked():
            marks += 1
        if self.radioButton_3465.isChecked():
            marks += 1
        if self.radioButton_3471.isChecked():
            marks += 1
        if self.radioButton_3475.isChecked():
            marks += 1
        if self.radioButton_3477.isChecked():
            marks += 1
        if self.radioButton_3484.isChecked():
            marks += 1
            
        self.pushButton_99.setEnabled(False)
        model = '1 = C, 2 = D \n 3 = C, 4 = A \n 5 = C, 6 = B \n 7 = A, 8 = B\n 9 = C, 10 = D'
        self.message(10, model)
        
    def test2read3(self):
        global marks
        if self.radioButton_3485.isChecked():
            marks += 1
        if self.radioButton_3491.isChecked():
            marks += 1
        if self.radioButton_3493.isChecked():
            marks += 1
        if self.radioButton_3497.isChecked():
            marks += 1
        if self.radioButton_3501.isChecked():
            marks += 1
        if self.radioButton_3506.isChecked():
            marks += 1
        if self.radioButton_3509.isChecked():
            marks += 1
        if self.radioButton_3514.isChecked():
            marks += 1
        if self.radioButton_3518.isChecked():
            marks += 1
        if self.radioButton_3524.isChecked():
            marks += 1
            
        self.pushButton_100.setEnabled(False)
        model = '1 = B, 2 = C \n 3 = C, 4 = C \n 5 = A, 6 = D \n 7 = C, 8 = A\n 9 = A, 10 = D'
        self.message(10, model)
        
    def test2read4(self):
        global marks
        if self.radioButton_3529.isChecked():
            marks += 1
        if self.radioButton_3534.isChecked():
            marks += 1
        if self.radioButton_3538.isChecked():
            marks += 1
        if self.radioButton_3544.isChecked():
            marks += 1
        if self.radioButton_3546.isChecked():
            marks += 1
        if self.radioButton_3550.isChecked():
            marks += 1
        if self.radioButton_3556.isChecked():
            marks += 1
        if self.radioButton_3559.isChecked():
            marks += 1
        if self.radioButton_3562.isChecked():
            marks += 1
        if self.radioButton_3567.isChecked():
            marks += 1
            
        self.pushButton_101.setEnabled(False)
        model = '1 = B, 2 = A \n 3 = B, 4 = D \n 5 = B, 6 = D \n 7 = D, 8 = B\n 9 = A, 10 = B'
        self.message(10, model)
        
    def test2read5(self):
        global marks
        if self.radioButton_3569.isChecked():
            marks += 1
        if self.radioButton_3575.isChecked():
            marks += 1
        if self.radioButton_3579.isChecked():
            marks += 1
        if self.radioButton_3582.isChecked():
            marks += 1
        if self.radioButton_3586.isChecked():
            marks += 1
        if self.radioButton_3591.isChecked():
            marks += 1
        if self.radioButton_3596.isChecked():
            marks += 1
        if self.radioButton_3597.isChecked():
            marks += 1
        if self.radioButton_3601.isChecked():
            marks += 1
        if self.radioButton_3607.isChecked():
            marks += 1
        if self.radioButton_3607.isChecked():
            marks += 1
            
        self.pushButton_102.setEnabled(False)
        model = '1 = B, 2 = C \n 3 = D, 4 = B \n 5 = B, 6 = C \n 7 = A, 8 = C\n 9 = D, 10 = D\n 11 = A'
        self.message(11, model)
        
#######################################################################################################
    
    def test2write1(self):
        global marks
        if self.radioButton_3610.isChecked():
            marks += 1
        if self.radioButton_3613.isChecked():
            marks += 1
        if self.radioButton_3832.isChecked():
            marks += 1
        if self.radioButton_3623.isChecked():
            marks += 1
        if self.radioButton_3619.isChecked():
            marks += 1
        if self.radioButton_3632.isChecked():
            marks += 1
        if self.radioButton_3635.isChecked():
            marks += 1
        if self.radioButton_3834.isChecked():
            marks += 1
        if self.radioButton_3644.isChecked():
            marks += 1
        if self.radioButton_3645.isChecked():
            marks += 1
        if self.radioButton_3652.isChecked():
            marks += 1
            
        self.pushButton_103.setEnabled(False)
        model = '1 = B, 2 = C \n 3 = A, 4 = D \n 5 = C, 6 = D \n 7 = C, 8 = C \n 9 = D , 10 = A \n 11 = D'
        self.message(11, model)
#######################################################################################################
    
    def test2write2(self):
        global marks
        if self.radioButton_3837.isChecked():
            marks += 1
        if self.radioButton_3657.isChecked():
            marks += 1
        if self.radioButton_3664.isChecked():
            marks += 1
        if self.radioButton_3672.isChecked():
            marks += 1
        if self.radioButton_3844.isChecked():
            marks += 1
        if self.radioButton_3675.isChecked():
            marks += 1
        if self.radioButton_3677.isChecked():
            marks += 1
        if self.radioButton_3683.isChecked():
            marks += 1
        if self.radioButton_3688.isChecked():
            marks += 1
        if self.radioButton_3689.isChecked():
            marks += 1
        if self.radioButton_3694.isChecked():
            marks += 1
            
        self.pushButton_104.setEnabled(False)
        model = '12 = B, 13 = A \n 14 = D, 15 = D \n 16 = C, 17 = C \n 18 = A, 19 = C \n 20 = D , 21 = B \n 22 = B'
        self.message(11, model)
#######################################################################################################
    
    def test2write3(self):
        global marks
        if self.radioButton_3847.isChecked():
            marks += 1
        if self.radioButton_3702.isChecked():
            marks += 1
        if self.radioButton_3708.isChecked():
            marks += 1
        if self.radioButton_3712.isChecked():
            marks += 1
        if self.radioButton_3716.isChecked():
            marks += 1
        if self.radioButton_3850.isChecked():
            marks += 1
        if self.radioButton_3721.isChecked():
            marks += 1
        if self.radioButton_3855.isChecked():
            marks += 1
        if self.radioButton_3731.isChecked():
            marks += 1
        if self.radioButton_3736.isChecked():
            marks += 1
        if self.radioButton_3738.isChecked():
            marks += 1
            
        self.pushButton_105.setEnabled(False)
        model = '23 = D, 24 = B \n 25 = D, 4 = 26 \n 27 = B, 28 = D \n 29 = A, 30 = A \n 31 = C , 32 = B \n 33 = C'
        self.message(11, model)
#######################################################################################################
    
    def test2write4(self):
        global marks
        if self.radioButton_3743.isChecked():
            marks += 1
        if self.radioButton_3746.isChecked():
            marks += 1
        if self.radioButton_3860.isChecked():
            marks += 1
        if self.radioButton_3756.isChecked():
            marks += 1
        if self.radioButton_3759.isChecked():
            marks += 1
        if self.radioButton_3764.isChecked():
            marks += 1
        if self.radioButton_3863.isChecked():
            marks += 1
        if self.radioButton_3868.isChecked():
            marks += 1
        if self.radioButton_3869.isChecked():
            marks += 1
        if self.radioButton_3777.isChecked():
            marks += 1
        if self.radioButton_3875.isChecked():
            marks += 1
            
        self.pushButton_106.setEnabled(False)
        model = '34 = A, 35 = B \n 36 = A, 37 = B \n 38 = C, 39 = D \n 40 = B, 41 = C \n 42 = C , 43 = D \n 44 = A'
        self.message(11, model)

#######################################################################################################
  
    def test2mathnocalc(self):
        global marks
        if self.radioButton_2714.isChecked():
            marks += 1
        if self.radioButton_2723.isChecked():
            marks += 1
        if self.radioButton_2728.isChecked():
            marks += 1
        if self.radioButton_2737.isChecked():
            marks += 1
        if self.radioButton_2747.isChecked():
            marks += 1
        if self.radioButton_2752.isChecked():
            marks += 1
        if self.radioButton_2761.isChecked():
            marks += 1
        if self.radioButton_2770.isChecked():
            marks += 1
        if self.radioButton_2776.isChecked():
            marks += 1
        if self.radioButton_2784.isChecked():
            marks += 1
        if self.radioButton_2942.isChecked():
            marks += 1
        if self.radioButton_2951.isChecked():
            marks += 1
        if self.radioButton_2957.isChecked():
            marks += 1
        if self.radioButton_2964.isChecked():
            marks += 1
        if self.radioButton_3119.isChecked():
            marks += 1
        if self.lineEdit_62.text() == "6":
            marks += 1
        if self.lineEdit_63.text() == "2.3":
            marks += 1
        if self.lineEdit_64.text() == "28" :
            marks += 1
        if self.lineEdit_65.text() == "3.25 & 13/4" :
            marks += 1
        if self.lineEdit_65.text() == "13/4" :
            marks += 1
        if self.lineEdit_65.text() == "3.25" :
            marks += 1
        if self.lineEdit_66.text() == "108" :
            marks += 1

        self.pushButton_112.setEnabled(False)
        model = '1 = C, 2 = A \n 3 = C, 4 = C \n 5 = A, 6 = C \n 7 = C, 8 = B\n 9 = D, 10 = D \n 11 = C, 12 = A \n 13 = D, 14 = D \n 15 = 6, 16 = 2,3 \n 17 = 28, 18 = 3.25 & 13/4 \n 19 = 108, 20 = B'
        self.message(20, model)  
        
########################################################################################################
    def test2mathcalc(self):
        global marks
        if self.radioButton_2789.isChecked():
            marks += 1
        if self.radioButton_2797.isChecked():
            marks += 1
        if self.radioButton_2804.isChecked():
            marks += 1
        if self.radioButton_2815.isChecked():
            marks += 1
        if self.radioButton_2821.isChecked():
            marks += 1
        if self.radioButton_2828.isChecked():
            marks += 1
        if self.radioButton_2836.isChecked():
            marks += 1
        if self.radioButton_2845.isChecked():
            marks += 1
        if self.radioButton_2853.isChecked():
            marks += 1
        if self.radioButton_2861.isChecked():
            marks += 1
    
        if self.radioButton_2874.isChecked():
            marks += 1
        if self.radioButton_2882.isChecked():
            marks += 1
        if self.radioButton_2889.isChecked():
            marks += 1
        if self.radioButton_2899.isChecked():
            marks += 1
        if self.radioButton_2905.isChecked():
            marks += 1
        if self.radioButton_2914.isChecked():
            marks += 1
        if self.radioButton_2923.isChecked():
            marks += 1
        if self.radioButton_2931.isChecked():
            marks += 1
        if self.radioButton_2936.isChecked():
            marks += 1


        self.pushButton_109.setEnabled(False)
        model = '1 = B, 2 = D \n 3 = C, 4 = A\n 5 = C, 6 = D \n 7 = D, 8 = C\n 9 = C, 10 = C \n 11 = C, 12 = B \n 13 = C, 14 = A \n 15 = B, 16 = B,3 \n 17 = A, 18 = B \n 19 = D'
        self.message(19, model)  
##########################################################################################        
    def test2mathcalc2(self):
        global marks
        if self.radioButton_2867.isChecked():
            marks += 1
        if self.radioButton_3038.isChecked():
            marks += 1
        if self.radioButton_3046.isChecked():
            marks += 1
        if self.radioButton_3062.isChecked():
            marks += 1
        if self.radioButton_3069.isChecked():
            marks += 1
        if self.radioButton_3076.isChecked():
            marks += 1
        if self.radioButton_3086.isChecked():
            marks += 1
        if self.radioButton_3094.isChecked():
            marks += 1
        if self.radioButton_3103.isChecked():
            marks += 1
            
        if self.radioButton_3055.isChecked():
            marks += 1
        if self.radioButton_3108.isChecked():
            marks += 1
        if self.lineEdit_54.text() == "1 , 3 , 4 , 12":
            marks += 1
        if self.lineEdit_55.text() == "4 , 5 , 6":
            marks += 1
        if self.lineEdit_56.text() == "15" :
            marks += 1
        if self.lineEdit_57.text() == "2.5 , 5/2" :
            marks += 1
        if self.lineEdit_58.text() == "90" :
            marks += 1
        if self.lineEdit_59.text() == "138 , 137" :
            marks += 1
        if self.lineEdit_60.text() == "36" :
            marks += 1
        if self.lineEdit_61.text() == "135" :
            marks += 1
        self.pushButton_110.setEnabled(False)
        model = '20 = D, 21 = C \n 22 = B, 23 = B\n 24 = B, 25 = D \n 26 = B, 27 = B\n 28 = A, 29 = D \n 30 = B\n 31 = 1 , 3 , 4 , 12 \n 32 = 4 , 5 , 6\n 33 = 15 \n 34 = 2.5 , 5/2 \n 35 = 90, 36 = 138 , 137 \n 37 = 36, 38 = 135'
        self.message(19, model) 
#########################################################################################         
    def test3read1(self):
        global marks
        '''  
        nums = ['2062','2065','2114','2123','2128','2129','2136','2140','2142']
        name = 'self.radioButton_'
        for n in nums:
            if eval(name+n+'.isChecked()'):
                marks+=1
            
        '''
        if self.radioButton_2062.isChecked():
            marks += 1
        if self.radioButton_2065.isChecked():
            marks += 1
        if self.radioButton_2114.isChecked():
            marks += 1
        if self.radioButton_2119.isChecked():
            marks += 1
        if self.radioButton_2123.isChecked():
            marks += 1
        if self.radioButton_2128.isChecked():
            marks += 1
        if self.radioButton_2129.isChecked():
            marks += 1
        if self.radioButton_2136.isChecked():
            marks += 1
        if self.radioButton_2140.isChecked():
            marks += 1
        if self.radioButton_2142.isChecked():
            marks += 1
          
        self.pushButton_70.setEnabled(False)
        model = '1 = D, 2 = B \n 3 = B, 4 = A \n 5 = C, 6 = A \n 7 = C, 8 = C \n 9 = B, 10 = C'
        self.message(10, model)
##########################################################################################
    def test3read2(self):
        global marks
        if self.radioButton_2146.isChecked():
            marks += 1
        if self.radioButton_2228.isChecked():
            marks += 1
        if self.radioButton_2232.isChecked():
            marks += 1
        if self.radioButton_2234.isChecked():
            marks += 1
        if self.radioButton_2238.isChecked():
            marks += 1
        if self.radioButton_2244.isChecked():
            marks += 1
        if self.radioButton_2247.isChecked():
            marks += 1
        if self.radioButton_2250.isChecked():
            marks += 1
        if self.radioButton_2253.isChecked():
            marks += 1
        if self.radioButton_2260.isChecked():
            marks += 1
            
        self.pushButton_77.setEnabled(False)
        model = '1 = D, 2 = D \n 3 = D, 4 = B \n 5 = B, 6 = C \n 7 = A, 8 = A\n 9 = C, 10 = D'
        self.message(10, model)
        
#######################################################################################################
    def test3read3(self):
        global marks
        if self.radioButton_2264.isChecked():
            marks += 1
        if self.radioButton_2265.isChecked():
            marks += 1
        if self.radioButton_2476.isChecked():
            marks += 1
        if self.radioButton_2479.isChecked():
            marks += 1
        if self.radioButton_2483.isChecked():
            marks += 1
        if self.radioButton_2485.isChecked():
            marks += 1
        if self.radioButton_2491.isChecked():
            marks += 1
        if self.radioButton_2493.isChecked():
            marks += 1
        if self.radioButton_2499.isChecked():
            marks += 1
        if self.radioButton_2502.isChecked():
            marks += 1
        if self.radioButton_2506.isChecked():
            marks += 1
                        
        self.pushButton_81.setEnabled(False)
        model = '1 = A , 2 = B \n 3 = D, 4 = A \n 5 = C, 6 = B \n 7 = A, 8 = D\n 9 = D, 10 = C \n 11 = B'
        self.message(11, model)
        
##########################################################################################
    def test3read4(self):
        global marks
        if self.radioButton_4202.isChecked():
            marks += 1
        if self.radioButton_4206.isChecked():
            marks += 1
        if self.radioButton_4241.isChecked():
            marks += 1
        if self.radioButton_4214.isChecked():
            marks += 1
        if self.radioButton_4217.isChecked():
            marks += 1
        if self.radioButton_4224.isChecked():
            marks += 1
        if self.radioButton_4225.isChecked():
            marks += 1
        if self.radioButton_4229.isChecked():
            marks += 1
        if self.radioButton_4233.isChecked():
            marks += 1
        if self.radioButton_4237.isChecked():
            marks += 1
        if self.radioButton_4247.isChecked():
            marks += 1

        self.pushButton_113.setEnabled(False)
        model = '1 = D , 2 = A \n 3 = A, 4 = B \n 5 = A, 6 = A \n 7 = C, 8 = D\n 9 = C, 10 = A \n 11 = C'
        self.message(11, model)
        
#########################################################################################
##########################################################################################
    def test3read5(self):
        global marks
        if self.radioButton_4211.isChecked():
            marks += 1
        if self.radioButton_4252.isChecked():
            marks += 1
        if self.radioButton_4253.isChecked():
            marks += 1
        if self.radioButton_4260.isChecked():
            marks += 1
        if self.radioButton_4263.isChecked():
            marks += 1
        if self.radioButton_4268.isChecked():
            marks += 1
        if self.radioButton_4271.isChecked():
            marks += 1
        if self.radioButton_4275.isChecked():
            marks += 1
        if self.radioButton_4277.isChecked():
            marks += 1
        if self.radioButton_4284.isChecked():
            marks += 1
            
        self.pushButton_114.setEnabled(False)
        model = '1 = C, 2 = D \n 3 = A, 4 = D \n 5 = C, 6 = A \n 7 = A, 8 = B\n 9 = C, 10 = D'
        self.message(10, model)
        
#################################################################################################################################################################################
    def test3write1(self):
        global marks
        if self.radioButton_3136.isChecked():
            marks += 1
        if self.radioButton_3137.isChecked():
            marks += 1
        if self.radioButton_3147.isChecked():
            marks += 1
        if self.radioButton_3160.isChecked():
            marks += 1
        if self.radioButton_3163.isChecked():
            marks += 1
        if self.radioButton_3170.isChecked():
            marks += 1
        if self.radioButton_3173.isChecked():
            marks += 1
        if self.radioButton_3179.isChecked():
            marks += 1
        if self.radioButton_3184.isChecked():
            marks += 1
        if self.radioButton_3186.isChecked():
            marks += 1
        if self.radioButton_3191.isChecked():
            marks += 1
            
        self.pushButton_86.setEnabled(False)
        model = '1 = D, 2 = A \n 3 = D, 4 = B \n 5 = C, 6 = B \n 7 = A, 8 = C \n 9 = D , 10 = B \n 11 = C'
        self.message(11, model)
        
##########################################################################################
    def test3write2(self):
        global marks
        if self.radioButton_3196.isChecked():
            marks += 1
        if self.radioButton_3197.isChecked():
            marks += 1
        if self.radioButton_3202.isChecked():
            marks += 1
        if self.radioButton_3206.isChecked():
            marks += 1
        if self.radioButton_4286.isChecked():
            marks += 1
        if self.radioButton_3213.isChecked():
            marks += 1
        if self.radioButton_4291.isChecked():
            marks += 1
        if self.radioButton_3224.isChecked():
            marks += 1
        if self.radioButton_3228.isChecked():
            marks += 1
        if self.radioButton_3231.isChecked():
            marks += 1
        if self.radioButton_3233.isChecked():
            marks += 1
            
        self.pushButton_87.setEnabled(False)
        model = '12 = D, 13 = A \n 14 = B, 15 = C \n 16 = B, 17 = A \n 18 = C, 19 = D \n 20 = D , 21 = A \n 22 = A'
        self.message(11, model)
##########################################################################################        
    def test3write3(self):
        global marks
        if self.radioButton_4294.isChecked():
            marks += 1
        if self.radioButton_3241.isChecked():
            marks += 1
        if self.radioButton_3246.isChecked():
            marks += 1
        if self.radioButton_4298.isChecked():
            marks += 1
        if self.radioButton_3255.isChecked():
            marks += 1
        if self.radioButton_3260.isChecked():
            marks += 1
        if self.radioButton_3264.isChecked():
            marks += 1
        if self.radioButton_3265.isChecked():
            marks += 1
        if self.radioButton_3270.isChecked():
            marks += 1
        if self.radioButton_4303.isChecked():
            marks += 1
        if self.radioButton_3249.isChecked():
            marks += 1
            
        self.pushButton_88.setEnabled(False)
        model = '23 = B, 24 = A \n 25 = B, 26 = B \n 27 = C, 28 = D \n 29 = B, 30 = C \n 31 = A , 32 = C \n 33 = D'
        self.message(11, model)
##########################################################################################        
    def test3write4(self):
        global marks
        if self.radioButton_4309.isChecked():
            marks += 1
        if self.radioButton_3286.isChecked():
            marks += 1
        if self.radioButton_3292.isChecked():
            marks += 1
        if self.radioButton_4306.isChecked():
            marks += 1
        if self.radioButton_4315.isChecked():
            marks += 1
        if self.radioButton_3304.isChecked():
            marks += 1
        if self.radioButton_4318.isChecked():
            marks += 1
        if self.radioButton_3310.isChecked():
            marks += 1
        if self.radioButton_3313.isChecked():
            marks += 1
        if self.radioButton_3318.isChecked():
            marks += 1
        if self.radioButton_3323.isChecked():
            marks += 1
            
        self.pushButton_89.setEnabled(False)
        model = '34 = B, 35 = B \n 36 = D, 37 = A\n 38 = D, 39 = D \n 40 = C, 41 = A \n 42 = D , 43 = A \n 44 = C'
        self.message(11, model)
#######################################################################################################
    def test3mathnocalc(self):

        global marks
        if self.radioButton_3326.isChecked():
            marks += 1
        if self.radioButton_3333.isChecked():
            marks += 1
        if self.radioButton_3341.isChecked():
            marks += 1
        if self.radioButton_3352.isChecked():
            marks += 1
        if self.radioButton_3357.isChecked():
            marks += 1
        if self.radioButton_3368.isChecked():
            marks += 1
        if self.radioButton_3374.isChecked():
            marks += 1
        if self.radioButton_3383.isChecked():
            marks += 1
        if self.radioButton_3390.isChecked():
            marks += 1
        if self.radioButton_3397.isChecked():
            marks += 1
        if self.radioButton_3402.isChecked():
            marks += 1
        if self.radioButton_3626.isChecked():
            marks += 1
        if self.radioButton_3656.isChecked():
            marks += 1
        if self.radioButton_3700.isChecked():
            marks += 1
        if self.radioButton_3725.isChecked():
            marks += 1
        if self.lineEdit_41.text() == "1, 2, 4, 8, 16":
            marks += 1
        if self.lineEdit.text() == "15/4, 3.75":
            marks += 1
        if self.lineEdit_43.text() == "30" :
            marks += 1
        if self.lineEdit_44.text() == "3/2, 1.5" :
            marks += 1
        if self.lineEdit_45.text() == "1/6, 0.166, 0.167" :
            marks += 1


        self.pushButton_92.setEnabled(False)
        model = '1 = B, 2 = B \n 3 = C, 4 = A \n 5 = D, 6 = A\n 7 = C, 8 = B\n 9 = C, 10 = D \n 11 = B, 12 = D \n 13 = A, 14 = A \n 15 = D\n 16 = 1, 2, 4, 8, 16 \n 17 = 15/4, 3.75, 18 = 30 \n 19 = 3/2, 1.5\n 20 = 1/6, 0.166, 0.167'
        self.message(20, model)  

##########################################################################################
    def test3mathcalc(self):
        global marks
        if self.radioButton_4153.isChecked():
            marks += 1
        if self.radioButton_3915.isChecked():
            marks += 1
        if self.radioButton_3922.isChecked():
            marks += 1
        if self.radioButton_3931.isChecked():
            marks += 1
        if self.radioButton_3940.isChecked():
            marks += 1
        if self.radioButton_3947.isChecked():
            marks += 1
        if self.radioButton_3953.isChecked():
            marks += 1
        if self.radioButton_3963.isChecked():
            marks += 1
        if self.radioButton_3971.isChecked():
            marks += 1
        if self.radioButton_3979.isChecked():
            marks += 1
        if self.radioButton_3990.isChecked():
            marks += 1
        if self.radioButton_4000.isChecked():
            marks += 1
        if self.radioButton_4007.isChecked():
            marks += 1
        if self.radioButton_4013.isChecked():
            marks += 1
        if self.radioButton_4022.isChecked():
            marks += 1
        if self.radioButton_4039.isChecked():
            marks += 1
        if self.radioButton_4048.isChecked():
            marks += 1
        if self.radioButton_4159.isChecked():
            marks += 1

        self.pushButton_96.setEnabled(False)
        model = '1 = A, 2 = C \n 3 = D, 4 = B \n 5 = C, 6 = D\n 7 = D, 8 = B\n 9 = B, 10 = B \n 11 = D, 12 = A \n 13 = B, 14 = D \n 15 = B\n 16 = B \n 17 = C, 18 = C'
        self.message(18, model)  
##########################################################################################
    def test3mathcalc2(self):
        global marks
        if self.radioButton_4057.isChecked():
            marks += 1
        if self.radioButton_4063.isChecked():
            marks += 1
        if self.radioButton_4067.isChecked():
            marks += 1
        if self.radioButton_4164.isChecked():
            marks += 1
        if self.radioButton_4071.isChecked():
            marks += 1
        if self.radioButton_4077.isChecked():
            marks += 1
        if self.radioButton_4088.isChecked():
            marks += 1
        if self.radioButton_4094.isChecked():
            marks += 1
        if self.radioButton_4102.isChecked():
            marks += 1
        if self.radioButton_4112.isChecked():
            marks += 1
    
        if self.radioButton_4119.isChecked():
            marks += 1
        if self.radioButton_4125.isChecked():
            marks += 1

        self.pushButton_97.setEnabled(False)
        model = '19 = A, 20 = C \n 21 = D, 22 = D \n 23 = B, 24 = B\n 25 = A, 26 = C\n 27 = C, 28 = A \n 29 = B, 30 = D'
        self.message(12, model)
##########################################################################################
    def test3mathcalc3(self):
        global marks
        if self.lineEdit_53.text() == "10":
            marks += 1
        if self.lineEdit_52.text() == "31":
            marks += 1
        if self.lineEdit_51.text() == "97, 98, 99, 100, 101" :
            marks += 1
        if self.lineEdit_50.text() == "5" :
            marks += 1
        if self.lineEdit_49.text() == "1.25, 5/4" :
            marks += 1
        if self.lineEdit_48.text() == "2.6, 13/5":
            marks += 1
        if self.lineEdit_47.text() == "30":
            marks += 1
        if self.lineEdit_46.text() == "8" :
            marks += 1

        self.pushButton_111.setEnabled(False)
        model = '31 = 10, 32 = 31 \n 33 = 97, 98, 99, 100, 101\n 34 = 5, 35 = 1.25, 5/4 \n 36 = 2.6, 13/5 \n 37 = 30, 38 = 8'
        self.message(8, model)  

#######################################################################################################

    def test4read1(self):
        global marks
        if self.radioButton_3982.isChecked():
            marks += 1
        if self.radioButton_4031.isChecked():
            marks += 1
        if self.radioButton_4053.isChecked():
            marks += 1
        if self.radioButton_4168.isChecked():
            marks += 1
        if self.radioButton_4172.isChecked():
            marks += 1
        if self.radioButton_4173.isChecked():
            marks += 1
        if self.radioButton_4179.isChecked():
            marks += 1
        if self.radioButton_4182.isChecked():
            marks += 1
        if self.radioButton_4188.isChecked():
            marks += 1
        if self.radioButton_4189.isChecked():
            marks += 1
            
        self.pushButton_107.setEnabled(False)
        model = '1 = D, 2 = C \n 3 = C, 4 = D \n 5 = D, 6 = B \n 7 = A, 8 = A\n 9 = B, 10 = A'
        self.message(10, model)
        
    def test4read2(self):
        global marks
        if self.radioButton_4195.isChecked():
            marks += 1
        if self.radioButton_4200.isChecked():
            marks += 1
        if self.radioButton_4321.isChecked():
            marks += 1
        if self.radioButton_4327.isChecked():
            marks += 1
        if self.radioButton_4329.isChecked():
            marks += 1
        if self.radioButton_4332.isChecked():
            marks += 1
        if self.radioButton_4336.isChecked():
            marks += 1
        if self.radioButton_4343.isChecked():
            marks += 1
        if self.radioButton_4347.isChecked():
            marks += 1
        if self.radioButton_4351.isChecked():
            marks += 1
            
        self.pushButton_108.setEnabled(False)
        model = '1 = C, 2 = D \n 3 = B, 4 = D \n 5 = B, 6 = B \n 7 = C, 8 = C\n 9 = B, 10 = D'
        self.message(10, model)
        
    def test4read3(self):
        global marks
        if self.radioButton_4352.isChecked():
            marks += 1
        if self.radioButton_4358.isChecked():
            marks += 1
        if self.radioButton_4362.isChecked():
            marks += 1
        if self.radioButton_4366.isChecked():
            marks += 1
        if self.radioButton_4370.isChecked():
            marks += 1
        if self.radioButton_4375.isChecked():
            marks += 1
        if self.radioButton_4377.isChecked():
            marks += 1
        if self.radioButton_4382.isChecked():
            marks += 1
        if self.radioButton_4385.isChecked():
            marks += 1
        if self.radioButton_4390.isChecked():
            marks += 1
            
        self.pushButton_115.setEnabled(False)
        model = '1 = B, 2 = C \n 3 = A, 4 = A \n 5 = C, 6 = A \n 7 = B, 8 = B\n 9 = A, 10 = B'
        self.message(10, model)
        
    def test4read4(self):
        global marks
        if self.radioButton_4394.isChecked():
            marks += 1
        if self.radioButton_4399.isChecked():
            marks += 1
        if self.radioButton_4401.isChecked():
            marks += 1
        if self.radioButton_4406.isChecked():
            marks += 1
        if self.radioButton_4410.isChecked():
            marks += 1
        if self.radioButton_4412.isChecked():
            marks += 1
        if self.radioButton_4416.isChecked():
            marks += 1
        if self.radioButton_4421.isChecked():
            marks += 1
        if self.radioButton_4426.isChecked():
            marks += 1
        if self.radioButton_4431.isChecked():
            marks += 1
            
        self.pushButton_116.setEnabled(False)
        model = '1 = C, 2 = D \n 3 = B, 4 = A \n 5 = C, 6 = B \n 7 = C, 8 = A\n 9 = D, 10 = D'
        self.message(10, model)
        
    def test4read5(self):
        global marks
        if self.radioButton_4434.isChecked():
            marks += 1
        if self.radioButton_4439.isChecked():
            marks += 1
        if self.radioButton_4443.isChecked():
            marks += 1
        if self.radioButton_4447.isChecked():
            marks += 1
        if self.radioButton_4450.isChecked():
            marks += 1
        if self.radioButton_4453.isChecked():
            marks += 1
        if self.radioButton_4457.isChecked():
            marks += 1
        if self.radioButton_4463.isChecked():
            marks += 1
        if self.radioButton_4467.isChecked():
            marks += 1
        if self.radioButton_4470.isChecked():
            marks += 1
            
        self.pushButton_117.setEnabled(False)
        model = '1 = C, 2 = D \n 3 = A, 4 = D \n 5 = A, 6 = B \n 7 = D, 8 = D\n 9 = C, 10 = C'
        self.message(10, model)
        
        
    def test4write1(self):
        global marks
        if self.radioButton_4479.isChecked():
            marks += 1
        if self.radioButton_4956.isChecked():
            marks += 1
        if self.radioButton_4487.isChecked():
            marks += 1
        if self.radioButton_4489.isChecked():
            marks += 1
        if self.radioButton_4495.isChecked():
            marks += 1
        if self.radioButton_4497.isChecked():
            marks += 1
        if self.radioButton_4503.isChecked():
            marks += 1
        if self.radioButton_4505.isChecked():
            marks += 1
        if self.radioButton_4510.isChecked():
            marks += 1
        if self.radioButton_4515.isChecked():
            marks += 1
        if self.radioButton_4519.isChecked():
            marks += 1
            
        self.pushButton_118.setEnabled(False)
        model = '1 = D, 2 = B \n 3 = A, 4 = C \n 5 = D, 6 = B \n 7 = A, 8 = C \n 9 = C , 10 = C \n 11 = D'
        self.message(11, model)
        
    def test4write2(self):
        global marks
        if self.radioButton_4520.isChecked():
            marks += 1
        if self.radioButton_4524.isChecked():
            marks += 1
        if self.radioButton_4529.isChecked():
            marks += 1
        if self.radioButton_4532.isChecked():
            marks += 1
        if self.radioButton_4536.isChecked():
            marks += 1
        if self.radioButton_4543.isChecked():
            marks += 1
        if self.radioButton_4547.isChecked():
            marks += 1
        if self.radioButton_4550.isChecked():
            marks += 1
        if self.radioButton_4552.isChecked():
            marks += 1
        if self.radioButton_4556.isChecked():
            marks += 1
        if self.radioButton_4563.isChecked():
            marks += 1
            
        self.pushButton_119.setEnabled(False)
        model = '12 = B, 13 = A \n 14 = B, 15 = A \n 16 = A, 17 = D \n 18 = D, 19 = C \n 20 = D , 21 = B \n 22 = A'
        self.message(11, model)
        
    def test4write3(self):
        global marks
        if self.radioButton_4960.isChecked():
            marks += 1
        if self.radioButton_4571.isChecked():
            marks += 1
        if self.radioButton_5269.isChecked():
            marks += 1
        if self.radioButton_4579.isChecked():
            marks += 1
        if self.radioButton_5272.isChecked():
            marks += 1
        if self.radioButton_4584.isChecked():
            marks += 1
        if self.radioButton_4589.isChecked():
            marks += 1
        if self.radioButton_4594.isChecked():
            marks += 1
        if self.radioButton_4598.isChecked():
            marks += 1
        if self.radioButton_4601.isChecked():
            marks += 1
        if self.radioButton_4604.isChecked():
            marks += 1
            
        self.pushButton_120.setEnabled(False)
        model = '23 = A, 24 = C \n 25 = D, 26 = B \n 27 = B, 28 = C \n 29 = D, 30 = A \n 31 = C , 32 = A \n 33 = B'
        self.message(11, model)
        
    def test4write4(self):
        global marks
        if self.radioButton_5278.isChecked():
            marks += 1
        if self.radioButton_5282.isChecked():
            marks += 1
        if self.radioButton_5286.isChecked():
            marks += 1
        if self.radioButton_5287.isChecked():
            marks += 1
        if self.radioButton_4629.isChecked():
            marks += 1
        if self.radioButton_4632.isChecked():
            marks += 1
        if self.radioButton_4634.isChecked():
            marks += 1
        if self.radioButton_4636.isChecked():
            marks += 1
        if self.radioButton_4640.isChecked():
            marks += 1
        if self.radioButton_4647.isChecked():
            marks += 1
        if self.radioButton_4648.isChecked():
            marks += 1
            
        self.pushButton_121.setEnabled(False)
        model = '34 = A, 35 = C \n 36 = D, 37 = A\n 38 = B, 39 = D \n 40 = B, 41 = D \n 42 = C , 43 = B \n 44 = C'
        self.message(11, model)
        
##########################################################################################
        
    def test5read1(self):
        global marks
        if self.radioButton_4475.isChecked():
            marks += 1
        if self.radioButton_4483.isChecked():
            marks += 1
        if self.radioButton_4566.isChecked():
            marks += 1
        if self.radioButton_4572.isChecked():
            marks += 1
        if self.radioButton_4583.isChecked():
            marks += 1
        if self.radioButton_4612.isChecked():
            marks += 1
        if self.radioButton_4618.isChecked():
            marks += 1
        if self.radioButton_4622.isChecked():
            marks += 1
        if self.radioButton_4625.isChecked():
            marks += 1
        if self.radioButton_5292.isChecked():
            marks += 1
            
        self.pushButton_127.setEnabled(False)
        model = '1 = A, 2 = D \n 3 = A, 4 = C \n 5 = D, 6 = B \n 7 = A, 8 = B\n 9 = A, 10 = C'
        self.message(10, model)
        
    def test5read2(self):
        global marks
        if self.radioButton_5298.isChecked():
            marks += 1
        if self.radioButton_5302.isChecked():
            marks += 1
        if self.radioButton_5305.isChecked():
            marks += 1
        if self.radioButton_5308.isChecked():
            marks += 1
        if self.radioButton_5313.isChecked():
            marks += 1
        if self.radioButton_5317.isChecked():
            marks += 1
        if self.radioButton_5320.isChecked():
            marks += 1
        if self.radioButton_304.isChecked():
            marks += 1
        if self.radioButton_5327.isChecked():
            marks += 1
        if self.radioButton_5333.isChecked():
            marks += 1
            
        self.pushButton_128.setEnabled(False)
        model = '1 = A, 2 = D \n 3 = A, 4 = B \n 5 = C, 6 = C \n 7 = B, 8 = C\n 9 = C, 10 = B'
        self.message(10, model)
        
    def test5read3(self):
        global marks
        if self.radioButton_5338.isChecked():
            marks += 1
        if self.radioButton_5341.isChecked():
            marks += 1
        if self.radioButton_5346.isChecked():
            marks += 1
        if self.radioButton_5348.isChecked():
            marks += 1
        if self.radioButton_5353.isChecked():
            marks += 1
        if self.radioButton_5357.isChecked():
            marks += 1
        if self.radioButton_5361.isChecked():
            marks += 1
        if self.radioButton_5366.isChecked():
            marks += 1
        if self.radioButton_5367.isChecked():
            marks += 1
        if self.radioButton_5373.isChecked():
            marks += 1
            
        self.pushButton_129.setEnabled(False)
        model = '1 = A, 2 = C \n 3 = D, 4 = B \n 5 = C, 6 = C \n 7 = A, 8 = C\n 9 = C, 10 = B'
        self.message(10, model)
        
    def test5read4(self):
        global marks
        if self.radioButton_5375.isChecked():
            marks += 1
        if self.radioButton_5380.isChecked():
            marks += 1
        if self.radioButton_5386.isChecked():
            marks += 1
        if self.radioButton_5387.isChecked():
            marks += 1
        if self.radioButton_5393.isChecked():
            marks += 1
        if self.radioButton_5398.isChecked():
            marks += 1
        if self.radioButton_5400.isChecked():
            marks += 1
        if self.radioButton_5406.isChecked():
            marks += 1
        if self.radioButton_5410.isChecked():
            marks += 1
        if self.radioButton_5414.isChecked():
            marks += 1
            
        self.pushButton_134.setEnabled(False)
        model = '1 = B, 2 = A \n 3 = D, 4 = C \n 5 = C, 6 = A \n 7 = B, 8 = C\n 9 = B, 10 = D'
        self.message(10, model)  
        
    def test5read5(self):
        global marks
        if self.radioButton_5416.isChecked():
            marks += 1
        if self.radioButton_5421.isChecked():
            marks += 1
        if self.radioButton_5425.isChecked():
            marks += 1
        if self.radioButton_5428.isChecked():
            marks += 1
        if self.radioButton_5434.isChecked():
            marks += 1
        if self.radioButton_5437.isChecked():
            marks += 1
        if self.radioButton_5442.isChecked():
            marks += 1
        if self.radioButton_5444.isChecked():
            marks += 1
        if self.radioButton_5448.isChecked():
            marks += 1
        if self.radioButton_5452.isChecked():
            marks += 1
            
        self.pushButton_135.setEnabled(False)
        model = '1 = D, 2 = C \n 3 = D, 4 = B \n 5 = D, 6 = C \n 7 = A, 8 = B\n 9 = A, 10 = B'
        self.message(10, model)
        
    def test5write1(self):
        global marks
        if self.radioButton_5457.isChecked():
            marks += 1
        if self.radioButton_5459.isChecked():
            marks += 1
        if self.radioButton_5466.isChecked():
            marks += 1
        if self.radioButton_5468.isChecked():
            marks += 1
        if self.radioButton_5474.isChecked():
            marks += 1
        if self.radioButton_5477.isChecked():
            marks += 1
        if self.radioButton_5482.isChecked():
            marks += 1
        if self.radioButton_6020.isChecked():
            marks += 1
        if self.radioButton_6024.isChecked():
            marks += 1
        if self.radioButton_6029.isChecked():
            marks += 1
        if self.radioButton_6032.isChecked():
            marks += 1
            
        self.pushButton_136.setEnabled(False)
        model = '1 = C, 2 = D \n 3 = A, 4 = C \n 5 = D, 6 = C \n 7 = B, 8 = D \n 9 = A , 10 = B \n 11 = B'
        self.message(11, model)
        
    def test5write2(self):
        global marks
        if self.radioButton_5502.isChecked():
            marks += 1
        if self.radioButton_5504.isChecked():
            marks += 1
        if self.radioButton_5510.isChecked():
            marks += 1
        if self.radioButton_5513.isChecked():
            marks += 1
        if self.radioButton_5515.isChecked():
            marks += 1
        if self.radioButton_6036.isChecked():
            marks += 1
        if self.radioButton_5525.isChecked():
            marks += 1
        if self.radioButton_5528.isChecked():
            marks += 1
        if self.radioButton_5532.isChecked():
            marks += 1
        if self.radioButton_5537.isChecked():
            marks += 1
        if self.radioButton_5541.isChecked():
            marks += 1
            
        self.pushButton_137.setEnabled(False)
        model = '12 = A, 13 = B \n 14 = D, 15 = B \n 16 = A, 17 = B \n 18 = B, 19 = B \n 20 = A , 21 = D \n 22 = D'
        self.message(11, model)
        
    def test5write3(self):
        global marks
        if self.radioButton_5546.isChecked():
            marks += 1
        if self.radioButton_5548.isChecked():
            marks += 1
        if self.radioButton_5551.isChecked():
            marks += 1
        if self.radioButton_5555.isChecked():
            marks += 1
        if self.radioButton_5562.isChecked():
            marks += 1
        if self.radioButton_5565.isChecked():
            marks += 1
        if self.radioButton_5569.isChecked():
            marks += 1
        if self.radioButton_6040.isChecked():
            marks += 1
        if self.radioButton_5577.isChecked():
            marks += 1
        if self.radioButton_5580.isChecked():
            marks += 1
        if self.radioButton_6044.isChecked():
            marks += 1
            
        self.pushButton_138.setEnabled(False)
        model = '23 = D, 24 = B \n 25 = C, 26 = A \n 27 = A, 28 = B \n 29 = C, 30 = B \n 31 = C , 32 = A \n 33 = A'
        self.message(11, model)
        
    def test5write4(self):
        global marks
        if self.radioButton_5591.isChecked():
            marks += 1
        if self.radioButton_6049.isChecked():
            marks += 1
        if self.radioButton_5597.isChecked():
            marks += 1
        if self.radioButton_5601.isChecked():
            marks += 1
        if self.radioButton_5606.isChecked():
            marks += 1
        if self.radioButton_5607.isChecked():
            marks += 1
        if self.radioButton_5612.isChecked():
            marks += 1
        if self.radioButton_5617.isChecked():
            marks += 1
        if self.radioButton_5619.isChecked():
            marks += 1
        if self.radioButton_5626.isChecked():
            marks += 1
        if self.radioButton_5629.isChecked():
            marks += 1
            
        self.pushButton_139.setEnabled(False)
        model = '34 = B, 35 = A \n 36 = B, 37 = C\n 38 = D, 39 = A \n 40 = C, 41 = B \n 42 = C , 43 = D \n 44 = A'
        self.message(11, model)
        
    def test4mathnocalc(self):
        global marks
        if self.radioButton_5483.isChecked():
            marks += 1
        if self.radioButton_5492.isChecked():
            marks += 1
        if self.radioButton_5521.isChecked():
            marks += 1
        if self.radioButton_5584.isChecked():
            marks += 1
        if self.radioButton_6054.isChecked():
            marks += 1
        if self.radioButton_6062.isChecked():
            marks += 1
        if self.radioButton_6070.isChecked():
            marks += 1
        if self.radioButton_6078.isChecked():
            marks += 1
        if self.radioButton_6089.isChecked():
            marks += 1
        if self.radioButton_6096.isChecked():
            marks += 1
        if self.radioButton_4652.isChecked():
            marks += 1
        if self.radioButton_4661.isChecked():
            marks += 1
        if self.radioButton_4668.isChecked():
            marks += 1
        if self.radioButton_4677.isChecked():
            marks += 1
        if self.radioButton_6980.isChecked():
            marks += 1
        if self.lineEdit_21.text() == "15/4 or 3.75" :
            marks += 1
        if self.lineEdit_21.text() == "15/4" :
            marks += 1
        if self.lineEdit_21.text() == "3.75" :
            marks += 1
        if self.lineEdit_29.text() == "2" :
            marks += 1
        if self.lineEdit_30.text() == "36" :
            marks += 1
        if self.lineEdit_31.text() == "5/6 or 0.833" :
            marks += 1
        if self.lineEdit_31.text() == "0.833" :
            marks += 1
        if self.lineEdit_31.text() == "5/6" :
            marks += 1
        if self.lineEdit_32.text() == "5/12 or 0.416 or 0.417" :
            marks += 1
        if self.lineEdit_32.text() == "5/12" :
            marks += 1
        if self.lineEdit_32.text() == "0.417" :
            marks += 1
        if self.lineEdit_32.text() == "0.416" :
            marks += 1

        self.pushButton_170.setEnabled(False)
        model = '1 = B, 2 = C \n 3 = A, 4 = B \n 5 = D, 6 = C\n 7 = D, 8 = D\n 9 = A, 10 = B \n 11 = A, 12 = D \n 13 = C, 14 = C \n 15 = 15/4 or 3.75\n 16 = 2\n 17 = 36, 18 = 5/6 or 0.833 \n 19 = 5/12 or 0.416 or 0.417\n 20 =B'
        self.message(20, model)
        
    def test4mathcalc(self):
        global marks
        if self.radioButton_4691.isChecked():
            marks += 1
        if self.radioButton_4699.isChecked():
            marks += 1
        if self.radioButton_4708.isChecked():
            marks += 1
        if self.radioButton_4717.isChecked():
            marks += 1
        if self.radioButton_4726.isChecked():
            marks += 1
        if self.radioButton_4736.isChecked():
            marks += 1
        if self.radioButton_4745.isChecked():
            marks += 1
        if self.radioButton_4752.isChecked():
            marks += 1
        if self.radioButton_4762.isChecked():
            marks += 1
        if self.radioButton_6959.isChecked():
            marks += 1
        if self.radioButton_4769.isChecked():
            marks += 1
        if self.radioButton_4775.isChecked():
            marks += 1
        if self.radioButton_4783.isChecked():
            marks += 1
        if self.radioButton_4792.isChecked():
            marks += 1
        if self.radioButton_4802.isChecked():
            marks += 1
        if self.radioButton_6961.isChecked():
            marks += 1
        if self.radioButton_4812.isChecked():
            marks += 1
        if self.radioButton_4819.isChecked():
            marks += 1
        if self.radioButton_4830.isChecked():
            marks += 1

        self.pushButton_148.setEnabled(False)
        model = '1 = A, 2 = B \n 3 = D, 4 = B \n 5 = C, 6 = C\n 7 = B, 8 = C\n 9 = A, 10 = D \n 11 = C, 12 = B \n 13 = D, 14 = D \n 15 = A\n 16 = A \n 17 = C, 18 = A \n 19 = C'
        self.message(19, model)
        
    def test4mathcalc2(self):
        global marks
        if self.radioButton_4833.isChecked():
            marks += 1
        if self.radioButton_6985.isChecked():
            marks += 1
        if self.radioButton_6993.isChecked():
            marks += 1
        if self.radioButton_7001.isChecked():
            marks += 1
        if self.radioButton_7010.isChecked():
            marks += 1
        if self.radioButton_7018.isChecked():
            marks += 1
        if self.radioButton_7026.isChecked():
            marks += 1
        if self.radioButton_7033.isChecked():
            marks += 1
        if self.radioButton_7038.isChecked():
            marks += 1
            
        if self.radioButton_6975.isChecked():
            marks += 1
        if self.radioButton_6972.isChecked():
            marks += 1
        if self.lineEdit_33.text() == "48" :
            marks += 1
        if self.lineEdit_34.text() == "558" :
            marks += 1
        if self.lineEdit_35.text() == "3.5" :
            marks += 1
        if self.lineEdit_35.text() == "7/2" :
            marks += 1
        if self.lineEdit_35.text() == "7/2 or 3.5" :
            marks += 1
        if self.lineEdit_36.text() == "16" :
            marks += 1
        if self.lineEdit_37.text() == "30" :
            marks += 1
        if self.lineEdit_38.text() == "0" :
            marks += 1
        if self.lineEdit_39.text() == "195" :
            marks += 1
        if self.lineEdit_40.text() == "15" :
            marks += 1

        self.pushButton_172.setEnabled(False)
        model = '20 = C, 21 = B \n 22 = B, 23 = D\n 24 = C, 25 = B \n 26 = D, 27 = D\n 28 = B, 29 = 48 \n 30 = 558\n 31 = 7/2 or 3.5 \n 32 = 16 \n 33 = 30 \n 34 = 0 \n 35 = 195, 36 = 15 \n 37 = A , 38 = B'
        self.message(19, model)
        
    def test5mathnocalc(self):
        global marks
        if self.radioButton_4865.isChecked():
            marks += 1
        if self.radioButton_4871.isChecked():
            marks += 1
        if self.radioButton_4880.isChecked():
            marks += 1
        if self.radioButton_4888.isChecked():
            marks += 1
        if self.radioButton_4897.isChecked():
            marks += 1
        if self.radioButton_4905.isChecked():
            marks += 1
        if self.radioButton_4914.isChecked():
            marks += 1
        if self.radioButton_4919.isChecked():
            marks += 1
        if self.radioButton_4928.isChecked():
            marks += 1
        if self.radioButton_4935.isChecked():
            marks += 1
        if self.radioButton_4939.isChecked():
            marks += 1
        if self.radioButton_5636.isChecked():
            marks += 1
        if self.radioButton_5645.isChecked():
            marks += 1
        if self.radioButton_5651.isChecked():
            marks += 1
        if self.radioButton_5662.isChecked():
            marks += 1
        if self.lineEdit_24.text() == "5" :
            marks += 1
        if self.lineEdit_25.text() == "5/13 or 0.384 or 0.385" :
            marks += 1
        if self.lineEdit_25.text() == "0.384" :
            marks += 1
        if self.lineEdit_25.text() == ".384" :
            marks += 1
        if self.lineEdit_25.text() == "0.385" :
            marks += 1
        if self.lineEdit_25.text() == ".385" :
            marks += 1
        if self.lineEdit_25.text() == "5/13" :
            marks += 1
        if self.lineEdit_26.text() == "130" :
            marks += 1
        if self.lineEdit_27.text() == "2" :
            marks += 1
        if self.lineEdit_28.text() == "17/4 or 4.25" :
            marks += 1
        if self.lineEdit_28.text() == "4.25" :
            marks += 1
        if self.lineEdit_28.text() == "17/4" :
            marks += 1

        self.pushButton_173.setEnabled(False)
        model = '1 = C, 2 = B \n 3 = D, 4 = C \n 5 = B, 6 = D\n 7 = A, 8 = D\n 9 = C, 10 = D \n 11 = A, 12 = D \n 13 = B, 14 = D \n 15 = A , 16 = 5\n 17 = 5/13 or 0.384 or 0.385 , 18 = 130 \n 19 = 2 \n 20 =17/4 or 4.25'
        self.message(20, model)
        
    def test5mathcalc(self):
        global marks
        if self.radioButton_5686.isChecked():
            marks += 1
        if self.radioButton_5691.isChecked():
            marks += 1
        if self.radioButton_5702.isChecked():
            marks += 1
        if self.radioButton_5709.isChecked():
            marks += 1
        if self.radioButton_5717.isChecked():
            marks += 1
        if self.radioButton_5723.isChecked():
            marks += 1
        if self.radioButton_5733.isChecked():
            marks += 1
        if self.radioButton_5742.isChecked():
            marks += 1
        if self.radioButton_5750.isChecked():
            marks += 1
        if self.radioButton_5755.isChecked():
            marks += 1
        if self.radioButton_5766.isChecked():
            marks += 1
        if self.radioButton_5773.isChecked():
            marks += 1
        if self.radioButton_5782.isChecked():
            marks += 1
        if self.radioButton_5792.isChecked():
            marks += 1
        if self.radioButton_5799.isChecked():
            marks += 1
        if self.radioButton_5808.isChecked():
            marks += 1
        if self.radioButton_5815.isChecked():
            marks += 1
        if self.radioButton_5826.isChecked():
            marks += 1
        if self.lineEdit.text() == "145":
            marks += 1

        self.pushButton_174.setEnabled(False)
        model = '1 = C, 2 = B \n 3 = A, 4 = B \n 5 = A, 6 = C\n 7 = B, 8 = A\n 9 = A, 10 = D \n 11 = A, 12 = B \n 13 = A, 14 = B \n 15 = D\n 16 = C \n 17 = D, 18 = A'
        self.message(18, model)
        
    def test5mathcalc2(self):
        global marks
        if self.radioButton_5829.isChecked():
            marks += 1
        if self.radioButton_5836.isChecked():
            marks += 1
        if self.radioButton_5850.isChecked():
            marks += 1
        if self.radioButton_5856.isChecked():
            marks += 1
        if self.radioButton_5863.isChecked():
            marks += 1
        if self.radioButton_5872.isChecked():
            marks += 1
        if self.radioButton_5880.isChecked():
            marks += 1
        if self.radioButton_5888.isChecked():
            marks += 1
        if self.radioButton_5898.isChecked():
            marks += 1
            
        if self.radioButton_5901.isChecked():
            marks += 1
        if self.radioButton_5907.isChecked():
            marks += 1
        if self.lineEdit_15.text() == "5, 6, or 7" :
            marks += 1
        if self.lineEdit_15.text() == "5, 6, 7" :
            marks += 1
        if self.lineEdit_15.text() == "5" :
            marks += 1
        if self.lineEdit_15.text() == "6" :
            marks += 1
        if self.lineEdit_15.text() == "7" :
            marks += 1
        if self.lineEdit_16.text() == "650" :
            marks += 1
        if self.lineEdit_17.text() == "64.1" :
            marks += 1
        if self.lineEdit_18.text() == "365" :
            marks += 1
        if self.lineEdit_19.text() == "8" :
            marks += 1
        if self.lineEdit_20.text() == "5" :
            marks += 1
        if self.lineEdit_22.text() == "14" :
            marks += 1
        if self.lineEdit_23.text() == "114" :
            marks += 1
 
        self.pushButton_176.setEnabled(False)
        model = '19 = B, 20 = D \n 21 = A, 22 = B\n 23 = C, 24 = D \n 25 = C, 26 = C\n 27 = A, 28 = B \n 29 = B \n 30 = 5, 6, or 7 \n 31 = 650 \n 32 = 64.1 \n 33 = 365 \n 34 = 8, 35 = 5 \n 36 = 14 , 37 = 114'
        self.message(19, model)
        
    def test6read1(self):
        global marks
        if self.radioButton_4943.isChecked():
            marks += 1
        if self.radioButton_4950.isChecked():
            marks += 1
        if self.radioButton_4952.isChecked():
            marks += 1
        if self.radioButton_5943.isChecked():
            marks += 1
        if self.radioButton_5949.isChecked():
            marks += 1
        if self.radioButton_5954.isChecked():
            marks += 1
        if self.radioButton_5956.isChecked():
            marks += 1
        if self.radioButton_5960.isChecked():
            marks += 1
        if self.radioButton_5964.isChecked():
            marks += 1
        if self.radioButton_5970.isChecked():
            marks += 1
            
        self.pushButton_143.setEnabled(False)
        model = '1 = B, 2 = D \n 3 = B, 4 = C \n 5 = C, 6 = A \n 7 = B, 8 = A\n 9 = A, 10 = D'
        self.message(10, model)
        
    def test6read2(self):
        global marks
        if self.radioButton_5973.isChecked():
            marks += 1
        if self.radioButton_5978.isChecked():
            marks += 1
        if self.radioButton_5982.isChecked():
            marks += 1
        if self.radioButton_5986.isChecked():
            marks += 1
        if self.radioButton_5988.isChecked():
            marks += 1
        if self.radioButton_306.isChecked():
            marks += 1
        if self.radioButton_5996.isChecked():
            marks += 1
        if self.radioButton_305.isChecked():
            marks += 1
        if self.radioButton_6003.isChecked():
            marks += 1
        if self.radioButton_6008.isChecked():
            marks += 1
            
        self.pushButton_144.setEnabled(False)
        model = '1 = C, 2 = D \n 3 = D, 4 = D \n 5 = B, 6 = A \n 7 = B, 8 = C\n 9 = A, 10 = B'
        self.message(10, model)
        
    def test6read3(self):
        global marks
        if self.radioButton_6011.isChecked():
            marks += 1
        if self.radioButton_6014.isChecked():
            marks += 1
        if self.radioButton_6017.isChecked():
            marks += 1
        if self.radioButton_6112.isChecked():
            marks += 1
        if self.radioButton_6113.isChecked():
            marks += 1
        if self.radioButton_6117.isChecked():
            marks += 1
        if self.radioButton_6121.isChecked():
            marks += 1
        if self.radioButton_6124.isChecked():
            marks += 1
        if self.radioButton_6127.isChecked():
            marks += 1
        if self.radioButton_6133.isChecked():
            marks += 1
            
        self.pushButton_145.setEnabled(False)
        model = '1 = C, 2 = A \n 3 = C, 4 = D \n 5 = A, 6 = B \n 7 = B, 8 = D\n 9 = C, 10 = B'
        self.message(10, model)
        
    def test6read4(self):
        global marks
        if self.radioButton_6140.isChecked():
            marks += 1
        if self.radioButton_6143.isChecked():
            marks += 1
        if self.radioButton_6146.isChecked():
            marks += 1
        if self.radioButton_6153.isChecked():
            marks += 1
        if self.radioButton_6156.isChecked():
            marks += 1
        if self.radioButton_6159.isChecked():
            marks += 1
        if self.radioButton_6165.isChecked():
            marks += 1
        if self.radioButton_6167.isChecked():
            marks += 1
        if self.radioButton_6173.isChecked():
            marks += 1
        if self.radioButton_6174.isChecked():
            marks += 1
            
        self.pushButton_146.setEnabled(False)
        model = '1 = C, 2 = A \n 3 = C, 4 = D \n 5 = C, 6 = D \n 7 = D, 8 = A\n 9 = B, 10 = A'
        self.message(10, model)
        
    def test6read5(self):
        global marks
        if self.radioButton_6181.isChecked():
            marks += 1
        if self.radioButton_6182.isChecked():
            marks += 1
        if self.radioButton_6189.isChecked():
            marks += 1
        if self.radioButton_6192.isChecked():
            marks += 1
        if self.radioButton_6194.isChecked():
            marks += 1
        if self.radioButton_6201.isChecked():
            marks += 1
        if self.radioButton_6205.isChecked():
            marks += 1
        if self.radioButton_6209.isChecked():
            marks += 1
        if self.radioButton_6213.isChecked():
            marks += 1
        if self.radioButton_6214.isChecked():
            marks += 1
            
        self.pushButton_149.setEnabled(False)
        model = '1 = A, 2 = B \n 3 = A, 4 = A \n 5 = C, 6 = D \n 7 = A, 8 = D\n 9 = C, 10 = A'
        self.message(10, model)
        
    def test6write1(self):
        global marks
        if self.radioButton_6791.isChecked():
            marks += 1
        if self.radioButton_6222.isChecked():
            marks += 1
        if self.radioButton_6228.isChecked():
            marks += 1
        if self.radioButton_6231.isChecked():
            marks += 1
        if self.radioButton_6235.isChecked():
            marks += 1
        if self.radioButton_6797.isChecked():
            marks += 1
        if self.radioButton_6245.isChecked():
            marks += 1
        if self.radioButton_6246.isChecked():
            marks += 1
        if self.radioButton_6252.isChecked():
            marks += 1
        if self.radioButton_6257.isChecked():
            marks += 1
        if self.radioButton_6260.isChecked():
            marks += 1
            
        self.pushButton_150.setEnabled(False)
        model = '1 = D, 2 = D \n 3 = D, 4 = C \n 5 = B, 6 = C \n 7 = B, 8 = C \n 9 = B , 10 = D \n 11 = D'
        self.message(11, model)
        
    def test6write2(self):
        global marks
        if self.radioButton_6265.isChecked():
            marks += 1
        if self.radioButton_6267.isChecked():
            marks += 1
        if self.radioButton_6270.isChecked():
            marks += 1
        if self.radioButton_6275.isChecked():
            marks += 1
        if self.radioButton_6281.isChecked():
            marks += 1
        if self.radioButton_6284.isChecked():
            marks += 1
        if self.radioButton_6289.isChecked():
            marks += 1
        if self.radioButton_6292.isChecked():
            marks += 1
        if self.radioButton_6297.isChecked():
            marks += 1
        if self.radioButton_6301.isChecked():
            marks += 1
        if self.radioButton_6305.isChecked():
            marks += 1
            
        self.pushButton_151.setEnabled(False)
        model = '12 = A, 13 = B \n 14 = A, 15 = D \n 16 = C, 17 = D \n 18 = D, 19 = D \n 20 = B , 21 = A \n 22 = B'
        self.message(11, model)
        
    def test6write3(self):
        global marks
        if self.radioButton_6801.isChecked():
            marks += 1
        if self.radioButton_6311.isChecked():
            marks += 1
        if self.radioButton_6317.isChecked():
            marks += 1
        if self.radioButton_6803.isChecked():
            marks += 1
        if self.radioButton_6808.isChecked():
            marks += 1
        if self.radioButton_6326.isChecked():
            marks += 1
        if self.radioButton_6331.isChecked():
            marks += 1
        if self.radioButton_6337.isChecked():
            marks += 1
        if self.radioButton_6341.isChecked():
            marks += 1
        if self.radioButton_6342.isChecked():
            marks += 1
        if self.radioButton_6349.isChecked():
            marks += 1
            
        self.pushButton_152.setEnabled(False)
        model = '23 = A, 24 = B \n 25 = A, 26 = B \n 27 = C, 28 = C \n 29 = D, 30 = A \n 31 = B , 32 = D \n 33 = C'
        self.message(11, model)
        
    def test6write4(self):
        global marks
        if self.radioButton_6357.isChecked():
            marks += 1
        if self.radioButton_6358.isChecked():
            marks += 1
        if self.radioButton_6812.isChecked():
            marks += 1
        if self.radioButton_6369.isChecked():
            marks += 1
        if self.radioButton_6370.isChecked():
            marks += 1
        if self.radioButton_6376.isChecked():
            marks += 1
        if self.radioButton_6378.isChecked():
            marks += 1
        if self.radioButton_6815.isChecked():
            marks += 1
        if self.radioButton_6387.isChecked():
            marks += 1
        if self.radioButton_6392.isChecked():
            marks += 1
        if self.radioButton_6396.isChecked():
            marks += 1
            
        self.pushButton_153.setEnabled(False)
        model = '34 = A, 35 = B \n 36 = D, 37 = D\n 38 = A, 39 = C \n 40 = D, 41 = A \n 42 = B , 43 = C \n 44 = A'
        self.message(11, model)
        
    def test6mathnocalc(self):
        global marks
        if self.radioButton_6136.isChecked():
            marks += 1
        if self.radioButton_6306.isChecked():
            marks += 1
        if self.radioButton_6322.isChecked():
            marks += 1
        if self.radioButton_6363.isChecked():
            marks += 1
        if self.radioButton_6400.isChecked():
            marks += 1
        if self.radioButton_6407.isChecked():
            marks += 1
        if self.radioButton_6418.isChecked():
            marks += 1
        if self.radioButton_6426.isChecked():
            marks += 1
        if self.radioButton_6433.isChecked():
            marks += 1
        if self.radioButton_6439.isChecked():
            marks += 1
        if self.radioButton_6445.isChecked():
            marks += 1
        if self.radioButton_6453.isChecked():
            marks += 1
        if self.radioButton_6460.isChecked():
            marks += 1
        if self.radioButton_6460.isChecked():
            marks += 1
        if self.radioButton_6475.isChecked():
            marks += 1
        if self.lineEdit_2.text() == "16":
            marks += 1
        if self.lineEdit_3.text() == "90":
            marks += 1
        if self.lineEdit_4.text() == "3/5 or 0.6" :
            marks += 1
        if self.lineEdit_5.text() == "1/4 or 0.25" :
            marks += 1
        if self.lineEdit_4.text() == ".6" :
            marks += 1
        if self.lineEdit_5.text() ==  ".25" :
            marks += 1
        if self.lineEdit_4.text() == "3/5" :
            marks += 1
        if self.lineEdit_5.text() == "0.25" :
            marks += 1
        if self.lineEdit_4.text() == "0.6" :
            marks += 1
        if self.lineEdit_5.text() == "1/4" :
            marks += 1
        if self.lineEdit_6.text() == "64":
            marks += 1
            
        self.pushButton_24.setEnabled(False)
        model = '1 = B, 2 = A \n 3 = A, 4 = D \n 5 = C, 6 = C\n 7 = A, 8 = C\n 9 = B, 10 = D \n 11 = C, 12 = C \n 13 = D, 14 = B \n 15 = D , 16 = 16\n 17 = 90 , 18 = 3/5 or 0.6 \n 19 = 1/4 or 0.25 \n 20 = 64'
        self.message(20, model)
        
    def test6mathcalc(self):
        global marks
        if self.radioButton_6499.isChecked():
            marks += 1
        if self.radioButton_6509.isChecked():
            marks += 1
        if self.radioButton_6516.isChecked():
            marks += 1
        if self.radioButton_6524.isChecked():
            marks += 1
        if self.radioButton_6534.isChecked():
            marks += 1
        if self.radioButton_6541.isChecked():
            marks += 1
        if self.radioButton_6548.isChecked():
            marks += 1
        if self.radioButton_6555.isChecked():
            marks += 1
        if self.radioButton_6570.isChecked():
            marks += 1
        if self.radioButton_6572.isChecked():
            marks += 1
        if self.radioButton_6582.isChecked():
            marks += 1
        if self.radioButton_6587.isChecked():
            marks += 1
        if self.radioButton_6595.isChecked():
            marks += 1
        if self.radioButton_6606.isChecked():
            marks += 1
        if self.radioButton_6617.isChecked():
            marks += 1
        if self.radioButton_6624.isChecked():
            marks += 1
        if self.radioButton_6632.isChecked():
            marks += 1
        if self.radioButton_6642.isChecked():
            marks += 1

        self.pushButton_78.setEnabled(False)
        model = '1 = B, 2 = C \n 3 = D, 4 = C \n 5 = D, 6 = D\n 7 = C, 8 = D\n 9 = A, 10 = B \n 11 = A, 12 = C \n 13 = C, 14 = C \n 15 = A\n 16 = C \n 17 = B, 18 = A'
        self.message(18, model)
        
    def test6mathcalc2(self):
        global marks
        if self.radioButton_6644.isChecked():
            marks += 1
        if self.radioButton_6652.isChecked():
            marks += 1
        if self.radioButton_6659.isChecked():
            marks += 1
        if self.radioButton_6673.isChecked():
            marks += 1
        if self.radioButton_6680.isChecked():
            marks += 1
        if self.radioButton_6690.isChecked():
            marks += 1
        if self.radioButton_6695.isChecked():
            marks += 1
        if self.radioButton_6703.isChecked():
            marks += 1
        if self.radioButton_6714.isChecked():
            marks += 1
        if self.radioButton_6716.isChecked():
            marks += 1
        if self.radioButton_6723.isChecked():
            marks += 1
        if self.radioButton_6731.isChecked():
            marks += 1
        if self.lineEdit_7.text() == "Any number between 4-6, inclusive":
            marks += 1
        if self.lineEdit_8.text() == "107":
            marks += 1
        if self.lineEdit_9.text() == "5/8" :
            marks += 1
        if self.lineEdit_9.text() == ".625" :
            marks += 1
        if self.lineEdit_9.text() == "0.625" :
            marks += 1
        if self.lineEdit_9.text() == "5/8 or 0.625" :
            marks += 1
        if self.lineEdit_10.text() == "96" :
            marks += 1
        if self.lineEdit_11.text() == "6" :
            marks += 1
        if self.lineEdit_12.text() ==  "3" :
            marks += 1
        if self.lineEdit_13.text() == "1.02" :
            marks += 1
        if self.lineEdit_14.text() == "6.11" :
            marks += 1
 
        self.pushButton_84.setEnabled(False)
        model = '19 = B, 20 = D \n 21 = C, 22 = B\n 23 = B, 24 = A \n 25 = D, 26 = B\n 27 = C, 28 = C \n 29 = D \n 30 = D \n 31 = Any number between 4-6, inclusive \n 32 = 107 \n 33 = 5/8 or 0.625 \n 34 = 96 , 35 = 6 \n 36 = 3 , 37 = 1.02 \n 38 = 6.11 '
        self.message(20, model)
        
    def mathnocalc3(self):
        global marks
        if self.radioButton_6766.isChecked():
            marks += 1
        if self.radioButton_6775.isChecked():
            marks += 1
        if self.radioButton_6781.isChecked():
            marks += 1
        if self.radioButton_6819.isChecked():
            marks += 1
        if self.radioButton_6825.isChecked():
            marks += 1
        if self.radioButton_6833.isChecked():
            marks += 1
        if self.radioButton_6840.isChecked():
            marks += 1
        if self.radioButton_6849.isChecked():
            marks += 1
        if self.radioButton_6858.isChecked():
            marks += 1
        if self.radioButton_6865.isChecked():
            marks += 1
    
        if self.radioButton_6870.isChecked():
            marks += 1
        if self.radioButton_6877.isChecked():
            marks += 1
        if self.radioButton_6887.isChecked():
            marks += 1
        if self.radioButton_6894.isChecked():
            marks += 1
        if self.radioButton_6902.isChecked():
            marks += 1
        if self.lineEdit_81.text() == "360" :
            marks += 1
        if self.lineEdit_82.text() == "2" :
            marks += 1
        if self.lineEdit_83.text() ==  "8" :
            marks += 1
        if self.lineEdit_84.text() == "3/4 or .75" :
            marks += 1
        if self.lineEdit_84.text() == ".75" :
            marks += 1
        if self.lineEdit_84.text() == "3/4" :
            marks += 1
        if self.lineEdit_84.text() == "0.75" :
            marks += 1
        if self.lineEdit_85.text() == "5/2" :
            marks += 1
        if self.lineEdit_85.text() == "2.5" :
            marks += 1
        if self.lineEdit_85.text() == "5/2 or 2.5" :
            marks += 1

        self.pushButton_1129.setEnabled(False)
        model = '41 = B, 42 = A \n 43 = D, 44 = A\n 45 = C, 46 = B \n 47 = D, 48 = C\n 49 = B, 50 = C \n 51 = B, 52 = D \n 53 = A, 54 = B \n 55 = B, 56 = 360 \n 57 = 2, 58 = 8 \n 59 = 3/4 or .75 , 60 = 5/2 or 2.5'
        self.message(20, model)
        
    def mathcalc(self):
        global marks
        if self.radioButton_7078.isChecked():
            marks += 1
        if self.radioButton_7087.isChecked():
            marks += 1
        if self.radioButton_7092.isChecked():
            marks += 1
        if self.radioButton_7103.isChecked():
            marks += 1
        if self.radioButton_7108.isChecked():
            marks += 1
        if self.radioButton_7116.isChecked():
            marks += 1
        if self.radioButton_7124.isChecked():
            marks += 1
        if self.radioButton_7135.isChecked():
            marks += 1
        if self.radioButton_7142.isChecked():
            marks += 1
        if self.radioButton_7150.isChecked():
            marks += 1
    
        if self.radioButton_6927.isChecked():
            marks += 1
        if self.radioButton_6933.isChecked():
            marks += 1
        if self.radioButton_6943.isChecked():
            marks += 1
        if self.radioButton_6950.isChecked():
            marks += 1
        if self.radioButton_6968.isChecked():
            marks += 1
        if self.radioButton_7051.isChecked():
            marks += 1
        if self.radioButton_7056.isChecked():
            marks += 1
        if self.radioButton_7066.isChecked():
            marks += 1
        if self.radioButton_7073.isChecked():
            marks += 1

        self.pushButton_1130.setEnabled(False)
        model = '1 = B, 2 = A \n 3 = C, 4 = A \n 5 = D, 6 = C\n 7 = D, 8 = A\n 9 = B, 10 = B \n 11 = C, 12 = D \n 13 = A, 14 = B \n 15 = C\n 16 = A \n 17 = D, 18 = B \n 19 = C'
        self.message(19, model)

    def mathcalc2(self):
        global marks
        if self.radioButton_7152.isChecked():
            marks += 1
        if self.radioButton_7160.isChecked():
            marks += 1
        if self.radioButton_7170.isChecked():
            marks += 1
        if self.radioButton_7181.isChecked():
            marks += 1
        if self.radioButton_7190.isChecked():
            marks += 1
        if self.radioButton_7198.isChecked():
            marks += 1
        if self.radioButton_7206.isChecked():
            marks += 1
        if self.radioButton_7213.isChecked():
            marks += 1
        if self.radioButton_7223.isChecked():
            marks += 1
        if self.radioButton_7224.isChecked():
            marks += 1
    
        if self.radioButton_7234.isChecked():
            marks += 1
        if self.lineEdit_86.text() == "120" :
            marks += 1
        if self.lineEdit_87.text() == "5" :
            marks += 1
        if self.lineEdit_88.text() ==  "880" :
            marks += 1
        if self.lineEdit_89.text() == "20" :
            marks += 1
        if self.lineEdit_90.text() == "950" :
            marks += 1
        if self.lineEdit_91.text() == "40" :
            marks += 1
        if self.lineEdit_92.text() == "1.03" :
            marks += 1
        if self.lineEdit_93.text() == "17.8" :
            marks += 1

        self.pushButton_1131.setEnabled(False)
        model = '1 = A, 2 = B \n 3 = B, 4 = C \n 5 = D, 6 = B\n 7 = B, 8 = C\n 9 = A, 10 = A \n 11 = C, 12 = 120 \n 13 = 5, 14 = 880 \n 15 = 20\n 16 = 950 \n 17 = 40, 18 = 1.03 \n 19 = 17.8'
        self.message(19, model)

    def mathcalc3(self):
        global marks
        if self.radioButton_7342.isChecked():
            marks += 1
        if self.radioButton_7349.isChecked():
            marks += 1
        if self.radioButton_7358.isChecked():
            marks += 1
        if self.radioButton_7367.isChecked():
            marks += 1
        if self.radioButton_7378.isChecked():
            marks += 1
        if self.radioButton_7387.isChecked():
            marks += 1
        if self.radioButton_7393.isChecked():
            marks += 1
        if self.radioButton_7403.isChecked():
            marks += 1
        if self.radioButton_7408.isChecked():
            marks += 1
        if self.radioButton_7271.isChecked():
            marks += 1
    
        if self.radioButton_7279.isChecked():
            marks += 1
        if self.radioButton_7285.isChecked():
            marks += 1
        if self.radioButton_7293.isChecked():
            marks += 1
        if self.radioButton_7302.isChecked():
            marks += 1
        if self.radioButton_7310.isChecked():
            marks += 1
        if self.radioButton_7318.isChecked():
            marks += 1
        if self.radioButton_7324.isChecked():
            marks += 1
        if self.radioButton_7338.isChecked():
            marks += 1

        self.pushButton_1132.setEnabled(False)
        model = '1 = B, 2 = D \n 3 = B, 4 = A \n 5 = D, 6 = A\n 7 = C, 8 = A\n 9 = D, 10 = D \n 11 = A, 12 = D \n 13 = C, 14 = B \n 15 = D\n 16 = B \n 17 = D, 18 = B'
        self.message(18, model)
        
    def mathcalc4(self):
        global marks
        if self.radioButton_7458.isChecked():
            marks += 1
        if self.radioButton_7467.isChecked():
            marks += 1
        if self.radioButton_7473.isChecked():
            marks += 1
        if self.radioButton_7482.isChecked():
            marks += 1
        if self.radioButton_7490.isChecked():
            marks += 1
        if self.radioButton_7496.isChecked():
            marks += 1
        if self.radioButton_7505.isChecked():
            marks += 1
        if self.radioButton_7512.isChecked():
            marks += 1
        if self.radioButton_7523.isChecked():
            marks += 1
        if self.radioButton_7529.isChecked():
            marks += 1
        if self.radioButton_7412.isChecked():
            marks += 1
        if self.radioButton_7421.isChecked():
            marks += 1
        if self.lineEdit_94.text() == "6":
            marks += 1
        if self.lineEdit_95.text() == "2":
            marks += 1
        if self.lineEdit_96.text() == "8" :
            marks += 1
        if self.lineEdit_97.text() == "9" :
            marks += 1
        if self.lineEdit_98.text() == "15" :
            marks += 1
        if self.lineEdit_99.text() == "3/2 or 1.5" :
            marks += 1
        if self.lineEdit_99.text() == "1.5" :
            marks += 1
        if self.lineEdit_99.text() == "3/2" :
            marks += 1
        if self.lineEdit_100.text() == "1.3" :
            marks += 1
        if self.lineEdit_101.text() == "3" :
            marks += 1

        self.pushButton_1133.setEnabled(False)
        model = '19 = B, 20 = A \n 21 = D, 22 = B\n 23 = B, 24 = C \n 25 = C, 26 = D\n 27 = A, 28 = C \n 29 = A \n 30 = D \n 31 = 6 \n 32 = 2 \n 33 = 8 \n 34 = 9 , 35 = 15 \n 36 = 3/2 or 1.5 , 37 = 1.3 \n 38 = 3 '
        self.message(20, model)

##########################################################################################
    def message (self, num, model):
        global marks
        if marks < num:
           QMessageBox.about(self, "Result", "%d/%d Hard luck!\n\nModel Answer: \n %s\n\nDon't Try Again ;)" % (
               marks, num, model))
           marks = 0
        elif marks == num:
           QMessageBox.about(self, "Result", "%d/%d Congratulations!\n\nYou Got It ^_^" % (marks, num))
           marks = 0
        
#######################################################################################################

app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('hack.ico'))
window = Ui()
app.exec_()


