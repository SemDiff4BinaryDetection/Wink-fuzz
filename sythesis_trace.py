from pdb import set_trace as bp
from library import is_trace, extract_trace_num,extract_syscall,read_syscall_table
import json

syscall_table={}
line_map={}#A list that maps between the line num and the trace num. Trace num is the number of single trace already recorded in the log. Line num include non-tracing lines and null lines.
syscall_json=None

deleted_trace_num=[]#A list recording the trace num that we deleted because their existance can cause wired python errors.

def synthesize():
  global line_map
  global deleted_trace_num
  global syscall_table
  logged_trace=r"C:\Users\nuc\Downloads\NTFuzz_logs\new_awatch_log_dependency.txt"
  f=open(logged_trace,'rb')
  content=f.read()
  lines=content.split('\r')
  maximum=1000#Maximum trace number for each iteration
  out_file=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\new_awatch_synthesized.py"
  
  syscall_table_path=r"C:\Users\nuc\Desktop\ntfuzz+\windows10_17134_syscall_table.txt"
  #read_syscall_table(syscall_table_path)
  syscall_table=read_syscall_table(syscall_table_path,syscall_table)
  
  syscall_json_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Debug\Types.json"
  read_syscall_json(syscall_json_path)
  
  out_str="from ctypes import *\nimport ctypes\nfrom sys import getsizeof\nfrom pdb import set_trace as bp\nfrom ctypes.wintypes import *\nimport argparse\nfrom structs_define import* \nwin32u=windll.LoadLibrary('win32u.dll') \nntdll=windll.LoadLibrary('ntdll.dll')\n"
  line_count=0
  absolute_line_num=0
  
  #create synthesized file again.
  f=open(out_file,'w')
  f.write("")
  f.close()
  
  
  for line_i in range(len(lines)):
    if is_trace(lines[line_i]):
      trace_num=extract_trace_num(lines[line_i])
      #if absolute_line_num==3360 or absolute_line_num==4822 or absolute_line_num==5107 or absolute_line_num==7596:
      #  absolute_line_num+=1
      #  continue  
      #if trace_num in ['A564','7DD8','5AE7','5A91','4065','3552','3453','31DB','3167','3160','30E3','2A3A','2A3B','2A3C','2A3D','2A3E','2A29','2A28','2A25','2899','2892','2885','288C','2893','289A','28A0','28A1','28A8','28A6','28A9','288B','2878','2829','282A','282B','282C','282D','2815','2817','2818','1EBC','1EA3','1918','1917','1916','1915','1914','1913','18AB','18A7','18A8','18A9','18AA','189C','189A','1899','14E7','128B','107A','105F','1057','EB2','90C','8A0','89F','89E','89D','89C','89B','89A','41A','348']:
      #  deleted_trace_num.append(trace_num)
      #  continue
      if (logged_trace.find("wordpad")!=-1) and (trace_num in ['3124','311D','107a','1057','105f','90C','348']):
        deleted_trace_num.append(trace_num)
        continue
      elif (logged_trace.find("dxdiag")!=-1) and (trace_num in ['348','55A','55B','6D4','B5A','B5B','BC0','10E4','10EA','10EB','10ED','10EF','10F2','10FD','10FF','115D','115E','1B09','1B17','1B48','1B4A','1B4B','1B4F','1B50','1B64','1B65','1B67','1BFA','1C10','1C11','1C1A','1C1B','1C1E','1C1F','1C22','1C23','1C26','1C27','1C2B','1C2C','1C2F','1C30','1C34','1C35','1C38','1C39','1C3C','1C3D','1C40','1C41','1C45','1C46','1C49','1C4A','1C50','1C51','1C7B','1C7C','1C95','1C99','1C9A','1C9D','1CA6','1CA7','1CAB','1CAC','1CB0','1CB1','1CB5','1CB6','1CBA','1CBB','1CBF','1C0E','1CC0','1CEA','1CEB','1D15','1D16','1D1A','1D1B','1D1F','1D20','1D24','1D25','1D29','1D2A','1D2E','1D2F','1D33','1D34','1D38','1D39','1D8F','1D92','1D98','1D9A','1DA7','1DB4','1DC2','1DC5','1DDA','1DDD','1DE2','1DE4','1DF1','1DF3','1E78','1E7B','277D','27DD','2AD7','2ADA','2AFA','2B2E','2B31','2B51','2DFC','2E14','2E15','2E39','2E3B','2E3C','2E45','2E46','2E49','2E4A','2E4D','2E4E','2E54','2E58','2E5A','2E5C','2E5E','2E5F','2E61','2E66','2E70','2E72','2E73','2E7C','2E7D','2E80','2E81','2E84','2E85','2E8B','2E8C','2E8E','2E90','2E92','2E93','2E95','2E9A','2EA3','2EA5','2EA6','2EAF','2E80','2EB0','2EB3','2EB4','2EB7','2EB8','2EBE','2EBF','2EC1','2EC3','2EC5','2EC6','2EC8','2ECD','2F0E','2F39','2F68','2F81','2F83','2F84','2F8D','2F8E','2F91','2F92','2F95','2F96','2F9C','2F9D','2F9F','2FA1','2FA3','2FA4','2FA6','2FAB','2FB1','2FB2','2FB9','2FBB','2FBC','2FC0','2FC1','2FC4','2FC5','2FC9','2FCA','2FCE','2FCF','2FD6','2FD8','2FD9','2FDD','2FDE','2FE5','2FE7','2FE8','2FEC','2FED','2FF0','3052','3053','30A7','30AB','30AD','30B0','30D1','30D7','30D9','30DB','30E4','30E6','30F2','30F4','3100','3102','310E','3110','311C','311E','312A','312D','3133','31FA','3203','3205','3208','3211','3213','3215','3217','3219','321B','321D','321F','3221','3223','3225','3227','322A','322D','3230','3233','3236','3239','323C','323F','3242','3245','3268','3273','3276','3294','3299','329A','32BA','32C8','32CB','32E0','32E3','3317','331A','3334','3335','3338','3582','35A5','35AC','35B9','35C0','35C4','35C6','35EA','35EB','35ED','35EF','35F2','35F3','35F5','35F7','35FA','35FB','35FD','35FF','3602','360E','361B','361D','3623','363B','363E','364B','375E','375F','3761','3763','389F','38A5','38A6','38B4','38BC','38C0','38C4','38C5','38C8','38C9','38CA','38CB','38CD','38D1','38D5','38DA','38DD','38DF','38FD','390D','390F','3910','3912','3914','3915','391B','393E','3944','3945','3963','3965','3969','3971','3975','3976','39B2','39B3','39B8','39B9','39BA','39BB','39C2','39C3','39C8','39D1','39D2','39D3','39F0','39F2','39F3','39F8','39F9','39FA','39FB','3A10','3A1A','3A1B','3A20','3A21','3A28','3A30','3A31','3A32','3A33','3A38','3A39','3A3A','3A3B','3A40','3A41','3A7B','3A7C','3A7D','3A84','3A85','3A87','3Z88','3A8B','3A8C','3A8D','3A8E','3A8F','3A90','3A91','3A94','3A95','3A96','3A98','3A99','3A9A','3A9B','3A9D','3A9E','3A9F','3AA0','3AA5','3AA6','3AA7','3AA8','3AA9','3AAA','3AAB','3AAF','3AB0','3AB1','3AB2','3AB3']):
        deleted_trace_num.append(trace_num)
        continue 
      elif (logged_trace.find("notepad")!=-1) and (trace_num in ['5B6','5B7','71F','917','A5C','D50','E88','11BD','11C5','11CF','11D7','1258']):
        deleted_trace_num.append(trace_num)
        continue       
      elif (logged_trace.find("awatch")!=-1) and (trace_num in ['C8','18E','1EA','342','7ED','7F3','12B3','12D5','12DF','12E7','20E6','2138']):
        deleted_trace_num.append(trace_num)
        continue         
      #elif trace_num=='582E':
      #  bp()      
      line_map[absolute_line_num]=trace_num
      synthesized=synthesize_single_trace(lines[line_i],trace_num,logged_trace)
      line_count+=1
      absolute_line_num+=1
      out_str+=synthesized
      if line_count==maximum:
        out_str.replace(r"\x",r"\\x")
        append2file(out_str,out_file)
        line_count=0
        out_str=""
        continue
      elif line_i==len(lines)-2:#If reaches the end of the trace but not enough traces, we still write them into file
        out_str.replace(r"\x",r"\\x")
        append2file(out_str,out_file)
        line_count=0
        out_str=""
        continue 
      print("absolute_line_num:",absolute_line_num,"trace_num:",trace_num)

  
    
