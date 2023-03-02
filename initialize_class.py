from pdb import set_trace as bp

#Read the log and according to the log to initialize the parameters for each syscall.
def read_log_and_initialize():
  log_path=r"C:\Users\nuc\Downloads\log8.txt"
  f=open(log_path,"r")
  lines=f.read().split("\n")
  bp()
  #for line in lines:
      
      
read_log_and_initialize()      
