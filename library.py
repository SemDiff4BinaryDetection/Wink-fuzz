from pdb import set_trace as bp

def is_trace(line):
  if line.find("ret:")!=-1 and line.find("TID:")!=-1:
    return True
  return False  
  
#Extract the string content after the "taint src:" as a dictionary structure             
def extract_src_dict(line): 
  result_dict={}
  start_index=line.find("taint src: ")
  left_bracket_index=line.find("{",start_index)
  right_bracket_index=line.find("}",start_index)
  string_content=line[left_bracket_index:right_bracket_index+1]
  if string_content=='{}':#Has no dependent syscall
    return result_dict
  if string_content.find("],")!=-1:#If contains more than 1 item (dependent argument), we should ignore the case.
    return result_dict
  key=string_content.split(":")[0][2:-1]
  dependent_str=string_content.split(":")[1][:-1].strip()

  if dependent_str=="[]":
    return result_dict
  left_bracket=dependent_str.find("[")
  right_bracket=dependent_str.find("]")
  value_str=dependent_str[left_bracket+1:right_bracket] 
  
  values=value_str.split(",")
  result_dict[key]=[]
  for value in values:  
    try:
      begin_quota_idx=value.find("'")
      end_quote_idx=value.find("'",begin_quota_idx+1)
      result_dict[key].append(value[begin_quota_idx+1:end_quote_idx])
    except:
      bp()    
  return result_dict  
  
#Create a table indexing each trace num. Key is the trace num in the trace. Value is the return value.
def create_result_table_by_trace_line(trace_lines):
  print("--------------------------create result table-----------------------------")
  result_table={}
  for line_i in  range(len(trace_lines)):
    if not is_trace(trace_lines[line_i]):
      continue
    result=extract_result(trace_lines[line_i])
    trace_num=extract_trace_num(trace_lines[line_i])
    print(line_i)
    result_table[trace_num]=result

  return result_table     
  
def extract_syscall(line):  
  syscall_hex_str=line.split("ret:")[0].split("(")[0].split(":")[-1]  
  return syscall_hex_str
  
def extract_result(line):  
  ret_str=line.split("ret:")[1].split(" ")[0]
  return ret_str  
  
def extract_trace_num(line):
  sub_str=line.split("ret:")[0]
  first_colon_index=sub_str.rfind(":")
  first_bracket=sub_str.rfind("}",0,first_colon_index)
  trace_num=sub_str[first_bracket+1:first_colon_index].strip()  
  return trace_num
  
#Read the table of syscall. Each syscall num mapps to a syscall name                  
def read_syscall_table(syscall_table_path,syscall_table):
  f=open(syscall_table_path,'r')
  lines=f.read().split("\n")
  for line in lines:
    if line.strip()=="":
      continue
    elements=line.split(" ")
    elements = list(filter(None, elements))
    syscall_table[int(elements[0])]=elements[1]  

  return syscall_table  
  