def extract_single_trace_args(line_trace):
  args=line_trace[line_trace.find('(')+1:line_trace.find(')')].split(',')
  args = list(filter(None, args))
  for arg_i in range(len(args)):
   args[arg_i]=args[arg_i].strip()
  return args 
  
#For a single trace line, we generate the cython code that mimic this trace's behaviour.
def synthesize_single_trace(line,trace_num,logged_trace):
   global syscall_json
   global deleted_trace_num
   max_string_len=0x1000
   syscall_hex_str=extract_syscall(line)
   arg_values=extract_single_trace_args(line)
   dependent_args=find_dependent_args_source(line)
   #if syscall_hex_str=="155" or syscall_hex_str=="1207" or syscall_hex_str=="160" or syscall_hex_str=="1204" or syscall_hex_str=="1220" or syscall_hex_str=="1061" or syscall_hex_str=="10DC" or syscall_hex_str=="1009":
   #  return ""     
   syscall,arg_types,arg_widths,in_outs=find_syscall(syscall_hex_str) 
   
   #Below are concluded from wordpad traces
   if syscall=="win32u!NtUserGetAtomName" or syscall=="win32u!NtUserCallOneParam" or syscall=="win32u!NtUserPeekMessage" or syscall=="win32u!NtUserGetCursorDims" or syscall=="win32u!NtUserCallTwoParam" or syscall=="win32u!NtUserCallNoParam" or syscall=="win32u!NtUserCallHwnd" or syscall=="win32u!NtUserCallHwndLock" or syscall=="win32u!NtUserCallHwndParamLock" or syscall=="win32u!NtGdiGetTextFaceW" or syscall=="ntdll!NtWaitForAlertByThreadId" or syscall=="ntdll!NtCreateThreadEx":#These syscall's existence lead to fatal error that pauses the script execution. Thus we must exclude them.
     deleted_trace_num.append(trace_num)
     return ""
   elif syscall=="win32u!NtUserCreateAcceleratorTable" or syscall=="win32u!NtGdiDoPalette":#These syscalls include array of structs. We have not yet implement auto-generation for this type. And their occurance time is very few, and there is no following syscalls depending on them.
     deleted_trace_num.append(trace_num)
     return ""
   arg_num=1
   args_list=[]#A list of arg strings that will be concatenated together in the end to form a syscall with args.
   cython_str=""
   #if trace_num=='137F':
   #      bp()
   for arg_type,arg_value,arg_width,in_out in zip(arg_types,arg_values,arg_widths,in_outs):
     if arg_value=='0':
       args_list.append("0")  
     elif arg_type[0]=="scalar":
       if (arg_num) in dependent_args:#Firstly check whether the value is a dependent value
         if dependent_args[arg_num][3:] in deleted_trace_num:#If the referenced value is not generated due to avoiding error, we use the constant then.
           pass
         else:  #If the referenced value exists in the previously synthesized cython.
           cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"="+dependent_args[arg_num]+"\n"
           args_list.append("L"+str(trace_num)+"_arg_"+str(arg_num))  
           arg_num+=1  
           continue
       if arg_width[0]==1:
         cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_byte(0x"+arg_value+")\n"
       elif arg_width[0]==2:
         cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_ushort(0x"+arg_value+")\n" 
       elif arg_width[0]==4:
         cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_ulong(0x"+arg_value+")\n" 
       elif arg_width[0]==8:
         cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_longlong(0x"+arg_value+")\n"   
       else:
         print("Did not expect this case!")
         bp()
       args_list.append("L"+str(trace_num)+"_arg_"+str(arg_num))  
     elif arg_type[0]=="handle":           
       handle_value=None
       if arg_num=="0" or arg_num=="FFFFFFFF":#If the handle value is spetial constant, just copy this constant
         handle_value="0x"+arg_value     
       elif (arg_num) in dependent_args:#Have the expected dependent handle in previous trace.
         handle_value=dependent_args[arg_num]
         if handle_value.startswith("ret"):
           if handle_value[3:] in deleted_trace_num:#If the referenced value is not generated due to avoiding error, we also ignore this syscall too.
             deleted_trace_num.append(trace_num)
             return ""
         elif handle_value.startswith("L"):
           dependent_trace_line=handle_value.split("_")[0].split("L")[1]
           if dependent_trace_line in deleted_trace_num:#If the referenced value is not generated due to avoiding error, we also ignore this syscall too.
             deleted_trace_num.append(trace_num)
             return ""         
       else:#Expect to have dependent handle but only have constant.
         handle_value="0x"+arg_value      
       cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"="+handle_value+"\n"      
       args_list.append("L"+str(trace_num)+"_arg_"+str(arg_num))  
     elif arg_type[0]=="ptr":         
       if arg_type[1]=="struct":
           if in_out=="in" or in_out=="inout":
             if len(arg_value)>=6:#If the arg value is indeed a memory address
                 '''if arg_num in dependent_args:#If the ptr to struct the ptr is dependent on previous ptr 
                 args_list.append(dependent_args[arg_num]) 
              
                 else:#If the ptr to struct has no dependency to previous ptr   '''        
                 struct_name=get_struct_name(syscall,arg_num,0)
                 cython_str+=prepare_struct_arg_value(line,trace_num,arg_num,arg_value,syscall,struct_name)
                 args_list.append("byref(struct_"+str(trace_num)+"_arg_"+str(arg_num)+"_0)")
             else:#If the arg value is expected to be a memory address according to types.json, but in the trace it records a constant.
               args_list.append("0x"+arg_value)
                            
           else:
             struct_name=get_struct_name(syscall,arg_num,0)
             cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"="+struct_name+"()\n"
             #cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=(c_ulong*0x100)()\n"
             args_list.append("byref("+"L"+str(trace_num)+"_arg_"+str(arg_num)+")")
       elif arg_type[1]=="scalar":
           ptr_content_value=find_ptr_content_value(line,arg_value)
           if ptr_content_value=='':
             ptr_content_value='0'
           ptr_content_width=arg_width[1]
           if ptr_content_width==1:
              cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_byte(0x"+ptr_content_value+")\n"
           elif ptr_content_width==2:
              cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_ushort(0x"+ptr_content_value+")\n" 
           elif ptr_content_width==4:
              cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_ulong(0x"+ptr_content_value+")\n" 
           elif ptr_content_width==8:
              cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_longlong(0x"+ptr_content_value+")\n"   
           else:
              bp()           
           args_list.append("byref("+"L"+str(trace_num)+"_arg_"+str(arg_num)+")")     
       elif arg_type[1]=="handle":
           if in_out=="in": 
             #args_list.append("byref("+dependent_args[arg_num]+")")    
             #If dependence is byref (current arg is the previous variable's memory address), then the dependent_args[arg_num] should already contain byref() because we processed it beforehand. If it is not byref, then dependent_args[arg_num] should also not contain byref.         
             args_list.append(dependent_args[arg_num])              
           else:
             ptr_content_width=arg_width[1]
             if ptr_content_width==1:
               cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_byte()\n"
             elif ptr_content_width==2:
               cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_ushort()\n"
             elif ptr_content_width==4:
               cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_ulong()\n"
             elif ptr_content_width==8:
               cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_longlong()\n"
             else:
               bp() 
             args_list.append("byref("+"L"+str(trace_num)+"_arg_"+str(arg_num)+")")           
       elif arg_type[1]=="array":
           #ptr_content_value=find_ptr_content_value(line,arg_value)
           if in_out=="in":
             #if "36DE:1009( 52010990, D7BC74, D7BC74, 1, 80000000, )  ret:1 TID:108C small array: large array: in entrie" in line:
             #  bp()
             array_content=find_ptr_content_value(line,arg_value)
             if array_content=="#" or array_content=="":#If expected to record value but no value in record
               array_json=syscall_json[syscall]["arg"+str(arg_num)]["content"]
               array_num=0
               #cython_str+=prepare_array(array_content,count,absolute_line_num,array_num,array_json)
               cython_str+=prepare_array_arg_value_by_type(line,trace_num,arg_num,array_num,arg_values,array_json,syscall)
               args_list.append("byref("+"L"+str(trace_num)+"_arg"+str(arg_num)+"_array_"+str(array_num)+")")
             else:
               #if absolute_line_num==1806:
               #  bp()
               #if "2B22:110B( CA9F00, 25, )  ret:410421" in line:
               #    bp()
               cython_str+=prepare_array_arg_value_by_trace(line,trace_num,arg_num,arg_value,syscall)             
               array_num=0
               args_list.append("byref("+"L"+str(trace_num)+"_arg"+str(arg_num)+"_array_"+str(array_num)+")")
           else:
             #if " group: 10 taint src: {'8D': ['L8E_arg_1 L8D_arg_2']} 8E:B6( 7C, 27, 0, 0, D7EF8C, )  ret:C0000023" in line:
             #  bp()
             #array_content,count=find_array(line,arg_value)
 
             array_json=syscall_json[syscall]["arg"+str(arg_num)]["content"]
             array_num=0
             #cython_str+=prepare_array(array_content,count,absolute_line_num,array_num,array_json)
             cython_str+=prepare_array_arg_value_by_type(line,trace_num,arg_num,array_num,arg_values,array_json,syscall)
             #cython_str+="L"+str(absolute_line_num)+"_arg_"+str(arg_num)+"=create_string_buffer('/0'*"+str(ptr_content_width)+")\n"
             args_list.append("byref("+"L"+str(trace_num)+"_arg"+str(arg_num)+"_array_"+str(array_num)+")")
       elif arg_type[1]=="stringw":
           if in_out=="in":
            #print(line)
            #bp()
            #str_width_str=raw_input("I am confused about the string length. Please help me figure out:")
            #str_width=int(str_width_str,16)
            str_width=-1
            string_value=find_string_value(line,arg_value)
            if string_value!="":#If really has string value in the trace.
              str_code=recode_str(string_value,str_width)
              cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_char_p('"+str_code+"')\n"
              args_list.append("byref("+"L"+str(trace_num)+"_arg_"+str(arg_num)+")")  
            else:
              cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_char_p(' '*0x"+str(max_string_len)+")\n"
              args_list.append("byref("+"L"+str(trace_num)+"_arg_"+str(arg_num)+")")       
           else:
            cython_str+="L"+str(trace_num)+"_arg_"+str(arg_num)+"=c_char_p(' '*0x"+str(max_string_len)+")\n"
            args_list.append("byref("+"L"+str(trace_num)+"_arg_"+str(arg_num)+")")               
       elif arg_type[1]=="ptr":
         if syscall=="win32u!NtGdiCreateDIBSection" and arg_num==9:
           args_list.append("0") 
         else:  
           print("Did not expect this case!")
           bp()
       elif arg_type[1]=="funcptr":
         print("Did not expect this case!")
         bp()
       else:
         print("Did not expect this case!")
         bp()
     #elif arg_type[0]=="array":
     #  if arg_type[1]=="fixed":
     #  elif arg_type[1]=="argfield":
     #  elif arg_type[1]=="adjacentfield":
     #  elif arg_type[1]=="unknown":
     elif arg_type[0]=="funcptr":
       if arg_value=='0':
         args_list.append("0")  
       else:  
         args_list.append("0x"+arg_value)  
         #print("Did not expect this case!")
         #bp()
     #elif arg_type[0]=="struct":
     else:
       print("Did not expect this case!")
       bp()
     arg_num+=1  
   
   cython_str+="ret"+trace_num+"="+syscall.replace("!",".")+"("

   #Now we rectify for specific syscalls.
   
   #Below are concluded from wordpad traces
   if logged_trace.find("wordpad")!=-1:
     if syscall == "ntdll!NtQuerySystemInformation":
       replace_arg_name="L"+trace_num+"_arg_2"
       start_index=cython_str.find(replace_arg_name)
       end_index=cython_str.find("\n",start_index)
       cython_str=cython_str[:start_index]+replace_arg_name+"=(c_ulong*0x100)()\n"+cython_str[end_index+1:]
       args_list[1]="byref("+replace_arg_name+")"
     elif syscall == "ntdll!NtQueryAttributesFile": 
       keyword="struct_"+trace_num+"_arg_1_0.reserve2="
       start_index=cython_str.find(keyword)+len(keyword)
       end_index=cython_str.find("c_char_p(")
       cython_str=cython_str[:start_index]+cython_str[end_index:]
     elif syscall == "ntdll!NtQueryInformationProcess":
       keyword="L"+trace_num+"_arg_3=c_ulong("
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_3[0]="+value+cython_str[end_index+1:] 
     elif syscall == "ntdll!NtQuerySecurityObject":  
       keyword="L"+trace_num+"_arg_3="
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]
     elif syscall=="win32u!NtUserSystemParametersInfo":
       keyword="L"+trace_num+"_arg_3=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_3[0]="+value+cython_str[end_index+1:]
     elif syscall=="win32u!NtGdiGetCharABCWidthsW":    
       keyword="L"+trace_num+"_arg_6=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_6=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_6[0]="+value+cython_str[end_index+1:]
     elif syscall=="win32u!NtGdiGetOutlineTextMetricsInternalW":
       keyword="L"+trace_num+"_arg_3=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]   
       else:
         keyword="L"+trace_num+"_arg_3=NtGdiGetOutlineTextMetricsInternalW_arg3_struct0"
         start_index=cython_str.find(keyword)  
         if start_index!=-1:     
           end_index=cython_str.find(")\n",start_index)
           value=cython_str[start_index+len(keyword):end_index]
           cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]         
     elif syscall=="ntdll!NtQueryWnfStateData":
       keyword="struct"+trace_num+"_arg_5_0="  
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"struct"+trace_num+"_arg_5_0=(c_ulong*0x100)()"+cython_str[end_index+1:] 
   elif logged_trace.find("dxdiag")!=-1:#Below are concluded from dxdiag traces.     
     if syscall == "ntdll!NtQuerySystemInformation":
       replace_arg_name="L"+trace_num+"_arg_2"
       start_index=cython_str.find(replace_arg_name)
       end_index=cython_str.find("\n",start_index)
       cython_str=cython_str[:start_index]+replace_arg_name+"=(c_ulong*0x100)()\n"+cython_str[end_index+1:]
       args_list[1]="byref("+replace_arg_name+")"
     elif syscall == "ntdll!NtQueryInformationProcess":
       keyword="L"+trace_num+"_arg_3=c_ulong("
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_3[0]="+value+cython_str[end_index+1:] 
     elif syscall == "ntdll!NtQuerySecurityObject":  
       keyword="L"+trace_num+"_arg_3="
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]
     elif syscall=="win32u!NtUserSystemParametersInfo":
       keyword="L"+trace_num+"_arg_3=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_3[0]="+value+cython_str[end_index+1:]
     elif syscall=="win32u!NtGdiGetCharABCWidthsW":    
       keyword="L"+trace_num+"_arg_6=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_6=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_6[0]="+value+cython_str[end_index+1:]
     elif syscall=="win32u!NtGdiGetOutlineTextMetricsInternalW":
       keyword="L"+trace_num+"_arg_3=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]   
       else:
         keyword="L"+trace_num+"_arg_3=NtGdiGetOutlineTextMetricsInternalW_arg3_struct0"
         start_index=cython_str.find(keyword)  
         if start_index!=-1:     
           end_index=cython_str.find(")\n",start_index)
           value=cython_str[start_index+len(keyword):end_index]
           cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]         
     elif syscall=="ntdll!NtDeviceIoControlFile":
       keyword="NtDeviceIoControlFile_arg5_struct0"  
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()"+cython_str[end_index+1:] 
     elif syscall=="ntdll!NtQueryAttributesFile":
       keyword="struct_"+trace_num+"_arg_1_0.reserve2="
       start_index=cython_str.find(keyword)+len(keyword)
       end_index=cython_str.find("c_char_p(")
       cython_str=cython_str[:start_index]+cython_str[end_index:]
       
       keyword="NtQueryAttributesFile_arg2_struct0"  
       start_index=cython_str.find(keyword)   
       arg_2_start_idx=cython_str.rfind("struct_",0,start_index)
       arg_2_struct_name=cython_str[arg_2_start_idx:start_index-1]#The index of "struct_1BE0_arg_6_0" string
       if start_index!=-1:     
         end_index=cython_str.find("_arg_2_0.reserve0=",start_index)
         value_start_idx=end_index+len("_arg_2_0.reserve0=")
         end_index=cython_str.find("\n",end_index)
         value=cython_str[value_start_idx:end_index]
         end_index=cython_str.find("\n",end_index)#refers to the next line that assigns value
         tail=cython_str[end_index:]
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()\n"
         cython_str+=arg_2_struct_name+"[0]="+value+tail
     elif syscall=="ntdll!NtQueryWnfStateData":
       keyword="NtQueryWnfStateData_arg4_struct0"  
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         end_index=cython_str.find("\n",end_index)#Find the second line that defines the value of arg4
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()"+cython_str[end_index:]
     
       keyword="NtQueryWnfStateData_arg5_struct0"  
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()"+cython_str[end_index+1:]  
     
       keyword="NtQueryWnfStateData_arg6_struct0"  
       start_index=cython_str.find(keyword)   
       arg6_start_idx=cython_str.rfind("struct_",0,start_index) 
       arg_6_struct_name=cython_str[arg6_start_idx:start_index-1]#The index of "struct_1BE0_arg_6_0" string
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value_start_idx=cython_str.find("=",end_index)
         value_end_idx=cython_str.find("\n",value_start_idx)
         value=cython_str[value_start_idx+1:value_end_idx]
         tail_str=cython_str[value_end_idx:] 
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()\n"
         cython_str+=arg_6_struct_name+"[0]="+value+tail_str         
   elif logged_trace.find("notepad")!=-1:#Below are concluded from notepad traces.     
     if syscall == "ntdll!NtQuerySystemInformation":
       replace_arg_name="L"+trace_num+"_arg_2"
       start_index=cython_str.find(replace_arg_name)
       end_index=cython_str.find("\n",start_index)
       cython_str=cython_str[:start_index]+replace_arg_name+"=(c_ulong*0x100)()\n"+cython_str[end_index+1:]
       args_list[1]="byref("+replace_arg_name+")"
     elif syscall == "ntdll!NtQueryInformationProcess":
       keyword="L"+trace_num+"_arg_3=c_ulong("
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_3[0]="+value+cython_str[end_index+1:] 
     elif syscall == "ntdll!NtQuerySecurityObject":  
       keyword="L"+trace_num+"_arg_3="
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]
     elif syscall=="win32u!NtUserSystemParametersInfo":
       keyword="L"+trace_num+"_arg_3=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_3[0]="+value+cython_str[end_index+1:]
     elif syscall=="win32u!NtGdiGetCharABCWidthsW":    
       keyword="L"+trace_num+"_arg_6=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_6=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_6[0]="+value+cython_str[end_index+1:]
     elif syscall=="win32u!NtGdiGetOutlineTextMetricsInternalW":
       keyword="L"+trace_num+"_arg_3=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]   
       else:
         keyword="L"+trace_num+"_arg_3=NtGdiGetOutlineTextMetricsInternalW_arg3_struct0"
         start_index=cython_str.find(keyword)  
         if start_index!=-1:     
           end_index=cython_str.find(")\n",start_index)
           value=cython_str[start_index+len(keyword):end_index]
           cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]     
     elif syscall=="ntdll!NtQueryAttributesFile":
       keyword="struct_"+trace_num+"_arg_1_0.reserve2="
       start_index=cython_str.find(keyword)+len(keyword)
       end_index=cython_str.find("c_char_p(")
       cython_str=cython_str[:start_index]+cython_str[end_index:]
       
       keyword="NtQueryAttributesFile_arg2_struct0"  
       start_index=cython_str.find(keyword)   
       arg_2_start_idx=cython_str.rfind("struct_",0,start_index)
       arg_2_struct_name=cython_str[arg_2_start_idx:start_index-1]#The index of "struct_1BE0_arg_6_0" string
       if start_index!=-1:     
         end_index=cython_str.find("_arg_2_0.reserve0=",start_index)
         value_start_idx=end_index+len("_arg_2_0.reserve0=")
         end_index=cython_str.find("\n",end_index)
         value=cython_str[value_start_idx:end_index]
         end_index=cython_str.find("\n",end_index)#refers to the next line that assigns value
         tail=cython_str[end_index:]
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()\n"
         cython_str+=arg_2_struct_name+"[0]="+value+tail           
     elif syscall=="ntdll!NtDeviceIoControlFile":
       keyword="NtDeviceIoControlFile_arg5_struct0"  
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()"+cython_str[end_index+1:] 
     elif syscall=="ntdll!NtQueryWnfStateData":
       keyword="NtQueryWnfStateData_arg4_struct0"  
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         end_index=cython_str.find("\n",end_index)#Find the second line that defines the value of arg4
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()"+cython_str[end_index:]
     
       keyword="NtQueryWnfStateData_arg5_struct0"  
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()"+cython_str[end_index+1:]  
     
       keyword="NtQueryWnfStateData_arg6_struct0"  
       start_index=cython_str.find(keyword)   
       arg6_start_idx=cython_str.rfind("struct_",0,start_index) 
       arg_6_struct_name=cython_str[arg6_start_idx:start_index-1]#The index of "struct_1BE0_arg_6_0" string
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value_start_idx=cython_str.find("=",end_index)
         value_end_idx=cython_str.find("\n",value_start_idx)
         value=cython_str[value_start_idx+1:value_end_idx]
         tail_str=cython_str[value_end_idx:] 
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()\n"
         cython_str+=arg_6_struct_name+"[0]="+value+tail_str 
   elif logged_trace.find("awatch")!=-1:#Below are concluded from dxdiag traces.     
     if syscall == "ntdll!NtQuerySystemInformation":
       replace_arg_name="L"+trace_num+"_arg_2"
       start_index=cython_str.find(replace_arg_name)
       end_index=cython_str.find("\n",start_index)
       cython_str=cython_str[:start_index]+replace_arg_name+"=(c_ulong*0x100)()\n"+cython_str[end_index+1:]
       args_list[1]="byref("+replace_arg_name+")"
     elif syscall == "ntdll!NtQueryInformationProcess":
       keyword="L"+trace_num+"_arg_3=c_ulong("
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_3[0]="+value+cython_str[end_index+1:] 
     elif syscall == "ntdll!NtQuerySecurityObject":  
       keyword="L"+trace_num+"_arg_3="
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]
     elif syscall=="win32u!NtUserSystemParametersInfo":
       keyword="L"+trace_num+"_arg_3=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_3[0]="+value+cython_str[end_index+1:]
     elif syscall=="win32u!NtGdiGetCharABCWidthsW":    
       keyword="L"+trace_num+"_arg_6=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_6=(c_ulong*0x100)()\n"+"L"+trace_num+"_arg_6[0]="+value+cython_str[end_index+1:]
     elif syscall=="win32u!NtGdiGetOutlineTextMetricsInternalW":
       keyword="L"+trace_num+"_arg_3=c_ulong("  
       start_index=cython_str.find(keyword)  
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value=cython_str[start_index+len(keyword):end_index]
         cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]   
       else:
         keyword="L"+trace_num+"_arg_3=NtGdiGetOutlineTextMetricsInternalW_arg3_struct0"
         start_index=cython_str.find(keyword)  
         if start_index!=-1:     
           end_index=cython_str.find(")\n",start_index)
           value=cython_str[start_index+len(keyword):end_index]
           cython_str=cython_str[:start_index]+"L"+trace_num+"_arg_3=(c_ulong*0x100)()"+cython_str[end_index+1:]         
     elif syscall=="ntdll!NtDeviceIoControlFile":
       keyword="NtDeviceIoControlFile_arg5_struct0"  
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()"+cython_str[end_index+1:] 
     elif syscall=="ntdll!NtQueryAttributesFile":
       keyword="struct_"+trace_num+"_arg_1_0.reserve2="
       start_index=cython_str.find(keyword)+len(keyword)
       end_index=cython_str.find("c_char_p(")
       cython_str=cython_str[:start_index]+cython_str[end_index:]
       
       keyword="NtQueryAttributesFile_arg2_struct0"  
       start_index=cython_str.find(keyword)   
       arg_2_start_idx=cython_str.rfind("struct_",0,start_index)
       arg_2_struct_name=cython_str[arg_2_start_idx:start_index-1]#The index of "struct_1BE0_arg_6_0" string
       if start_index!=-1:     
         end_index=cython_str.find("_arg_2_0.reserve0=",start_index)
         value_start_idx=end_index+len("_arg_2_0.reserve0=")
         end_index=cython_str.find("\n",end_index)
         value=cython_str[value_start_idx:end_index]
         end_index=cython_str.find("\n",end_index)#refers to the next line that assigns value
         tail=cython_str[end_index:]
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()\n"
         cython_str+=arg_2_struct_name+"[0]="+value+tail
     elif syscall=="ntdll!NtQueryWnfStateData":
       keyword="NtQueryWnfStateData_arg4_struct0"  
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         end_index=cython_str.find("\n",end_index)#Find the second line that defines the value of arg4
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()"+cython_str[end_index:]
     
       keyword="NtQueryWnfStateData_arg5_struct0"  
       start_index=cython_str.find(keyword)   
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()"+cython_str[end_index+1:]  
     
       keyword="NtQueryWnfStateData_arg6_struct0"  
       start_index=cython_str.find(keyword)   
       arg6_start_idx=cython_str.rfind("struct_",0,start_index) 
       arg_6_struct_name=cython_str[arg6_start_idx:start_index-1]#The index of "struct_1BE0_arg_6_0" string
       if start_index!=-1:     
         end_index=cython_str.find(")\n",start_index)
         value_start_idx=cython_str.find("=",end_index)
         value_end_idx=cython_str.find("\n",value_start_idx)
         value=cython_str[value_start_idx+1:value_end_idx]
         tail_str=cython_str[value_end_idx:] 
         cython_str=cython_str[:start_index]+"(c_ulong*0x256)()\n"
         cython_str+=arg_6_struct_name+"[0]="+value+tail_str         
             
         
   for arg in args_list:
     cython_str+=arg+","
   if cython_str[-1]==',':
    cython_str=cython_str[:-1]
   cython_str+=')\n'  
   cython_str+="print('ret"+trace_num+"',ret"+trace_num+")\n"
   #Append the memory clear cython codes
   for arg,arg_type,in_out in zip(args_list,arg_types,in_outs):
     if in_out=="in":
       if arg.startswith("byref("):
         varable=arg[6:-1]
       else:
         if arg=="0":
           continue
         varable=arg       
       #cython_str+="del "+varable+"\n"
     elif arg_type[0]=="ptr" and arg_type[1]=="array":
       if arg.startswith("byref("):
         varable=arg[6:-1]
       else:
         if arg=="0":
           continue
         varable=arg  
       #cython_str+="del "+varable+"\n"     
   cython_str+="\n"  
   return cython_str

