from pymarc import MARCReader
#import re - the Python Regular Expressions library
import re
#import csv - the Python Comma-Separated Values library
import csv

#create a CSV file - note tab delimiter would be '/t'
csv_out = csv.writer(open('output.csv', 'w'), delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)

#write a header row in your CSV file
csv_out.writerow(['title','oclc_number'])

#trim OCLC number prefixes (ocn, ocm, OCoLC)
with open('marc.mrc', 'rb') as fh:
  reader = MARCReader(fh)
  for record in reader:
    oclc_number = title = ''
  
    #Get title (245 |a)
    if record['245'] is not None:
      if record['245']['a'] is not None:
        #title = record['245']['a']
        title = record['245']['a'].rsplit('/', 1)[0]
        title = title.rsplit(':', 1)[0]
      else:
        title = 'None'
    else:
        title = 'None'
    
    #Check to make sure OCLC number exists in MARC 035 field
    if record['035'] is not None:
      
      #Check to make sure there's a |a
      if record['035']['a'] is not None:
        oclc_number = record['035']['a']
        
        #else remove 01cals_network
        if oclc_number.find("01cals_network") >= 0:
          oclc_number = oclc_number.replace('-01cals_network', '')
          oclc_number = re.sub("[^0-9]", "", oclc_number)
        else:
          #remove everything that remains except the numbers
          oclc_number = re.sub("[^0-9]", "", oclc_number)
          
      #if no 035|a, skip
      else:
        oclc_number = 'None'
    #if no 035, skip
    else:
      oclc_number = 'None'

    #print(oclc_number)
    csv_out.writerow([title, oclc_number])
