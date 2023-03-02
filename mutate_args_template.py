import json
from pdb import set_trace as bp   

#Find the name of the syscall in the specific cython code
def find_cython_syscall(syscall_cython):
  lines=syscall_cython.split("\n")
  for line in lines:
    if line.find("=")==-1:#skip any line that does not assign value
      continue
    elif line.startswith("'''") or line.endswith("'''"):
      continue      
    right=line.split("=")[1]  
    if right.startswith("ntdll.") or right.startswith("win32u."):
      syscall=right[:right.find("(")]
      syscall=syscall.replace(".","!")
      return syscall
      

#find in the lines to find the definition of struct_instance_name
def find_struct_define(lines,struct_instance_name):
  struct_type_name=""
  for line_i in range(len(lines)-1,-1,-1):
    if lines[line_i].find("=")==-1:
      continue
    elif lines[line_i].startswith("'''") or lines[line_i].endswith("'''"):
      continue      
    left=lines[line_i].split("=")[0].strip()
    right=lines[line_i].split("=")[1].strip()
    if left==struct_instance_name:
      if right.find("(temp")!=-1:#In case struct_5_arg_3_0.reserve2=struct_5_arg_3_1(temp1), we need to instead find the struct type for the right side
        struct_instance_name=right[:right.find("(")]
      elif right.startswith("struct_"):
        struct_instance_name=right
      else:    
        if right.endswith("()"):
          struct_type_name=right[:right.find("(")]
        elif right.startswith("POINTER("):
          struct_type_name=right[right.find("(")+1:right.find(")")]       
        break    
  return struct_type_name
      
#find the map of each field in the structure from the structs_define. 
def find_field_type(structure_type_name,structs_define):
  field_map={}
  start_line_idx=-1
  for line_i in range(len(structs_define)):
    if structs_define[line_i].startswith("class "+structure_type_name):
      start_line_idx=line_i
      break
  for line_i in range(start_line_idx+1,len(structs_define)):
    first_coma_idx=structs_define[line_i].find(",")
    left_bracket_idx=structs_define[line_i].rfind("(",0,first_coma_idx)
    if left_bracket_idx==-1:#No left bracket, this indicates the end of the structure.
      break
    else:
      right_bracket_idx=structs_define[line_i].find(")",left_bracket_idx)   
      string=structs_define[line_i][left_bracket_idx+1:right_bracket_idx] 
      reserve=string.split(",")[0].strip('"')
      #offset=int(reserve.replace("reserve",""))
      field_type=string.split(",")[1].strip()        
      if field_type=="BYTE":
        field_map[reserve]="c_byte"
      elif field_type=="USHORT":
        field_map[reserve]="c_ushort"
      elif field_type=="ULONG":
        field_map[reserve]="c_ulong"
      elif field_type=="c_longlong":
        field_map[reserve]=field_type   
      #elif  field_type.startswith("POINTER"):
      #  field_map[offset]=      
  return field_map    
  
#find the type of the array from the lines. 
def find_array_define(lines,array_instance_name):
  for line in lines:
    if line.find("=")==-1:#We skip the lines that does not assign value
       continue
    elif line.startswith("'''") or line.endswith("'''"):
       continue   
    left=line.split("=")[0].strip()
    right=line.split("=")[1].strip()
    if left==array_instance_name:
      if "c_ulong" in right:
        return "c_ulong"
      elif "c_ushort" in right:
        return "c_ushort"
      elif "c_byte" in right:
        return "c_byte"   
      elif "c_longlong" in right:
        return "c_longlong"    

