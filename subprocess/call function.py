import subprocess

# call function is used to make the system calls
subprocess.call('ls')

# call function with arguments
subprocess.call(['ls', '-l', '/'])

# to store the stdin, stdout, stderr as file
input = open('input.txt', 'w')
output = open("output.txt", 'w')
error = open("error.txt", 'w')

subprocess.call(['ls', '-l', '/'], stdin=input, stdout=output, stderr=error)

