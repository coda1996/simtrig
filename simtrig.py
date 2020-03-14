import time as t
from graphics import GraphWin, Rectangle, Point, color_rgb, Line, Text, Circle
import argparse
import math
import re
import classSimtrig


def draw_background(win_x, win_y, win, axis_flg):
    if (axis_flg != 1):
        backround = Rectangle(Point(0,0), Point(win_x, win_y))
        backround.setFill(color_rgb(30,30,30))
        backround.draw(win)
    else:

        backround = Rectangle(Point(10,10), Point(win_x, win_y))
        backround.setFill(color_rgb(30,30,30))
        backround.draw(win)
    #win.update()



def draw_sensors(win):
    global s1, s2, s3

    s1 = classSimtrig.sensor(300, 400, 5, "Green", "s1", win)
    s2 = classSimtrig.sensor(400, 400, 5, "Red", "s2", win)
    s3 = classSimtrig.sensor(500, 400, 5, "Yellow", "s3", win)
    #win.update()


def draw_sensors_with_distance_on_x_axis(x, y, d, win):
    global s1, s2, s3, draw_sensors_with_distance_on_x_axis_flg

    s1 = classSimtrig.sensor(x, y, 5, "Green", "s1", win)
    s2 = classSimtrig.sensor(x+d, y, 5, "Red", "s2", win)
    s3 = classSimtrig.sensor(x+d+d, y, 5, "Yellow", "s3", win)
    draw_sensors_with_distance_on_x_axis_flg = 1
    #win.update()

def refresh(win_x, win_y, win):
    
    try:
        if (draw_sensors_with_distance_on_x_axis_flg != 1):
            draw_background(win_x, win_y, win, axis_flg)
            draw_sensors(win)
        else:
            draw_background(win_x, win_y, win, axis_flg)
            draw_sensors_with_distance_on_x_axis(args.sensor_start_x, args.sensor_start_y, args.distance, win)
    except NameError:
        draw_background(win_x, win_y, win, axis_flg)
        draw_sensors(win)
    win.update()

def get_mouse_data():
        while True:
            cp = win.getMouse()
            refresh(win_x, win_y, win)
        
            s1.click_circle(cp.getX(), cp.getY(), cp.getX()+50, cp.getY() - 70)
            s2.click_circle(cp.getX(), cp.getY(), cp.getX()+100, cp.getY() - 70)
            s3.click_circle(cp.getX(), cp.getY(), cp.getX()+150, cp.getY() - 70)
            if (args.contact_circle == 1):
                contact_circle(cp.getX(), cp.getY())
            #win.update()
def target_data(x, y):

        s1.click_circle(x, y, x+50, y - 70)
        s2.click_circle(x, y, x+100, y - 70)
        s3.click_circle(x, y, x+150, y - 70)
        if (args.contact_circle == 1):
            contact_circle(x, y)

        #win.update()
        
    
        
        

def socket_data():
    # todo!!!
    pass

def file_data(file_dir):
    new_speed = 1

    f = open(str(file_dir), "r")
    
    for line in f:
        new_speed_flg = re.match("speed=", line)

        if new_speed_flg:
            speed = re.split("speed=", line)
            new_speed = float(speed[1])
        else:
        
            data = re.split(";", line)
            
            s1.sensor_radius(int(data[0]))
            s2.sensor_radius(int(data[1]))
            s3.sensor_radius(int(data[2]))
            refresh(win_x, win_y, win)
            t.sleep(new_speed)
            refresh(win_x, win_y, win)
            

    get_mouse_data()

def target_file_data(target_file_dir):
    new_speed = 1
    f = open(str(target_file_dir), "r")

    for line in f:
            new_speed_flg = re.match("speed=", line)

            if new_speed_flg:
                speed = re.split("speed=", line)
                new_speed = float(speed[1])
            else:
                refresh(win_x, win_y, win)
                data = re.split(";", line)
                s1.click_circle_no_txt(int(data[0]), int(data[1]))
                s2.click_circle_no_txt(int(data[0]), int(data[1]))
                s3.click_circle_no_txt(int(data[0]), int(data[1]))
                
                if (args.contact_circle == 1):
                    contact_circle(int(data[0]), int(data[1]))
                t.sleep(new_speed)

               
                
    get_mouse_data()


