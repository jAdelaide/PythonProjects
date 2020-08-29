import os
    #os.system is a function that other devs have made for you
    #(" ") takes the string as a command to run on the function (runs ls on os.system
print("\tOS System (ls):")
os.system("ls")

print()
        # subproccess.run is better as you can spawn new processes, connect to input/output/error pipes, obtain error codes and can take a lot of new arguments
import subprocess
        #
print("\tSubprocess (ls -l ..):")
        # also got -l for long format and the RELATIVE path to the directory to ls
subprocess.run(["ls","-l",".."])

print()
        # retrieving disk space info
command="ps"
commandArgument="-x"
print(f'\tGathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
