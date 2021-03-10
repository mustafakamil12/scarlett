# This function is to decide which ADVA you will use ....

def select_ADVA():
 print ("""\nPlease select ADVA Type:- 
=============================\n
1. ADVA 825
2. ADVA 114

\n """)
 a = input("Enter your Choice please ...: ")
 My_ADVA_Type = int(a)
 
 if My_ADVA_Type == 1:
   return My_ADVA_Type

 elif My_ADVA_Type == 2:
   return My_ADVA_Type

 elif My_ADVA_Type > 2 or My_ADVA_Type < 1:
   print ("Please Select a vaild Choice between 1 and 2")
  #break