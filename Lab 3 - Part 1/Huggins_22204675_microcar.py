import numpy as np
import matplotlib.pyplot as plt

def getresult(expected,actual):        # this is a helper function to open the csv file and perform calculations for each microcar
    with open(expected,'r') as expcar:    # open the csv files of the 'expected' car actions
        lst_exp_hor_sec = []       
        lst_exp_hor_speed = []
        lst_exp_ver_sec = []
        lst_exp_ver_speed = []
        contents_exp = expcar.readlines()
        for line in contents_exp:
            fields = line.split(',')
            if (fields[0]=='E') or (fields[0]=='W'):     # detects the horizontal displacements
                if fields[0]=='W':
                    lst_exp_hor_sec.append(float(fields[1])*-1)     # if the car travels West, make the value negative
                    lst_exp_hor_speed.append(float(fields[2]))
                else:
                    lst_exp_hor_sec.append(float(fields[1]))
                    lst_exp_hor_speed.append(float(fields[2]))
            if (fields[0]=='N') or (fields[0]=='S'):     # detects the vertical displacements
                if fields[0]=='S':
                    lst_exp_ver_sec.append(float(fields[1])*-1)     # if the car travels South, make the value negative
                    lst_exp_ver_speed.append(float(fields[2]))
                else:
                    lst_exp_ver_sec.append(float(fields[1]))
                    lst_exp_ver_speed.append(float(fields[2]))
        
    with open(actual,'r') as actcar:     # open the csv files of the 'actual' car actions
        lst_act_hor_sec = []
        lst_act_hor_speed = []
        lst_act_ver_sec = []
        lst_act_ver_speed = []
        contents_act = actcar.readlines()
        for line in contents_act:
            fields = line.split(',')
            if (fields[0]=='E') or (fields[0]=='W'):     # detects the horizontal displacements
                if fields[0]=='W':
                    lst_act_hor_sec.append(float(fields[1])*-1)    # if the car travels West, make the value negative
                    lst_act_hor_speed.append(float(fields[2]))
                else:
                    lst_act_hor_sec.append(float(fields[1]))
                    lst_act_hor_speed.append(float(fields[2]))
            if (fields[0]=='N') or (fields[0]=='S'):    # detects the vertical displacements
                if fields[0]=='S':
                    lst_act_ver_sec.append(float(fields[1])*-1)    # if the car travels South, make the value negative
                    lst_act_ver_speed.append(float(fields[2]))
                else:
                    lst_act_ver_sec.append(float(fields[1]))
                    lst_act_ver_speed.append(float(fields[2]))
        
        #expected car calculations
        Exp_Hor_seconds = np.array(lst_exp_hor_sec)
        Exp_Hor_speed = np.array(lst_exp_hor_speed)
        Exp_Ver_seconds = np.array(lst_exp_ver_sec)
        Exp_Ver_speed = np.array(lst_exp_ver_speed)
        Exp_Horizontal_Disp = sum(Exp_Hor_seconds*Exp_Hor_speed)
        Exp_Horizontal_Dist = sum(abs(Exp_Hor_seconds*Exp_Hor_speed))
        Exp_Vertical_Disp = sum(Exp_Ver_seconds*Exp_Ver_speed)
        Exp_Vertical_Dist = sum(abs(Exp_Ver_seconds*Exp_Ver_speed))
        Exp_Dist_Travelled = Exp_Horizontal_Dist + Exp_Vertical_Dist
        
        #actual car calculations
        Act_Hor_seconds = np.array(lst_act_hor_sec)
        Act_Hor_speed = np.array(lst_act_hor_speed)
        Act_Ver_seconds = np.array(lst_act_ver_sec)
        Act_Ver_speed = np.array(lst_act_ver_speed)
        Act_Horizontal_Disp = sum(Act_Hor_seconds*Act_Hor_speed)
        Act_Horizontal_Dist = sum(abs(Act_Hor_seconds*Act_Hor_speed))
        Act_Vertical_Disp = sum(Act_Ver_seconds*Act_Ver_speed)
        Act_Vertical_Dist = sum(abs(Act_Ver_seconds*Act_Ver_speed))
        Act_Dist_Travelled = Act_Horizontal_Dist + Act_Vertical_Dist
        
    return Exp_Horizontal_Disp, Exp_Vertical_Disp, Act_Horizontal_Disp, Act_Vertical_Disp, Exp_Dist_Travelled, Act_Dist_Travelled


