from pdb import set_trace as bp
from collections import OrderedDict
from library import read_syscall_table
import json

output_values=[]#A list recording each output's corresponding group id.
output_values_tag=[]#A list marking each output value's group id.
output_values_line_num=[]#A list recording the line num each output is from.
output_source_arg=[]#A list recording the output is from which arg in the source trace 

tag_soure_line_num=[]#A list recording where each line gets its tag from (the closest taint source)
group_id=0 #Indicates the group id the current trace should belong to.
lines_group_tag=[]

def group_traces():
  global group_id
  global lines_group_tag
  log_path=r"C:\Users\nuc\Downloads\NTFuzz_logs\awatch_log.txt"
  out_log_path=r"C:\Users\nuc\Downloads\NTFuzz_logs\new_awatch_log_dependency.txt"
  
  syscall_json_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\Types.json"
  f=open(syscall_json_path, 'r')
  syscall_json = json.load(f)
  f.close()
  
  syscall_table_path=r"C:\Users\nuc\Desktop\ntfuzz+\windows10_17134_syscall_table.txt"
  #read_syscall_table(syscall_table_path)
  syscall_table={}
  syscall_table=read_syscall_table(syscall_table_path,syscall_table)
  
  f=open(log_path,'rb')
  content=f.read().replace("\x00","")
  #content=f.read()
  lines=content.split("\n")
  #Each line contains a tag marking which group the current trace line belongs to.
  #initialize lines_group_tag
  for i in range(len(lines)):
    lines_group_tag.append(-1)
    tag_soure_line_num.append({})
  
  #Next we scan backward to find the trace dependencies
  line_num=0
  #lines=lines[:701]
  while line_num<len(lines):
    if is_trace(lines[line_num]):
      #if "ADFD :1039( 66010B8D, 5A0509B8, )  ret: 85000F" in lines[line_num]:
      #  bp()
      trace_line_num=find_trace_num(lines[line_num])
      syscall=find_syscall_num(lines[line_num])
      syscall_args_jsons=None
      if "ntdll!"+syscall_table[int(syscall,16)] in syscall_json:
        syscall_args_jsons=syscall_json["ntdll!"+syscall_table[int(syscall,16)]]
      elif "win32u!"+syscall_table[int(syscall,16)] in syscall_json:
        syscall_args_jsons=syscall_json["win32u!"+syscall_table[int(syscall,16)]]
        
      tag=find_tag(lines[line_num],line_num,trace_line_num,syscall_args_jsons)
      outputs,src_args=extract_single_trace_output(lines[line_num],trace_line_num)
      if len(outputs)>0:
        
        print("trace_line_num:",trace_line_num,"len(trace_groups):",group_id)
        if tag==None:#If this trace log is a starting one that has no relations to any other traces.
         group_id+=1
         print("outputs:",outputs)
         insert_outputs_in_map(outputs,src_args,group_id,trace_line_num)
         lines_group_tag[line_num]=group_id
         tag_soure_line_num[line_num]={trace_line_num:[]}
        else:#If this trace is also dependent on existing traces, mark the same tag for it.
         insert_outputs_in_map(outputs,src_args,tag,trace_line_num)
         lines_group_tag[line_num]=tag
      else:
        if tag!=None:
         lines_group_tag[line_num]= tag     
    else:
      line_num+=1
      continue      
    line_num+=1
  
  write_file(lines,out_log_path)  
  
def write_file(lines,out_log_path):
  global lines_group_tag
  global tag_soure_line_num
  f=open(out_log_path,'w')
  out_str=""
  for line, tag, src_line in zip(lines,lines_group_tag,tag_soure_line_num):
    #if type(src_line)!=int:
    #  if len(src_line)>1:
    #    bp()
    out_str+=" group: "+str(tag)+" taint src: "+str(src_line)+" "+line
  f.write(out_str)  
  f.close()
   
