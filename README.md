# CITS2401-Labs
Lab work from the unit CITS2401 Computer Analysis and Visualisation

## Lab 2 - Part 4
### Honeybee Population
**Background:**
A honey bee colony is a population of related and closely interacting individuals that form a highly complex society. The population dynamics of this group is complicated, because the fates of individuals within it are not independent, and an individual's lifespan is strongly influenced by their role in the colony. To aid exploration of honey bee population dynamics here, a simple mathematical representation is described of how the social regulation of worker division of labour can influence the longevity of individual bees, and colony growth.\
You can find more details at: http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0018491

**Inputs:**
- H0: Initial population of bees working in the hive
- F0: Initial population of bees working outside the hive
- L: Queen bee’s eggs laying rate
- w: Rate at L(n/w+n) approaches L
- m: Bees’ death rate
- n: Total number of days which need to be simulated

**Outputs:**
- a list containing the population of bees working in the hive for all simulated days
- a list containing the population of bees working outside the hive for all simulated days
- Maximum population of bees working in the hive over all simulated generations n
- Maximum population of bees working outside the hive over all simulated generations n

**Testing Data Inputs:** \
H, F, Hmax, Fmax = honeybee(1,1,1000,80,0.4,10)

***Testing Data Outputs:*** \
H = [1, 26, 265, 975, 1706, 2396, 3034, 3621, 4160, 4654, 5106]\
F = [1, 0, 6, 65, 237, 413, 583, 742, 889, 1024, 1148]\
Hmax = 5106\
Fmax = 1148 

<br><br>
## Lab 3 - Part 1
### Microcar Movements

#### Required Python3 Packages:
- numpy
- matplotlib

#### Background:
The purpose of this lab is to test and compare the expected and actual movements of autonomous vehicles - remote controlled Zen Wheel microcars (http://zenwheels.com).
Each microcar is able to perform the following actions:
- Move North
- Move West
- Move East
- Move South

Multiple cars were tested and the data was recorded in two csv files per microcar. One contains the instructions given to the car, and the other contains the actual actions performed by it. 
The expected movements of cars 1 and 2 are located in the files 'exp1.csv' and 'exp2.csv', respectively. \
Similarly, the actual movements of cars 1 and 2 are located in the files 'act1.csv' and 'act2.csv', respectively. \

#### CSV File format:
The CSV files contain lines for the car movements in the following format: Action, Time, Speed. \
For example... \
N, 10, 8 = Move **North** for **10** seconds with speed **8** meters per second


#### Function 1:
microcar(expected,actual)

- #### Inputs:
    - The 'expected' input is a list of strings containing names of the CSV files 'exp1.csv' and 'exp2.csv'
    - The 'actual' input is a list of strings containing names of the CSV files 'act1.csv' and 'act2.csv'

- #### Outputs:
The function returns six numpy arrays:
    - The expected horizontal displacements for each microcar (ExpHorDisp)
    - The expected vertical displacements for each microcar (ExpVerDisp)
    - The actual horizontal displacements for each microcar (ActHorDisp)
    - The actual vertical displacements for each microcar (ActVerDisp)
    - The expected distances travelled by each microcar (ExpDistance)
    - The actual distances travelled by each microcar (ActDistance)

All displacements and distances are presented in meters and rounded to 2 decimal places.


#### Function 2:
plotmicrocar(expected,actual)

- #### Inputs:
(accepts the same arguments as the microcar function)

- #### Outputs:
The function will create and output the following plots:
- A bar-plot comparing the expected and actual distance covered by each microcar.
- A scatter-plot of the expected final horizontal and vertical displacements for each microcar.
- A scatter-plot of the actual final horizontal and vertical displacements for each microcar.

- #### Example function call:
plotmicrocar(['exp1.csv','exp2.csv'],['act1.csv','act2.csv'])

- #### Sample Files:
