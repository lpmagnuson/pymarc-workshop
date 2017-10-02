from pymarc import MARCReader

#trim OCLC number prefixes (ocn, ocm, OCoLC)
with open('marc.mrc', 'rb') as fh:
  reader = MARCReader(fh)
  for record in reader:
    
    #Check to make sure OCLC number exists in MARC 035 field
    if record['035'] is not None:
      
      #Check to make sure there's a |a
      if record['035']['a'] is not None:
        oclc_number = record['035']['a']
        
        #remove OCN if present
        if oclc_number.find("ocn") >= 0:
          oclc_number = oclc_number.replace('ocn', '')
        else:
          oclc_number = oclc_number
        
        #remove OCM if present - needs work!
        if oclc_number.find("xyz") >= 0:
          oclc_number = oclc_number.replace('xyz', '')
        else:
          oclc_number = oclc_number
        
        #else remove 01cals_network
        if oclc_number.find("01cals_network") >= 0:
          oclc_number = oclc_number.replace('-01cals_network', '')
        else:
          oclc_number = oclc_number
          
      #if no 035|a, skip
      else:
        oclc_number = 'None'
    #if no 035, skip
    else:
      oclc_number = 'None'
      
    print(oclc_number)