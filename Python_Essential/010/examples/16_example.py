import re

string = "sa dfas?df,asd;fa:s!df"
result = re.sub(r'[,;?:!\s]', ' ', string)
print(result)

