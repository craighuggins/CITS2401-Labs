# Author: Craig Ian Bond Huggins
# Version: 28/4/2019
# Student ID: 22204675

def honeybee(H0,F0,L,w,m,n):
    if (type(H0) != int) or (type(F0) != int):     #ensures that the initial population is a valid integer
        print("Initial population of bees must be a valid integer")
        return
    elif H0 < 0 or F0 < 0 or L < 0 or w < 0 or m < 0 or n < 0:     #ensures that none of the inputs to the function can be negative
        print("Inputs cannot be negative")
        return
    else:
        H = [0]*(n+1)
        F = [0]*(n+1)
        H[0] = H0     #stores the initial population of bees inside the hive as the first element in the list
        F[0] = F0     #stores the initial population of bees outside the hive as the first element in the list
        for t in range (1,(n+1)):
            N = H[t-1] + F[t-1]
            H[t] = round(H[t-1] + L * (N/(w + N)) - H[t-1] * (0.25-0.75*(F[t-1]/(N + 0.001))))
            if H[t] < 0:
                H[t] = 0     #sets the H population to 0 if it becomes smaller than 0
            F[t] = round(F[t-1] + H[t-1] * (0.25-0.75*(F[t-1]/(N + 0.001))) - m * F[t-1])
            if F[t] < 0:
                F[t] = 0     #sets the F population to 0 if it becomes smaller than 0
            Hmax = max(H)     #finds the maximum population of bees in the hive
            Fmax = max(F)     #finds the maximum population of bees outside the hive
        return H, F, Hmax, Fmax     #returns the output values