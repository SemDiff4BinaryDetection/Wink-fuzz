from subprocess import Popen, PIPE
import time
import os
import subprocess
import signal
from pdb import set_trace as bp


for i in range(20000):
  print("Fuzz %01x time" % i)
  #Popen("python C:\\Users\\1\\Desktop\\vm_test.py")
  #time.sleep(1)
  #p=Popen("python C:\\Users\\1\\Desktop\\args_mutate_template.py", stdout=PIPE, bufsize=1, universal_newlines=True,shell=True)
  
  process=Popen("python C:\\Launcher\\wordpad_L3_args_mutate_template_test.py")
  timeout=120
  delay=120
  '''try:
        (msg, errs) = p.communicate(timeout=timeout)
        ret_code = p.poll()
        if ret_code:
            code = 1
            msg = "[Error]Called Error ： " + str(msg.decode('utf-8'))
        else:
            code = 0
            msg = str(msg.decode('utf-8'))
  except subprocess32.TimeoutExpired:
        # 注意：不能只使用p.kill和p.terminate，无法杀干净所有的子进程，需要使用os.killpg
        p.kill()
        p.terminate()
        os.killpg(p.pid, signal.SIGTERM)

  time.sleep(60)'''
  timeout-=delay
  time.sleep(delay)
  process.kill()
  process.terminate()
  #out=""
  #last_line=None
  #current_line=None
  #while (process.poll() is None) and (timeout > 0):
  #while timeout > 0:
  #   do other things too if necessary e.g. print, check resources, etc.
  #   time.sleep(delay)
  #   timeout -= delay
     
  #   current_line=process.stdout.readline()
  #   print("timeout",timeout,current_line)
  #   out+=current_line
  #   if current_line!= None and current_line !="":
  #     bp()
  #     pass
  #   else:
  #     continue
  #     last_line=current_line  
  '''     try:
         for line in p.stdout:
           print(line)
       except:
         pass       '''
  #out+=process.stdout.read()
  #print("process out:",out)  
  if timeout<=0:   
   print("kill process due to timeout!")
   process.kill()
   process.terminate()
  elif process.poll():   
   print("kill process due to process not running! time left=%01x"%timeout)
   process.kill()
   process.terminate() 
  