class ReportItem:
    def __init__(self, 
                id: str,
                email: str, 
                name: str, 
                department: str, 
                hours_worked: str, 
                rate: str):
        self.id = id
        self.email = email
        self.name = name
        self.department = department
        self.hours_worked = int(hours_worked)
        self.rate = float(rate)

    @property
    def payout(self):
        return self.hours_worked * self.rate

    def __str__(self):
        headers = 'email\t'.expandtabs(25) + 'name\tdepartment\thours\trate\n'.expandtabs(15)
        item = f'{self.email}\t'.expandtabs(25) + f'{self.name}\t{self.department}\t{self.hours_worked}\t{self.rate}'.expandtabs(15)
        return headers + item
    
    def __eq__(self, other):
        return self.__str__() == other.__str__()
    
class Report:
    def __init__(self, items: list[ReportItem]):
        self.items = items
    
    def payout_report(self):
        departments = sorted(list(set([item.department for item in self.items])), key=lambda x: x.lower())
        report_data = {}
        for dep in departments:
            items = filter(lambda x:x.department == dep, self.items)
            report_data[dep] = list(items)
        return report_data