#decode each character \x into a string starting as \x and concatenate these strings.
def recode_str(string_value,str_width):
 out_str=""
 if str_width==-1:
   pass
 else:  
   string_value=string_value[:(str_width/2)]
 for char in string_value:
   out_str+="\\x"
   digit_str=hex(ord(char))[2:]
   if len(digit_str)==1:
     digit_str="0"+digit_str
   out_str+=digit_str 
   out_str+="\\x00"
 return out_str  
   
   
#Find the string pointer's content in the trace.   
def find_string_value(line,arg_value):
   sub_str=line[line.find("strings:"):]
   str_mem=sub_str.find(arg_value+":")
   next_str_mem=sub_str.find(":",str_mem+len(arg_value)+1)
   if str_mem==-1:#not found desired string mem
     return ""  
   if next_str_mem==-1:#No next string record
     return sub_str[str_mem+len(arg_value)+1:]
   else:#Has next string record
     space_seperator=sub_str.rfind(" ",0,next_str_mem)
     return sub_str[str_mem+len(arg_value)+1:space_seperator] 


    
#Input syscall num in hex string, output the corresponding name,arg_types,arg_widths,in_outs    
def find_syscall(syscall_hex_str):
  global syscall_table    
  global syscall_json
  arg_types=[]
  arg_widths=[]
  in_outs=[]
  syscall_num=int(syscall_hex_str,16)
  syscall_name=syscall_table[syscall_num]
  if "ntdll!"+syscall_name in syscall_json:
    syscall_name="ntdll!"+syscall_name
  elif "win32u!"+syscall_name in syscall_json:
    syscall_name="win32u!"+syscall_name
  arg_num = syscall_json[syscall_name]["argnum"]
  
  for i in range(1,arg_num+1):
    arg="arg"+str(i)
    levels_types=[]#For pointers. If arg is a pointer, this can record both the pointer width and the content width
    
    #record arg types
    if syscall_json[syscall_name][arg]["type"]=="ptr":
      levels_types.append(syscall_json[syscall_name][arg]["type"])
      levels_types.append(syscall_json[syscall_name][arg]["content"]["type"])
      arg_types.append(levels_types)
    else:
      levels_types.append(syscall_json[syscall_name][arg]["type"])
      arg_types.append(levels_types)
      
    #record arg width  
    if "width" in syscall_json[syscall_name][arg]:
      arg_widths.append([syscall_json[syscall_name][arg]["width"]])
      in_outs.append("in")
    else:
      if syscall_json[syscall_name][arg]["type"]=="ptr":
        width=[]
        if "inout" in syscall_json[syscall_name][arg]:
          width.append(4)
          in_outs.append(syscall_json[syscall_name][arg]["inout"])
        if syscall_json[syscall_name][arg]["content"]["type"]=="scalar":
          width.append(syscall_json[syscall_name][arg]["content"]["width"])
        elif syscall_json[syscall_name][arg]["content"]["type"]=="handle":
          width.append(syscall_json[syscall_name][arg]["content"]["width"])  
        arg_widths.append(width)
      elif syscall_json[syscall_name][arg]["type"]=="funcptr":  
        arg_widths.append(4)
        in_outs.append("in")
      else:
        print("Did not expect this case!")
        bp()        
  return syscall_name,arg_types,arg_widths,in_outs
   