#Extract the output memory and its output value. Record this in the global so that later traces can easily find the source if they are originated from this trace.   
def extract_single_trace_output(line_trace,trace_line_num): 
  out_args=[]
  src_args=[]
  #Check return value
  ret_idx=line_trace.find('ret:')
  ret=line_trace[ret_idx+4:line_trace.find('TID')]
  ret=ret.strip()
  if ret_idx==-1:#If not found "ret" in string, that means the trace is incomplete, directly return
    return out_args,src_args
  if len(ret)!=0 and ret!='0':
    out_args.append(ret)
    src_args.append("ret"+str(trace_line_num))
    
  first_bracket_index=line_trace.find("(")
  close_bracket_index=line_trace.find(")",first_bracket_index)
  arg_str= line_trace[first_bracket_index+1:close_bracket_index]
  arguments=arg_str.split(",")
  arguments= list(filter(None, arguments))
  #Next check out entities
  out_entity_idx=line_trace.find("out entries:")
  if out_entity_idx==-1:#If not found "out entities" in string, that means the trace is incomplete, directly return
    return out_args,src_args
  out_entity=line_trace[out_entity_idx+12:line_trace.find("strings:")]  
  elements=out_entity.split(" ")
  #elements = list(OrderedDict.fromkeys(elements))
  elements= list(filter(None, elements))
  out_entities={}
  out_entry_srg_args=[]
  if len(elements)!=0:
    idx=0
    for element in elements:
    #while idx<(len(elements)):
      #print("out_entity:",out_entity)
      #print("elements[idx]:",elements[idx])
      #if "3223DC0: 20000 3223DC4: 1 3223DD0: 1 3223DD4: 20001E "==out_entity:
      #  bp()
      mem=element.split(":")[0].strip()
      content=element.split(":")[1].strip()
      arg_num=find_arg_by_addr(arguments,line_trace,mem)
      #For some out entities, even though in types.json it claims to be inout, but the out value is the same as the in value. Thus we should not include these value in thr out entries.
      '''in_entities_str=line_trace.split("in entries:")[1].split("out entries:")[0]
      mem_index=in_entities_str.find(mem+":")
      next_space_index=in_entities_str.find(" ",mem_index)
      origin_content=in_entities_str[mem_index+len(mem)+1:next_space_index]'''
      origin_content=find_in_addr_content(line_trace, mem)
      if origin_content==content:#If the in and out entry value does not change, skip it.
        continue
      out_entities[mem]=content
      if arg_num!="-1":
        out_entry_srg_args.append("L"+str(trace_line_num)+"_arg_"+arg_num)
      else:
        syscall=find_syscall_num(line_trace)   
        #if syscall=="182":
        #  out_entry_srg_args.append("struct_"+str(trace_line_num)+"_arg_4_0.reserve1")
    
        
  if len(out_entities)!=0:      
   out_args.append(out_entities)    
   src_args.append(out_entry_srg_args) 
  return out_args,src_args  
  
def find_in_addr_content(line_trace, mem):
  in_entities_str=line_trace.split("in entries:")[1].split("out entries:")[0]
  mem_index=in_entities_str.find(mem+":")
  if mem_index==-1:#Did not find the memory and its content in the trace log. This means the value is zero and we have skipped recording that for simplicity.
    return "0"
    
  next_space_index=in_entities_str.find(" ",mem_index)
  origin_content=in_entities_str[mem_index+len(mem)+1:next_space_index]
  return origin_content
  
  
#Find which arg does this output mem_addr refer to.
def find_arg_by_addr(args,line_trace,mem_addr):
  arg_i=0
  #If any arg matches the memory address, we directly return this arg num.
  for arg in args:
    if arg.strip()==mem_addr:
      return str(arg_i+1)  
    arg_i+=1 
  #When none of the arg matches the mem address, this is because the mem should matches some member within this arg. We need to find out who (the field name) does this arg map to.
    
  return "-1"  
  
