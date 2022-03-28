from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5.uic import loadUiType
from first_udated_with_draw import *
from drawUpdated import *


MainUI,_ = loadUiType('untitled.ui')

########queues to store data returned from UI###########
#memory_D=[]
queue_HStartAdd = []
queue_HSize =[]
queue_Process_num = []
queue_segments =[]
queue_SegName =[]
queue_SegSize =[]
MEM_Size = 0
#memNEW = []
class Main(QMainWindow, MainUI):  
    def __init__(self, parent=None):           #push button hena &&& ay 7aga tab3 el ui 
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Memory Allocation")
        #self.setGeometry(200,300,600,500)
        
        

        ######################## First Fit ##############################
        self.tableWidget_FF.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #self.lineEdit_memSize_FF.textChanged.connect(self.MemSIZE_FF)
        #self.lineEdit_HStartAdd_FF.textChanged.connect(self.HStartAdd_FF)
        #self.lineEdit_HSize_FF.textChanged.connect(self.HSize_FF)
        #self.lineEdit_PName_FF.textChanged.connect(self.PName_FF)
        self.pushButton_FF.clicked.connect(self.PName_FF)
        self.lineEdit_SegNum_FF.textChanged.connect(self.New_row_FF)
        self.pushButton_FF.clicked.connect(self.check_empty_cells_FF)
        self.pushButton_FF.clicked.connect(self.read_table_data_FF)
        self.pushButton_FF.clicked.connect(self.SEGMENTS_FF)
        self.pushButton_FF.clicked.connect(self.clear_FF)
        self.pushButton_clear_FF.clicked.connect(self.clear_all_FF)
        #self.lineEdit_DeAlloc_FF.textChanged.connect(self.DeAlloc_FF)
        self.pushButton_DeAlloc_FF.clicked.connect(self.DeAlloc_button_FF)
        self.pushButton_add_holes_FF.clicked.connect(self.Add_New_Hole)
        #self.pushButton_DeAlloc_FF.clicked.connect(self.ERROR_MSG_FF)
        self.pushButton_Finish_Alloc_FF.clicked.connect(self.Finish_FF)
        

        ######################## Best Fit ##############################
        self.tableWidget_BF.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #self.lineEdit_memSize_BF.textChanged.connect(self.MemSIZE_BF)
        #self.lineEdit_HStartAdd_BF.textChanged.connect(self.HStartAdd_BF)
        #self.lineEdit_HSize_BF.textChanged.connect(self.HSize_BF)
        #self.lineEdit_PName_BF.textChanged.connect(self.PName_BF)
        self.pushButton_BF.clicked.connect(self.PName_BF)
        self.lineEdit_SegNum_BF.textChanged.connect(self.New_row_BF)
        self.pushButton_BF.clicked.connect(self.check_empty_cells_BF)
        self.pushButton_add_holes_BF.clicked.connect(self.Add_New_Hole_BF)
        self.pushButton_BF.clicked.connect(self.read_table_data_BF)
        self.pushButton_BF.clicked.connect(self.SEGMENTS_BF)
        self.pushButton_BF.clicked.connect(self.clear_BF)
        self.pushButton_clear_BF.clicked.connect(self.clear_all_BF)
        #self.lineEdit_DeAlloc_BF.textChanged.connect(self.DeAlloc_BF)
        self.pushButton_DeAlloc_BF.clicked.connect(self.DeAlloc_button_BF)
        #self.pushButton_Add_Hole_BF.clicked.connect(self.Add_New_Hole_BF)
        #self.pushButton_DeAlloc_BF.clicked.connect(self.ERROR_MSG_BF)
        self.pushButton_Finish_Alloc_BF.clicked.connect(self.Finish_BF)


        ######################## Worst Fit ##############################
        self.tableWidget_WF.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #self.lineEdit_memSize_BF.textChanged.connect(self.MemSIZE_BF)
        #self.lineEdit_HStartAdd_BF.textChanged.connect(self.HStartAdd_BF)
        #self.lineEdit_HSize_BF.textChanged.connect(self.HSize_BF)
        #self.lineEdit_PName_BF.textChanged.connect(self.PName_BF)
        self.pushButton_WF.clicked.connect(self.PName_WF)
        self.lineEdit_SegNum_WF.textChanged.connect(self.New_row_WF)
        self.pushButton_WF.clicked.connect(self.check_empty_cells_WF)
        self.pushButton_add_holes_WF.clicked.connect(self.Add_New_Hole_WF)
        self.pushButton_WF.clicked.connect(self.read_table_data_WF)
        self.pushButton_WF.clicked.connect(self.SEGMENTS_WF)
        self.pushButton_WF.clicked.connect(self.clear_WF)
        self.pushButton_clear_WF.clicked.connect(self.clear_all_WF)
        #self.lineEdit_DeAlloc_BF.textChanged.connect(self.DeAlloc_BF)
        self.pushButton_DeAlloc_WF.clicked.connect(self.DeAlloc_button_WF)
        #self.pushButton_Add_Hole_BF.clicked.connect(self.Add_New_Hole_BF)
        #self.pushButton_DeAlloc_BF.clicked.connect(self.ERROR_MSG_BF)
        self.pushButton_Finish_Alloc_WF.clicked.connect(self.Finish_WF)

    

    ######################## First Fit ##############################
    
    #def MemSIZE_FF (self):
        #MemSIZE_FF = self.lineEdit_memSize_FF.text()
        #MEM_Size.append (int(MemSIZE_FF)) 
        #if (MemSIZE_FF is ""):
         #   self.lineEdit_memSize_FF.clear()
        #else:    
         #   MemSIZE_FF = int(MemSIZE_FF)
            
        #print (MemSIZE_FF+10)

    def HStartAdd_FF(self):
        HStartAdd_FF = self.lineEdit_HStartAdd_FF.text()
        if (HStartAdd_FF is ""):
            self.lineEdit_HStartAdd_FF.clear()
        else:    
            HStartAdd_FF = int(HStartAdd_FF)
        

    def HSize_FF (self):
        HSize_FF = self.lineEdit_HSize_FF.text()
        if (HSize_FF is ""):
            self.lineEdit_HSize_FF.clear()
        else:    
            HSize_FF = int(HSize_FF)

    
    def PName_FF (self):
        if (len(self.lineEdit_PName_FF.text())!=0):
            PName_FF = self.lineEdit_PName_FF.text()
            queue_Process_num.append(int(PName_FF))
        #print (queue_Process_num)
        #for i in range(0,len(PName_FF)):
         #   if ((PName_FF[0] != "p")):
          #      if ( (PName_FF[0] != "P")):
           #         QMessageBox.about(self, "ERROR", "Enter Process name as Pn where n is the number of the process")
                #self.lineEdit_PName_FF.clear()
                #self.lineEdit_PName_FF.setText("P")
        #if (PName_FF is ""):
         #       QMessageBox.about(self, "ERROR", "Empty Cell!")    

    def New_row_FF (self,text):
        if (text is ""):
            self.lineEdit_SegNum_FF.clear()
        else:
            noofrows = int(text)
            self.tableWidget_FF.setRowCount(noofrows)

    def read_table_data_FF(self):
        not_valid=0
        rowCount = self.tableWidget_FF.rowCount()     #no of rows #tableWidgetfcfs ---> name of table
        columnCount = self.tableWidget_FF.columnCount() #no of columns
        x = 0
        for column in range(columnCount):
            columnData = ''
            x = x + 1
            for row in range(rowCount):
                widgetItem = self.tableWidget_FF.item(row, column) #.item ---> return value as string
                if (widgetItem and widgetItem.text):
                    columnData = columnData + ' ' + widgetItem.text()
                else:
                    columnData = columnData + ' ' + '-1'
            if (x == 1):
                Seg_name = columnData.split()  # put column data in array of string
                if (('-1') in Seg_name):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1

        if len(Seg_name) != 0:
            queue_SegName.append(Seg_name)
            #print (queue_SegName)               
                #else:
                    #for i in range(0, len(Seg_name)):
                        #Seg_name[i] = Seg_name[i]
                        #if (arrival[i]<0):
                         #   QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                          #  not_valid=1
                    #print(arrival, 1, "\n")
            #print(columnData)
            

            if (x == 2):
                Seg_Size = columnData.split()
                if (('-1') in Seg_Size):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                else:
                    for j in range(0, len(Seg_Size)):
                        Seg_Size[j] = float(Seg_Size[j])
                        if (Seg_Size[j]<0):
                            QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                            not_valid=1
                    #print(Seg_Size, 2, "\n")
                if len(Seg_Size) != 0:
                    queue_SegSize.append(Seg_Size)
                    #print (queue_SegSize)    
        

    #def DeAlloc_FF (self):
     #   PName_FF = self.lineEdit_DeAlloc_FF.text()
        #for i in range(0,len(PName_FF)):
         #  if ((PName_FF[0] != "p")):
          #      if ( (PName_FF[0] != "P")):
           #         QMessageBox.about(self, "ERROR", "Enter Process name as Pn where n is the number of the process")

    def DeAlloc_button_FF (self):
        flag4 =0
        if self.lineEdit_DeAlloc_Type_FF.text() == "":
            flag4 =1
            QMessageBox.about(self, "ERROR", "Empty Process Type ('P' OR 'o')")
        if self.lineEdit_DeAlloc_Num_FF.text() == "":
            flag4 =1
            QMessageBox.about(self, "ERROR", "Empty Process Number")
        PName = self.lineEdit_DeAlloc_Type_FF.text()
        for i in range(0,len(PName)):
            if ((PName[0] != "P")):
                if ( (PName[0] != "o")):
                    self.lineEdit_DeAlloc_Type_FF.clear()
                    QMessageBox.about(self, "ERROR", "Enter Process Type as ('P' OR 'o') only") 
                    flag4=1
        PNum = int(self.lineEdit_DeAlloc_Num_FF.text())
        
        if (flag4 == 0):
            MemSIZE_FF = self.lineEdit_memSize_FF.text()
            MEM_Size=int(MemSIZE_FF)
            memNEW = holes_map(queue_HStartAdd,queue_HSize,MEM_Size)   #queue_HStartAdd = []queue_HSize =[]
            process = process_map(queue_Process_num,queue_segments,queue_SegName,queue_SegSize)
            arr = ALLOCATION_FIRST_FIT(memNEW,process,queue_segments,queue_Process_num)
            mem=DEALLOCATION(PNum,PName,arr[1])
            drawchart(mem)

    def check_empty_cells_FF(self):
        if self.lineEdit_memSize_FF.text() == "":
            QMessageBox.about(self, "ERROR", "Empty Total Memory Size")
        if self.lineEdit_PName_FF.text() == "":
           QMessageBox.about(self, "ERROR", "Empty Process Number")
        if self.lineEdit_SegNum_FF.text() == "":
           QMessageBox.about(self, "ERROR", "Empty Number Of Segments ")       

    def Add_New_Hole(self):
        if self.lineEdit_HStartAdd_FF.text() == "":
            QMessageBox.about(self, "ERROR", "Empty Holes Starting Address")
        if self.lineEdit_HSize_FF.text() == "":
           QMessageBox.about(self, "ERROR", "Empty Holes Size")
        if(len(self.lineEdit_HStartAdd_FF.text())!=0 and len(self.lineEdit_HSize_FF.text())!=0):
            queue_HStartAdd.append (int(self.lineEdit_HStartAdd_FF.text()))
            queue_HSize.append (int(self.lineEdit_HSize_FF.text()))
            self.lineEdit_HStartAdd_FF.clear()
            self.lineEdit_HSize_FF.clear()
            #print(queue_HStartAdd)
            #print (queue_HSize)
    
    def SEGMENTS_FF(self):
        if (len(self.lineEdit_SegNum_FF.text())!=0):
            queue_segments.append(int(self.lineEdit_SegNum_FF.text()))      
            #print (queue_segments)

    def clear_FF (self):
        self.lineEdit_PName_FF.clear()
        self.lineEdit_SegNum_FF.clear()
        self.tableWidget_FF.clearContents()
        self.tableWidget_FF.setRowCount(0)


    def clear_all_FF (self):
        self.lineEdit_memSize_FF.clear()
        self.lineEdit_HStartAdd_FF.clear()
        self.lineEdit_HSize_FF.clear()
        self.lineEdit_PName_FF.clear()
        self.lineEdit_SegNum_FF.clear()
        self.tableWidget_FF.clearContents()
        self.tableWidget_FF.setRowCount(0)
        self.lineEdit_DeAlloc_Type_FF.clear()
        self.lineEdit_DeAlloc_Num_FF.clear()
        queue_HStartAdd.clear()
        queue_HSize.clear()
        queue_Process_num.clear()
        queue_segments.clear()
        queue_SegName.clear()
        queue_SegSize.clear()
        MEM_Size = 0



    def Finish_FF (self):
        #arr=[12,13,10]
        MemSIZE_FF = self.lineEdit_memSize_FF.text()
        #MEM_Size.append (int(MemSIZE_FF)) 
        MEM_Size=int(MemSIZE_FF)
        memNEW = holes_map(queue_HStartAdd,queue_HSize,MEM_Size)   #queue_HStartAdd = []queue_HSize =[]
        process = process_map(queue_Process_num,queue_segments,queue_SegName,queue_SegSize)
        arr = ALLOCATION_FIRST_FIT(memNEW,process,queue_segments,queue_Process_num)
        drawchart(arr[1])
        
        s=''
        err_array =arr[0] 
        if len(err_array)!=0:
            for i in range (0,len(err_array)):
                s+=("P")
                s+=(str(err_array[i]))
                #print("ERROR MSG",str(err_array[i]))
                s+=(" ")
            s+= 'Can not be allocated'    
            self.lineEdit_msg_FF.setText (s)               



    ######################## Best Fit ##############################    
    #def MemSIZE_BF (self):
     ##   MemSIZE_BF = self.lineEdit_memSize_BF.text()
        #MEM_Size.append (int(MemSIZE_BF)) 
        #if (MemSIZE_BF is ""):
         #   self.lineEdit_memSize_BF.clear()
        #else:    
         #   MemSIZE_BF = int(MemSIZE_BF)
        #print (MemSIZE_BF+10)

    def HStartAdd_BF(self):
        HStartAdd_BF = self.lineEdit_HStartAdd_BF.text()
        if (HStartAdd_BF is ""):
            self.lineEdit_HStartAdd_BF.clear()
        else:    
            HStartAdd_BF = int(HStartAdd_BF)
        

    def HSize_BF (self):
        HSize_BF = self.lineEdit_HSize_BF.text()
        if (HSize_BF is ""):
            self.lineEdit_HSize_BF.clear()
        else:    
            HSize_BF = int(HSize_BF)


    def PName_BF (self):
        if (len(self.lineEdit_PName_BF.text())!=0):
            PName_BF = self.lineEdit_PName_BF.text()
            queue_Process_num.append(int(PName_BF))
        print ("process num",queue_Process_num)
        #for i in range(0,len(PName_BF)):
         #   if ((PName_BF[0] != "p")):
          #      if ( (PName_BF[0] != "P")):
           #         QMessageBox.about(self, "ERROR", "Enter Process name as Pn where n is the number of the process")
                #self.lineEdit_PName_FF.clear()
                #self.lineEdit_PName_FF.setText("P")
        #if (PName_FF is ""):
         #       QMessageBox.about(self, "ERROR", "Empty Cell!")    

    def New_row_BF (self,text):
        if (text is ""):
            self.lineEdit_SegNum_BF.clear()
        else:
            noofrows = int(text)
            self.tableWidget_BF.setRowCount(noofrows)

    def read_table_data_BF(self):
        not_valid=0
        rowCount = self.tableWidget_BF.rowCount()     #no of rows #tableWidgetfcfs ---> name of table
        columnCount = self.tableWidget_BF.columnCount() #no of columns
        x = 0
        for column in range(columnCount):
            columnData = ''
            x = x + 1
            for row in range(rowCount):
                widgetItem = self.tableWidget_BF.item(row, column) #.item ---> return value as string
                if (widgetItem and widgetItem.text):
                    columnData = columnData + ' ' + widgetItem.text()
                else:
                    columnData = columnData + ' ' + '-1'
            if (x == 1):
                Seg_name = columnData.split()  # put column data in array of string
                if (('-1') in Seg_name):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                #else:
                    #for i in range(0, len(Seg_name)):
                        #Seg_name[i] = Seg_name[i]
                        #if (arrival[i]<0):
                         #   QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                          #  not_valid=1
                    #print(arrival, 1, "\n")
        if len(Seg_name) != 0:
            queue_SegName.append(Seg_name)        
            print ("seg name",queue_SegName)    
            #print(columnData)

            if (x == 2):
                Seg_Size = columnData.split()
                if (('-1') in Seg_Size):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                else:
                    for j in range(0, len(Seg_Size)):
                        Seg_Size[j] = float(Seg_Size[j])
                        if (Seg_Size[j]<0):
                            QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                            not_valid=1
                    print(Seg_Size, 2, "\n")
                if len(Seg_Size) != 0:
                    queue_SegSize.append(Seg_Size)
                    print ("seg size",queue_SegSize)        

    #def DeAlloc_BF (self):
     #   PName_BF = self.lineEdit_DeAlloc_BF.text()
        #for i in range(0,len(PName_BF)):
         #   if ((PName_BF[0] != "p")):
          #      if ( (PName_BF[0] != "P")):
           #         QMessageBox.about(self, "ERROR", "Enter Process name as Pn where n is the number of the process")

    def DeAlloc_button_BF (self):
        flag4 =0
        if self.lineEdit_DeAlloc_Type_BF.text() == "":
            flag4 =1
            QMessageBox.about(self, "ERROR", "Empty Process Type ('P' OR 'o')")
        if self.lineEdit_DeAlloc_Num_BF.text() == "":
            flag4 =1
            QMessageBox.about(self, "ERROR", "Empty Process Number")
        PName = self.lineEdit_DeAlloc_Type_BF.text()
        for i in range(0,len(PName)):
            if ((PName[0] != "P")):
                if ( (PName[0] != "o")):
                    self.lineEdit_DeAlloc_Type_BF.clear()
                    QMessageBox.about(self, "ERROR", "Enter Process Type as ('P' OR 'o') only") 
                    flag4=1
        PNum = int(self.lineEdit_DeAlloc_Num_BF.text())
        
        if (flag4 == 0):
            MemSIZE_BF = self.lineEdit_memSize_BF.text()
            MEM_Size=int(MemSIZE_BF)
            memNEW = holes_map(queue_HStartAdd,queue_HSize,MEM_Size)   #queue_HStartAdd = []queue_HSize =[]
            process = process_map(queue_Process_num,queue_segments,queue_SegName,queue_SegSize)
            arr = ALLOCATION_BEST_FIT(memNEW,process,queue_segments,queue_Process_num)
            mem=DEALLOCATION(PNum,PName,arr[1])
            drawchart(mem)
            
   

    def check_empty_cells_BF(self):
        if self.lineEdit_memSize_BF.text() == "":
            QMessageBox.about(self, "ERROR", "Empty Total Memory Size")
        if self.lineEdit_PName_BF.text() == "":
           QMessageBox.about(self, "ERROR", "Empty Process Number")
        if self.lineEdit_SegNum_BF.text() == "":
           QMessageBox.about(self, "ERROR", "Empty Number Of Segments ")       

    def Add_New_Hole_BF(self):
        if self.lineEdit_HStartAdd_BF.text() == "":
            QMessageBox.about(self, "ERROR", "Empty Holes Starting Address")
        if self.lineEdit_HSize_BF.text() == "":
           QMessageBox.about(self, "ERROR", "Empty Holes Size")
        if(len(self.lineEdit_HStartAdd_BF.text())!=0 and len(self.lineEdit_HSize_BF.text())!=0):   
            queue_HStartAdd.append(int(self.lineEdit_HStartAdd_BF.text()))
            queue_HSize.append(int(self.lineEdit_HSize_BF.text()))
            self.lineEdit_HStartAdd_BF.clear()
            self.lineEdit_HSize_BF.clear()
            print("holes",queue_HStartAdd)
            print ("holes",queue_HSize)

    def SEGMENTS_BF(self):
        if (len(self.lineEdit_SegNum_BF.text())!=0):
            queue_segments.append(int(self.lineEdit_SegNum_BF.text()))        
            print ("segnum",queue_segments)    

    def clear_BF (self):
        self.lineEdit_PName_BF.clear()
        self.lineEdit_SegNum_BF.clear()
        self.tableWidget_BF.clearContents()
        self.tableWidget_BF.setRowCount(0)


    def clear_all_BF (self):
        self.lineEdit_memSize_BF.clear()
        self.lineEdit_HStartAdd_BF.clear()
        self.lineEdit_HSize_BF.clear()
        self.lineEdit_PName_BF.clear()
        self.lineEdit_SegNum_BF.clear()
        self.tableWidget_BF.clearContents()
        self.tableWidget_BF.setRowCount(0)
        self.lineEdit_DeAlloc_Type_BF.clear()
        self.lineEdit_DeAlloc_Num_BF.clear()
        queue_HStartAdd.clear()
        queue_HSize.clear()
        queue_Process_num.clear()
        queue_segments.clear()
        queue_SegName.clear()
        queue_SegSize.clear()
        MEM_Size = 0




    def Finish_BF (self):
        #arr=[12,13,10]
        MemSIZE_BF = self.lineEdit_memSize_BF.text()
        #MEM_Size.append (int(MemSIZE_FF)) 
        MEM_Size=int(MemSIZE_BF)
        memNEW = holes_map(queue_HStartAdd,queue_HSize,MEM_Size)   #queue_HStartAdd = []queue_HSize =[]
        process = process_map(queue_Process_num,queue_segments,queue_SegName,queue_SegSize)
        arr = ALLOCATION_BEST_FIT(memNEW,process,queue_segments,queue_Process_num)
        drawchart(arr[1])
        
        s=''
        err_array =arr[0] 
        if len(err_array)!=0:
            for i in range (0,len(err_array)):
                s+=("P")
                s+=(str(err_array[i]))
                #print("ERROR MSG",str(err_array[i]))
                s+=(" ")
            s+= 'Can not be allocated'    
            self.lineEdit_msg_BF.setText (s)  





    ######################## Worst Fit ##############################    
    #def MemSIZE_BF (self):
     ##   MemSIZE_BF = self.lineEdit_memSize_BF.text()
        #MEM_Size.append (int(MemSIZE_BF)) 
        #if (MemSIZE_BF is ""):
         #   self.lineEdit_memSize_BF.clear()
        #else:    
         #   MemSIZE_BF = int(MemSIZE_BF)
        #print (MemSIZE_BF+10)

    def HStartAdd_WF(self):
        HStartAdd_WF = self.lineEdit_HStartAdd_WF.text()
        if (HStartAdd_WF is ""):
            self.lineEdit_HStartAdd_WF.clear()
        else:    
            HStartAdd_WF = int(HStartAdd_WF)
        

    def HSize_WF (self):
        HSize_WF = self.lineEdit_HSize_WF.text()
        if (HSize_WF is ""):
            self.lineEdit_HSize_WF.clear()
        else:    
            HSize_WF = int(HSize_WF)


    def PName_WF (self):
        if (len(self.lineEdit_PName_WF.text())!=0):
            PName_WF = self.lineEdit_PName_WF.text()
            queue_Process_num.append(int(PName_WF))
        print ("process num",queue_Process_num)
        #for i in range(0,len(PName_BF)):
         #   if ((PName_BF[0] != "p")):
          #      if ( (PName_BF[0] != "P")):
           #         QMessageBox.about(self, "ERROR", "Enter Process name as Pn where n is the number of the process")
                #self.lineEdit_PName_FF.clear()
                #self.lineEdit_PName_FF.setText("P")
        #if (PName_FF is ""):
         #       QMessageBox.about(self, "ERROR", "Empty Cell!")    

    def New_row_WF (self,text):
        if (text is ""):
            self.lineEdit_SegNum_WF.clear()
        else:
            noofrows = int(text)
            self.tableWidget_WF.setRowCount(noofrows)

    def read_table_data_WF(self):
        not_valid=0
        rowCount = self.tableWidget_WF.rowCount()     #no of rows #tableWidgetfcfs ---> name of table
        columnCount = self.tableWidget_WF.columnCount() #no of columns
        x = 0
        for column in range(columnCount):
            columnData = ''
            x = x + 1
            for row in range(rowCount):
                widgetItem = self.tableWidget_WF.item(row, column) #.item ---> return value as string
                if (widgetItem and widgetItem.text):
                    columnData = columnData + ' ' + widgetItem.text()
                else:
                    columnData = columnData + ' ' + '-1'
            if (x == 1):
                Seg_name = columnData.split()  # put column data in array of string
                if (('-1') in Seg_name):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                #else:
                    #for i in range(0, len(Seg_name)):
                        #Seg_name[i] = Seg_name[i]
                        #if (arrival[i]<0):
                         #   QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                          #  not_valid=1
                    #print(arrival, 1, "\n")
        if len(Seg_name) != 0:
            queue_SegName.append(Seg_name)        
            print ("seg name",queue_SegName)    
            #print(columnData)

            if (x == 2):
                Seg_Size = columnData.split()
                if (('-1') in Seg_Size):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                else:
                    for j in range(0, len(Seg_Size)):
                        Seg_Size[j] = float(Seg_Size[j])
                        if (Seg_Size[j]<0):
                            QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                            not_valid=1
                    print(Seg_Size, 2, "\n")
                if len(Seg_Size) != 0:
                    queue_SegSize.append(Seg_Size)
                    print ("seg size",queue_SegSize)        

    #def DeAlloc_WF (self):
     #   PName_WF = self.lineEdit_DeAlloc_WF.text()
        #for i in range(0,len(PName_BF)):
         #   if ((PName_BF[0] != "p")):
          #      if ( (PName_BF[0] != "P")):
           #         QMessageBox.about(self, "ERROR", "Enter Process name as Pn where n is the number of the process")

    def DeAlloc_button_WF (self):
        flag4 =0
        if self.lineEdit_DeAlloc_Type_WF.text() == "":
            flag4 =1
            QMessageBox.about(self, "ERROR", "Empty Process Type ('P' OR 'o')")
        if self.lineEdit_DeAlloc_Num_WF.text() == "":
            flag4 =1
            QMessageBox.about(self, "ERROR", "Empty Process Number")
        PName = self.lineEdit_DeAlloc_Type_WF.text()
        for i in range(0,len(PName)):
            if ((PName[0] != "P")):
                if ( (PName[0] != "o")):
                    self.lineEdit_DeAlloc_Type_WF.clear()
                    QMessageBox.about(self, "ERROR", "Enter Process Type as ('P' OR 'o') only") 
                    flag4=1
        PNum = int(self.lineEdit_DeAlloc_Num_WF.text())
        
        if (flag4 == 0):
            MemSIZE_WF = self.lineEdit_memSize_WF.text()
            MEM_Size=int(MemSIZE_WF)
            memNEW = holes_map(queue_HStartAdd,queue_HSize,MEM_Size)   #queue_HStartAdd = []queue_HSize =[]
            process = process_map(queue_Process_num,queue_segments,queue_SegName,queue_SegSize)
            arr = ALLOCATION_WORST_FIT(memNEW,process,queue_segments,queue_Process_num)
            mem=DEALLOCATION(PNum,PName,arr[1])
            drawchart(mem)
   

    def check_empty_cells_WF(self):
        if self.lineEdit_memSize_WF.text() == "":
            QMessageBox.about(self, "ERROR", "Empty Total Memory Size")
        if self.lineEdit_PName_WF.text() == "":
           QMessageBox.about(self, "ERROR", "Empty Process Number")
        if self.lineEdit_SegNum_WF.text() == "":
           QMessageBox.about(self, "ERROR", "Empty Number Of Segments ")       

    def Add_New_Hole_WF(self):
        if self.lineEdit_HStartAdd_WF.text() == "":
            QMessageBox.about(self, "ERROR", "Empty Holes Starting Address")
        if self.lineEdit_HSize_WF.text() == "":
           QMessageBox.about(self, "ERROR", "Empty Holes Size")
        if(len(self.lineEdit_HStartAdd_WF.text())!=0 and len(self.lineEdit_HSize_WF.text())!=0):   
            queue_HStartAdd.append(int(self.lineEdit_HStartAdd_WF.text()))
            queue_HSize.append(int(self.lineEdit_HSize_WF.text()))
            self.lineEdit_HStartAdd_WF.clear()
            self.lineEdit_HSize_WF.clear()
            print("holes",queue_HStartAdd)
            print ("holes",queue_HSize)

    def SEGMENTS_WF(self):
        if (len(self.lineEdit_SegNum_WF.text())!=0):
            queue_segments.append(int(self.lineEdit_SegNum_WF.text()))        
            print ("segnum",queue_segments)    

    def clear_WF (self):
        self.lineEdit_PName_WF.clear()
        self.lineEdit_SegNum_WF.clear()
        self.tableWidget_WF.clearContents()
        self.tableWidget_WF.setRowCount(0)


    def clear_all_WF (self):
        self.lineEdit_memSize_WF.clear()
        self.lineEdit_HStartAdd_WF.clear()
        self.lineEdit_HSize_WF.clear()
        self.lineEdit_PName_WF.clear()
        self.lineEdit_SegNum_WF.clear()
        self.tableWidget_WF.clearContents()
        self.tableWidget_WF.setRowCount(0)
        self.lineEdit_DeAlloc_Type_WF.clear()
        self.lineEdit_DeAlloc_Num_WF.clear()
        queue_HStartAdd.clear()
        queue_HSize.clear()
        queue_Process_num.clear()
        queue_segments.clear()
        queue_SegName.clear()
        queue_SegSize.clear()
        MEM_Size = 0



    def Finish_WF (self):
        #arr=[12,13,10]
        MemSIZE_WF = self.lineEdit_memSize_WF.text()
        #MEM_Size.append (int(MemSIZE_FF)) 
        MEM_Size=int(MemSIZE_WF)
        memNEW = holes_map(queue_HStartAdd,queue_HSize,MEM_Size)   #queue_HStartAdd = []queue_HSize =[]
        process = process_map(queue_Process_num,queue_segments,queue_SegName,queue_SegSize)
        arr = ALLOCATION_WORST_FIT(memNEW,process,queue_segments,queue_Process_num)
        drawchart(arr[1])
        
        s=''
        err_array =arr[0] 
        if len(err_array)!=0:
            for i in range (0,len(err_array)):
                s+=("P")
                s+=(str(err_array[i]))
                #print("ERROR MSG",str(err_array[i]))
                s+=(" ")
            s+= 'Can not be allocated'    
            #self.my_line_edit.setStyleSheet("color: red;")
            #self.lineEdit_msg_WF.setText ("color: red;",s)  
            self.lineEdit_msg_WF.setText (s)  


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__' :
    main()