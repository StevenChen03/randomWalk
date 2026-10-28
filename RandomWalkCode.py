## This file will use the lessons learned from the Chapter 6 Exercises and calculate how long
## it takes for a photon to journey from the SUn's core to the surface.

## Importations:


## Step 2: First, set up your code to simulate a random walk of the photon. This can be done like

## function step:
## x = Gaussian random number with mu = 0.0 and sigma = 0.00577 m
## y = Gaussian random number with mu = 0.0 and sigma = 0.00577 m
## z = Gaussian random number with mu = 0.0 and sigma = 0.00577 m
## return x, y, z

## These values can then be added to the current position of the photon and the process can be 
## repeated. Note, however, if you are using Python, it will be more efficient to have have Numpy 
## generate the values for many steps all at once, then x, y and z will be arrays. We can do a sum 
## on the array elements with a Numpy function to get the net effect of all those steps. Test your 
## code by performing many single steps, taking the average and the standard deviation to see if 
## they match what we expect.


## Step 3: