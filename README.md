# Wink-fuzz
This is a fuzzing tool called WinkFuzz for Windows Kernel.

##Usage
Firstly, one should execute and trace the seed applocation. In the log folder, we uploaded the traced log in our experiment.

Secondly, trace_dependence.py analyzes the dependencies among the logged syscalls. It would output a .txt file recording the dependencies
ending with _log_dependency.txt.
