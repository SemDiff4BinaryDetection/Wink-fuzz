import json
from pdb import set_trace as bp

def read_json_define_class():
 json_template_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\Types.json"
 f=open(json_template_path, 'r')
 data = json.load(f)
 f.close()
 
 python_code_path=r"\Users\nuc\Desktop\NTFuzz\Hooker\Debug\structs_define.py"
 header="from ctypes import * \nimport ctypes \nfrom sys import getsizeof \nfrom pdb import set_trace as bp \nfrom ctypes.wintypes import * \nfrom _multiprocessing import win32 \nimport argparse\n\n\n"
 f=open(python_code_path, 'w')
 f.write(header)
 f.close()
 f=open(python_code_path, 'a')
 
 test_step=0
 for syscall in data:
   arg_num=data[syscall]['argnum']
   for arg_i in range(1,arg_num+1):
     arg_i_template=""#The output python code to define the argument class
     arg_symbol="arg"+str(arg_i)
     arg=data[syscall][arg_symbol]
     arg_type=arg['type']
     fields_template=[]#The output python code for each filed in this argument template
     struct_num=-1
     struct_out_str=""#Used to store this argument's all structures' output python code
     if arg_type=="ptr":
       if arg["content"]["type"]=="struct":
           new_struct_content=arg["content"]["fields"]
           real_syscall_name=syscall.split("!")[1]
           #We do not need useless_struct_num in here. So it is useless.
           struct_out_str,useless_struct_num=parse_struct(new_struct_content,real_syscall_name,arg_i,struct_num+1)
           f.write(struct_out_str)
       elif arg["content"]["type"]=="array":
            if arg["content"]["content"]["type"]=="struct":
                new_struct_content=arg["content"]["content"]["fields"]
                real_syscall_name=syscall.split("!")[1]
                #We do not need useless_struct_num in here. So it is useless.
                struct_out_str,useless_struct_num=parse_struct(new_struct_content,real_syscall_name,arg_i,struct_num+1)
                f.write(struct_out_str)
            #Note we do not need to process other pointer cases as they are not structure thus do not need definition.
   test_step+=1
   #if test_step>=100:
   #  break   
 f.close()          
     
     
