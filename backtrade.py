# import modules
import backtrader
import datetime
import matplotlib

# import the strategy you want to test
from stocks.strategies.GoldenCross import GoldenCross
from stats.stats import *

def main():
    # initialize cerebro
    cerebro = backtrader.Cerebro()

    # set how much money to trade with
    cerebro.broker.set_cash(10000)

    # input time frame dates
    start_year = 1993
    start_month = 1
    start_day = 3
    end_year = 2020
    end_month = 12
    end_day = 31

    L = [start_year, end_year, end_month, start_month, end_day, start_day]

    # input data from a csv and the timeframe
    data = backtrader.feeds.YahooFinanceCSVData(
        dataname = 'data/SPY93-20.csv',
        fromdate = datetime.datetime(start_year, start_month, start_day),
        todate = datetime.datetime(end_year, end_month, end_day),
        reverse = False
    )

    # add historical data
    cerebro.adddata(data)

    # add the strategy we want to test
    cerebro.addstrategy(GoldenCross)

    # add position size we want to trade with if fixed
    # change this for more generalized strategies that pick the stake based on probabilities
    #cerebro.addsizer(backtrader.sizers.FixedSize, stake=100)

    # save the starting value
    start = cerebro.broker.getvalue()
    print("Starting value: ", start)

    # run the backtest
    cerebro.run()

    # save the ending value
    end = cerebro.broker.getvalue()

    # calculate and print stats
    L.append(end)
    L.append(start)
    print_stats(L)

    # plot the results via matplotlib
    cerebro.plot()

if __name__ == '__main__':
    main()
