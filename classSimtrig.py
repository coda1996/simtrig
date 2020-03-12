from graphics import GraphWin, Rectangle, Circle, Text, Point, color_rgb, Line
import time as t
import math



class start():
    def __init__(self, win_x, win_y, axis_width, win): 
        
        self.win = win
        self.axis_width = axis_width
        self.win_x = win_x
        self.win_y = win_y


        y_axis_color = "Red"
        x_axis_color = "Blue"

        

        y_axis = Line(Point(20,20), Point(20, win_y-10))
        y_axis.setWidth(axis_width)
        y_axis.setFill(y_axis_color)
        y_axis.draw(win)

        arrow_line_1_y = Line(Point(20, win_y-10), Point(30, win_y-40))
        arrow_line_1_y.setFill(y_axis_color)
        arrow_line_1_y.setWidth(axis_width)
        arrow_line_1_y.draw(win)

        arrow_line_2_y = Line(Point(20, win_y-10), Point(10, win_y-40))
        arrow_line_2_y.setFill(y_axis_color)
        arrow_line_2_y.setWidth(axis_width)
        arrow_line_2_y.draw(win)

        txt_y_axis = Text(Point(45, win_y-20), "Y")
        txt_y_axis.setFill(y_axis_color)
        txt_y_axis.draw(win)





        x_axis = Line(Point(20,20), Point(win_x-10, 20))
        x_axis.setWidth(axis_width)
        x_axis.setFill(x_axis_color)
        x_axis.draw(win)

        arrow_line_1_x = Line(Point(win_x-10, 20), Point(win_x-40, 10))
        arrow_line_1_x.setFill(x_axis_color)
        arrow_line_1_x.setWidth(axis_width)
        arrow_line_1_x.draw(win)

        arrow_line_2_x = Line(Point(win_x-10, 20), Point(win_x-40, 30))
        arrow_line_2_x.setFill(x_axis_color)
        arrow_line_2_x.setWidth(axis_width)
        arrow_line_2_x.draw(win)

        txt_x_axis = Text(Point(win_x-20, 45), "X")
        txt_x_axis.setFill(x_axis_color)
        txt_x_axis.draw(win)







class sensor():

    def __init__(self, x, y, radius, color, name, win):
        self.x = x
        self.y = y
        self.win = win
        self.radius = radius
        self.color = color
        self.name = name


        s = Circle(Point(x,y), radius)
        s.setFill(color)
        s.draw(win)
        


    def sensor_radius(self, radius):
        
        c = Circle(Point(self.x, self.y), radius)
        c.setOutline(self.color)
        c.draw(self.win)

    def click_circle(self, click_x, click_y, txt_x, txt_y):
        
        self.click_x = click_x
        self.click_y = click_y

        radius = math.sqrt(math.pow((self.x - click_x), 2) + math.pow((self.y - click_y), 2))
        s = Circle(Point(self.x,self.y), radius)
        s.setOutline(self.color)
        s.draw(self.win)

        l = Line(Point(self.x,self.y), Point(click_x, click_y))
        l.setFill(self.color)
        l.draw(self.win)

        
        t = Text(Point(txt_x,txt_y), int(radius))
        t.setSize(17)
        t.setFill(self.color)
        t.draw(self.win)

    def click_circle_no_txt(self, click_x, click_y):
        
        self.click_x = click_x
        self.click_y = click_y

        radius = math.sqrt(math.pow((self.x - click_x), 2) + math.pow((self.y - click_y), 2))
        s = Circle(Point(self.x,self.y), radius)
        s.setOutline(self.color)
        s.draw(self.win)


    