def microcar(expected,actual):      # the microcar function receives the calculated displacements and distances from the 'getresult' helper function
    ExpHorDisp = np.arange(0,len(expected))   # create the expected horizontal displacements numpy array
    ExpVerDisp = np.arange(0,len(expected))   # create the expected vertical displacements numpy array
    ActHorDisp = np.arange(0,len(expected))   # create the actual horizontal displacements numpy array
    ActVerDisp = np.arange(0,len(expected))   # create the actual vertical displacements numpy array
    ExpDistance = np.arange(0,len(expected))  # create the expected distances numpy array
    ActDistance = np.arange(0,len(expected))  # create the actual distances numpy array
    for i in range(0,len(expected)):
        ExpHorDisp[i], ExpVerDisp[i], ActHorDisp[i], ActVerDisp[i], ExpDistance[i], ActDistance[i] = getresult(expected[i],actual[i])    # passes the values for each microcar into the 6 numpy arrays
    return ExpHorDisp, ExpVerDisp, ActHorDisp, ActVerDisp, ExpDistance, ActDistance    #return the 6 numpy arrays

def plotmicrocar(expected,actual):
    a, b, c, d, e, f = microcar(expected,actual)
    
    yvals_Exp_Dist = []
    yvals_Act_Dist = []
    for p in range(0,len(expected)):
        yvals_Exp_Dist.append(e[p])
        yvals_Act_Dist.append(f[p])
        
    plt.subplot(2,1,1)
    y_min = 0       # set the minimum y axis value
    y_max = 1250    # set the maximum y axis value
    if max(e) > y_max:    # if the maximum Expected Distance exceeds the current highest y-axis value
        y_max = max(e)    # adjust the highest y-axis value accordingly
    if max(f) > y_max:    # if the maximum Actual Distance exceeds the current highest y-axis value
        y_max = max(f)    # adjust the highest y-axis value accordingly
    x_axis = np.arange(0,len(expected))   #sets the x-axis to reflect the number of cars being tested
    y_axis = np.arange(y_min, y_max, 250)   
    plt.bar(x_axis, yvals_Exp_Dist, align='edge', width=-0.3)
    plt.bar(x_axis, yvals_Act_Dist, align='edge', width=0.3)
    plt.ylabel('Dist (m)')
    plt.xlabel('mcar')
    plt.xticks(x_axis)
    plt.yticks(y_axis)
    plt.legend(['Expected','Actual'])
    plt.title('Distance')
    plt.tight_layout()
    
    Legend_Disp = []
    for e in range(0,len(expected)):
        Legend_Disp.append('Car%d' % e)   # this sets the scatter plot legends to reflect the number of cars being tested
        
    x_axis_min = -75
    y_axis_min = -75
    x_axis_max = 100
    y_axis_max = 100
        
    for i in range(0,len(expected)):
        plt.subplot(2,2,3)
        if max(a) > x_axis_max:
            x_axis_max = max(a)   # adjusts the highest x-axis value if the horizontal displacement is outside the range
        if min(a) < x_axis_min:
            x_axis_min = min(a)   # adjusts the lowest x-axis value if the horizontal displacement is outside the range
        if max(b) > y_axis_max:
            y_axis_max = max(b)   # adjusts the highest y-axis value if the vertical displacement is outside the range
        if min(b) < y_axis_min:
            y_axis_min = min(b)   # adjusts the lowest y-axis value if the vertical displacement is outside the range
        x_axis = np.arange(x_axis_min, x_axis_max, 25)
        y_axis = np.arange(y_axis_min, y_axis_max, 25)
        plt.scatter([a[i]], [b[i]])
        plt.ylabel('y Disp (m)')
        plt.xlabel('x Displacement (m)')
        plt.xticks(x_axis, fontsize="small")
        plt.yticks(y_axis, fontsize="small")
        plt.legend(Legend_Disp, loc="best", fontsize="small")
        plt.title('Expected Displacement')
        plt.tight_layout()
    
        plt.subplot(2,2,4)
        if max(c) > x_axis_max:
            x_axis_max = max(c)   # adjusts the highest x-axis value if the horizontal displacement is outside the range
        if min(c) < x_axis_min:
            x_axis_min = min(c)   # adjusts the lowest x-axis value if the horizontal displacement is outside the range
        if max(d) > y_axis_max:
            y_axis_max = max(d)   # adjusts the highest y-axis value if the vertical displacement is outside the range
        if min(d) < y_axis_min:
            y_axis_min = min(d)   # adjusts the lowest y-axis value if the vertical displacement is outside the range
        x_axis = np.arange(x_axis_min, x_axis_max, 25)
        y_axis = np.arange(y_axis_min, y_axis_max, 25)
        plt.scatter([c[i]], [d[i]])
        plt.ylabel('y Disp (m)')
        plt.xlabel('x Displacement (m)')
        plt.xticks(x_axis, fontsize="small")
        plt.yticks(y_axis, fontsize="small")
        plt.legend(Legend_Disp, loc="best", fontsize="small")
        plt.title('Actual Displacement')
        plt.tight_layout()
    
    plt.show()
