# Wink-fuzz
This is a fuzzing tool called WinkFuzz for Windows Kernel.

## Preparations
Firstly, since there are too many structures used in Windows syscalls, one should define all the structures beforehand. Run read_json_define_class.py to parse the Types.json and define all the structures within it. Types.json is an output file describing 
each Windows syscalls along with their argument field. This is inferred by NtFuzz by analyzing multiple system binaries. We uploaded 
a sample Types.json and an example of the output structs_define.py for simplicity.

## Usage
Firstly, one should execute and trace the seed applocation. In the log folder, we uploaded the traced log in our experiment.

Secondly, trace_dependence.py analyzes the dependencies among the logged syscalls. It would output a .txt file recording the dependencies
ending with _log_dependency.txt.

Thirdly, synthesis_trace.py generates a model python script that recovers the syscalls from the log.

Fourthly, insert_syscall_sequence.py learns from the trace about the syscalls' dependencies and use the dependencies to insert new syscalls.

Finally, mutate_args_template.py adds the mutation functionality into the just inserted new script file. It uses the APIs provided in the
mutate_lib.py, which mutates non-pointers on its own, and ask NtFuzz's fuzzing module (a driver) to mutate pointers. Note that mutate_lib.py need to be placed under Ntfuzz's Hooker/Debug folder as it uses APIs provided in hooker32.py.

Now we have a new syscall script, one can iteratively execute it for fuzzing. To automatically execute the script file in a infinite loop, run 
start_vm_template.py. This py file sets a time limit for each loop to ignore any errors or hangs.
