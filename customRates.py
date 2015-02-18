# here a custom rate is calculated for unique events in the simulation
# Author = Thomas Davis, email = txd283@bham.ac.uk / University of Birmingham

from KMCLib import *
import numpy
import math

#### values required for vacancy diffusion, energy in eV, T in K, v is the jump attemps in s^-1
E_m = 0.55
E_b = 0.2
k = 0.862e-4
T = 560
v = 1e13
kT = k*T
diffusion_rate = v*math.exp(-E_m/(kT))
v_clustering_rate = v*math.exp(-(E_m + E_b)/(kT))
class CustomRateCalculator(KMCRateCalculatorPlugin):

    def rate(self, geometry, types_before, types_after, rate_constant, process_number, coordinate):

        # For every vacancy, check the neighbours around it to see if they are V.
        first_neighbours = len([ i for i in [types_before[1], types_before[2], types_before[3], types_before[4], types_before[5],types_before[6], types_before[7], types_before[8]] if i == "V"])
        second_neighbours = len([ i for i in [types_before[9], types_before[10], types_before[11], types_before[12], types_before[13],types_before[14]] if i == "V"])
        
        #print("--------- Check -----------")
        #print("first_neighbours = %i \n"%(first_neighbours))
        #print("second_neighbours = %i \n"%(second_neighbours))

        # change the value of the activation energy with or without a binding energy of a V-V pair, or more.        
        if first_neighbours >= 1 or second_neighbours >= 1:
            v_rate = v_clustering_rate
        elif first_neighbours == 0 and second_neighbours == 0:
            v_rate = diffusion_rate
        #print ("Rate = %.1f\n"%(v_rate))    
        return v_rate
        
        """
    def cutoff(self):
        # To determine the radial cutoff of the geometry around the central lattice site to cut out and send down to the custom rate function.
        # Restricts the custom rate to look in the primitive cell internal coordinates (float)
        return 1.0
        """