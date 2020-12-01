def get_time(A):
    start_year = A[0]
    end_year = A[1]
    end_month = A[2]
    start_month = A[3]
    end_day = A[4]
    start_day = A[5]
    end = A[6]
    start = A[7]
    L = []

    years = end_year - start_year
    months = end_month - start_month
    days = end_day - start_day

    if(days < 0):
        months -= 1
        days = days**2
        days = days / (days / 2)

    if(months < 0):
        years -= 1
        months = months**2
        months = months / (months / 2)

    L.append(years)
    L.append(months)
    L.append(days)
    L.append(end)
    L.append(start)
    return(L)

def get_stats(A):
    years = A[0]
    months = A[1]
    days = A[2]
    end = A[3]
    start = A[4]
    L = []

    # calculate statistics
    percent_change = ((end / start) - 1) * 100
    total_time_in_years = (years) + (months / 12) + (days / 365)
    total_time_in_months = (years * 12) + (months) + (days / 30.42)
    total_time_in_days = (years * 365) + (months * 30.42) + (days)

    total_profit = end - start
    avg_yr_profit = total_profit / total_time_in_years
    avg_yr_pct_chg = (avg_yr_profit / start) * 100
    stdev_yr_pct_chg = 0
    stdev_yr_profit = 0

    avg_monthly_profit = total_profit / total_time_in_months
    avg_monthly_pct_chg = (avg_monthly_profit / start) * 100
    stdev_monthly_pct_chg = 0
    stdev_monthly_profit = 0

    avg_daily_profit = total_profit / total_time_in_days
    avg_daily_pct_chg = (avg_daily_profit / start) * 100
    stdev_daily_pct_chg = 0
    stdev_daily_profit = 0

    L.append(start)
    L.append(end)
    L.append(total_profit)
    L.append(percent_change)
    L.append(years)
    L.append(months)
    L.append(days)
    L.append(avg_yr_pct_chg)
    L.append(avg_yr_profit)
    L.append(avg_monthly_pct_chg)
    L.append(avg_monthly_profit)
    L.append(avg_daily_pct_chg)
    L.append(avg_daily_profit)
    return(L)

def print_stats(L):
    # array that looks like below will be passed in
    # [start, end, profit, percent_change, years, months, days, avg_yr_pct_chg, avg_yr_profit, avg_monthly_pct_chg, avg_monthly_profit, avg_daily_pct_chg, avg_daily_profit]

    time = get_time(L)
    L = get_stats(time)

    # print final statistics
    print()
    print("==========================STATISTICS=============================")
    print()
    print("Starting value:  ${:.2f}".format(L[0]))
    print("Ending value:    ${:.2f}".format(L[1]))
    print("Total Profit:    ${:.2f}".format(L[2]))
    print("Percent change:  {:.6f}".format(L[3]),"%")
    print("Total timeframe: ", L[4], "Years,", L[5], "Months,", L[6], "Days")
    print()
    print("YEARLY: ")
    print("  Average Yearly Percentage Change:            {:.6f}".format(L[7]), "%")
    print("  Std Dev Yearly Percentage Change:           ", 0, "%")
    print("  Average Yearly Profit:                       ${:.2f}".format(L[8]))
    print("  Std Dev Yearly Profit:                       $", 0)
    print()
    print("MONTHLY: ")
    print("  Average Monthly Percentage Change:            {:.6f}".format(L[9]), "%")
    print("  Std Dev Monthly Percentage Change:           ", 0, "%")
    print("  Average Monthly Profit:                       ${:.2f}".format(L[10]))
    print("  Std Dev Monthly Profit:                       $", 0)
    print()
    print("DAILY: ")
    print("  Average Daily Percentage Change:              {:.6f}".format(L[11]), "%")
    print("  Std Dev Daily Percentage Change:             ", 0, "%")
    print("  Average Daily Profit:                         ${:.2f}".format(L[12]))
    print("  Std Dev Daily Profit:                         $", 0)
    print()
    #print("Based on statistical tests this strategy is: ", test(avg_daily_pct_chg))
    print()
    print("====================================================================")
