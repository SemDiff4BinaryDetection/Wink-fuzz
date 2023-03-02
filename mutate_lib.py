import sys
from pdb import set_trace as bp
import random
import base64
import hooker32
import ctypes
from ctypes import pointer, c_ulong

#syscall_count=0
#threashold=0
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
      
def mutate_ptr(value,syscall_count,threashold,mutate_ratio, dll_name, syscall_num, arg_idx):
  prob=random.random()
  #print("value=",value,"type=",type(value),pointer(c_ulong(value)))
  #print("syscall_count:",syscall_count,"threashold:",threashold,"mutate_ratio:",mutate_ratio,"prob:",prob)
  if syscall_count<=threashold or prob>mutate_ratio:
    return value
  specials = [0x0, 0x7fffffff, 0x80000000, 0x80000001, 0xffffffff]
  newArg=None
  dice=None
  
  dice = random.randint(0,3)
  if dice == 0:
    newArg = (0xFFFFFFFF & BitFlip(value, 32))
  elif dice == 1:
    newArg = (0xFFFFFFFF & ArithMutate(value, 0x10000))
  elif dice == 2:
    dice = random.randint(0,sys.maxsize) % 5
    newArg = specials[dice]
  else:
    newArg = ((0xFFFFFFFF & random.randint(0,sys.maxsize)) & 0xffffffff)
  #Tell the driver that the ptr value now mutated to newArg. So that the driver will keep modify the value in that memory location.  
  print("original ptr:",value)
  hooker32.notify_driver(newArg, dll_name,syscall_num, arg_idx)  
  return newArg  
  
  
def mutate_ulong(value,syscall_count,threashold,mutate_ratio):
  #global syscall_count
  #global threashold
  #print("syscall_count:",syscall_count)
  #print("threashold:",threashold)
  prob=random.random()
  if syscall_count<=threashold or prob>mutate_ratio:
    return value
  #value=int(value_str,16)
  specials = [0x0, 0x7fffffff, 0x80000000, 0x80000001, 0xffffffff]
  newArg=None
  dice=None
  
  if type(value)!=int:#In some cases, the value can be c_ulong something.
    if type(value)==long:
      pass
    elif type(value)==c_ulong:  
      value=value.value
  dice = random.randint(0,3)
  if dice == 0:
    newArg = (0xFFFFFFFF & BitFlip(value, 32))
  elif dice == 1:
    newArg = (0xFFFFFFFF & ArithMutate(value, 0x10000))
  elif dice == 2:
    dice = random.randint(0,sys.maxsize) % 5
    newArg = specials[dice]
  else:
    newArg = ((0xFFFFFFFF & random.randint(0,sys.maxsize)) & 0xffffffff)  
  return newArg


def mutate_ushort(value,syscall_count,threashold,mutate_ratio):
  #global syscall_count
  #global threashold
  prob=random.random()
  if syscall_count<=threashold or prob>mutate_ratio:
    return value
  #value=int(value_str,16)
  specials = [0x0, 0x7fff, 0x8000, 0x8001, 0xffff]
  newArg=None
  dice=None

  if type(value)!=int:#In some cases, the value can be c_ulong something.
    value=value.value
  
  dice = random.randint(0,3)
  if dice == 0:
    newArg = (0xFFFF & BitFlip(value, 16))
  elif dice == 1:
    newArg = (0xFFFF & ArithMutate(value, 0x100))
  elif dice == 2:
    dice = random.randint(0,sys.maxsize) % 5
    newArg = specials[dice]
  else:
    newArg = (0xFFFF & (random.randint(0,sys.maxsize)) & 0x100)
  return newArg

def mutate_byte(value,syscall_count,threashold,mutate_ratio):
  #global syscall_count
  #global threashold
  prob=random.random()
  if syscall_count<=threashold or prob>mutate_ratio:
    return value
  #value=int(value_str,16)
  specials = [0x0, 0x7f, 0x80, 0x81, 0xff]
  newArg=None
  dice=None

  if type(value)!=int:#In some cases, the value can be c_ulong something.
    value=value.value

  dice = random.randint(0,3)
  if dice == 0:
    newArg = (0xFF & BitFlip(value, 8))
  elif dice == 1:
    newArg = (0xFF & ArithMutate(value, 0xf))
  elif dice == 2:
    dice = random.randint(0,sys.maxsize) % 5
    newArg = specials[dice]
  else:
    newArg = ((0xFF & random.randint(0,sys.maxsize)) & 0x10)
  return newArg

