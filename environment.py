# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:44:03 2022

@author: Jaewon
"""

class Environment:
    def __init__(self, chart_data = None):
        self.chart_data = chart_data
        self.observation = None
        self.idx = -1
        self.close = 4 # 종가의 위치 인덱스
    
    def reset(self):
        self.idx = -1
        self.observation = None
    
    def observe(self):
        if len(self.chart_data) > self.idx + 1:
            self.idx += 1
            self.observation = self.chart_data.iloc[self.idx]
            return self.observation
        return None
    
    def get_price(self):
        if self.observation is not None:
            return self.observation[self.close]
        return None