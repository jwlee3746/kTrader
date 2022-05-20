# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:14:29 2022

@author: Jaewon
"""
import numpy as np

class Agent:
    # 에이전트 상태가 구성하는 값 개수
    STATE_DIM = 3 # 주식 보유 비율, 현재 손익, 평균 매수 단가 대비 등락률

    # 매매 수수료 및 세금
    TRADING_CHARGE = 0.00015  # 거래 수수료 0.015%
    TRADING_TAX = 0.0025  # 거래세 0.25%

    # 행동
    ACTION_BUY = 0  # 매수
    ACTION_SELL = 1  # 매도
    ACTION_HOLD = 2  # 관망
    
    # 인공 신경망에서 확률을 구할 행동들
    ACTIONS = [ACTION_BUY, ACTION_SELL, ACTION_HOLD]
    NUM_ACTIONS = len(ACTIONS)  # 인공 신경망에서 고려할 출력값의 개수
    
    def __init__(self, environment, initial_balance, min_trading_price, max_trading_price):
        # Agent 클래스의 초기 속성
        self.environment = environment
        self.initial_balance = initial_balance
        self.min_trading_price = min_trading_price
        self.max_trading_price = max_trading_price
        
        # Agent 클래스의 속성
        self.balance = initial_balance # 현재 현금 잔고
        self.num_stocks = 0 # 보유 주식 수
        
        # 포트폴리오 가치: balance + num_stocks * {현재 주식 가격}
        self.portfolio_value = 0
        self.num_buy = 0 # 매수 횟수
        self.num_sell = 0 # 매도 횟수
        self.num_hold = 0 # 관망 횟수
        
        # Agent 클래스의 현재 상태
        self.ratio_hold = 0 # 주식 보유 비율
        self.profitloss = 0 # 현재 손익
        self.avg_buy_price = 0 # 주당 매수 단가
        
    def reset(self):
        self.balance = self.initial_balance
        self.num_stocks = 0
        
        self.portfolio_value = self.initial_balance
        self.num_buy = 0
        self.num_sell = 0
        self.num_hold = 0
        
        self.ratio_hold = 0
        self.profitloss = 0
        self.avg_buy_price = 0
    
    def set_balance(self, balance):
        self.initial_balance = balance
    
    def get_status(self):
        # 주식 보유 비율 = 보유 주식 수 / (포트폴리오 가치 / 현재 주가)
        self.ratio_hold = self.num_stocks * self.environment.get_price() / self.portfolio_value
        return (
            self.ratio_hold, # 주식 보유 비율
            self.profitloss, # 현재 손익
            (self.environment.get_price() / self.avg_buy_price) - 1 \
                if self.avg_buy_price > 0 else 0 # 주당 매수 단가 대비 주가 등락률
        )
            
    #def decide_action(self, pred_value, pred_policy, epsilon):
        