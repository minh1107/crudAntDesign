import os
import sys

if len(sys.argv) >= 2:
    folder_python_path = str(sys.argv[1])
else:
    folder_python_path = os.getcwd()
print('folder_python_path:', folder_python_path)

os.putenv('PYTHONPATH', folder_python_path)
os.system('bash')
