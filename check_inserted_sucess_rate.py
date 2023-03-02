from library import extract_src_dict, extract_result, extract_trace_num,create_result_table_by_trace_line
from pdb import set_trace as bp

#Calculates how many mutated (inserted) syscalls are called successfully.
def main():
  inserted_result=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\notepad_synthesized_inserted_L3_result.txt"
  f=open(inserted_result,'r')
  content=f.read()
  result_lines=content.split("\n")
 
  log_path=r"C:\Users\nuc\Downloads\NTFuzz_logs\notepad_log.txt"
  f1=open(log_path,'rb')
  content=f1.read().replace("\x00",'')
  log_lines=content.split("\n")
  
  
  log_trace_num_result_dic=create_result_table_by_trace_line(log_lines)
  total_match1=0
  total_inserted1=0
  total_match2=0
  total_inserted2=0
  total_match3=0
  total_inserted3=0
  keyword1="inserted_L0_ret"
  keyword2="inserted_L1_ret"
  keyword3="inserted_L2_ret"
  for line in result_lines:
    if line.startswith("('"+keyword1):
      total_inserted1+=1
      line_str=line[1:-1]
      ret=line_str.split(",")[0].strip("'")
      value=line_str.split(",")[1].strip()
      trace_num=line_str.split(",")[0].strip("'").split(keyword1)[-1]
      match=find_same_result_by_tracenum(value,trace_num,log_trace_num_result_dic)
      #print("0")
      total_match1+=match
    elif line.startswith("('"+keyword2):
      total_inserted2+=1
      line_str=line[1:-1]
      ret=line_str.split(",")[0].strip("'")
      value=line_str.split(",")[1].strip()
      trace_num=line_str.split(",")[0].strip("'").split(keyword2)[-1]
      match=find_same_result_by_tracenum(value,trace_num,log_trace_num_result_dic)
      #print("0")
      total_match2+=match
    elif line.startswith("('"+keyword3):
      total_inserted3+=1
      line_str=line[1:-1]
      ret=line_str.split(",")[0].strip("'")
      value=line_str.split(",")[1].strip()
      trace_num=line_str.split(",")[0].strip("'").split(keyword3)[-1]
      match=find_same_result_by_tracenum(value,trace_num,log_trace_num_result_dic)
      #print("0")
      total_match3+=match 
  print("match rate1:",(total_match1*1.0)/total_inserted1) 
  print("match rate2:",(total_match2*1.0)/total_inserted2)  
  print("match rate3:",(total_match3*1.0)/total_inserted3)
  total_match=total_match1+total_match2+total_match3
  total_inserted=total_inserted1+total_inserted2+total_inserted3
  print("match rate:",(total_match*1.0)/total_inserted)
  
#Find whether the inserted (mutated) trace has the same return result as where we learnt from the trace.
def find_same_result_by_tracenum(value,trace_num,log_trace_num_result_dic):
   log_ret=log_trace_num_result_dic[trace_num]
   match=0
   if log_ret==value:
     match= 1
     #print("match",trace_num,log_ret,value)       
   else:
     if log_ret.startswith("800") and len(log_ret)==8:#both are error
       if value[0]=='-':
         #print("both error",trace_num,log_ret,value)
         match= 1
     elif log_ret.startswith("C00") and len(log_ret)==8:#both are error   
       if value[0]=='-':
         #print("both error",trace_num,log_ret,value)
         match= 1
     elif log_ret!='0' and value[0]!='-' and value!='0':#both are positive value (i.e., handle)
         #print("both positive constant",trace_num,log_ret,value)
         match=1         
     else:
        print("mismatch",trace_num,log_ret,value)            
   return match
     
     
def is_trace(line):
  if line.find("ret:")!=-1 and line.find("TID:")!=-1:
    return True
  return False  
  
  
 
  
main()  