def mutate_by_line():
 indend="  "
 syscall_json_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\Types.json"
 f=open(syscall_json_path, 'r')
 syscall_json = json.load(f)
 f.close()
 
 synthesized_mutated=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\synthesized_inserted.py"
 f=open(synthesized_mutated,'r')
 syscall_cythons=f.read().split("\n\n")
 f.close()
 
 structures_define_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\structs_define.py"
 f=open(structures_define_path,'r')
 structs_define=f.read().split("\n")
 f.close()
 
 name_in_memory={"name":"","type":""}
 new_string=""
 new_string+="import random\n"
 new_string+="import sys\n"
 new_string+="from mutate_lib import *\n"
 new_string+="import random\n"
 new_string+="import sys\n"
 new_string+="from ctypes import *\n"
 new_string+="import ctypes\n"
 new_string+="from sys import getsizeof\n"
 new_string+="from pdb import set_trace as bp\n"
 new_string+="from ctypes.wintypes import *\n"
 new_string+="from _multiprocessing import win32\n"
 new_string+="import argparse\n"
 new_string+="from structs_define import* \n"
 new_string+="import threading\n"
 new_string+="import time\n"
 new_string+="win32u=windll.LoadLibrary('win32u.dll')\n" 
 new_string+="ntdll=windll.LoadLibrary('ntdll.dll')\n"  
 new_string+="def main():\n"
 new_string+=indend+"threashold=random.randint(0,sys.maxsize) % 0xa0f2\n"
 new_string+=indend+"syscall_count=0\n"
 fields_map={}
 count=0
 for syscall_cython in syscall_cythons:
   print(count,"/",len(syscall_cythons))
   syscall=find_cython_syscall(syscall_cython)
   lines=syscall_cython.split("\n")
   for line in lines:
     if line.startswith("from "):
       continue
     elif line.startswith("import "):
       continue  
     elif line.find("=")==-1:#We skip the lines that does not assign value
       new_string+=indend+line+"\n"
       continue
     elif line.startswith("'''") or line.endswith("'''"):
       new_string+=indend+line+"\n"
       continue     
     left=line.split("=")[0].strip()
     right=line.split("=")[1].strip()
     if left.find("_arg_")!=-1 and left.find(".")==-1 and left.startswith("L") and left.find("[")==-1:#left is not a field of some structure, this denotes the definition of some arg.
       arg_num=left.split("_arg_")[-1]
       arg_type=syscall_json[syscall]["arg"+arg_num]["type"]
       if arg_type=="handle":#We do not mutate handle
         new_string+=indend+line+"\n"
         continue
       else:
         if arg_type=="scalar":
           width=syscall_json[syscall]["arg"+arg_num]["width"]
           if width==1:
             new_right="mutate_byte("+right+",syscall_count,threashold,mutate_ratio)"
           elif width==2:
             new_right="mutate_ushort("+right+",syscall_count,threashold,mutate_ratio)"  
           elif width==4:
             new_right="mutate_ulong("+right+",syscall_count,threashold,mutate_ratio)" 
           elif width==8:
             new_right="mutate_longlong("+right+",syscall_count,threashold,mutate_ratio)"             
           new_string+=indend+left+"="+new_right+"\n"
         elif arg_type=="ptr" or arg_type=="func_ptr": 
           new_right="mutate_ulong("+right+",syscall_count,threashold,mutate_ratio)" 
           new_string+=indend+left+"="+new_right+"\n"  
         else:
           bp()         
     elif right.startswith("c_ulong(0x"):
       new_right="c_ulong(mutate_ulong(0x"+right.split("c_ulong(0x")[1].replace(")","")+",syscall_count,threashold, mutate_ratio))"
     elif right.startswith("c_ushort(0x"):
       new_right="c_ushort(mutate_ushort(0x"+right.split("c_ushort(0x")[1].replace(")","")+",syscall_count,threashold, mutate_ratio))"
     elif right.startswith("c_byte(0x"):
       new_right="c_byte(mutate_byte(0x"+right.split("c_byte(0x")[1].replace(")","")+",syscall_count,threashold, mutate_ratio))"
     elif right.startswith("c_longlong(0x"):
       new_right="c_longlong(mutate_longlong(0x"+right.split("c_longlong(0x")[1].replace(")","")+",syscall_count,threashold, mutate_ratio))"
     elif right.startswith("0x"):#if right (assigned value) is a constant value, we must consider mutate it.
       if left.startswith("struct"):#is struct field definition
         struct_instance_name=left[:left.rfind(".")]
         bracket_index=struct_instance_name.find("[")
         if bracket_index!=-1:
           struct_instance_name=struct_instance_name[:bracket_index]
         struct_field=left[left.rfind(".")+1:]
         if name_in_memory["name"]!= struct_instance_name:#cache the strucs to avoid find it again
           name_in_memory["name"]=struct_instance_name
           structure_type_name=find_struct_define(lines,struct_instance_name)
           name_in_memory["type"]=structure_type_name
           fields_map=find_field_type(structure_type_name,structs_define)
         else:#we are still in the same struct's other fields. Reuse the cache.  
           structure_type_name=name_in_memory["type"]
         try:  
           field_type=fields_map[struct_field]  
         except:
           bp()         
         if field_type=="c_byte":
           new_right="mutate_byte(0x"+right.split("0x")[1]+",syscall_count,threashold, mutate_ratio)"
         elif field_type=="c_ushort":
           new_right="mutate_ushort(0x"+right.split("0x")[1]+",syscall_count,threashold, mutate_ratio)"
         elif field_type=="c_ulong":
           if right.split("0x")[1]=="0'''":
             bp()
           new_right="mutate_ulong(0x"+right.split("0x")[1]+",syscall_count,threashold, mutate_ratio)"
         elif field_type=="c_longlong":
           new_right="mutate_longlong(0x"+right.split("0x")[1]+",syscall_count,threashold, mutate_ratio)"
       elif left.endswith("]"):#is array field definition
         array_instance_name=left[:left.rfind("[")]    
         if array_instance_name!=name_in_memory["name"]:
           name_in_memory["name"]=array_instance_name  
           array_type=find_array_define(lines,array_instance_name)      
           name_in_memory["type"]=array_type
         else:
           array_type=name_in_memory["type"]         
         if array_type=="c_byte":
           new_right="mutate_byte(0x"+right.split("0x")[1]+",syscall_count,threashold, mutate_ratio)"
         elif array_type=="c_ushort":
           new_right="mutate_ushort(0x"+right.split("0x")[1]+",syscall_count,threashold, mutate_ratio)"
         elif array_type=="c_ulong":
           new_right="mutate_ulong(0x"+right.split("0x")[1]+",syscall_count,threashold, mutate_ratio)"
         elif array_type=="c_longlong":
           new_right="mutate_longlong(0x"+right.split("0x")[1]+",syscall_count,threashold, mutate_ratio)"  
       else:#If right is 0x... then left should be structure or array fields. Other wise we pause and debug.
         bp()
     elif right.startswith("c_char_p("):
       start_quote_idx=right.find("'")
       end_quote_idx=right.rfind("'")
       new_right="c_char_p(mutate_string("+right[start_quote_idx:end_quote_idx+1]+",syscall_count,threashold, mutate_ratio)"+right[end_quote_idx+1:]
     elif right.startswith("'\\x"):#the right is a string (not a pointer to a string)
       new_right="mutate_string("+right+",syscall_count,threashold, mutate_ratio)"     
     else:
       #print("not mutated line:",line)  
       new_string+=indend+line+"\n"
       continue       
     new_line=left+"="+new_right  
     new_string+=indend+new_line+"\n"
   new_string+=indend+"syscall_count+=1\n"  
   new_string+="\n"  
   count+=1
 #new_string+="while(True):\n"
 #new_string+="  thread=threading.Thread(target=main)\n"
 #new_string+="  thread.start()\n"
 #new_string+="  time.sleep(60)\n"
 new_string+="main()\n" 
 mutated_arg_cython_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\args_mutate_template.py"
 f=open(mutated_arg_cython_path,'w')
 f.write(new_string)
 f.close()
 
 
