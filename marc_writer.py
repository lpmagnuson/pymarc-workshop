import csv
import re
import pymarc

#define a function
def csvmarcwriter(file):

  #Open your CSV File
  with open(file) as fh:
    itemread = csv.reader(fh)
    itemlist = list(itemread)

  #create an output file for the created MARC records (wb means 'write binary')  
  outputfile = open('writer.mrc', 'wb')
  
  for row in itemlist[1:]:

    item_load = pymarc.Record(to_unicode=True, force_utf8=True)
  
    ocn = row[0]
    barcode = row[1]
    ltitle = row[2]
    
    ocn = re.sub("[^0-9]", "", ocn)
  
    field_001 = pymarc.Field(tag='001', data=ocn)
    field_974 = pymarc.Field(
      tag='974', 
      indicators = [' ',' '],
      subfields = ['a', ltitle, '9', "LOCAL"],
      )
    field_949 = pymarc.Field(
      tag='949', 
      indicators = [' ',' '],
      subfields = ['a', barcode]
      )
    item_load.add_ordered_field(field_001)
    item_load.add_ordered_field(field_974)
    item_load.add_ordered_field(field_949)
  
    outputfile.write(item_load.as_marc())

  outputfile.close()

csvmarcwriter('records.csv')
  

  