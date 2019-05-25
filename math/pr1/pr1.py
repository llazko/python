# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:41:08 2019

@author: lazko
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import os
clear = lambda: os.system('cls')
clc=clear()
clc

plt.close('all')
os.system('cls')
#%%
a = np.random.rand(1,10000)
print(a)
print('Proba1')
time.sleep(5)
clc
print('Proba2')


b = np.fft.fft(a[0,:]-np.mean(a[0,:]))
m = np.abs(b)
r = np.real(b)
im = np.imag(b)

#%%
t=np.linspace(0,1,10000)
plt.plot(t,a[0,:])
plt.figure();
plt.hist(a[0,:])

#%%
plt.figure()
plt.subplot(2,2,1)
plt.plot(t,a[0,:])
plt.subplot(2,2,2)
plt.plot(m)
plt.subplot(2,2,3)
plt.plot(r)
plt.subplot(2,2,4)
plt.plot(im)

plt.show()