def mutate_by_arg(): 
 indend="  "
 syscall_json_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\Types.json"
 f=open(syscall_json_path, 'r')
 syscall_json = json.load(f)
 f.close()
 
 synthesized_mutated=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\wordpad_synthesized_inserted_L1.py"
 f=open(synthesized_mutated,'r')
 syscall_cythons=f.read().split("\n\n")
 f.close()
 
 structures_define_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\structs_define.py"
 f=open(structures_define_path,'r')
 structs_define=f.read().split("\n")
 f.close()
 
 new_string=""
 new_string+="import sys\n"
 new_string+="from mutate_lib import *\n"
 new_string+="import random\n"
 new_string+="import sys\n"
 new_string+="from ctypes import *\n"
 new_string+="import ctypes\n"
 new_string+="from sys import getsizeof\n"
 new_string+="from pdb import set_trace as bp\n"
 new_string+="from ctypes.wintypes import *\n"
 new_string+="from _multiprocessing import win32\n"
 new_string+="import argparse\n"
 new_string+="from structs_define import* \n"
 new_string+="import threading\n"
 new_string+="import time\n"
 new_string+="import gc\n"
 new_string+="win32u=windll.LoadLibrary('win32u.dll')\n" 
 new_string+="ntdll=windll.LoadLibrary('ntdll.dll')\n"
 new_string+="def main():\n"
 new_string+=indend+"threashold=random.randint(0,sys.maxsize) % 0xa0f2\n"
 new_string+=indend+"syscall_count=0\n"
 new_string+=indend+"mutate_ratio=0.01\n"
 
 count=0
 syscall=""
 
 
 for syscall_cython in syscall_cythons:
   print(count,"/",len(syscall_cythons))
   syscall=find_cython_syscall(syscall_cython)
   lines=syscall_cython.split("\n")
   
   #Firstly find the syscall line
   syscall_line=""
   syscall_line_idx=-1
   for line_i in range(len(lines)):
     if lines[line_i].startswith("print('ret") or lines[line_i].startswith("print('inserted_ret"):
       syscall_line=lines[line_i-1]
       syscall_line_idx=line_i-1
       break
   #Next parse the arg types
   first_left_bracket=syscall_line.find("(")
   last_right_bracket=syscall_line.rfind(")")
   str_before_left_bracket=syscall_line[:first_left_bracket]
   str_after_right_braket=syscall_line[last_right_bracket+1:]
   str_in_the_middle=syscall_line[first_left_bracket+1:last_right_bracket]
   
   syscall_args=str_in_the_middle.split(",")
   syscall_args = list(filter(None, syscall_args))
   
   #mutate_str=""#The added lines to specify which args are to be mutated
   mutated_args=[]#The list of the mutated args or the args not need mutation
   #For each arg, we check the type
   for i in range(0,len(syscall_args)):
     #mutate_str+=indend+"if should_mutate():\n"
     arg_type=syscall_json[syscall]["arg"+str(i+1)]["type"]     
     if arg_type=="ptr" or arg_type=="funcptr":
       memory_address=""
       if "content" in syscall_json[syscall]["arg"+str(i+1)]:
         if syscall_json[syscall]["arg"+str(i+1)]["content"]["type"]=="struct":
           syscall_num=syscall_json[syscall]["sysnum"]
           if syscall_args[i].strip().startswith("byref("):
             variable_name=syscall_args[i].strip()[6:-1]#byref(variable_name)
             memory_address="addressof("+variable_name+")"
             #memory_address=syscall_args[i].strip()
           else:#in case like special value as a memory address e.g., 0
             variable_name=syscall_args[i].strip()   
             memory_address=variable_name             
           dll_name=syscall.split("!")[0]
           mutated_args.append("mutate_ptr("+memory_address+", syscall_count, threashold, mutate_ratio, '"+dll_name+"', "+str(syscall_num)+","+str(i+1)+")")
         else:
           if syscall_args[i].strip().startswith("byref("):
             variable_name=syscall_args[i].strip()[6:-1]#byref(variable_name)
             memory_address="addressof("+variable_name+")"
             #memory_address=syscall_args[i].strip()
           else:#in case like special value as a memory address e.g., 0
             variable_name=syscall_args[i].strip()   
             memory_address=variable_name      
           mutated_args.append("mutate_ulong("+memory_address+", syscall_count, threashold, mutate_ratio)") 
       else:
         if syscall_args[i].strip().startswith("byref("):
           variable_name=syscall_args[i].strip()[6:-1]#byref(variable_name)
           memory_address="addressof("+variable_name+")"
           #memory_address=syscall_args[i].strip()
         else:#in case like special value as a memory address e.g., 0
           variable_name=syscall_args[i].strip()   
           memory_address=variable_name       
         mutated_args.append("mutate_ulong("+memory_address+", syscall_count, threashold, mutate_ratio)")  
     elif arg_type=="scalar":  
       width=syscall_json[syscall]["arg"+str(i+1)]["width"]
       if width==1:
         mutated_args.append("mutate_byte("+syscall_args[i].strip()+", syscall_count, threashold, mutate_ratio)")
       elif width==2:
         mutated_args.append("mutate_ushort("+syscall_args[i].strip()+", syscall_count, threashold, mutate_ratio)")
       elif width==4:
         mutated_args.append("mutate_ulong("+syscall_args[i].strip()+", syscall_count, threashold, mutate_ratio)")
       elif width==8:
         mutated_args.append("mutate_longlong("+syscall_args[i].strip()+", syscall_count, threashold, mutate_ratio)")    
     elif arg_type=="handle":#We do not mutate handle type
       mutated_args.append(syscall_args[i].strip())
   new_syscall_line=str_before_left_bracket+"("
   for mutated_arg in mutated_args:
     new_syscall_line+=mutated_arg+", "
   if len(mutated_args)>0:#If has at least one argument
     new_syscall_line=new_syscall_line[:-2]#Trim the ending ", "
   else:#Has no argument
     pass  
   new_syscall_line+=")\n"
   
   new_cython_line=""
   #Now put together the mutataed lines and the other lines in the cython code
   for line_i in range(len(lines)):   
     if lines[line_i].startswith("from "):
       continue
     elif lines[line_i].startswith("import "):
       continue 
     elif lines[line_i].startswith("win32u=windll.LoadLibrary"):
       continue
     elif lines[line_i].startswith("ntdll=windll.LoadLibrary"):
       continue     
     if line_i != syscall_line_idx:
       new_cython_line+=indend+lines[line_i]+"\n"
     else:
       new_cython_line+=indend+new_syscall_line+"\n"
   new_cython_line+=indend+"syscall_count+=1\n"    
   new_string+=new_cython_line+"\n\n"    
   count+=1
   
 new_string+="main()\n" 
 mutated_arg_cython_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\wordpad_L1_args_mutate_template.py"
 f=open(mutated_arg_cython_path,'w')
 f.write(new_string)
 f.close()
   
#mutate_by_line() 
mutate_by_arg()
  