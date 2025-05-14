def print_payout_report(data: dict):
    print('\t'.expandtabs(15) + 'name\t'.expandtabs(20) + 'hours\trate\tpayout'.expandtabs(10))
    for dep in data:
        print(dep)
        for item in data[dep]:
            print('______________\t'.expandtabs(15) + f'{item.name}\t'.expandtabs(20) + f'{item.hours_worked}\t{item.rate}\t{item.payout}'.expandtabs(10))