#If the current field is a struct, we try to parse it. 
#First argument is the json content of the structure.
#Second argument is the syscall name.
#Third argument is the argument number in the syscall.
#Fourth argument is the structure number of the argument. For each argument, we have this counter indicating which substruct we are now in.
def parse_struct(struct_content,syscall,arg_num,struct_num):
   contains_struct=False#Indicates whether the structure contains a sub structure. Used for our python code template creation
   field_count=0
   fields_template=[]#The output python code for each filed in this argument template
   sub_struct_str=""#Used to store the current structure's substructure's output python code.
   
   fields_out_str="class "+syscall+"_arg"+str(arg_num)+"_struct"+str(struct_num)+"("  
   
   #if syscall=="NtAccessCheckByType" and struct_num==0:
   #  bp()
   for field in struct_content:
     field_type=field["content"]["type"]
     if field_type=="handle":
         field_width=field["content"]['width']
         field_template="(\"reserve"+str(field_count)+"\", "
         field_template+=width2ctype(field_width)+"),\n"
     elif field_type=="scalar":
         field_width=field["content"]['width']
         field_template="(\"reserve"+str(field_count)+"\", "
         field_template+=width2ctype(field_width)+"),\n"         
     elif field_type=="array":
         field_template,delta_sub_struct_str,struct_num,contains_struct=process_array(field["content"], syscall,arg_num,struct_num,field_count)
         sub_struct_str+=delta_sub_struct_str
     elif field_type=="stringw":       
         if field_count==len(struct_content)-1:#If the string field is the last offset in the struct, it is hard to determine the size.
             field_template="(\"reserve"+str(field_count)+"\", "
             field_template+="c_char*1024),\n" 
         else:#If the string field is not the last offset, it is possible to calculate its size.
             current_offset=field["offset"]
             next_offset=struct_content[field_count+1]["offset"]
             string_length= next_offset-current_offset
             field_template="(\"reserve"+str(field_count)+"\", "
             field_template+="c_char*"+str(string_length)+"),\n"              
     elif field_type=="ptr":
       '''content_type=field["content"]["content"]["type"]
       if content_type=="struct":
           contains_struct=True
           field_template,delta_sub_struct_str,struct_num=process_sub_struct(field["content"]["content"]["fields"],syscall,arg_num,struct_num,field_count,"POINTER(")
           sub_struct_str+=delta_sub_struct_str
       elif content_type=="scalar" or content_type=="handle":
           field_template="(\"reserve"+str(field_count)+"\", "
           field_template+="LPVOID),\n" 
       elif content_type=="array":
           #If we find the pointer array is an array of structure, we only need to define this structure. 
           if field["content"]["content"]["content"]["type"]=="struct":
             contains_struct=False
             useless_field_template,delta_sub_struct_str,struct_num=process_sub_struct(field["content"]["content"]["content"]["fields"],syscall,arg_num,struct_num,field_count,"")
             #We don't need useless_field_template because this field is a LPVOID in the current structure. But we need the string containing the newly defined sub structure.
             sub_struct_str+=delta_sub_struct_str
           field_template="(\"reserve"+str(field_count)+"\", "
           field_template+="LPVOID),\n"            
           #Note we do not need to process other pointer cases as they are not structure thus do not need definition.
       elif content_type=="stringw":
           field_template="(\"reserve"+str(field_count)+"\", "
           field_template+="c_char_p),\n" 
       elif content_type=="ptr":
           delta_field_template,delta_sub_struct_str,struct_num,contains_struct=process_ptr(field["content"],syscall,arg_num,struct_num,field_count)          
           field_template+=delta_field_template
           sub_struct_str+=delta_sub_struct_str
       elif content_type=="funcptr":
           field_template="(\"reserve"+str(field_count)+"\", "
           field_template+="c_longlong*2),\n"''' 
       delta_field_template,delta_sub_struct_str,struct_num,contains_struct=process_ptr(field,syscall,arg_num,struct_num,field_count)  
       field_template=""
       field_template+=delta_field_template
       sub_struct_str+=delta_sub_struct_str
     elif field_type=="struct":
       contains_struct=True
       #bp()
       field_template,delta_sub_struct_str,struct_num=process_sub_struct(field["content"]["fields"],syscall,arg_num,struct_num,field_count,"")
       #bp()
       sub_struct_str=delta_sub_struct_str+sub_struct_str
       
     elif field_type=="funcptr":
       if field_count==len(struct_content)-1:#If the string field is the last offset in the struct, it is hard to determine the size.
             field_template="(\"reserve"+str(field_count)+"\", "
             field_template+="c_longlong*2),\n" 
       else:#If the string field is not the last offset, it is possible to calculate its size.
             current_offset=field["offset"]
             next_offset=struct_content[field_count+1]["offset"]
             ptr_length= next_offset-current_offset
       
             field_template="(\"reserve"+str(field_count)+"\", "
             field_template+=width2ctype(ptr_length)+"),\n"     
     else:
       print("Didn't expect this case!")
       bp()     
          
     fields_template.append(field_template)
     field_count+=1
     
     
   #Assemble each part of the structure definition here  
   if contains_struct==True and len(struct_content)==1:
     contains_struct=False
   if contains_struct==False:
       fields_out_str+="Structure):\n     _fields_ = ["  
   else:
       fields_out_str+="ctypes.Structure):\n     _fields_ = ("  
   for field_i in range(len(fields_template)): 
       if field_i==0:
           fields_out_str+=fields_template[field_i]
       else:    
           fields_out_str+="                 "+fields_template[field_i]
   fields_out_str=fields_out_str[:fields_out_str.rfind(",")]#delete extra comma in the end of the string
   if contains_struct==False:
       fields_out_str+="\n                ]\n"
   else:
       fields_out_str+="\n                )\n" 
     
   return sub_struct_str+fields_out_str,struct_num   