#Check whether current trace log's arg matches any previous out value. If yes, mark this trace as the same tag as that out trace.  
#Return matched tags
def find_tag(line_trace,line_num,trace_line_num,syscall_args_jsons):
  global tag_soure_line_num  
  updated_tag=None
  args=extract_single_trace_args(line_trace)
  tags,dbg_args,src_line_nums=find_interest_args_tags(args,trace_line_num,line_trace, syscall_args_jsons)
  #if "5D :164( 31D22C4, F, 0, 0, 10, 1000000, 58, )  ret: 0 TID: 131C small" in line_trace:
  #    bp()
  #print(args)    
  #print("dbg_args:",dbg_args)
  #print("len(tags):",len(tags))
  if len(tags)==0:
    return 
  else: #Current trace matches one or more existing out value
    updated_tag,source_line_num=remark_out_tags(tags,src_line_nums)   
    remark_line_group(tags,updated_tag)    
    #if trace_line_num=="102D":
    #  bp()
    tag_soure_line_num[line_num]=source_line_num
    #if source_line_num=='9 ':
    #  bp()
  return updated_tag
   
#merge the group ids in lines_group_tag into a single id when they are implicitly dependent on each other.   
def remark_line_group(tags,updated_tag):
   global lines_group_tag
   for tag_idx in range(len(lines_group_tag)):
    if lines_group_tag[tag_idx]==-1:#skip trace lines that has no any tags
      continue
    elif lines_group_tag[tag_idx] in tags:  
      #if tag_idx==21011:
      #  bp()
      #if updated_tag==4:
      #  bp()
      lines_group_tag[tag_idx]=updated_tag
      
  
#Simply extract all args in one trace log   
def extract_single_trace_args(line_trace):
  syscall_args=line_trace[line_trace.find('(')+1:line_trace.find(')')].split(',')
  for arg_i in range(len(syscall_args)):
   syscall_args[arg_i]=syscall_args[arg_i].strip()
  syscall_args = list(filter(None, syscall_args))
  return syscall_args 
  
#add one log trace's output and their group_id into the global record  
def insert_outputs_in_map(outputs,src_args,tag,line_num):
  global output_values
  global output_values_tag  
  global output_values_line_num
  global output_source_arg
  for item,src_arg in zip(outputs,src_args):
    if type(item)==str:#For return value
      if len(item)==1 or item=="FFFFFFFF":#skip values too small, they are highly likely the scalar value.
        continue  
      if item not in output_values:
        output_values.append(item)
        output_values_tag.append(tag)
        output_values_line_num.append(line_num)
        output_source_arg.append(src_arg)
      else:
        index=output_values.index(item)
        del output_values[index]
        del output_values_tag[index]
        del output_values_line_num[index]
        del output_source_arg[index]
        output_values.append(item)
        output_values_tag.append(tag)
        output_values_line_num.append(line_num)
        output_source_arg.append(src_arg)
    else:#For out entries   
      for mem,mem_src in zip(item,src_arg):
        if len(item[mem])==1:#skip values too small, they are highly likely the scalar value.
         continue
        index=mem_in_output_values(mem)

        if index==-1:
          new_dict={mem:item[mem]}
          output_values.append(new_dict)
          output_values_tag.append(tag)
          output_source_arg.append(mem_src)
          #if mem=="305EF38":
          #  bp()
          output_values_line_num.append(line_num)
        else:
          del output_values[index]
          del output_values_tag[index]
          del output_values_line_num[index]
          del output_source_arg[index]
          new_dict={mem:item[mem]}
          output_values.append(new_dict)
          output_values_tag.append(tag) 
          output_values_line_num.append(line_num)   
          output_source_arg.append(mem_src)          



def mem_in_output_values(mem):
 for item_idx in range(len(output_values)):
   if type(output_values[item_idx])==dict:
     if mem in output_values[item_idx]:
       return item_idx  
 return -1      

#Find the trace number within the single line trace
def find_trace_num(line_trace):
   first_colon_index=line_trace.find(":")  
   trace_num=line_trace[:first_colon_index].strip()
   return trace_num
   
#Find the syscall number within the single line trace
def find_syscall_num(line_trace):
   first_colon_index=line_trace.find(":") 
   next_bracket_index=line_trace.find("(",first_colon_index)   
   syscall_num=line_trace[first_colon_index+1:next_bracket_index].strip()
   return syscall_num   
    
