# import module
import os
  

  
# assign folder path
Folderpath = 'C:/Users/Geetansh Sahni/Documents/R'    
  
# get size
for ele in os.scandir(Folderpath):
    size+=os.path.getsize(ele)
      
print(size)