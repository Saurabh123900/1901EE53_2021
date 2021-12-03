from fpdf import FPDF
from datetime import date
today = date.today()
import os

class PDF(FPDF):

    def header(self, st1 = '',st2 = ''):
        
        self.set_font("times","",10)
        
        self.image('header.jpg', 5, 5, 410)
        self.ln()
        self.set_y(self.get_y()+5)
        self.set_x(self.get_x()+130)
        self.cell(100, 10, st1, border=0)
        self.ln()
        self.set_y(self.get_y()-5)
        self.set_x(self.get_x()+130)
        self.cell(100, 10, st2, border=0)
        
    
    # Page footer
    def footer(self):
        date = today.strftime("%b-%d-%Y")
        date = "Date of Issue: "+ str(date)
        
        path1=os.path.join("uploaded_sign","seal.jpg")
        path2=os.path.join("uploaded_sign","signature.png")
        self.set_font(size = 15)
        self.image(path1, 160,200, 65)
        self.image(path2, 300,200, 75)

        self.set_y(self.get_y() + 55)
        self.set_x(self.get_x() + 20)
        self.cell(10, 10, date, border=0)
        x_left = self.get_x() +22
        y1 = self.get_y() + 10
        x_right = self.get_x() + 50
        self.line(x_left,y1,x_right,y1)
        self.set_y(self.get_y() - 55)
        self.set_x(self.get_x() - 20)

        self.set_y(self.get_y() + 65)
        self.set_x(self.get_x() + 300)

        x_left = self.get_x()
        y1 = self.get_y() 
        x_right = self.get_x() + 65
        self.line(x_left,y1,x_right,y1)
        self.cell(200 , 10, "Assistant Registrar (Academic)", border=0)

    def create_table(self, table_data, title='', data_size = 5, title_size=10, align_data='L', align_header='L', cell_width='even', x_start='x_default',y_start = 'y_default',emphasize_data=[], emphasize_style=None,emphasize_color=(0,0,0),f = 0,st = ""): 
        
        default_style = self.font_style
        if emphasize_style == None:
            emphasize_style = default_style
            
        def get_col_widths():
            col_width = [10,30,8,8,8]
            return col_width

        header = table_data[0]
        data = table_data[1:]

        line_height = 7

        col_width = get_col_widths()
        self.set_font(size=title_size)

        self.set_y(y_start)
        self.set_x(x_start)

        #print (self.get_x(),self.get_y())


        if title != '':
            self.multi_cell(0, line_height, title, border=0, align='j', ln=3, max_line_height=self.font_size)
            self.ln(line_height) # move cursor back to the left margin

        self.set_font(size=data_size)
        

        
        y1 = self.get_y()
        if x_start:
            x_left = x_start
        else:
            x_left = self.get_x()



        #print (self.get_x(),self.get_y())



        x_right = self.epw + x_left
        if x_start:
            self.set_x(x_start)
        for i in range(len(header)):
            datum = header[i]
            self.multi_cell(col_width[i], line_height, datum, border=0, align=align_header, ln=3, max_line_height=self.font_size)
            x_right = self.get_x()
        self.ln(line_height) # move cursor back to the left margin
        y2 = self.get_y()

        self.line(x_left,y1,x_right,y1)
        self.line(x_left,y2,x_right,y2)


        for i in range(len(data)):
            if x_start:
                self.set_x(x_start)
            row = data[i]
            for i in range(len(row)):
                datum = row[i]
                if not isinstance(datum, str):
                    datum = str(datum)
                adjusted_col_width = col_width[i]
                self.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
            self.ln(line_height) 
        
        y3 = self.get_y()
        self.line(x_left,y3,x_right,y3)
        self.set_x(x_start)
        self.multi_cell(100, 10, st, border=0, align=align_data, ln=3, max_line_height=self.font_size)
        