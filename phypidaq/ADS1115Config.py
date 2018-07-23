# -*- coding: utf-8 -*-
from __future__ import print_function, division, unicode_literals
from __future__ import absolute_import

import numpy as np, time, sys

# import relevant pieces from adafruit
import Adafruit_ADS1x15

class ADS1115Config(object):
  '''ADC ADS1115Config configuration and interface'''

  def __init__(self, confdict = None):
    if confdict==None: confdict={}
          
# -- chosen ADCChannels ADC ADS1115
    if "ADCChannels" in confdict:
      self.ADCChannels = confdict["ADCChannels"]  
    else:
      self.ADCChannels = [0]
    self.NChannels = len(self.ADCChannels)
    
# -- differential mode
    if 'DifModeChan' in confdict:
      self.DifModeChan = confdict['DifModeChan']
    else:
      self.DifModeChan = [ False for i, c in enumerate(self.ADCChannels) ]

# -- gain configuration ADC ADS1115
    if "Gain" in confdict:
      self.gain = confdict["Gain"]
      for i, c in enumerate(self.ADCChannels):
        if self.gain[i] == '2/3':
          self.gain[i] = 2/3
    else:
      self.gain = [ 2/3 for i, c in enumerate(self.ADCChannels)]

# -- sample rate ADC ADS1115
    if "sampleRate" in confdict:
      self.sampleRate = confdict["sampleRate"]
    else:
      self.sampleRate = 860 # sample rate


### --- determine reference voltage for ADC calculation
  # possible values reference voltage
    self.ADCVRef = [6.114, 4.096, 2.048, 1.024, 0.512, 0.256]
  # determine the corresponding index
    self.VRef = [0., 0., 0., 0.]
    self.posGain = [2/3, 1, 2 , 4, 8, 16]
    for i, c in enumerate(self.ADCChannels):
      self.VRef[i] = self.ADCVRef[self.posGain.index(self.gain[i])]
    
  #   remove python 2 vs. python 3 incompatibility for gain: 2/3 (Adafruit_ADS1x15)
  #   when using Python 2 Adafruit_ADS1x15 expects an integer
  #   (in case of gain = 2/3 int(self.gain[i] = 0)
    for i, c in enumerate(self.ADCChannels):
      if sys.version_info[:2] <=(2,7):
        if self.gain[i] == 2/3:
          self.gain[i] = int(self.gain[i])

  def init(self):
  #Hardware configuration:
    try:
      # Create an ADS1115 ADC (16-bit) instance.
      self.ADS = Adafruit_ADS1x15.ADS1115()
    except:
      print("ADS1115Config: Error initialising device - exit")
      sys.exit(1)

 # provide configuration parameters
    self.ChanNams = [ str(i) for i, c in enumerate(self.ADCChannels) ]
    self.ChanLims = [ [0., 0.] for i, c in enumerate(self.ADCChannels) ]
    for i, c in enumerate(self.ADCChannels):
      if self.DifModeChan[i]:
        self.ChanLims[i] = [-self.VRef[i], self.VRef[i]]
      else:
        self.ChanLims[i] = [0, self.VRef[i]]
      
  def acquireData(self, buf): 
    for i, c in enumerate(self.ADCChannels):
      # read data from ADC in differential mode
      if self.DifModeChan[i]:
        buf[i] = self.ADS.read_adc_difference(self.ADCChannels[i], gain = self.gain[i],
                            data_rate = self.sampleRate)*self.VRef[i]/32767
      else:
      # read data from adc in single mode
        buf[i] = self.ADS.read_adc(self.ADCChannels[i], gain = self.gain[i],
                            data_rate = self.sampleRate)*self.VRef[i]/32767

  def closeDevice(self):
   # nothing to do here
   pass
