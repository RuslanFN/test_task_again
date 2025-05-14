from .report import ReportItem

HEADERS_TO_PARSE = {
    'email': 'email', 
    'name': 'name', 
    'department':'department',
    'hours_worked': 'hours_worked',
    'hourly_rate':'rate',
    'salary':'rate',
    'rate':'rate',
    'id':'id',
    }

def parse(file_strings: list[str]):
    headers = ''
    line_dict = {}
    ind_to_header = {}
    list_report_items = []

    if file_strings:
        headers = file_strings[0]
    headers = headers.replace('\n', '')
    list_headers = headers.split(',')
    for i in range(len(list_headers)):
        ind_to_header[i] = list_headers[i]
    
    for line in file_strings[1:]:
        line = line.replace('\n', '')
        values = line.split(',')
        for i in range(len(values)):
            header = HEADERS_TO_PARSE[ind_to_header[i]]
            line_dict[header] = values[i]  
        list_report_items.append(ReportItem(**line_dict))
    return list_report_items
    