#Synthesize full name of this structure arg.   
def get_struct_name(syscall,arg_num,struct_num): 
 full_name=syscall.split("!")[1]+"_arg"+str(arg_num)+"_struct"+str(struct_num)
 return full_name
 
def read_syscall_json(syscall_json_path):
   global syscall_json
   f=open(syscall_json_path, 'r')
   syscall_json = json.load(f)
   f.close()
     
 
#arg is a pointer. We need to find its pointed value.
def find_ptr_content_value(line_trace,arg_mem_addr): 
  start_index=line_trace.find(arg_mem_addr+":")
  if start_index!=-1:
    start_index+=len(arg_mem_addr)+1
    end_index=line_trace.find(" ",start_index)
    value=line_trace[start_index:end_index]
    return value
  else:
    return ""  
  
    
#From this line trace, find its arg which sources from previous traces.
#In the analyzed trace, the sources are written like this: src:{12:[1 ret12],45:[2 14_arg3]}. Which means, argument 1 comes from trace number 12. The value is its return value ret12. argument 2 comes from trace number 45, its value is the output value in arg 14_arg3. 
def find_dependent_args_source(line_trace):
  result={}#A dict takes current trace's argument number as key, and source trace's argument as value.
  ret_index=line_trace.find("ret:")
  taint_src_index=line_trace.rfind("taint src: {",0,ret_index)
  close_bracket_index=line_trace.find("}",taint_src_index)
  
  elements=split_dict_str(line_trace[taint_src_index+12:close_bracket_index])
  #if "LA02_arg_5 L9A2_arg_1']} A02:13A( 314, 10, 1, 35C62D0, 314, " in line_trace:
  #  bp()
  #arg_sources={}#A map recording which arg comes from which trace's which arg/ret
  for element in elements:
    #trace_num=element.split(":")[0].split("'")[1]
    if element=='':
      continue
    else:  
      try:
        arg=element.split(":")[1]
      except:
        bp()      
      if arg.find("'")==-1:#An empty record like '5': []
        continue
      try:  
        first_quote_idx=arg.find("'")
        last_quote_idx=arg.rfind("'")
        sub_str=arg[first_quote_idx+1:last_quote_idx]   
        if sub_str.find(" ")!=-1:#contains source arg information     
          if sub_str.find(",")==-1:#only contains one target-source pair
            current_arg_num=sub_str.split(" ")[0]
            source_arg_num=sub_str.split(" ")[1]            
            #current_trace_num=current_arg_num[1:current_arg_num.find("_")]
            if source_arg_num.startswith("byref_"):
              value=source_arg_num[6:]
              source_arg_num="byref("+value+")"
            result[int(current_arg_num.split("_")[-1],16)]=source_arg_num
          else:#contains multiple target-source pairs
            subelements=sub_str.split(",")
            for subelement in subelements:
              #first clean the subelement
              subelement=subelement.strip()
              subelement=subelement.strip("'")
              current_arg_num=subelement.split(" ")[0]
              source_arg_num=subelement.split(" ")[1]             
              if source_arg_num.startswith("byref_"):
                value=source_arg_num[6:]
                source_arg_num="byref("+value+")"              
              result[int(current_arg_num.split("_")[-1],16)]=source_arg_num   
              
      except:
        bp()   
  return result  
   
