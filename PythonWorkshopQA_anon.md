# Questions Log from Webinar 2

## Q1: Hi, can you recommend a good way to learn the indentation rules in Python 3? I can't seem to get it right. [Q: 1:02 PM] 

The Python Style Guide has some good examples.  
https://www.python.org/dev/peps/pep-0008/#indentation

A typical conditional should look like this:

Good:
```
If something:
    Action A
    Action B
Elif something else:
    Action C
Else:
    Action D
```
Bad:
```
If something:
    Action A
         Action B (this is wrong - we’re indenting this when it should be aligned with action A)
Elif something else:
      Action C (this should be aligned with Action A above)
Else:
    Action D
```
As long as your conditionals (if/elif/else) are lined up and your actions are indented consistently, you should be good.  A nested conditional would have additional indentations:

```
If something:
    Action A
Elif something else:
    If this other thing:
        Action B
        Action C
    Else:
        Action D
Else:
    Action E
```

Getting used to the indentation is really just a matter of trial and error.  It's a good idea to keep chocolate handy in case of indentation errors - give yourself some kind of reward when you fix them.

## Q2: Hi. What is the syntax for printing the 001 control number without the field label? [Q: 1:18 PM] 


I am not sure if this is the correct way, but it works!
This script finds the 001 fields and turns the fields into a string (they output as an object, which can't be manipulated with methods designed for strings/text).
Then it cuts the first 6 characters off of the string (the field label, =001  )
```
#print all control numbers
with open('marc.mrc', 'rb') as fh:
  reader = MARCReader(fh)
    for record in reader:
      if record['001'] is not None:
        control = str(record['001'])
        control = control[6:]
        print(control)
```    
I don't know why PyMARC treats control numbers so differently - perhaps a good question for the PyMARC Google Group. 

## Q3: Why the colon after the zero? [Q: 1:21 PM] 

I am thinking this comes from around slide 9 (manipulating fields and string data)

#remove OCN if present
  if oclc_number.find("ocn") >= 0:
       
The colon has nothing to do with the 0; it's ending the if clause in the conditional.  

Python conditional syntax requires colons to indicate the condition has ended, e.g.:
```
if something:
  do action
else:
  do other action
```
The action indicated within the conditional has no required punctuation, but must be indented.

## Q4: 0: [Q: 1:21 PM] 

## Q5: You have a colon after the first if clause but not the second???? [Q: 1:22 PM] 

I am hoping that the answers above for Q3 clarified Qs 4+5, but please let me know if this is still confusing!

## Q6: How did this work in the ISBN file - some ISBNs have x ? [Q: 1:26 PM] 

Check out line 23 of isbn-gobi.py:
https://github.com/lpmagnuson/pymarc-workshop/blob/master/isbn-gobi.py

This is the regular expression statement:
```
fisbn = re.sub("[^X0-9]", "", fisbn)
```
This will ensure capital X's are retained in any ISBN entry.  To ensure that lower case x's are retained, I think you could use:
```
fisbn = re.sub("[^xX0-9]", "", fisbn)
```

## Q7: (The above question relates to Activity 3.) [Q: 1:29 PM] 

## Q8: What is the indendation?  Is it a tab or a certain number of spaces? [Q: 1:32 PM] 

Indentation is spaces - tabs are not advisable in Python.

## Q9: f is a variable? but what is it meaning? where do you define that? [Q: 1:33 PM] 

I think this question has to do with slide 18 (isbn-gobi.py).  If you're looking at line 18 of this script:

https://github.com/lpmagnuson/pymarc-workshop/blob/master/isbn-gobi.py

```
for f in record.get_fields('020'):
```

You do not need to formally define or declare a variable in Python prior to using it in a 'for' statement. Here, Python understands that we're storing
the contents of all of the 020 fields in the variable 'f' and we can then use f later in the script when we're referencing each '020' value.  

In plain English this could be translated as:

for each 020 field (where f stores the field value): 

## Q10: Is there a limit on the number of records that a script can process at once? [Q: 1:53 PM] 

I don't believe so - I've run these types of scripts on millions of records, and while it might take a while, your only limit should be making sure you have
enough hard drive space for the output file.

## Q11: I believe it's two spaces [Q: 1:54 PM] 

## Q12: Here's a free Python course from CodeSchool:  https://www.codeschool.com/courses/try-python[Q: 1:55 PM] 

+1 for free CodeSchool!  There's a free one from EdX as well if you don't want the certificate:

https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-11

## Q13: Any recomendation to learn about the use of Python for linked data? [Q: 1:55 PM] 

I haven't used Python a lot with linked data, but here are a couple of nice introductions to traversing RDF with Python:

https://www.oclc.org/developer/news/2016/making-sense-of-linked-data-with-python.en.html

http://pyvideo.org/pydata-berlin-2014/semantic-python-mastering-linked-data-with-pytho.html

## Q14: How do you access leader or 008? [Q: 1:57 PM] 
```
from pymarc import MARCReader

#print all OCLC numbers (035|a)
with open('marc.mrc', 'rb') as fh:
  reader = MARCReader(fh)
  for record in reader:
    #to get byte 6 of the Leader
    if record.leader is not None:
      leader = record.leader
      leader = leader[6]
      print(leader)
    #get bytes 7-10 of the 008 field (Date 1)  
    if record['008'] is not None:
      #str below converts the field to a string - I am not sure why fixed-length fields between 001-008 require this
      ooeight = str(record['008'])
      #13:17 below retrieves characters 13-17 of the field
      #you start at character 13 because you have to skip over the first 6 characters to get past the =008 in the record
      #17 is the stop character
      ooeight = ooeight[13:17]
      print(ooeight)
```

## Q15: but what is it doing in this example? [Q: 1:58 PM] 

I attempted to answer this in Q9 above, but please let me know if I can clarify any of this!

## Q16: Do you have to use invidivual import statements, or can they all be on one line[Q: 1:58 PM] 

They can be in one statement if they stand on their own, e.g., 

import re, csv

specific library references like pymarc need to be on their own line:

from pymarc import MARCReader

## Q17: the plain f[Q: 1:58 PM] 

See Q9 above.

## Q18: no 020 example [Q: 1:58 PM] 

See Q9 above.

## Q19: I missed the beginning. Where are today's slides and files? [Q: 1:55 PM] [A: 1:59 PM] 

The presentation recording and slides will be emailed to all attendees shortly after the end of the webinar.

## Q20: thank you [Q: 2:00 PM] 

## Q21: so you don't have to define f explicity? [Q: 2:00 PM] 

Not when using it in a loop (e.g., for f in some_variable) - that syntax provides all the definition needed.

## Q22: Thank you!  This was great! [Q: 2:00 PM] 

## Q23: Thanks Lauren! [Q: 2:00 PM] 

## Q24: Thank you very much! [Q: 2:00 PM] 

Thank you all for participating! :)

