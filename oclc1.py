from pymarc import MARCReader

with open('marc.mrc', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        print(record['035']['a'])