#For one trace log's arguments, find how many of them belong to the existing output value recorded globally.
def find_interest_args_tags(arguments,trace_line_num, line_trace, syscall_args_jsons):
  global output_values
  global output_values_tag  
  global output_source_arg
  global output_values_line_num
  tags=[]
  line_nums={}#The matched output's line num. Each key is the trace number. Values are the arg number in current trace and the arg number in source trace. Since each trace number can have multiple outputs, the values for each key here is a list. 
  dbg_args=[]
  arg_num=0
  for arg in arguments:
    #if trace_line_num=="102D" and arg=="328":
    # bp()
    if "arg"+str(arg_num+1) not in syscall_args_jsons:
      bp()
    arg_json=syscall_args_jsons["arg"+str(arg_num+1)]
    if "inout" in arg_json:
      if arg_json["inout"]=="out":#for output args, we don't look for its input relations
        arg_num+=1
        continue
    for item,src_arg,tag,line_idx in reversed(zip(output_values,output_source_arg,output_values_tag,output_values_line_num)):
      #if line_idx=='5C ':
      #  bp()
      if type(item)==str:#match for return value
        if item==arg:
          tags.append(tag)
          if line_idx not in line_nums:
            line_nums[line_idx]=["L"+str(trace_line_num)+"_arg_"+str(arg_num+1)+" "+src_arg]
          else:
            line_nums[line_idx].append("L"+str(trace_line_num)+"_arg_"+str(arg_num+1)+" "+src_arg)          
          dbg_args.append(arg)
          break
      else:#match for out entities
         mem=item.keys()[0]
         if item[mem]==arg:#If the content in the output memory address matches the current arg, this is a dependency
            tags.append(tag)
            if line_idx not in line_nums:
              line_nums[line_idx]=["L"+str(trace_line_num)+"_arg_"+str(arg_num+1)+" "+src_arg]
            else:
              line_nums[line_idx].append("L"+str(trace_line_num)+"_arg_"+str(arg_num+1)+" "+src_arg)            
            dbg_args.append({mem:item[mem]})
            break
         elif mem==arg:#If the previous output memory address matches the current arg, we need further checking some conditions   
            if arg_json["type"]!="ptr":#If the current arg is not ptr type, this is obviously not a match to the previous output memory
              continue
            else:#The arg is ptr type.
              in_value=find_in_addr_content(line_trace, arg)      
              if in_value!=item[mem]:#The output value does not match the current arg's in memory content. This implies a non-dependency. Only when the two values equal implies dependency.
                continue
            tags.append(tag)
            if line_idx not in line_nums:
              line_nums[line_idx]=["L"+str(trace_line_num)+"_arg_"+str(arg_num+1)+" byref_"+src_arg+""]
            else:
              line_nums[line_idx].append("L"+str(trace_line_num)+"_arg_"+str(arg_num+1)+" byref_"+src_arg+"")            
            dbg_args.append({mem:item[mem]})
            break
            
    arg_num+=1        
 
  return tags,dbg_args,line_nums        

#We merge multiple tags into one tag. We select the smallest tag as the new tag.
#Return the updated tag
def remark_out_tags(tags,src_line_nums):
  global output_values_tag
  minest=1000000
  source_line_num={}
  #if src_line_nums=={'C1': ['L102D_arg_7 LC1_arg_1'], '102A': ['L102D_arg_1 L102A_arg_1']}:
  #  bp()
  for tag,line_num in zip(tags,src_line_nums):
    if tag < minest:
       minest=tag
       source_line_num[line_num]=src_line_nums[line_num]
    elif tag==minest:
       if line_num in source_line_num:
        for element in src_line_nums[line_num]:
         source_line_num[line_num].append(element)
       else:
         source_line_num[line_num]=src_line_nums[line_num]       
    else:#tag > minest:
       if line_num in source_line_num:
        for element in src_line_nums[line_num]:
         source_line_num[line_num].append(element)
       else:
         source_line_num[line_num]=src_line_nums[line_num]     
      

  for idx in range(len(output_values_tag)):
    if output_values_tag[idx] in tags:
      output_values_tag[idx]=minest
  return minest,source_line_num    
          
  