#split the dict string by each ',' that seperates each key-value tuple   
def split_dict_str(dict_str): 
    result=[]
    
    left_bracket=0
    
    start_index=0
    for index in range(len(dict_str)):
      if dict_str[index]=='[':
        left_bracket+=1
      elif dict_str[index]==']':
        left_bracket-=1
        if index!=len(dict_str)-1:
          pass
        else:
          result.append(dict_str[start_index:])        
      elif dict_str[index]==',':
        if left_bracket==0:#Is the comma that seperates the dictionary elements rather than seperating the dict in the value
          result.append(dict_str[start_index:index])  
          start_index=index+1
    return result         
    
#When the current syscall's arg is a pointer to a structure, we need to generate code that prepare the structure's value. 
def prepare_struct_arg_value(line,line_num,arg_num,arg_value,syscall,struct_name):
  global syscall_json
  #struct_instance_name="struct_"+str(line_num)+"_"+"arg"+str(arg_num+1)
  #cython_str=struct_instance_name+"="+struct_name+"()"
  cython_str=""
  
  arg_json_fields=syscall_json[syscall]["arg"+str(arg_num)]["content"]["fields"]
  
  struct_base=int(arg_value,16)
  if struct_base==0:#When the arg is expected to be a pointer to a struct, but the trace records a zero
    pass
  else:  
    cython_str,offsets_list,useless_struct_num,useless_array_num=prepare_struct_value(line,arg_json_fields,struct_base,0,0,arg_num,line_num,syscall,"arg_ptr")
    struct_insntance_name="struct_"+str(line_num)+"_"+"arg_"+str(arg_num)+"_0"
    for offset in offsets_list:
      cython_str+=struct_insntance_name+offset
    
  return cython_str
   
