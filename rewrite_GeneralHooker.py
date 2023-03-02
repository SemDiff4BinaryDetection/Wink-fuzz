from pdb import set_trace as bp


#Since the original GeneralHooker only logs the syscall when some situations are satisfied, rather than delligently record all syscalls,
#we need to rewrite it.
def main():
 cpp_path=r"C:\Users\nuc\Desktop\NTFuzz\Hooker\Driver\src\original_c_file\GeneralHooker.cpp"
 f=open(cpp_path,'r')
 lines=f.read().split("\n")
 new_lines=[]
 
 line_i=0
 while line_i <len(lines):
   if lines[line_i].find("sysType->kind == HANDLE_LOG")!=-1:
     if lines[line_i+4].find("#endif")==0:
       new_lines.append("    else if (sysType->kind == HANDLE_LOG) {")
       new_lines.append("       log = ObtainLog(sysType);")
       new_lines.append("      SetupLog(log, execCount, sysType);")
       new_lines.append("      logTarget = true;")
       new_lines.append("#endif")
       new_lines.append("    }")
       
       new_lines.append("#ifdef LOGGING_FLAG")
       new_lines.append("    else {")
       new_lines.append("        log = ObtainLog(sysType);")
       new_lines.append("        SetupLog(log, execCount, sysType);")
       new_lines.append("        logTarget = true;")
       new_lines.append("    }")
       new_lines.append("#endif")
       line_i+=6
     else:
       bp()     
   else:
       new_lines.append(lines[line_i])   
       line_i+=1
 
 out_string=""
 for line in new_lines:
   out_string+=line+"\n"
 
 new_GeneralHooker_path=r"C:\Users\nuc\Desktop\ntfuzz+\new_GeneralHooker.cpp" 
 f=open(new_GeneralHooker_path,"w")
 f.write(out_string)
 f.close()
 
main() 