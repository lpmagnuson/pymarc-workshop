import csv
import re
import pymarc
import sys

#define a function
def csvmarcwriter(file):

  #Open your CSV File
  with open(file) as fh:
    itemread = csv.reader(fh)
    itemlist = list(itemread)

  #create an output file for the created MARC records (wb means 'write binary')  
  outputfile = open('writer.mrc', 'wb')
  
  #iterate through each row of the CSV file
  for row in itemlist[1:]:
    
    #declare PyMARC record object
    item_load = pymarc.Record(to_unicode=True, force_utf8=True)
  
    #define data fields in CSV file
    ocn = row[0]
    barcode = row[1]
    ltitle = row[2]
    
    #Clean up OCLC numbers with regular expression
    ocn = re.sub("[^0-9]", "", ocn)
  
    #write data to field variables   
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
    
    #add field variables to PyMARC record object  
    item_load.add_ordered_field(field_001)
    item_load.add_ordered_field(field_974)
    item_load.add_ordered_field(field_949)
  
    #Create output file
    outputfile.write(item_load.as_marc())

  #close the output file
  outputfile.close()

file = sys.argv[1]
csvmarcwriter(file)

#To call the function, try:  python marc_writer.py records.csv

  