from pdb import set_trace as bp

def main():
 #result_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\simulate_result.txt" 
 result_path=r"C:\Users\nuc\Downloads\NTFuzz_logs\dxdiag_result.txt"
 f=open(result_path,'r')
 content=f.read()
 result_lines=content.split("\n")
 
 log_path=r"C:\Users\nuc\Downloads\NTFuzz_logs\dxdiag_log.txt"
 f1=open(log_path,'rb')
 content=f1.read().replace("\x00",'')
 log_lines=content.split("\n")
 absolute_log_line_num=0#A global variable to record which line in the log we have already reached.
 
 total_match=0
 for line in result_lines:
   if line.startswith("('ret"):
     line_str=line[1:-1]
     ret=line_str.split(",")[0].strip("'")
     value=line_str.split(",")[1].strip()
     absolute_log_line_num,match=find_by_tracenum(ret,absolute_log_line_num,log_lines,value)
     total_match+=match
     print(absolute_log_line_num)
 print("match rate:",(total_match*1.0)/len(result_lines))  
   
#Find forwardly to locate the trace in log_lines that records the trace num same as ret. Update the absolute_log_line_num and check whether the return value same or not
def find_by_tracenum(ret,absolute_log_line_num,log_lines,value):
   trace_num=ret[3:]
   match=0
   for i in range(absolute_log_line_num,len(log_lines)):
     if is_trace(log_lines[i]):
       log_trace_num=log_lines[i][:log_lines[i].find(":")]
       if log_trace_num==trace_num:
         start_index=log_lines[i].find("ret:")
         end_index=log_lines[i].find(" ",start_index)
         log_ret_value=log_lines[i][start_index+4:end_index]
         if log_ret_value==value:
           #print("equal",trace_num,log_ret_value,value)
           match= 1
         else:
           if log_ret_value.startswith("800") and len(log_ret_value)==8:#both are error
             if value[0]=='-':
               #print("both error",trace_num,log_ret_value,value)
               match= 1
           elif log_ret_value.startswith("C00") and len(log_ret_value)==8:#both are error   
             if value[0]=='-':
               #print("both error",trace_num,log_ret_value,value)
               match= 1
           elif log_ret_value!='0' and value[0]!='-' and value!='0':#both are positive value (i.e., handle)
               #print("both positive constant",trace_num,log_ret_value,value)
               match=1         
           else:
              print("mismatch",trace_num,log_ret_value,value)            
         return i,match
     
     
def is_trace(line):
  if line.find("ret:")!=-1 and line.find("TID:")!=-1:
    return True
  return False  

main()  