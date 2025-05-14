import pytest
import os
import app.report
from app.view_report import print_payout_report
from app.report import Report, ReportItem
from app.reader import read_files
from app.parser import parse
from .test_data import HEADERS_REPORT, TEST_DATA_FILE, ANSWERE_DATA

@pytest.fixture()
def get_file_path():
    with open('tests/test.csv', 'a') as f:
        for line in TEST_DATA_FILE:
            f.write(line)
    yield 'tests/test.csv'
    os.remove('tests/test.csv')

@pytest.fixture()   
def get_dict_files():
    return {'tests/test.csv': TEST_DATA_FILE}    

@pytest.fixture()
def get_parse_data():
    return [
        ReportItem('1', 'alice@example.com', 'Alice Johnson', 'Marketing', '160', '50'),
        ReportItem('2', 'bob@example.com', 'Bob Smith', 'Design', '150', '40'),
        ReportItem('3', 'carol@example.com', 'Carol Williams', 'Design', '170', '60')
    ]

@pytest.fixture()
def get_report():
    return {
    'Design':
        [ReportItem('2', 'bob@example.com', 'Bob Smith', 'Design', '150', '40'),
        ReportItem('3', 'carol@example.com', 'Carol Williams', 'Design', '170', '60')],
    'Marketing':
        [ReportItem('1', 'alice@example.com', 'Alice Johnson', 'Marketing', '160', '50')]
    }

def test_reader(get_file_path, get_dict_files):
    result = read_files([get_file_path])
    assert result == get_dict_files

def test_parser(get_file_path, get_parse_data):
    parse_data = []
    files = read_files([get_file_path])
    for file_path in files:
        parse_data.extend(parse(files[file_path]))
    assert sorted(parse_data, key=lambda x: x.id) == sorted(get_parse_data, key=lambda x: x.id)

def test_report(get_parse_data, get_report):
    report = Report(get_parse_data)
    assert report.payout_report() == get_report


def test_print_payout_report(capsys):
    print_payout_report({})
    captured = capsys.readouterr()
    assert captured.out == HEADERS_REPORT
    data = parse(TEST_DATA_FILE)
    report = Report(data)
    print_payout_report(report.payout_report())
    captured = capsys.readouterr()
    assert captured.out == HEADERS_REPORT + ANSWERE_DATA


#def test_report():
    #report = Report()