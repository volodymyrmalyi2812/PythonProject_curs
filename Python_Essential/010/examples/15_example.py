import re

string = "sa dfas?df,asd;fa:s!df"
result = re.split(r'[,;?:!\s]', string)
print(result)

