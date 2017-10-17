from pymarc import MARCReader

#print all OCLC numbers (035|a)
with open('marc.mrc', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        print(record['035']['a'])