#Encountered a substructure in the current structure. Now we need to reserve this field in the current structure (as a pointer or not). 
#And at the same time make a new definition for this substructure
#new_struct_content: The Json data of the substructure.
#syscall: syscall name
#arg_num: number of argument in the syscall
#struct_num: number of structure in this argument
#pointer_or_not: indicate whether the substructure is referenced as a pointer in the current structure or as the substructure.
def process_sub_struct(new_struct_content,syscall,arg_num,struct_num,field_count,pointer_or_not):
   new_struct_name=syscall+"_arg"+str(arg_num)+"_struct"+str(struct_num+1)
   field_template="(\"reserve"+str(field_count)+"\", "
   if pointer_or_not=='':
     field_template+=pointer_or_not+new_struct_name+"),\n" 
   else:
     field_template+=pointer_or_not+new_struct_name+")),\n" 
   sub_struct_str,struct_num=parse_struct(new_struct_content,syscall,arg_num,struct_num+1)
   sub_struct_str+="\n"
   
   return field_template,sub_struct_str,struct_num

#Encountered an array in the structure. Now we need to detect whether this is an array of normal variable (i.e., ULONG, UCHAR, BYTE),
#or is an array of new structure. If is an array of new structure, we need to define this new structure.
def process_array(array_content, syscall,arg_num,struct_num,field_count):
   sub_struct_str=""
   field_template=""
   kind=array_content["size"]["kind"]
   contains_struct=False
   if kind=="fixed":
       if array_content["content"]["type"]=="struct":
          contains_struct=True
          delta_field_template,delta_sub_struct_str,struct_num=process_sub_struct(array_content["content"]["fields"],syscall,arg_num,struct_num,field_count,"")
          sub_struct_str+=delta_sub_struct_str
          
          #The delta_field_template is not right at this moment, we need to modify it into struct_size*struct_count.
          insert_pos=delta_field_template.find("),\n")
          modified_field_template=delta_field_template[:insert_pos]+"*"+str(array_content["size"]["val"])+delta_field_template[insert_pos:]
          field_template+=modified_field_template
       elif array_content["content"]["type"]=="ptr":
          '''field_template="(\"reserve"+str(field_count)+"\", "
          field_template+="LPVOID),\n"
          if array_content["content"]["content"]["type"]=="struct":'''
          delta_field_template,delta_sub_struct_str,struct_num,contains_struct=process_ptr(array_content,syscall,arg_num,struct_num,field_count)          
          
          field_template+="(\"reserve"+str(field_count)+"\", "
          field_template+="LPVOID"+"*"+str(array_content["size"]["val"])+")"
          sub_struct_str+=delta_sub_struct_str
       elif array_content["content"]["type"]=="funcptr":
          print("Did not expect that!")
          bp()   
       else:
           field_template="(\"reserve"+str(field_count)+"\", "
           field_template+=width2ctype(array_content["content"]["width"])+"*"+str(array_content["size"]["val"])+"),\n"
   elif kind=="argfield" or kind=="adjacentfield" or kind=="unknown":
       if array_content["content"]["type"]=="struct":
          contains_struct=True
          delta_field_template,delta_sub_struct_str,struct_num=process_sub_struct(array_content["content"]["fields"],syscall,arg_num,struct_num,field_count,"")
          sub_struct_str+=delta_sub_struct_str
          
          #The delta_field_template is not right at this moment, we need to modify it into struct_size*struct_count.
          insert_pos=delta_field_template.find("),\n")
          modified_field_template=delta_field_template[:insert_pos]+"*"+str(int(0x1000/(array_content["width"])))+delta_field_template[insert_pos:]
          field_template+=modified_field_template
       elif array_content["content"]["type"]=="ptr":
          '''field_template="(\"reserve"+str(field_count)+"\", "
          field_template+="LPVOID),\n"
          if array_content["content"]["content"]["type"]=="struct":'''
          delta_field_template,delta_sub_struct_str,struct_num,contains_struct=process_ptr(array_content,syscall,arg_num,struct_num,field_count)          
          
          field_template+="(\"reserve"+str(field_count)+"\", "
          field_template+="LPVOID"+"*"+str(int(0x1000/(array_content["width"])))+")"
          sub_struct_str+=delta_sub_struct_str
       elif array_content["content"]["type"]=="funcptr":
          print("Did not expect that!")
          bp()      
       else:     
          field_template="(\"reserve"+str(field_count)+"\", "
          field_template+=width2ctype(array_content["content"]["width"])+"*"+str(int(0x1000/array_content["content"]["width"]))+"),\n"
   else:
       print("Didn't expect this situation!")
       bp()                 
   return  field_template, sub_struct_str, struct_num,contains_struct   

