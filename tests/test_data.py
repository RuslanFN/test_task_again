TEST_DATA_FILE = ['id,email,name,department,hours_worked,hourly_rate\n',
'1,alice@example.com,Alice Johnson,Marketing,160,50\n',
'2,bob@example.com,Bob Smith,Design,150,40\n',
'3,carol@example.com,Carol Williams,Design,170,60\n']

ANSWERE_DATA = 'Design\n'
ANSWERE_DATA += '______________ Bob Smith           150       40.0      6000.0\n'

ANSWERE_DATA += '______________ Carol Williams      170       60.0      10200.0\n'

ANSWERE_DATA += 'Marketing\n'
ANSWERE_DATA += '______________ Alice Johnson       160       50.0      8000.0\n'

HEADERS_REPORT = '\t'.expandtabs(15) + 'name\t'.expandtabs(20) + 'hours\trate\tpayout\n'.expandtabs(10)