def draw_path(output_file):
    f = open(str(output_file), "w")

    cp1 = win.getMouse()
    p = Circle(Point(cp1.getX(), cp1.getY()), 3)
    p.setFill("Yellow")
    p.draw(win)

    cp_start_x = cp1.getX()
    cp_start_y = cp1.getY()

    f.write("speed=0.1\n")
    f.write(str(int(cp1.getX())) + ";" + str(int(cp1.getY())) + "\n")
    while True:
        try:
            cp2 = win.getMouse()
            f.write(str(int(cp2.getX())) + ";" + str(int(cp2.getY())) + "\n")
            p = Circle(Point(cp2.getX(), cp2.getY()), 3)
            p.setFill("Yellow")
            p.draw(win)

            l = Line(Point(cp_start_x, cp_start_y), Point(cp2.getX(), cp2.getY()))
            l.setFill("Red")
            l.draw(win)

            cp_start_x = cp2.getX()
            cp_start_y = cp2.getY()
        except KeyboardInterrupt:
            f.close()
            print("done")
            break
            
    
def contact_circle(x, y):
    c = Circle(Point(x, y), 5)
    c.setFill("Red")
    c.draw(win)
    win.update()



def main():
    global args, win, win_x, win_y, axis_width, axis_flg

    parser = argparse.ArgumentParser(description="Quick script")

    parser.add_argument("-d", "--distance", default=None, type=int, help="This is the distance between sensors")
    parser.add_argument("-sx", "--sensor_start_x", default=200, type=int, help="This is starting point for sensors on X axis")
    parser.add_argument("-sy", "--sensor_start_y", default=200, type=int, help="This is starting point for sensors on Y axis")


    parser.add_argument("-tx", "--target_x", default=None, type=int, help="This is target distance in pixels on X axis")
    parser.add_argument("-ty", "--target_y", default=None, type=int, help="This is target distance in pixels on Y axis")
    
    parser.add_argument("-m", "--mouse", default=1, type=int, help="For using mouse to get data")
    parser.add_argument("-s", "--socket", default=0, type=int, help="For using socket to get data")
    parser.add_argument("-f", "--file", default="", type=str, help="For using file to get data")
    parser.add_argument("-tf", "--target_file", default="", type=str, help="File with target data (x and y cordinates)")

    parser.add_argument("-wx", "--win_x", default=1000, type=int, help="For defining window size in px on X axis")
    parser.add_argument("-wy", "--win_y", default=700, type=int, help="For defining window size in px on Y axis")

    parser.add_argument("-aw", "--axis_width", default=2, type=int, help="For defining window size in px on Y axis")

    parser.add_argument("-a", "--axis", default=0, type=int, help="For choosing if you want axis or not")

    parser.add_argument("-o", "--output", default="", type=str, help="For choosing output file")


    parser.add_argument("-cc", "--contact_circle", default=1, type=int, help="For choosing if you want contact circle")

    args = parser.parse_args()


    
    win_x = args.win_x
    win_y = args.win_y

    axis_width = args.axis_width

    axis_flg = args.axis


    win = GraphWin("SimTrig", win_x, win_y, autoflush=False)
    draw_background(win_x, win_y, win, draw_background)
    classSimtrig.start(win_x, win_y, axis_width,win)
    
    

    if(args.distance != None):
        draw_sensors_with_distance_on_x_axis(args.sensor_start_x, args.sensor_start_y, args.distance, win)
    else:
        draw_sensors(win)  


    if (args.target_x == None) & (args.target_y != None):
        print("Missing target_y argument")

    elif (args.target_x != None) & (args.target_y == None):
         print("Missing target_x argument")

    if (args.socket == 1):
        socket_data()

    elif (args.file != ""):
        file_data(args.file)

    elif (args.target_file != ""):
        target_file_data(args.target_file)


    elif (args.target_x != None) & (args.target_y != None):
        target_data(args.target_x, args.target_y)
        get_mouse_data()

    elif (args.output != ""):
        draw_path(args.output)

    else:
        get_mouse_data()

    pass


main()



    
