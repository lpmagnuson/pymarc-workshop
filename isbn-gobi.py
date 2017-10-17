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
    #loop through each record
    for record in reader:
      #loop through each ISBN and print on new line
      for f in record.get_fields('020'):
        #make sure 020|a exists
        if f['a'] is not None:
          fisbn = (f['a'])
          #Only include numbers
          fisbn = re.sub("[^0-9]", "", fisbn)
          #write to CSV file
          csv_out.writerow([fisbn, account])
          
    