#We use the recorded values in the trace to initialize the array. This is usually for input array case.   
def prepare_array_arg_value_by_trace(line,line_num,arg_num,arg_value,syscall):
  global syscall_json
  array_num=0
  if arg_value=='0':#When the arg is expected to be some pointer but record shows it's a zero
    return ""  
  #if "2B22:110B( CA9F00, 25, )  ret:410421" in line: 
  #  bp()  
  array_content,count=find_array(line,arg_value)
  if count==None:# Count not find for arrays. This could be because the arrays are recorded as structs (NTFuzz implementations, dont know why they do this). So we try to resolve this by reading the contents in the structure-lie records.
    array_json=syscall_json[syscall]["arg"+str(arg_num)]["content"]
    extra_cython_code=try_prepare_array_as_struct(line,line_num,arg_value,array_num,arg_num,array_json)
    return extra_cython_code
  
  array_json=syscall_json[syscall]["arg"+str(arg_num)]["content"]
  extra_cython_code=prepare_array(array_content,count,line_num,array_num,arg_num,array_json)
  return extra_cython_code
  
#For the cases that NTFuzz record array as structs, we need to manage to prepare the cython code by reading from the structure contends.  
def try_prepare_array_as_struct(line,line_num,arg_value,array_num,arg_num,array_json): 
  cython_str=""
  if array_json["content"]["type"]=="handle":
    array_name="L"+str(line_num)+"_arg"+str(arg_num)+"_array_"+str(array_num)
    cython_str+=array_name+"=(c_ulong*0x256)()\n"
    start_index=line.find(arg_value+":")# strings like '65cda4:' is in the trace
    field_count=0
    next_memory_addr=arg_value
    while start_index!=-1:#As long as the next 4 bytes are recorded, that means the array haven't stop.
      next_space_index=line.find(" ",start_index)
      memory_value=line[start_index+len(next_memory_addr)+1:next_space_index]#Find memory content from string like '5426a2:123 5426a6:124' 
      cython_str+=array_name+"["+str(field_count)+"]=0x"+memory_value+"\n"
      next_memory_addr=hex(int(next_memory_addr,16)+4)[2:].upper()#trim the 0x prefix
      start_index=line.find(next_memory_addr+":",start_index)
      field_count+=1
    return cython_str  
  else:  
    cython_str+="Array of none-trival type here! Please manually fill this field!\n"
    return cython_str
      
   
  
#We use the type in the types.json as the model to initialze the array. This is usually for output array case.
def prepare_array_arg_value_by_type(line,line_num,arg_num,array_num,arg_values,array_json,syscall):  
  cython_code=""
  array_count=find_array_size(array_json,arg_values)
  if array_json["content"]["type"]=="struct":
    cython_code+=define_struct_by_type(line_num,0,arg_num,syscall)
    array_type=syscall.split("!")[1]+"_arg"+str(arg_num)+"_struct0"
  elif array_json["content"]["type"]=="ptr":
    print("Did not expect this case!")
    bp()
  elif array_json["content"]["type"]=="funcptr":
    print("Did not expect this case!")
    bp()
  elif array_json["content"]["type"]=="scalar" or array_json["content"]["type"]=="handle":
    content_width=array_json["content"]["width"]
    array_type=None
    if content_width==1:
      array_type="c_byte"
    elif content_width==2:
      array_type="c_ushort"
    elif content_width==4:
      array_type="c_ulong"     
    elif content_width==8:
      array_type="c_longlong"
    else:
      print("Did not expect this case!")
      bp()  
  else:
    print("Did not expect this case!")
    bp()       
  if array_count>0x100:
    array_count=0x100  
  cython_code+="L"+str(line_num)+"_arg"+str(arg_num)+"_array_"+str(array_num)+"=("+array_type+"*0x"+str(array_count)+")()\n"  
  return cython_code  

#Find array element count. 
def find_array_size(array_json,arg_values): 
  kind=array_json["size"]["kind"]
  if kind=="fixed":
    return array_json["size"]["val"]
  elif kind=="argfield":
    idx=array_json["size"]["idx"]
    return arg_values[idx]
  elif kind=="adjacentfield":
    bp()
  elif kind=="unknown":#If count is unknown, for simplicity, we assume it is 1.
    return 1
  return 1  
  
#Directly define struct out of types.json 
def define_struct_by_type(line_num,struct_num,arg_num,syscall):
  cython_str=""
  struct_name=get_struct_name(syscall,arg_num,struct_num)
  struct_instance_name="struct_"+str(line_num)+"_"+"arg"+str(arg_num)
  cython_str+=struct_instance_name+"="+struct_name+"()\n"
  return cython_str
    
  
