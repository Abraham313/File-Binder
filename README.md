# Binder

For linux. 

This program takes multiple executable files and combines them into a single executable. When the bound executable is run, the
bytecode of each executable is read from an array and is written to a tmp file that is executed by a child process. For each
executable file you bind, a child is forked to run the executable. 

This was built for a security class and is based upon a provided skeleton. 
