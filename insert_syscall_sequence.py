from pdb import set_trace as bp
from library import extract_src_dict, extract_syscall, is_trace, extract_trace_num, extract_result, read_syscall_table
import random

class record:
    def __init__(self):
        self.current_dep_arg= [] #Indicates which argument the current syscall has dependent relation
        self.prior_dep_arg = [] #Indicates which argument the prior syscall has dependent relation
        self.syscall_cython_str=None #Record the string of the cython code that prepare all the arguments.
        self.dbg_reason=""#For debuging purpose. Records the learnt example of the syscall sequence.


#We extract local sequence as a dictionary. That is, for each syscall, we extract the necessary syscall must be called prior to it. It possible to extract multiple prior calls prior to some syscalls, but for simplicity, here we only consider the case that only calls one prior syscall
def extract_local_seq_dictionary(fast_trace_table_by_trace,fast_cython_table,trace_lines,synthesized_result_table,syscall_success_table,syscall_trace_num_table):
 print("-----------------------Extract local dependent sequences-----------------------------")
 local_syscall_seq_dic={}#A dictionary that treat each syscall as a key and records the must to be called syscall prior to this key.

 syscalls_seen={}#A list records all the syscalls seen in the log and their statstics. 
 line_num=0
 
 syscall_table={}
 syscall_table_path=r"C:\Users\nuc\Desktop\ntfuzz+\windows10_17134_syscall_table.txt"
 syscall_table=read_syscall_table(syscall_table_path,syscall_table)

 for line in trace_lines:
   print("line_num:",line_num)
   if not is_trace(line):
     continue
   taint_src_dict=extract_src_dict(line)
   syscall=extract_syscall(line)
   
   #----------------------------------------
   #Below codes are for syscall statistics
   syscall_num=int(syscall,16)
   syscall_name=syscall_table[syscall_num]
   if syscall_name not in syscalls_seen:
     syscalls_seen[syscall_name]=1
   else:
     syscalls_seen[syscall_name]+=1   
   #----------------------------------------
   #Above codes are for syscall statistics  
     
   trace_num=extract_trace_num(line)
   if len(taint_src_dict)==1:#We only consider one-prior syscall cases for simplicity
     keys=list(taint_src_dict.keys())
     if keys[0]!=trace_num:#Ensure that the src is some prior syscall rather than the current syscall.
       if syscall not in local_syscall_seq_dic:#Add the syscall as key
         local_syscall_seq_dic[syscall]={}
       prior_syscall=fast_trace_table_by_trace[keys[0]]  
       if prior_syscall not in local_syscall_seq_dic[syscall]:#Add the dependent syscall as subkey
         #success_trace_num=select_success_trace(syscall,trace_num,synthesized_result_table,syscall_success_table,syscall_trace_num_table)
         if trace_num not in synthesized_result_table:#If the syscall was deleted from the synthesized cython code
           continue
         if not is_success_ret_value(synthesized_result_table,syscall_success_table,trace_num,syscall):#If current rear syscall in the synthesized cython was unsuccessful, skip it.
           continue
         if trace_num==-1:#If the rear syscall cannot find any other instances executed successfully, we skip it.
           continue
         local_syscall_seq_dic[syscall][prior_syscall]=record()
         #if trace_num=="72F":
         #  bp()
         values=taint_src_dict[keys[0]]
         for value in values:
           self_arg=value.split(" ")[0]
           local_syscall_seq_dic[syscall][prior_syscall].current_dep_arg.append(self_arg.split("_")[-1])
           src_arg=value.split(" ")[1]
           if src_arg.startswith("ret"): 
             local_syscall_seq_dic[syscall][prior_syscall].prior_dep_arg.append("ret")
           else:
             local_syscall_seq_dic[syscall][prior_syscall].prior_dep_arg.append(src_arg.split("_")[-1])    
         local_syscall_seq_dic[syscall][prior_syscall].syscall_cython_str=find_cython_by_trace_num(fast_cython_table,trace_num)
         local_syscall_seq_dic[syscall][prior_syscall].dbg_reason=trace_num
   line_num+=1 

 #------------------------------------------------------------------------------------------------------------
 #The following code before bp() is used to count the syscalls statstics
 import operator
 sort_by_grade = operator.itemgetter(1)
 sorted_value_key_pairs = sorted(syscalls_seen.items(), key=sort_by_grade, reverse=True)
 #sorted_dict={k: v for v, k in sorted_value_key_pairs}
 print(sorted_value_key_pairs)
 bp()  
 #------------------------------------------------------------------------------------------------------------ 
   
   
 '''
 #------------------------------------------------------------------------------------------------------------
 #The following code before bp() is used to count the dictionary info
 dictionary_working_size=0#The real size of the dictionary that recording the true sequences rather than null
 max_sub_sequence_count=-1#The maximum subsequent syscall number
 #min_sub_sequence_count=-1#The minimum subsequent syscall number
 avg_sub_sequence_count=-1#The avg subsequent syscall number
 total_children_num=0#Total children number
 for key in  local_syscall_seq_dic:
   children_count=len(local_syscall_seq_dic[key])
   if children_count>0:
     dictionary_working_size+=1
   if children_count> max_sub_sequence_count:
     max_sub_sequence_count=children_count
   total_children_num+=children_count 
 avg_sub_sequence_count= total_children_num*1.0/dictionary_working_size
 print("dictionary_working_size:",dictionary_working_size,"max_sub_sequence_count:",max_sub_sequence_count,"avg_sub_sequence_count:",avg_sub_sequence_count)  
 bp()  
 #The above code before bp() is used to count the dictionary info
 #------------------------------------------------------------------------------------------------------------ 
 '''
 return local_syscall_seq_dic,trace_lines        

