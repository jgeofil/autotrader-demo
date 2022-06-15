#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class StrategyClass:
    ''' 
    AutoTrader Strategy Template
    ----------------------------    
    '''

    def __init__(self, parameters, data, instrument):
        ''' Define all indicators used in the strategy '''
        self.name   = "Strategy Name"
        self.data   = data
        self.params = parameters
        
        # Define indicators used in strategy logic 
        
        # Construct indicators dictionary for plotting
        self.indicators = {'Indicator name': {'type': 'INDICATOR',
                                              'data': 'indicator_data'}
                           }
        
        
    def generate_signal(self, i, current_position):
        ''' Define strategy to determine entry signals '''
        
        order_type  = 'market'
        # Define strategy logic - 1 for long, -1 for short
        signal = 0

        return {"order_type": order_type, "direction": signal}
    