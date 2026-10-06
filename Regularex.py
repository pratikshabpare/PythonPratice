import re
text="12345"
result=re.fullmatch(r"\d",text)
if result:
    print("Only digits")
else:
    print("not only digits")