#We want to record the rear syscall's cython code. However, that trace itself might be unsuccessful. Thus, if the current trace is unsuccessful, we look around in all the trace and instead record the cython code of other successfull trace calling the same syscall.
'''def select_success_trace(syscall,trace_num,synthesized_result_table,syscall_success_table,syscall_trace_num_table):
  if trace_num not in synthesized_result_table:#If the trace was deleted in the synthesized trace
    return -1
  if is_success_ret_value(synthesized_result_table,syscall_success_table,trace_num,syscall):
    return trace_num
  else:
    for trace_num_i in syscall_trace_num_table[syscall]:
      if trace_num_i not in synthesized_result_table:#If the trace num not in our synthesized trace (because the trace hangs and was not recorded at the last syscalls), just skip it.
        continue
      if is_success_ret_value(synthesized_result_table,syscall_success_table,trace_num_i,syscall):
        return trace_num_i
    return -1    '''
      
def is_success_ret_value(synthesized_result_table,syscall_success_table,trace_num,syscall):
  if synthesized_result_table[trace_num]>0:#If the current trace_num call have success return value
    return True
  elif synthesized_result_table[trace_num]==0 and syscall_success_table[syscall]==0:#If the return value is 0 and this is the success value
    return True
  return False    
         
#Try to find the gap after some syscalls, where subsequent dependent syscalls can be inserted but not inserted in the trace.         
def find_insertable_sites(local_syscall_seq_dic,trace_lines,fast_trace_table,syscall_success_table,synthesized_result_table):
  print("-----------------------finding insertable sites-----------------------------")
  prior_syscall_considered=[]#To avoid deduplicate finding for the same prior syscall, we should remember the already checked prior syscalls and skip them.
  insert_sites={}#A map recording all the insertable sites and the cython code can be inserted.
  rear_syscall_i=0
  for rear_syscall in local_syscall_seq_dic:
    print("rear syscall:",rear_syscall_i,"/",len(local_syscall_seq_dic))
    prior_syscall_i=0
    for prior_syscall in  local_syscall_seq_dic[rear_syscall]:
      print("prior_syscall_i:",prior_syscall_i,"/",len(local_syscall_seq_dic[rear_syscall]))
      if prior_syscall in prior_syscall_considered:#skip the already considered prior syscall
        continue
      else:
        #prior_syscall_considered.append(prior_syscall)
        for line_num in range(len(trace_lines)):#Now iterate each syscall in trace and find insertable sites.
          trace_syscall=extract_syscall(trace_lines[line_num])
          trace_num=extract_trace_num(trace_lines[line_num])
          if trace_syscall==prior_syscall:#matches the prior syscall, next find whether it is insertable
            contains_dependent_syscall=find_dependent_syscall(rear_syscall,fast_trace_table,trace_num,line_num,len(trace_lines))
            if trace_num not in synthesized_result_table:#If the syscall was deleted in our synthesized cython, skip it.
              continue
            result=synthesized_result_table[trace_num]
            is_success_ret=is_success_syscall(trace_syscall,result,syscall_success_table)
            if (not contains_dependent_syscall) and is_success_ret:#The site is insertable
              if trace_num in insert_sites:
                insert_sites[trace_num].append(rear_syscall)
              else:  
                insert_sites[trace_num]=[rear_syscall]
      prior_syscall_i+=1        
    rear_syscall_i+=1          
  return insert_sites            
          
