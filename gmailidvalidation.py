#Python Program to check whether the given mail id is valid gmail id or not?

import re
s = input("Enter Mail id:")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)

if m!=None:
    print("Valid Mail Id");
else:
    print("Invalid Mail id")
    
    
"""
Output:
Enter Mail id:vijaybhaskar@gmail.com
Valid Mail Id

Enter Mail id:123@gmail.com
Valid Mail Id

Enter Mail id:abc@mail.com
Invalid Mail id

Enter Mail id:vijay@rediff.com
Invalid Mail id
"""
