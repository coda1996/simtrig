# simtrig
Made for testing triangulation

## Requirements
### graphics.py

```
pip install graphics.py
```

## Usage
```
-h  Displays help
```
### Using mouse clicks
```
-m=1
```
This is by default enabled

### Entering target position manualy
```
-tx=<number of pixels on x axis>
-ty=<number of pixels on y axis>  
```
### Importing sensor reading data from .txt file
```
-f=/dir/of/tile.txt
```
There is exemple of this file, its called data.txt
In this file ```speed=num``` represents number of seconds between each cycle 

Syntax:
s1_radius;s2_radius;s3_radius

### Importing target data from .txt file
```
-tf=/dir/of/tile.txt
```
There is exemple of this file, its called target_data.txt
In this file speed=<num> represents number of seconds between each cycle.

Syntax:
x_cordinates_of_target;y_cordinates_of_target

### Changing window width(x) and length(y)
```
-wx=<number of pixels for x axis>
-wy=<number of pixels for y axis>
 ``` 
### For positioning sensors on x and y axis
```
-sx=<Number of pixels on x axis where the sensors will start>
-sy=<Number of pixels on y axis where the sensors will start>
-d=<number of pixels between the sensors>
```

### For enabiling and disabling axis drawing
```
-a=1 axis is enabled and shown
-a=0 axis is disabled and not shown (Default)
```
You can edit simtrig.py for placing more sensors and for changing x and y position of each sensor

### For generating output file
```
-o=out_file.txt
```
With this you can draw path and it will be generated in file that is specifide
Speed in this file will be by default 0.1

After generating this file you can feed it to simulation by using ```-tf=out.txt``` flag

### Contact circle
```
-cc=num
```
If set to 1 will generate circle where there is contact 
This is by default set to 1



