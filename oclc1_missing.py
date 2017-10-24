from pymarc import MARCReader

#print all OCLC numbers (035|a)
with open('marc_missing035.mrc', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        if record['035'] is not None:
          if record['035']['a'] is not None:
            print(record['035']['a'])