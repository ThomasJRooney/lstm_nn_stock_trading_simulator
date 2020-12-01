# sample of how a backtrading strategy must be set up to be tested

# import modules
import backtrader
import math

# instantiate class
class GoldenCross(backtrader.Strategy):
    # define parameters
    params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95), ('ticker', 'SPY'))
    def __init__(self):
        self.fast_moving_average = backtrader.indicators.SMA(
            self.data.close, period=self.params.fast, plotname='50 day moving avg'
        )
        self.slow_moving_average = backtrader.indicators.SMA(
            self.data.close, period=self.params.slow, plotname='200 day moving avg'
        )
        self.crossover = backtrader.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order = None

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log("BUY EXECUTED {}".format(order.executed.price))
            elif order.issell():
                self.log("SELL EXECUTED {}".format(order.executed.price))
            self.bar_executed = len(self)
        self.order = None

    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                amount_to_invest = (self.params.order_percentage + self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)
                print("Buy {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))
                self.buy(size = self.size)

        if self.position.size > 0:
            if self.crossover < 0:
                print("Sell {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))
                self.close()
        '''
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        print(len(self))
        print(self.order)
        print(self.position)

        if self.order:
            return

        if not self.position:
            if self.dataclose[0] < self.dataclose[-1]:
                # current close less than previous close

                if self.dataclose[-1] < self.dataclose[-2]:
                    # previous close less than the previous close

                    # BUY, BUY, BUY!!! (with all possible default parameters)
                    self.log('BUY CREATE, %.2f' % self.dataclose[0])
                    self.buy()
        else:
            if len(self) >= (self.bar_executed + 2):
                self.log("SELL CREATED {}".format(self.dataclose[0]))
                self.order = self.sell()
            '''
