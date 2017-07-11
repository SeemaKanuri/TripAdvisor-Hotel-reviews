# int,list,tuple,string,dictionary
# No error handling in the code
import pandas as pd
import json
import re


def smileyreplace(obj,smileydict):
     temp1 = [];
     for i in obj:
       temp2=[];
       for j in i:    
           if j in smileydict:
               temp2.append(smileydict[j]);
           else:
               temp2.append(j);
       temp1.append(temp2);         
     return temp1;    
         
    

class lower:
    
 def main(obj):
     if type(obj) is dict:
         return lower.dict2lower(obj);
     elif type(obj) is str:
         return str.lower(obj);
     elif type(obj) is tuple: 
         return tuple(map(str.lower,obj))
     elif type(obj) is list:
         return list(map(str.lower,obj))
     elif isinstance(obj,pd.DataFrame):
         return obj.applymap(lower.main);
     else :
         return obj;
         
 # function to convert dictionaries to lower        
         
 def dict2lower(obj):
   temp = {} # create an empty dictionary
   keys = list(obj.keys()) 
   values = list(obj.values())
   keys = list(map(str.lower,keys))
   values = list(map(str.lower,values))
   for i in range(0,len(keys)):
     temp[keys[i]]= values[i];
   return temp;      

 

        
        
