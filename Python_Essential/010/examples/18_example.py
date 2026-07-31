import re

import re

string = "test1 test2 test3 test4 test5"

# re.fullmatch(pattern, string) - Пошук рядку, повністю співпадаючий з регулярним виразом
# pattern - рядок, шаблон регулярного виразу,
# string - рядок для пошуку,
# flags=0 - один або декілька прапорців.

result = re.fullmatch(r"test1", string)
# None
print(result)

result = re.fullmatch(r"\w+\s{1, 5}", string)
print(result)

print(re.fullmatch(r'[a-z]+\s\d+', 'super 205'))