#Find the cython code that perpares the syscall        
def find_cython_by_trace_num(fast_table,trace_num):
  if trace_num in fast_table:
    return fast_table[trace_num]
  else:
    return ""  

#Create a table indexing each trace and its syscall and the taint src lines. Key is the line num in the trace  
def create_trace_table_by_line_num(trace_lines):
  result_table={}
  for line_i in  range(len(trace_lines)):
    if not is_trace(trace_lines[line_i]):
      continue
    syscall=extract_syscall(trace_lines[line_i])
    print(line_i)
    taint_src_dict=extract_src_dict(trace_lines[line_i])
    if len(taint_src_dict)==1:
      keys=list(taint_src_dict.keys())
      result_table[line_i]=[keys[0],syscall]
    else:
      result_table[line_i]=['',syscall]    
  return result_table   
  
#Create a table indexing each trace and its syscall and the taint src lines. Key is the trace num.
def create_trace_table_by_trace_num(trace_lines):
  result_table={}
  for line_i in  range(len(trace_lines)):
    if not is_trace(trace_lines[line_i]):
      continue
    syscall=extract_syscall(trace_lines[line_i])
    trace_num=extract_trace_num(trace_lines[line_i])
    result_table[trace_num]=syscall
  return result_table    
      
#To find whether there is a rear syscall using the prior syscall's result 
def find_dependent_syscall(rear_syscall,fast_trace_table,trace_num,start_line,end_line):
  for line_i in range(start_line,end_line):
    if line_i not in fast_trace_table:
      continue
    if rear_syscall==fast_trace_table[line_i][1]:#rear syscall matches
        if fast_trace_table[line_i][0]==trace_num:
          return True
          
#Analyze the cython code and create a table that indexes each syscall to the cython code         
def create_cython_syscall_table(synthesized_syscalls_cython):
  result_map={}
  for synthesized_syscall_cython in synthesized_syscalls_cython:
    start_index=synthesized_syscall_cython.find("print('ret")+len("print('ret")
    end_index=synthesized_syscall_cython.find("'",start_index)
    current_trace_num=synthesized_syscall_cython[start_index:end_index]
    result_map[current_trace_num]=synthesized_syscall_cython
  return result_map  

#Create a table. Keys are syscall, values are success return value. We decide the success return value by scanning all the syscall's return value and find the maximum value (if it is above or equals zero) as the correct one. If some syscall never has any return value above or equals zero, we record its maximum return value too.
def create_syscall_success_table(trace_lines):
  result_table={}
  for line_i in trace_lines:
    if not is_trace(line_i):
      continue
    syscall=extract_syscall(line_i)
    return_value=int(extract_result(line_i),16)
    if extract_result(line_i).startswith("C00") and len(extract_result(line_i))==8:#both are error 
      return_value=~return_value
    elif extract_result(line_i).startswith("800") and len(extract_result(line_i))==8:#both are error  
      return_value=~return_value
    if syscall not in result_table:
      result_table[syscall]=return_value
    else:
      if return_value>result_table[syscall]:
          result_table[syscall]=return_value 
  return result_table   

#Create a table that treat syscall as key, the trace num that calls the syscall as the value.
def create_syscall_trace_num_table(trace_lines):
  result_table={}
  for line_i in trace_lines:
    if not is_trace(line_i):
      continue
    syscall=extract_syscall(line_i)
    trace_num=extract_trace_num(line_i)
    if syscall not in result_table:
      result_table[syscall]=[trace_num]
    else:
      result_table[syscall].append(trace_num)
  return result_table      
    
#Check whether the current syscall's return value matches the table
def is_success_syscall(trace_syscall,result,syscall_success_table):
  success_ret=syscall_success_table[trace_syscall]
  if result>0:#As long as the synthesized syscall was successfull
    return True
  elif result==0 and success_ret==0:#both equals zero 
    return True
  return False  