#Finds all the dependent traces of the current trace line line_idx.
'''def find_all_dependent_traces(line_idx,traces,lines_group_tag):  
  idx=line_idx
  output_bag=[]#store the output values.
  dependent_lines=[idx]#store all the dependent line number in the trace.
  intersting_args=extract_single_trace_interesting_args(traces[idx])  
  for arg in intersting_args:
    output_bag.append(arg)
  idx-=1
  if len(output_bag)==0:
     return "no",None,[]
  elif len(output_bag)==1:
     if output_bag[0]=='0':
       return "no",None,[]
     elif output_bag[0].startswith("FF"):
       return "no",None,[]  
  
  while len(output_bag)>0 and idx>=0:
    print("find_all_dependent_traces idx=",idx)
    #if "600A :121A( C03B6, )  ret: 0 TID: 131C" in traces[idx]:
    #  bp()
    if not is_trace(traces[idx]):#skip non-trace lines such as separator lines for every 32 logs
      idx-=1
      continue
    if contains_interesting_in_arg(traces[idx],output_bag):
      if lines_group_tag[idx]!=-1:#If the line has a belonging group, we need to merge the current dependent lines with that.
        return "add",lines_group_tag[idx],dependent_lines
      
      intersting_args=extract_single_trace_interesting_args(traces[idx])  
      for arg in intersting_args:
         if arg not in output_bag:
           output_bag.append(arg)
      dependent_lines.append(idx)  
    else:
      out_args=contains_interesting_out_arg(traces[idx],output_bag)  
      if len(out_args)>0:#If we find the source trace generating the interesting arg.
      
         if lines_group_tag[idx]!=-1:#If the line has a belonging group, we need to merge the current dependent lines with that.
           return "add",lines_group_tag[idx],dependent_lines
           
         #We first delete that interesting args in the bag.
         for arg in out_args:
             output_bag.remove(arg)       
         #Next further explore whether this trace log contains any interesting in args
         intersting_args=extract_single_trace_interesting_args(traces[idx])  
         for arg in intersting_args:
           if arg not in output_bag:
             output_bag.append(arg)
         dependent_lines.append(idx)
    idx-=1  
  return "new",None,dependent_lines  '''
      
def extract_single_trace_interesting_args(line_trace):
  interesting_args=[]
  args=line_trace[line_trace.find('(')+1:line_trace.find(')')].split(',')
  args = list(filter(None, args))
  for arg in args:
    arg=arg.strip()
    if not_entities(arg,line_trace) and len(arg)>=6 and (not arg.startswith('FF')):#We assume the value with 6 digits and not having memory record in logs as interesting value we want to find source ourput. This excludes the value like 0, ffffff, 12, etc.
      interesting_args.append(arg)
  return interesting_args  

def not_entities(arg,line_trace):
  memory_str=line_trace[line_trace.find("small array:"):]
  if arg+": " in memory_str:
    return False
  else:
    return True 

def contains_interesting_in_arg(line_trace,intersting_args_bag):
  # First, we find whether the syscall contains same interesting arg
  args=line_trace[line_trace.find('(')+1:line_trace.find(')')].split(',')
  args = list(filter(None, args))
  for arg_i in range(len(args)):
    args[arg_i]=args[arg_i].strip()
    
  for arg in intersting_args_bag:
    if arg in args:
      return True
      
def contains_interesting_out_arg(line_trace,intersting_args_bag):  
  out_args=[]
  #Check whether ret value is interesting
  ret=line_trace[line_trace.find('ret:')+4:line_trace.find('TID')]
  ret=ret.strip()
  if ret in intersting_args_bag:
    out_args.append(ret)
    
  #Next check whether out entities is interesting
  out_entity=line_trace[line_trace.find("out entries:")+12:line_trace.find("strings:")]  
  for arg in intersting_args_bag:
    if arg in out_entity:
      out_args.append(arg)
  out_args = list(dict.fromkeys(out_args))    
      
  return out_args  

'''def not_init_func(line_trace):  
  args=line_trace[line_trace.find('(')+1:line_trace.find(')')].split(",")
  args = list(filter(None, args))
  if len(args)==1:
    if args[0].strip()=="0":
      return False
  elif len(args)==0:
      return False  
  return True    '''
  
def is_trace(line):
  if line.find("ret:")!=-1 and line.find("TID:")!=-1:
    return True
  return False
  
group_traces()