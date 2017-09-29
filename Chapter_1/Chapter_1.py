#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 23:25:34 2017

@author: lxwhu
"""

import pylab as pl
class uranium_decay_A_and_B:
    def __init__(self, number_of_nuclei_A = 100, number_of_nuclei_B = 0, time_constant = 0.5, time_of_duration = 5, time_step = 0.05):
        self.n_uranium_A = [number_of_nuclei_A]
        self.n_uranium_B = [number_of_nuclei_B]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nuclei_A ->", number_of_nuclei_A)
        print("Initial number of nuclei_B ->", number_of_nuclei_B)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmp_A = self.n_uranium_A[i] - self.n_uranium_A[i] / self.tau * self.dt+self.n_uranium_B[i] / self.tau * self.dt
            tmp_B = self.n_uranium_B[i] - self.n_uranium_B[i] / self.tau * self.dt+self.n_uranium_A[i] / self.tau * self.dt
            self.n_uranium_A.append(tmp_A)
            self.n_uranium_B.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.n_uranium_A)
        pl.plot(self.t, self.n_uranium_B)
        pl.title('Decay problem with nuclei A and B')
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei A and B')
        pl.show()
a = uranium_decay_A_and_B()        
a.calculate()
a.show_results()
