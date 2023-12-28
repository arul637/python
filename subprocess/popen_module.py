import subprocess

terminal = subprocess.Popen("gnome-system-monitor")
print(f'return code: {terminal.poll()}')
print(f"terminal process id {terminal.pid}")
terminal.wait(10)
print(f'return code: {terminal.poll()}')