#Insert the syscalls into potential sites of the current cython code.            
#insert_sites: all the insertable sites in the trace
#fast_cython_table: syscall --> cython code table
#local_syscall_seq_dic: a syscall --> syscall local dictionary
#fast_trace_table_by_trace: a trace_num --> syscall table
#level: denote how many levels of cython code we want to insert
def synthesize_new_cython(insert_sites,fast_cython_table,local_syscall_seq_dic,fast_trace_table_by_trace, level):  
  random_sites=select_sites(insert_sites)
  for site in random_sites:
    for rear_syscall in random_sites[site]:
      if site not in fast_cython_table:#In case trace num exists in trace but not in synthesized (because of failure of calling etc and deleted)
        continue  
      #if site=="12B5":
      #  bp()      
      #We firstly insert the first level cython code here.
      #if site==None or site=="":
      #  bp()
      #inserted_cython=adapt_cython_code(site, local_syscall_seq_dic[rear_syscall][fast_trace_table_by_trace[site]],3-level)
      #fast_cython_table[site]+="\n\n"+inserted_cython+"\n\n"
      
      #And we insert the other levels here if level > 1
      #inserted_trace_num=extract_trace_num_from_cython(local_syscall_seq_dic[rear_syscall][fast_trace_table_by_trace[site]].syscall_cython_str)
      #if inserted_trace_num==None or inserted_trace_num=="":
      #  bp()
      #if site=="13":
      #  bp()
      extract_inserted_cython=adapt_high_level_cython_code(level,site,rear_syscall,local_syscall_seq_dic[rear_syscall][fast_trace_table_by_trace[site]],local_syscall_seq_dic)
      fast_cython_table[site]+="\n\n"+extract_inserted_cython+"\n\n"
      
  new_cython=compose_traces(fast_cython_table)  
  return new_cython  

def extract_trace_num_from_cython(syscall_cython_str):
  key_str="print('ret"
  start_index=syscall_cython_str.find(key_str)
  trace_num=""
  if start_index!=-1:
    next_quote_idx=syscall_cython_str.find("'",start_index++len(key_str))
    trace_num=syscall_cython_str[start_index+len(key_str):next_quote_idx]
    return trace_num

#Modify the cython code. Adjust the dependent argument variable names
def adapt_cython_code(site, record,level):
  modified_cython=record.syscall_cython_str
  #if site=="A" and record.syscall_cython_str.startswith("L72F_arg_1=c_ulong(0xF)"):
  #  bp()
  if modified_cython=="":
    return modified_cython
  for cur_arg, src_arg in zip(record.current_dep_arg, record.prior_dep_arg):   
    start_str="_arg_"+cur_arg+"="  
    start_index=modified_cython.find(start_str)
    end_index=modified_cython.find("\n",start_index)
    if start_index==-1 or end_index==-1:
      return modified_cython  
    if not src_arg.startswith("ret"):
      new_substr="_arg_"+cur_arg+"="+"L"+site+"_arg_"+src_arg   
    else:
      new_substr="_arg_"+cur_arg+"="+"ret"+site   
    modified_cython=modified_cython[:start_index]+new_substr+modified_cython[end_index:]
  
  modified_cython=modified_cython.replace("print('ret","print('inserted_L"+str(level)+"_ret")  
  return modified_cython  

#Further add higher level cython code into the synthesized script. e.g., originally, we only append syscall_1, syscall_2 in one insertable site. Now we insert more syscalls that depends on the syscall_1 or syscall_2. This means higher level.
#level: the total level we want to insert into
#inserted_trace_num: the last level inserted syscall trace num
#syscall: The last level inserted syscall 
#local_syscall_seq_dic: The dictionary recording all the syscall sequences
def adapt_high_level_cython_code(level,inserted_trace_num,syscall,record,local_syscall_seq_dic):
  cython_str=""
  cython_str+="\n\n"+adapt_cython_code(inserted_trace_num, record,3-level)+"\n\n"
  candidates=candidate_subsequent_syscalls(syscall,local_syscall_seq_dic)
  next_inserted_trace_num=extract_trace_num_from_cython(record.syscall_cython_str)
  for candidate in candidates: #For each potential subsequent syscall
    #if "NtUserSetTimer" in candidate:
    #  bp()
    #if next_inserted_trace_num=="137F" and inserted_trace_num=="1271":
    #  bp()
    if level-1!=0:#Must not exceed the defined level.
      delta_cython=adapt_high_level_cython_code(level-1,next_inserted_trace_num,candidate,local_syscall_seq_dic[candidate][syscall],local_syscall_seq_dic)
      cython_str+=delta_cython
  return cython_str    
 
