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


## Lab 3 - Part 1
### Microcar Movements
**Background:**
Testing and comparing the expected and actual movements of autonomous vehicles - remote controlled Zen Wheel microcars (http://zenwheels.com).
Each microcar is able to perform the following actions:
- Move North
- Move West
- Move East
- Move South

Multiple microcars were testing and the data was recorded in two csv files per microcar. One contains the instructions given to each microcar, and the other contains the actual actions performed by each microcar. 
The expected movements of cars 1 and 2 are located in the files 'exp1.csv' and 'exp2.csv' respectively. \
Similarly, the actual movements of cars 1 and 2 are located in the files 'act1.csv' and 'act2.csv' respectively. \

**CSV File format**
The CSV files contain lines for the car movements in the following format: Action, Time, Speed. \
For example... \
N, 10, 8 = Move North for 10 seconds with speed 8 meters per second


**Inputs:**


**Outputs:**


**Testing Data Inputs:** \


***Testing Data Outputs:*** \
