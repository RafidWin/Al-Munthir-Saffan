names = input('Write the names of providers (Separate each name with a comma): ').split(',')
if len(names) == 5:
    costs = input('Write the cost of offers (Separate each amount with a comma): ').split(',')
    if len(costs) == 5:
        rates = [float(input(f"Write the rate of {names[0]}'s bid, with cost {costs[0]}: ")),
                 float(input(f"Write the rate of {names[1]}'s bid, with cost {costs[1]}: ")),
                 float(input(f"Write the rate of {names[2]}'s bid, with cost {costs[2]}: ")),
                 float(input(f"Write the rate of {names[3]}'s bid, with cost {costs[3]}: ")),
                 float(input(f"Write the rate of {names[4]}'s bid, with cost {costs[4]}: "))]
        accepted = [[], [], []]
        if rates[0] >= 5:
            accepted[0].append(names[0])
            accepted[1].append(int(costs[0]))
            accepted[2].append(rates[0])
        if rates[1] >= 5:
            accepted[0].append(names[1])
            accepted[1].append(int(costs[1]))
            accepted[2].append(rates[1])
        if rates[2] >= 5:
            accepted[0].append(names[2])
            accepted[1].append(int(costs[2]))
            accepted[2].append(rates[2])
        if rates[3] >= 5:
            accepted[0].append(names[3])
            accepted[1].append(int(costs[3]))
            accepted[2].append(rates[3])
        if rates[4] >= 5:
            accepted[0].append(names[4])
            accepted[1].append(int(costs[4]))
            accepted[2].append(rates[4])
        print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*')
        print(f'Number of offered bids: {len(names)}')
        print(f'Number of accepted offers: {len(accepted)}')
        print(f'The winner offer is: {accepted[0][accepted[1].index(min(accepted[1]))]}, with cost {min(accepted[1])}, and its rate is {accepted[2][accepted[1].index(min(accepted[1]))]}')
    else:
        print('Please enter five costs of offers exactly')
else:
    print('Please enter five names of providers exactly' )
