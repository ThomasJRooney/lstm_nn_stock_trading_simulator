# import portfolio
from portfolio import Portfolio

# import all the strategies I will be running
from portfolio.stock_portfolio.stock_trader import *
from portfolio.stock_portfolio.strategies.swing_mean_reversion import *

def main():

    # create asset trader objects for each asset portfolio
    trader = SMR('AAPL')

    # add the asset trader objects to each asset portfolio
    stock_portfolio.add_asset_trader(trader)

    # start up the portfolio
    # portfolio.run()

    stock_portfolio.run()

if __name__ == '__main__':
    main()
