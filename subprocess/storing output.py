import subprocess

output = subprocess.check_output(['whoami'], shell=True)

print(f"i am {output}")