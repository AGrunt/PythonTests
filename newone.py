import subprocess
result = subprocess.run(['python', '-m' , 'pip', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
print (result)