#Encountered a pointer in the array or in the struct.
def process_ptr(field,syscall,arg_num,struct_num,field_count):
    content_type=field["content"]["content"]["type"]
    field_template=""
    sub_struct_str=""
    contains_struct=False
    if content_type=="struct":
        contains_struct=True
        field_template,delta_sub_struct_str,struct_num=process_sub_struct(field["content"]["content"]["fields"],syscall,arg_num,struct_num,field_count,"POINTER(")
        sub_struct_str+=delta_sub_struct_str
    elif content_type=="scalar" or content_type=="handle":
        field_template="(\"reserve"+str(field_count)+"\", "
        ptr_c_type=None
        if field["content"]["content"]["width"]==1:
          ptr_c_type="BYTE"
        elif field["content"]["content"]["width"]==2:
          ptr_c_type="USHORT"
        elif field["content"]["content"]["width"]==4:
          ptr_c_type="ULONG"
        elif field["content"]["content"]["width"]==8:
          ptr_c_type="c_longlong"
        else:
          bp()      
        field_template+="POINTER("+ptr_c_type+")),\n" 
    elif content_type=="array":
        #If we find the pointer array is an array of structure, we only need to define this structure. 
        if field["content"]["content"]["content"]["type"]=="struct":
          contains_struct=True
          useless_field_template,delta_sub_struct_str,struct_num=process_sub_struct(field["content"]["content"]["content"]["fields"],syscall,arg_num,struct_num,field_count,"")
          #We don't need useless_field_template because this field is a LPVOID in the current structure. But we need the string containing the newly defined sub structure.
          sub_struct_str+=delta_sub_struct_str
        field_template="(\"reserve"+str(field_count)+"\", "
        field_template+="LPVOID),\n"            
        #Note we do not need to process other pointer cases as they are not structure thus do not need definition.
    elif content_type=="stringw":
        field_template="(\"reserve"+str(field_count)+"\", "
        field_template+="c_char_p),\n" 
    elif content_type=="ptr":
        field_template="(\"reserve"+str(field_count)+"\", "
        field_template+="LPVOID),\n"
        delta_field_template,delta_sub_struct_str,struct_num,contains_struct=process_ptr(field["content"],syscall,arg_num,struct_num,field_count)
        sub_struct_str+=delta_sub_struct_str
    elif content_type=="funcptr":
        field_template="(\"reserve"+str(field_count)+"\", "
        field_template+="c_longlong*2),\n" 
    else:
        print("Didn't expect this case!")
        bp()        
    return field_template,sub_struct_str,struct_num,contains_struct
    
#Output ctype according to width
def width2ctype(width):
 if width==2:
   return "USHORT"
 elif width==4:
   return "ULONG" 
 elif width==1:
   return "BYTE"
 elif width==8:
   return "c_longlong" 
 elif width==16:
   return "c_longlong*2" 
   
 
read_json_define_class()