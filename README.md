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

balabala

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-Cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)

# Theory of Path Planning Algorithm 

balabala

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-Cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)

# Introduction of the Engineering Tools 

## a.Python

balabala

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-Cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)

## b.Github

balabala

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-Cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)

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

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-Cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)

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

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-Cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)

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

[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-Cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)

# Reflective Essay
### 1
balabala
### 2
### 3
### 4
### 5


[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-Cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)
# Reference


[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-Cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)