#Given current structure's information, return the corresponding cython code preparing this structure's values.  
def prepare_struct_value(line_trace,arg_json_fields,base_addr,struct_num,array_num,arg_num,line_num,syscall,ptr_or_not):
  struct_name=get_struct_name(syscall,arg_num,struct_num)
  if ptr_or_not=="content":#This structure is not a pointer structure
    struct_instance_name="struct_"+str(line_num)+"_"+"arg_"+str(arg_num)+"_"+str(struct_num)
    cython_str=struct_instance_name+"="+struct_name+"()\n"
  elif ptr_or_not=="ptr":#This structure is a pointer structure
    struct_instance_name="struct_"+str(line_num)+"_"+"arg_"+str(arg_num)+"_"+str(struct_num)
    cython_str=struct_instance_name+"=POINTER("+struct_name+")\n"
    cython_str+="temp"+str(struct_num)+"="+struct_instance_name+"()\n"
  elif ptr_or_not=="arg_ptr":  
    struct_instance_name="struct_"+str(line_num)+"_"+"arg_"+str(arg_num)+"_"+str(struct_num)
    cython_str=struct_instance_name+"="+struct_name+"()\n"
    pass
      
  extra_cython_code=""#The code that prepares the iterative structure's value
  
  offsets_list=[]#The code that prepares each field in current structure.
  
  offset_i=0
  #if "160( D7E670, 1FFFFF, 0, FFFFFFFF, 754E6AE0, 4DE2458, 1, 0, 0, 0, D7E680" in line_trace and arg_num==11:
  #  bp()
  for entry in arg_json_fields:
    offset=entry["offset"]
    entry_addr=hex(base_addr+offset)[2:].upper()    
    ptr_content=find_entry_content(line_trace,entry_addr)
    if entry["content"]["type"]=="scalar":
      #if "160( D7E670, 1FFFFF, 0, FFFFFFFF, 754E6AE0, 4DE2458, 1, 0, 0, 0, D7E680,"==ptr_content:
      #  bp()
      offsets_list.append(".reserve"+str(offset_i)+"=0x"+ptr_content+"\n")
    elif entry["content"]["type"]=="handle":
      offsets_list.append(".reserve"+str(offset_i)+"=0x"+ptr_content+"\n")
    elif entry["content"]["type"]=="array":
      offsets_list.append(".reserve"+str(offset_i)+"=L"+str(line_num)+"_arg"+str(arg_num)+"_array_"+str(array_num+1)+"\n")
      array_num+=1
      #if entry_addr=='6CCE38':
      #  bp()
      array_content,count=find_array(line_trace,entry_addr)
      array_json=entry["content"]
      if array_content=="":#If not found the array content in the trace
        pass
      else:#If found the array content in the trace  
        if array_content=='6CCF40:{  group: -1 taint src: {} write time:60D':
          bp()
        extra_cython_code+=prepare_array(array_content,count,line_num,array_num,arg_num,array_json)
    elif entry["content"]["type"]=="stringw":
      #By our observation, when there are only three fields in the struct, and the last one is stringw, then the first two fields represent string length and max string length respectively.
      if len(arg_json_fields)==3 and offset_i==len(arg_json_fields)-1:
        '''str_addr=hex(base_addr+arg_json_fields[offset_i-2]["offset"])[2:].upper()
        str_width=int(find_entry_content(line_trace,str_addr),16)'''
        str_width=-1
      else:
        str_width=-1
      str_content=find_string_value(line_trace,entry_addr)  
      #str_content=find_entry_content(line_trace,entry_addr)
      str_code=recode_str(str_content,str_width)
      offsets_list.append(".reserve"+str(offset_i)+"='"+str_code+"'\n")
    elif entry["content"]["type"]=="ptr":
      if ptr_content=='0':#When the pointer value is zero
        array_num,struct_num=walk_json(entry["content"]["content"],array_num,struct_num)
        pass
      elif  ptr_content+":" not in line_trace:#When the pointer does not points to an address
        #if "6C6:160( D7E670, 1FFFFF, 0, FFFFFFFF, 754E6AE0, 4DE2458, 1, 0, 0, 0, D7E680, )  ret:0 TID:108C small array: large array: in entries:D7E680:24 D7E684:10003 D7E688:8 D7E68C:D7E64C D7E654:2 D7E65C:FFFFFFFF D7E694:4 D7E696:1 D7E698" in line_trace:
        #  bp()
        array_num,struct_num=walk_json(entry["content"]["content"],array_num,struct_num)
        pass      
      else:#When the pointer value is not zero  
        delta_cython_str,struct_num,array_num=prepare_ptr_cython_code(entry["content"]["content"],arg_json_fields,line_trace,ptr_content,line_num,arg_num,struct_num,array_num,syscall,offset_i,base_addr)
        if delta_cython_str[0].startswith("c_char_p"):#ptr points to a string
          offsets_list.append(".reserve"+str(offset_i)+"="+delta_cython_str[0][:-1]+"\n")
        elif delta_cython_str[0].find("(temp")!=-1:#ptr points to a structure
          sub_offsets_list=delta_cython_str[2]
          offsets_list.append(".reserve"+str(offset_i)+"="+delta_cython_str[0][:-1]+"\n") 
          for sub_offset_i in range(len(sub_offsets_list)):
            sub_offsets_list[sub_offset_i]=".reserve"+str(offset_i)+"[0]"+sub_offsets_list[sub_offset_i]
          for item in sub_offsets_list:
            offsets_list.append(item)              
        else:#ptr points to other kinds. like a constant etc.
          offsets_list.append(".reserve"+str(offset_i)+"=pointer("+delta_cython_str[0][:-1]+")\n")
        extra_cython_code+=delta_cython_str[1]
    elif entry["content"]["type"]=="struct":
      struct_num+=1
      struct_instance_name="struct_"+str(line_num)+"_"+"arg_"+str(arg_num)+"_"+str(struct_num)
      int_entry_addr=int(entry_addr,16)
      delta_extra_cython_code,sub_offsets_list,struct_num,array_num=prepare_struct_value(line_trace,entry["content"]["fields"],int_entry_addr,struct_num,array_num,arg_num,line_num,syscall,"content")
      offsets_list.append(".reserve"+str(offset_i)+"="+struct_instance_name+"\n")
      #Now we reassemble the sub structure's offset fields to make them from xxx.reserve1 to xxx.xxx.reserve1.
      for sub_offset_i in range(len(sub_offsets_list)):
        sub_offsets_list[sub_offset_i]=".reserve"+str(offset_i)+sub_offsets_list[sub_offset_i]
      for item in sub_offsets_list:
        offsets_list.append(item)      
      extra_cython_code+=delta_extra_cython_code
    elif entry["content"]["type"]=="funcptr":
      print("Did not expect this case!")
      #bp()
    else:
      print("Did not expect this case!")
      bp()
    offset_i+=1  
  
  return extra_cython_code+cython_str,offsets_list,struct_num,array_num

#When the current field is a pointer, we need to prepare its corresponding cython code.    
def prepare_ptr_cython_code(json_content,arg_json_fields,line_trace,ptr_content,line_num,arg_num,struct_num,array_num,syscall,offset_i,base_addr):  
    extra_cython_code=""
    cython_str=""
    sub_offsets_list=None
    if json_content["type"]=="scalar":
      ptr_content=find_entry_content(line_trace,ptr_content)
      if json_content["width"]==1:
        cython_str+="c_byte(0x"+ptr_content+")\n"
      elif json_content["width"]==2:
        cython_str+="c_ushort(0x"+ptr_content+")\n"  
      elif json_content["width"]==4:
        cython_str+="c_ulong(0x"+ptr_content+")\n"  
      elif json_content["width"]==8:
        cython_str+="c_longlong(0x"+ptr_content+")\n"    
      else:
        print("Did not expect this case!")
        bp()      
    elif json_content["type"]=="handle":
      print("Did not expect this case!")
      bp()
    elif json_content["type"]=="array":
       cython_str+="array_"+line_num+"_"+array_num+"\n"
       array_num+=1
       array_content,count=find_array(line_trace,ptr_content)
       array_json=json_content["content"]
       extra_cython_code=prepare_array(array_content,count,line_num,array_num,arg_num,array_json)
    elif json_content["type"]=="stringw":
       #By our observation, when there are only three fields in the struct, and the last one is stringw, then the first two fields represent string length and max string length respectively.
       if len(arg_json_fields)==3 and offset_i==len(arg_json_fields)-1:
         '''possible_str_len=arg_json_fields[offset_i-2]#If the pointer points to a string, we may need this field's memory address later
         possible_str_addr=hex(base_addr+possible_str_len["offset"])[2:].upper()
         str_width=int(find_entry_content(line_trace,possible_str_addr),16)'''
         str_width=-1
       else:
         str_width=-1    
       ptr_content=find_string_value(line_trace,ptr_content)
       #ptr_content=find_entry_content(line_trace,ptr_content)
       str_code=recode_str(ptr_content,str_width)
       cython_str+="c_char_p('"+str_code+"')\n"    
    elif json_content["type"]=="ptr":
      print("Did not expect this case!")
      bp()
    elif json_content["type"]=="struct":
      struct_num+=1
      #struct_name=get_struct_name(syscall,arg_num,struct_num)
      struct_instance_name="struct_"+str(line_num)+"_"+"arg_"+str(arg_num)+"_"+str(struct_num)
      cython_str+=struct_instance_name+"(temp"+str(struct_num)+")\n"
      #base_addr=find_entry_content(line_trace,ptr_content)
      int_base_addr=int(ptr_content,16)
 
      extra_cython_code,sub_offsets_list,struct_num,array_num=prepare_struct_value(line_trace,json_content["fields"],int_base_addr,struct_num,array_num,arg_num,line_num,syscall,"ptr")
            
    elif json_content["type"]=="funcptr":
      print("Did not expect this case!")
      bp()
    else:
      print("Did not expect this case!")
      bp()
    return [cython_str,extra_cython_code,sub_offsets_list], struct_num,array_num

