import argparse
from app.report import Report
from app.parser import parse
from app.view_report import print_payout_report
from app.reader import read_files

parser = argparse.ArgumentParser('Files to order')
parser.add_argument('files', type=str, help='Files for report', nargs='*')
parser.add_argument('--report', const='payout', default='payout', nargs='?')
namespace = parser.parse_args()
files = read_files(namespace.files)
parse_data = [] #Строки со всех таблиц

for file in files:
    parse_data.extend(parse(files[file]))

report = Report(parse_data)
item_by_dep = report.payout_report()
print_payout_report(item_by_dep)