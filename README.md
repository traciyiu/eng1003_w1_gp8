 <h1 align="center">Group8's Report For PolyU ENG1003 AAE Freshman Project </h1>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
    <li><a href="#Background-of-Path-Planning-to-Aviation-Engineering">Background of Path Planning to Aviation Engineering</a></li>
    <li><a href="#Theory-of-Path-Planning-Algorithm">Theory of Path Planning Algorithm</a></li>
    <li><a href="#Introduction-of-the-Engineering-Tools">Introduction of the Engineering Tools</a></li>
    <li><a href="#Task-1-Methodology-results-and-Discussion">Task 1:Methodology, results and Discussion</a></li>
    <li><a href="#Task-2-Methodology-results-and-Discussion">Task 2:Methodology, results and Discussion</a></li>
    <li><a href="#task-3-Methodology-results-and-Discussion">task 3:Methodology, results and Discussion</a></li>
    <li><a href="#Reflective-Essay">Reflective Essay </a></li>
    <li><a href="#Reference">Reference </a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
# Background of Path Planning to Aviation Engineering
![1](https://github.com/LiTaiZong/pictures/blob/main/pro10.png)

The Real-time flight tracking technology provides global flight tracking, prediction technology, analysis, and decision-making tools through cooperation with air traffic control systems in different countries/regions. It also includes cooperation with different companies, such as airlines, banks, and technology companies. It will display professional information such as the aircraft's airline, model, current altitude, flight speed, and location to different aircraft operators and service providers, and passengers.


[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)

# Theory of Path Planning Algorithm 

The method used in path planning algorithm is A-star. As Baijayanta Roy[[1]](#jump6) points, A-star is one of the most successful search algorithms to find the shortest path between nodes or graphs.
The advantage of A-star is its heuristic function. The heuristic function includes two aspects.
One is the exact cost from the starting node to the next node. The other is the estimated cost from the next node to the goal node. And the heuristic function combines them together to calculate the cost of the neighboring node. By using this method, it’s much easier for path planning to find the best path from the starting node to the goal node


[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)

# Introduction of the Engineering Tools 

## a.Python
![1](https://github.com/LiTaiZong/pictures/blob/main/pro9.png)

balabala

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)

## b.Github
![1](https://github.com/LiTaiZong/pictures/blob/main/pro8.png)

### What is Github?

1. GitHub is a web-based interface that uses Git 
2. It lets multiple people make separate changes to web pages at the same time
3. Lets different people share their code 
4. Having over 40 million users and more than 190 million repositories[[2]](#jump7)



### When did it start?

1. It began on October 19, 2007
2. The website was launched as a beta version in February 2008 and officially launched in April


### Main Function of Github

GitHub is usually used for software development. GitHub also supports the following formats and functions

1. document
2. Issue tracking system
3. Wiki
4. task list
5. Gantt chart
6. Visual location analysis
7. Preview 3D rendering files
8. Preview PSD files of Adobe Photoshop, and even compare different versions of the same file.

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)

# Task 1 Methodology results and Discussion
## Methodology:
### First,we should find the code which needs to be changed.
**Start and Finish Point:**

![1](https://github.com/LiTaiZong/pictures/blob/main/pro1.png)
****
**Set obstacle positions:**  

![2](https://github.com/LiTaiZong/pictures/blob/main/pro2.png)
****
**Set fuel consuming area and time consuming area:**

![3](https://github.com/LiTaiZong/pictures/blob/main/pro2.png)

### Secondly,according to our goal,we change the code:
```python
    # start and goal position
    sx = 0.0  # [m]
    sy = 0.0  # [m]
    gx = 50.0  # [m]
    gy = 0.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]
```
****
```python
# Group 8 area
for i in range(20, 60): # draw the free border
    ox.append(40.0)
    oy.append(i)

for i in range(0, 20):
    ox.append(i)
    oy.append(-1 * i + 10)
```
****
```python
    # set fuel consuming area
    fc_x, fc_y = [], []
    for i in range(30, 35):
        for j in range(0, 40):
            fc_x.append(i)
            fc_y.append(j)
    
    # set time consuming area
    tc_x, tc_y = [], []
    for i in range(10, 20):
        for j in range(20, 50):
            tc_x.append(i)
            tc_y.append(j)
```
## Result:
<img width="570" height="450" src="https://github.com/LiTaiZong/pictures/blob/main/GIF1.gif"/>  

****
**We tried all the data and found that the model PolyU-A380 achieved minimum cost.**

![5](https://github.com/LiTaiZong/pictures/blob/main/pro4.png)

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)

# Task 2 Methodology results and Discussion
## Methodology:
### Firstly,we found that when the two values are equal, the cost will be the least.
### Secondly,we calculate all the possible values and find that when the values equal to 20, the cost will be the least.
### Finally,We use linear programming to prove that the cost is the least when the values are 20.

**How to prove:**

![111](https://github.com/LiTaiZong/pictures/blob/main/pro6.png)
**Running results:**

![111](https://github.com/LiTaiZong/pictures/blob/main/pro5.png)
****
**_By trying we found that when both variables are taken as 20, the total cost is the least_**

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)

# task 3 Methodology results and Discussion
## Methodology:
### First,we should find the code which needs to be changed:
* 1. Calculate the cost.
* 2. Design a minus cost area
* 3. Make the new area overlap the flight route as much as possible
### Secondly,according to our goal,we change the code:
**Calculate the cost:** 
```python
 # add more cost in minus cost area
                if self.calc_grid_position(node.x, self.min_x) in self.pc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.pc_y:
                        # print("minus cost area!!")
                        node.cost = node.cost + self.C_P * self.Delta_P * self.motion[i][2]
```
****
**Set minus cost area:**
```python
# set minus cost area
    pc_x, pc_y = [], []
    for i in range(-2, 1):
            pc_x.append(i)
            pc_y.append(4-i)
    for i in range(11, 24):
            pc_x.append(i)
            pc_y.append(23-i)
```
**Change the color of minus cost area:**
```python
    plt.plot(fc_x, fc_y, "oy") # plot the fuel consuming area
    plt.plot(tc_x, tc_y, "or") # plot the time consuming area
    plt.plot(pc_x, pc_y, "ob")
```
## Result:
<img width="570" height="450" src="https://github.com/LiTaiZong/pictures/blob/main/gif2.gif"/>

****
**We found that the cost is under our expectation:**

![5](https://github.com/LiTaiZong/pictures/blob/main/pro7.png)

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)

# Additional Task 1
## Methodology:
** To finish the addition task 1(extra check point), we decide to use thecode of startpoint and goalpoint.**
****
**conduct the main function**
```python
if __name__ == '__main__':
    main()
```
****
**The most important part:use class:AStarPlanner
```python
a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)
```
**We found it difficult to print the value orgnized, so we create "AstarPlanner2"and "AstarPlanner3"to make the results easier to see.
****
**Besides, we found that this code is the reason why the program stops.
```python
plt.show() # show the plot
```
**So we need to put it into the last part.
**After we change everything above, what we should do is only to change the main function.
```python
def main():
    print(__file__ + " start the A star algorithm demo !!") # print simple notes

    # start and goal position
    sx = 0.0  # [m]
    sy = 0.0  # [m]
    gx = 15.0  # [m]
    gy = 25.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]


    # set obstacle positions for group 9
    ox, oy = [], []
    for i in range(-10, 60): # draw the button border 
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 60): # draw the right border
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60): # draw the top border
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60): # draw the left border
        ox.append(-10.0)
        oy.append(i)

    for i in range(20, 60): # draw the free border
        ox.append(40.0)
        oy.append(i)

    for i in range(0, 20):
        ox.append(i)
        oy.append(-1 * i + 10)
    
    fc_x, fc_y = [], []
    for i in range(30, 35):
        for j in range(0, 40):
            fc_x.append(i)
            fc_y.append(j)
    
    # set time consuming area
    tc_x, tc_y = [], []
    for i in range(10, 20):
        for j in range(20, 50):
            tc_x.append(i)
            tc_y.append(j)

    if show_animation:  # pragma: no cover
        plt.plot(ox, oy, ".k") # plot the obstacle
        plt.plot(0, 0, "xg") # plot the start position 
        plt.plot(15, 25, "oy") # plot the end position
        plt.plot(32, 5, "ob") # plot the start position 
        plt.plot(50, 0, "xb") # plot the end position
        
        plt.plot(fc_x, fc_y, "oy") # plot the fuel consuming area
        plt.plot(tc_x, tc_y, "or") # plot the time consuming area

        plt.grid(True) # plot the grid to the plot panel
        plt.axis("equal") # set the same resolution for x and y axis 

    a_star = AStarPlanner1(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)
    
    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-b") # show the route 
        plt.pause(0.001) # pause 0.001 seconds

 # start and goal position
    sx = 15.0  # [m]
    sy = 25.0  # [m]
    gx = 32.0  # [m]
    gy = 5.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]

    if show_animation:  # pragma: no cover
        plt.plot(ox, oy, ".k") # plot the obstacle
        plt.plot(0, 0, "xg") # plot the start position 
        plt.plot(15, 25, "oy") # plot the end position
        plt.plot(32, 5, "ob") # plot the start position 
        plt.plot(50, 0, "xb") # plot the end position

        plt.grid(True) # plot the grid to the plot panel
        plt.axis("equal") # set the same resolution for x and y axis 

    a_star = AStarPlanner2(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-b") # show the route 
        plt.pause(0.001) # pause 0.001 seconds

    sx = 32.0  # [m]
    sy = 5.0  # [m]
    gx = 50.0  # [m]
    gy = 0.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]

    if show_animation:  # pragma: no cover
        plt.plot(ox, oy, ".k") # plot the obstacle
        plt.plot(0, 0, "xg") # plot the start position 
        plt.plot(15, 25, "oy") # plot the end position
        plt.plot(32, 5, "ob") # plot the start position 
        plt.plot(50, 0, "xb") # plot the end position


        plt.grid(True) # plot the grid to the plot panel
        plt.axis("equal") # set the same resolution for x and y axis 

    a_star = AStarPlanner3(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-b") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.show() # show the plot
```
## result
<img width="570" height="450" src="https://github.com/LiTaiZong/pictures/blob/main/gif3.gif"/> 
<img width="500" height="200" src="https://github.com/LiTaiZong/pictures/blob/main/pro11.png"/> 

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)
# Additional Task 2
## Methodology:
### Modify the code so that:
* **Only the fuel-consuming area remains and generate it randomly with a fixed area (30x30)**  
**solution:**
```python
fc_x, fc_y = [], []
    r_fc_x = random.randrange(-9, 31)
    r_fc_y = random.randrange(-9, 31)
    for i in range(r_fc_x, r_fc_x+30):
        for j in range(r_fc_y, r_fc_y+30):
            fc_x.append(i)
            fc_y.append(j)
```
****
* **Diagonal movement is disabled, change parameter(s) so that the object could travel within one grid size**  
**solution:**
travel within one grid size:
```python
    grid_size = 1  
    robot_radius = 0  
```
**Diagonal movements are disabled:**
```python
@staticmethod
    def get_motion_model(): 
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1]]
```

****
* **Destination and starting points are generated randomly with at least a 50-unit distance in-between**
**solution:**
```python
while True:
        sx = random.randrange(-10, 59)  # [m]
        sy = random.randrange(-10, 59)  # [m]
        gx = random.randrange(-10, 59)  # [m]
        gy = random.randrange(-10, 59)  # [m]
        if (gx-sx) >= 50 or (sx-gx) >= 50 or (gy-sy) >= 50 or (sy-gy) >= 50:
            break
```
* **Plotting of the fuel-consuming area would not cover the obstacles, and obstacles should not generateat/near the start and end poin**
**solution:**
```python
    for i in range(0,1200):
        g=random.randrange(-9, 60)
        #if(abs(g-sx)>=3 and abs(g-gx)>=3):
        if g==sx:
            g=-10
        if g==sx+1:
            g=-10
        if g==sx-1:
            g=-10
        if g==gx:
            g=-10
        if g==gx+1:
            g=-10
        if g==gx-1:
            g=-10
        ox.append(g)
        g=random.randrange(-9, 60)
        #if(abs(g-sy)>=2 and abs(g-gy)>=2):
        if g==sy:
            g=-10  
        if g==sy+1:
            g=-10
        if g==sy-1:
            g=-10
        if g==gy:
            g=-10
        if g==gy+1:
            g=-10
        if g==gy-1:
            g=-10
        oy.append(g)
```
****
# result:
**Here are the examples.**  
**Result 1**

<img width="570" height="450" src="https://github.com/LiTaiZong/pictures/blob/main/gif4.gif"/> 

**Result 2**

<img width="570" height="450" src="https://github.com/LiTaiZong/pictures/blob/main/gif5.gif"/> 

**Result 3**

<img width="570" height="450" src="https://github.com/LiTaiZong/pictures/blob/main/gif6.gif"/> 

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)

# Reflective Essay
### 1
balabala
### 2

### 3
### 4
### 5


[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)
# Reference

<span id="jump6">[1]</span> *B. Roy “A-Star Search algorithm with step-by-step code” (2019).Github. https://towardsdatascience.com/a-star-a-search-algorithm-eb495fb156bb*  
*  

<span id="jump7">[2]</span> *“User search.” (2021). Github. https://github.com/search?q=type:user&type=Users*  


[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-red.svg)](https://github.com/traciyiu/eng1003_w1_gp8/blob/main/README.md)
