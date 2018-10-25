
# coding: utf-8

# #Task 1.1. You survey households in your area to find the average rent they are paying. Find the standard deviation from the following data:$1550, $1700, $900, $850, $1000, $950.

# In[1]:


import statistics as stat
from math import sqrt  
#Setp 1: Creating a list from given data, in this case rent paid:
rent_paid_list = [1550, 1700, 900, 850, 1000,950] 
#Through Defined Functionals
def searchMean(lst):
 return sum(lst)/len(lst)
def searchVariance(lst):
 temp_mean = searchMean(lst)
 variance = sum((x - temp_mean)**2 for x in lst) / (len(lst)-1)
 return variance
def searchStdDev(lst):
 return searchVariance(lst)**0.5
#Step 2: To Find the average rent paid in the households which is the mean:
print("The Average of Rent Paid Sample is % s " % (stat.mean(rent_paid_list))) 
#Step 3: To Find the standard deviation of Rent Paid Sample data 
print("The Standard Deviation of Rent Paid Sample is % s " % (stat.stdev(rent_paid_list))) 
#Step 4: To Find the variance of Rent Paid Sample data
print("The Variance of Rent Paid Sample is % s " % (stat.variance(rent_paid_list)))
print("\n")
#Step 5: To Find Mean, Standard Deviation from Defined functions
print ("The Average of Rent Paid Sample is " + str(searchMean(rent_paid_list)))
print("The Standard Deviation of Rent Paid Sample is " + str(searchStdDev(rent_paid_list)))
print ("The Variance of Rent Paid Sample is " + str(searchVariance(rent_paid_list)))


# Task 1.2. Find the variance for the following set of data representing trees in California (heights in
# feet):
# 3, 21, 98, 203, 17, 9

# In[2]:


#Step 1: creating a simple data - set 
trees_height_ft = [3, 21, 98, 203, 17, 9] 

#define the function to calculate the mean
def searchMean(lst):
 return sum(lst)/len(lst)

#define the function to calculate the variance
def searchVariance(lst):
 temp_mean = searchMean(lst)
 variance = sum((x - temp_mean)**2 for x in lst) / (len(lst)-1)
 return variance


print("Variance of the sample is",searchVariance(trees_height_ft) )

#Step 2: Variance is approximately the squared result of what stdev is 
print("Variance of the sample is % s" 
     %(stat.variance(trees_height_ft))) 


# Task 1.3. In a class on 100 students, 80 students passed in all subjects, 10 failed in one subject, 7 failed
# in two subjects and 3 failed in three subjects. Find the probability distribution of the variable for
# number of subjects a student from the given class has failed in.

# In[3]:


import pandas as pd
import numpy as np

print("Probability Distribution:\n")
data={'X': [0,1,2,3],'P(X)': [0.8,0.1,0.07,0.03]}
df = pd.DataFrame.from_dict(data)
print(df)

print("\n")
data = [80,10,7,3]
Total = 100
def printProbability(events, result):
        probability = (events / result)
        return round(probability,2)
    
print("Probability Distribution:\n")
for PofX in data:
    print("P(X={}) = {}".format(data.index(PofX),printProbability(PofX,Total)))


# Task 2.1. A test is conducted which is consisting of 20 MCQs (multiple choices questions) with every
# MCQ having its four options out of which only one is correct. Determine the probability that a
# person undertaking that test has answered exactly 5 questions wrong.
# Find the probabilities of all the possible outcomes.

# In[4]:


import math
from decimal import Decimal
"""
Here n    =20, which is total number of MCQs
     x    =5 , which is answered exactly 5 questions wrong.
     n-x  =15
     
     Probability of wrong answer = 3/4 = P
     Probability of correct answer = 1/4 = 1-P 
          
     Binomial Probability Distribution
     P(x) = n!/x! (n-x)! (P)x (1-P)n-x
          = (20!/5! * 15!) (3/4)^5 (1/4)^15
          = (20*19*18*17*16) / (5*4*3*2*1) * (3/5)^5 * (1/4)^15
          = 0.00000343

     Thus the required probability is 0.00000343 approximately.
"""
#define function to calculate the cobination of r elements from n elements
def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

# Defining a function Bin_prob() to find the probability using binomial distribution theorem taking p,q,n,x as arguments
def Bin_prob(p,q,n,x):
    return round(Decimal(nCr(n,x)*(p)**x*(q)**(n-x)),8)
p = 3/4
q = 1/4
n = 20
x = 5
print("The probability of answering exactly 5 questions wrongly is:",Bin_prob(p,q,n,x))


# Task 2.2. A die marked A to E is rolled 50 times. Find the probability of getting a “D” exactly 5 times.
# Find the probabilities of all the possible outcomes.

# In[5]:


import math
from decimal import Decimal
"""
Here n    =50, which is total number of die rolled
     x    =5 , which is getting a "D" exactly 5 times.
     n-x  =45
     
     Probability of getting D exactly 5 times = 1/5 = P
     Probability of not getting D exactly 5 times= 4/5 = 1-P 
          
     Binomial Probability Distribution
     P(x) = n!/x! (n-x)! (P)x (1-P)n-x
          = (50!/5! * 45!) (1/5)^5 (4/5)^45
          = (50*49*48*47*46) / (5*4*3*2*1) * (1/5)^5 * (4/5)^45
          = 0.02953120

     Thus the required probability is 0.000216 approximately.
"""
#define function to calculate the cobination of r elements from n elements
def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

# Defining a function Bin_prob() to find the probability using binomial distribution theorem taking p,q,n,x as arguments
def Bin_prob(p,q,n,x):
    return round(Decimal(nCr(n,x)*(p)**x*(q)**(n-x)),8)

p = 1/5
q = 4/5
n = 50
x = 5

print("The probability of getting a “D” exactly 5 times is:",Bin_prob(p,q,n,x))


# Task 2.3. Two balls are drawn at random in succession without replacement from an urn containing 4
# red balls and 6 black balls.
# 
# Find the probabilities of all the possible outcomes.

# """
# Red Balls=4
# Black Balls=6
# 
# Below mentioned are possible outcomes for without Replacement:
# 
# 
# Considering Probability of Only Red Ball:
# 1. Probability of not getting a Red ball in the first draw    = (6/10)               = 0.600
# 2. Probability of not getting a Red ball in the second draw   = (5/9)                = 0.556
# 3. Probability of getting atleast one ball is Red ball        = 1 - (6/10)*(5/9)     = 0.667
# 
# Considering Probability of Only Black Ball:
# 1. Probability of not getting a Black ball in the first draw  = (4/10)               = 0.400
# 2. Probability of not getting a Black ball in the second draw = (3/9)                = 0.333
# 3. Probability of getting atleast one ball is Black ball      = 1 - (4/10)*(3/9)     = 0.867
# 
# Considering Probability of Both Red and Black Balls:
# 1. Probability of getting both Red balls                      = 4/10*3/9= 12/90      = 0.133
# 2. Probability of getting both Black balls                    = 6/10*5/9= 30/90      = 0.333
# 3. Probability of getting one of each Red and Black ball      = 4/10*6/9 + 6/10*4/9  = 0.533
# 4. Probability of getting First Red and Second Black ball    = 4/10*6/9= 24/90      = 0.267
# 5. Probability of getting First Black and Second Red         = 6/10*4/9= 24/90      = 0.267
# 
# """