#Find entry content. We do not assume space as a separator as strings can contain spaces. We find each xxxx: pattern as the entry memory, thus the separator.
def find_entry_content(line_trace,entry_addr): 
  if (" "+entry_addr+":" in line_trace) or (":"+entry_addr+":" in line_trace): #If entry content is recorded
    start_index=line_trace.find(entry_addr+":")+len(entry_addr)+1
    next_colon=line_trace.find(":",start_index)
    space_before_next_colon=line_trace.rfind(" ",start_index,next_colon)
    entry_mem=line_trace[space_before_next_colon+1:next_colon]
    if not is_hex(entry_mem):
      last_last_space=line_trace.rfind(" ",start_index,space_before_next_colon-1)
      if last_last_space==-1:#Can not fond the xxxx:xx xxxx:xx pattern. For example, CA3C92:{0,}{0,}{0,}{0,}{0,}{5,}#  width:4 
        content='0'
      else:  
        content=line_trace[start_index:last_last_space]
    else:  
      content=line_trace[start_index:space_before_next_colon]
      if content.strip()=="":#If thie value in the trace happens to be cutted out bevause of incomplete trace.
          content='0'
    if " strings" in content:
      content=content.replace(" strings","") 

  else:#If entry content not recorded, its because its zero
    return '0'  
  return content


def is_hex(entry_mem):
  for char in entry_mem:
    if char=='0':
      pass
    elif char=='1':
      pass
    elif char=='2':
      pass
    elif char=='3':
      pass
    elif char=='4':
      pass
    elif char=='5':
      pass
    elif char=='6':
      pass
    elif char=='7':
      pass
    elif char=='8':
      pass
    elif char=='9':
      pass
    elif char=='A':
      pass
    elif char=='B':
      pass
    elif char=='C':
      pass
    elif char=='D':
      pass
    elif char=='E':
      pass
    elif char=='F':
      pass
    else:
      return False    
  return True    

#Generate cython code that prepares for array.  
def prepare_array(array_content,count,line_num,array_num,arg_num,array_json):
  cython_str=""
  if array_json["content"]["type"]=="struct":
    print("Did not expect this case!")
    bp()
  elif array_json["content"]["type"]=="ptr":
    print("Did not expect this case!")
    bp()
  elif array_json["content"]["type"]=="funcptr":
    print("Did not expect this case!")
    bp()
  elif array_json["content"]["type"]=="scalar":
    content_width=array_json["content"]["width"]
    array_type=None
    if content_width==1:
      array_type="c_byte"
    elif content_width==2:
      array_type="c_ushort"
    elif content_width==4:
      array_type="c_ulong"     
    elif content_width==8:
      array_type="c_longlong"
    else:
      print("Did not expect this case!")
      bp()    
    if count>0x100:
      count=0x100    
    cython_str+="L"+str(line_num)+"_arg"+str(arg_num)+"_array_"+str(array_num)+"=("+array_type+"*"+str(count)+")()\n"
    array_elements=array_content[array_content.find(":")+1:].split("}")
    array_elements = list(filter(None, array_elements))
    for i,array_element in zip(range(count),array_elements):
      byte_sequence=array_element.strip("{").split(",")
      byte_sequence = list(filter(None, byte_sequence))
      #if byte_sequence==['9:6 35AA2FE:500 D7E8E0:35AA2F8 35AA2F8:1 35AA2F9:6 D7E8E8:35B45D0 35B45D0:2 35B45D2:198 35B45D4:5 D7E90C:20001 D7E91C:E2160CE3 D7E8F0:38 D7E8A0:35B45D0  out entries:strings']:
      #  bp()
      if byte_sequence==[]:
        bp()
      value,value_str=transform_bytes(byte_sequence,content_width)
      if value!=0:
        cython_str+="L"+str(line_num)+"_arg"+str(arg_num)+"_array_"+str(array_num)+"["+str(i)+"]=0x"+value_str+"\n"
  elif array_json["content"]["type"]=="handle":      
    if count>0x100:
      count=0x100    
    array_type="c_ulong"  
    cython_str+="L"+str(line_num)+"_arg"+str(arg_num)+"_array_"+str(array_num)+"=("+array_type+"*"+str(count)+")()\n"    
    array_elements=array_content[array_content.find(":")+1:].split("}")
    array_elements = list(filter(None, array_elements))
    print("count:",count)
    for i,array_element in zip(range(count),array_elements):
      byte_sequence=array_element.strip("{").split(",")
      byte_sequence = list(filter(None, byte_sequence))
      #if byte_sequence==['9:6 35AA2FE:500 D7E8E0:35AA2F8 35AA2F8:1 35AA2F9:6 D7E8E8:35B45D0 35B45D0:2 35B45D2:198 35B45D4:5 D7E90C:20001 D7E91C:E2160CE3 D7E8F0:38 D7E8A0:35B45D0  out entries:strings']:
      #  bp()
      if byte_sequence==[]:
        bp()
      value,value_str=transform_bytes(byte_sequence,content_width)
      if value!=0:
        cython_str+="L"+str(line_num)+"_arg"+str(arg_num)+"_array_"+str(array_num)+"["+str(i)+"]=0x"+value_str+"\n"
  else:
    print("Did not expect this case!")
    bp()
  return cython_str  
  
#Translate the consecutive bytes into type array_type.    
def transform_bytes(byte_sequence,array_type):
  result_str=""
  for i in range(array_type-1,-1,-1):
    try:
      result_str+=byte_sequence[i].strip()  
    except:
      bp()    
  try:
    value=int(result_str,16)
  except:
    bp()    
  return value,result_str  
  
#Find string length. Through our observation, the previous two fields before the string memory stands for string length and string max length repsectively. We just simply use the string length (the first one).  
def find_str_width(line_trace,string_mem_addr):
  start_index=line_trace.find(string_mem_addr+":")
  first_previous_colon=line_trace.rfind(":",0,start_index)
  second_previous_colon=line_trace.rfind(":",0,first_previous_colon)
  next_space_index=line_trace.find(" ",second_previous_colon)
  length_str=line_trace[second_previous_colon+1:next_space_index]
  length=int(length_str,16)
  return length
  
#Find the array content and its count in the line_trace  
def find_array(line_trace,ptr_content):
  start_index=line_trace.find(ptr_content+":")
  if start_index==-1:#Not found the array content in the trace
    return "",None
  end_index=line_trace.find("#",start_index)
  if end_index==-1:#Found the array starting pattern but bit find the array ending pattern. This means the trace is broken at the end, so we stop play with this array.
    return "",None
  array_content=line_trace[start_index:end_index]
  count_index=line_trace.rfind("count:",0,start_index)
  count_end=line_trace.find(" ",count_index)
  count_str=line_trace[count_index+6:count_end].strip()
  #if "8B39:19B( 4AC, 20000, C1A810, 79DDAF4, C1A810, 6CCE34, 79DDAF4, 0, ) " in count_str:
  #  bp()
  if count_str=='':
    bp()  
  count=int(count_str,16)

  return array_content,count
  
#Append string to file  
def append2file(out_str,out_file):
  f=open(out_file,'a')
  f.write(out_str)
  f.close()
  
#When the ptr content is zero. But we need to walk through the json contents to correctly add struct num and array num.
def walk_json(json_content,array_num,struct_num):
  if json_content["type"]=="struct":
    string=str(json_content)
    struct_num+=string.count("struct")
    array_num+=string.count("array")
  else:
    pass
  return array_num,struct_num
  
synthesize()