def candidate_subsequent_syscalls(syscall,local_syscall_seq_dic):
  candidates=[]
  #rear_syscall_i=0
  for rear_syscall in local_syscall_seq_dic:
    #print("rear syscall:",rear_syscall_i,"/",len(local_syscall_seq_dic))
    #prior_syscall_i=0
    for prior_syscall in local_syscall_seq_dic[rear_syscall]:
      #print("prior_syscall_i:",prior_syscall_i,"/",len(local_syscall_seq_dic[rear_syscall]))
      if prior_syscall==syscall: 
        candidates.append(rear_syscall)
        #if rear_syscall=="1220" and syscall=="1220":
        #  bp()
  return candidates      


#Now concatenate the cython codes based on the oirder of the trace num.  
def compose_traces(fast_cython_table):
  result_str=""
  trace_list=fast_cython_table.keys()
  trace_list = list(filter(None, trace_list))
  trace_list.sort(key=lambda h: int(h, 16))
  for trace_num in trace_list:
    result_str+=fast_cython_table[trace_num]+"\n\n"
  return result_str  
    
#Randomly select part of all insert sites for insertion later.    
def select_sites(insert_sites, rate=1.0):
  print("------------------------------randomly select insertions sites----------------------------------")
  print("Totally ",len(insert_sites)," insertable sites.")
  
  total_inserted_syscalls=0
  for site in insert_sites:
    total_inserted_syscalls+=len(site)
  print("Totally ",total_inserted_syscalls," inserted syscalls.")  
  
  indexes=[]
  for i in insert_sites:
    indexes.append(i)
  
  randomly_selected_indexes={}  
  for i in range(0,int(len(insert_sites)*rate)):  
    random_index=random.randint(0, len(indexes)-1)
    randomly_selected_indexes[indexes[random_index]]=insert_sites[indexes[random_index]]
    del indexes[random_index] 
  
  return randomly_selected_indexes  

#Create a table. Keys are trace num, values are return value. This demonstrates how many our synthesized syscalls are called successfully.   
def extract_synthesized_result_table(synthesized_result_path):
  ret_table={}
  f=open(synthesized_result_path)  
  lines=f.read().split("\n")
  lines = list(filter(None, lines))
  for line in lines:
    line_str=line[1:-1]#delete quotations
    trace_num=line_str.split(",")[0].strip("'").split("ret")[1]
    return_value=int(line_str.split(",")[1].strip(" "))
    ret_table[trace_num]=return_value
    
  return ret_table
            
def main():

  level=3
  
  trace_dependency_path=r"C:\Users\nuc\Downloads\NTFuzz_logs\dxdiag_log_dependency.txt"
  trace_dependent_f=open(trace_dependency_path,'rb')
  trace_content=trace_dependent_f.read()
  trace_lines=trace_content.split("\r")
 
  synthesized_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\synthesized_cython\dxdiag_synthesized.py"
  synthesized_f=open(synthesized_path,'r')
  synthesize_content=synthesized_f.read()
  synthesized_syscalls_cython=synthesize_content.split("\n\n")
  fast_cython_table=create_cython_syscall_table(synthesized_syscalls_cython)
  
  synthesized_result_path=r"C:\Users\nuc\Downloads\NTFuzz_logs\dxdiag_result.txt"
  synthesized_result_table=extract_synthesized_result_table(synthesized_result_path)
  
  syscall_success_table=create_syscall_success_table(trace_lines)
  syscall_trace_num_table=create_syscall_trace_num_table(trace_lines)
  
  fast_trace_table_by_line=create_trace_table_by_line_num(trace_lines)
  fast_trace_table_by_trace=create_trace_table_by_trace_num(trace_lines)
  local_syscall_seq_dic,trace_lines=extract_local_seq_dictionary(fast_trace_table_by_trace,fast_cython_table,trace_lines,synthesized_result_table,syscall_success_table,syscall_trace_num_table) 
  
  insert_sites=find_insertable_sites(local_syscall_seq_dic,trace_lines,fast_trace_table_by_line,syscall_success_table,synthesized_result_table)  
  new_cython=synthesize_new_cython(insert_sites,fast_cython_table,local_syscall_seq_dic,fast_trace_table_by_trace,level)
  synthesized_muted_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\synthesized_cython\___.py"
  f=open(synthesized_muted_path,'w')
  f.write(new_cython)
  f.close()
  '''dic_path=r"C:\Users\nuc\Downloads\dic.txt"
  insert_path=r"C:\Users\nuc\Downloads\insert.txt"
  f=open(dic_path,'w')
  f.write(str(local_syscall_seq_dic))
  f.close()
  f=open(insert_path,'w')
  f.write(str(insert_sites))
  f.close()'''
  
main()  