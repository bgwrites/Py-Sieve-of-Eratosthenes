#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Project: Sieve of Eratosthenes 
"""

import matplotlib.pyplot as plt
import numpy as np

class Primes(object):
    
    def __init__(self, nums):
        self.nums = nums
        self.primeCheck = [True] * self.nums
        self.primes = []
        self.summed = []
        
    def solve(self):
        if self.nums < 2:
            return False
        for p in range(3, self.nums, 2):
            if p ** 2 > self.nums:
                break
            if self.primeCheck[p]:
                for i in range(p * p, self.nums, 2 * p):
                    self.primeCheck[i] = False
        self.primes = [1] + [p for p in range(3, self.nums, 2) if self.primeCheck[p]]
    
    def sumPrimes(self):
        for i in range(1, len(self.primes)+1):
            self.summed.append(sum(self.primes[:i])) 

    def plotVals(self):
        x = np.array(self.primes)
        y = np.array(self.summed)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x, y)
        plt.show()
                          
            
if __name__ == "__main__":
    p = Primes(10000)
    p.solve()
    p.sumPrimes()
    p.plotVals()