def mutate_longlong(value,syscall_count,threashold,mutate_ratio):
  #global syscall_count
  #global threashold
  prob=random.random()
  if syscall_count<=threashold or prob>mutate_ratio:
    return value
  #value=int(value_str,16)
  specials = [0x0,0x7fffffffffffffff,0x8000000000000000,0x8000000000000001,0xffffffffffffffff]
  highDword = (0xFFFFFFFF & (value >> 32))
  lowDword = (0xFFFFFFFF & (value & 0xffffffff))
  newArg=None
  dice=None

  if type(value)!=int:#In some cases, the value can be c_ulong something.
    value=value.value

  dice = random.randint(0,3)
  if dice == 0:
    highDword = (0xFFFFFFFF & BitFlip(highDword, 32))
    lowDword = (0xFFFFFFFF & BitFlip(lowDword, 32))
  elif dice == 1:
    lowDword = (0xFFFFFFFF & ArithMutate(lowDword, 0x10000))
  elif dice == 2:
    dice = random.randint(0,sys.maxsize) % 5
    highDword = 0xFFFFFFFF & (specials[dice] >> 32)
    lowDword = 0xFFFFFFFF & (specials[dice] & 0xffffffff)
  else:
    highDword = random.randint(0,sys.maxsize)
    lowDword = random.randint(0,sys.maxsize)
  newArg = (0xFFFFFFFF & (highDword << 32)) + (0xFFFFFFFFFFFFFFFF & lowDword)
  return newArg

#Convert the string to \x.. if for some character base64.b16encode(string.encode()) fails to produce the value, we calculate the value through ord
def make_escape(string):
  escaped_string=""
  bp()
  for char in string:
    try:
      int_str=base64.b16encode(char.encode())
      escaped_string+=int_str
    except:
      int_str=hex(ord(char)).upper()[2:]
      escaped_string+=int_str
  return escaped_string    
  
def mutate_string(string,syscall_count,threashold,mutate_ratio):
  #global syscall_count
  #global threashold
  prob=random.random()
  if syscall_count<=threashold or prob>mutate_ratio:
    return string
  #bp()
  #print("before mutate:",string)
  escaped_string=make_escape(string)
  escaped_string_len=len(escaped_string)/2
  chars=[]
  try:
    for i in range(escaped_string_len):
      int_str=escaped_string[2*i:2*i+2]
      chars.append(int(int_str,16))
  except:
    bp()  
  '''chars=string.strip("'").split("\\x")
  #chars = list(filter(None, chars))
  for char_i in range(len(chars)):
    if chars[char_i]==' ':
      chars[char_i]='\x32'''   
  dice = random.randint(0,3)
  seed=None
  if dice==0 and len(chars)>0: #Mutate a random character.
    idx=random.randint(0,sys.maxsize) % len(chars)
    chars[idx]=(random.randint(0,sys.maxsize) & 0x5e) + 0x20
  elif dice==1 and len(chars)>0: #Truncate
    idx=random.randint(0,sys.maxsize) % len(chars) 
    chars[idx]=0
  else:#Append
    extendLen = random.randint(0,sys.maxsize) % 0x40
    seed=random.randint(0,sys.maxsize)
    char=(seed & 0x5e) + 0x20
    for idx in range(0,extendLen-1):
      chars.append(int(char))
    chars.append(0)
  new_char=""
  for char in chars:
    '''if len(char)==2:
      str_char=char
    elif len(char)==1:
      str_char="0"+char 
    else:
      bp()  '''    
    try:  
      str_char=hex(char).upper()[2:] 
      if len(str_char)==1:
        str_char='0'+ str_char 
        
      new_char+=base64.b16decode(str_char)  
    except:
      bp()    
  dbg_new_char=new_char[:1022] 
  if len(new_char)>1022:
    new_char=new_char[:1022] 
    #last_slash_idx= new_char.rfind("\\")
    #new_char=new_char[:last_slash_idx]
  new_char="'"+str(new_char)+"'"
  #print("mutated string=",new_char)
  #bp()
  return new_char     
  
def BitFlip(value, width):
  position = random.randint(0,sys.maxsize) % width;
  return (value ^ (1<< position));

def ArithMutate(value, bound):
  delta = random.randint(0,sys.maxsize) % (bound - 1) + 1
  if random.randint(0,sys.maxsize) % 2:
    return (value + delta)
  else:
    return (value - delta)

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
        
'''def should_mutate(mutate_ratio):
  prob=random.random
  if prob<mutate_ratio:
    return True
  else:
    return False  '''
    