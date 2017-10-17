from pymarc import MARCReader
import re
import csv

csv_out = csv.writer(open('isbn-output.csv', 'w'), delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)

csv_out.writerow(['isbn','account'])

#replace 999999 with GOBI account number
account = '999999'

#print all ISBNs (020|a)
with open('marc.mrc', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
      for f in record.get_fields('020'):
        if f['a'] is not None:
          fisbn = (f['a'])
          fisbn = re.sub("[^0-9]", "", fisbn)
          csv_out.writerow([fisbn, account])
          
    


