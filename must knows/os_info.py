# OS module capabilities
import os

# gets PWD
print(os.getcwd()) 

# to change PWD
os.chdir('')
print(os.getcwd) # updated PWD

# lists all directories in the PWD
os.listdir() 

# makedirs() creates top and sun level dirs simultaneously
os.makedir('OS-demo-1')
os.makedirs('OS-demo-1/Sub-dir-1') # no worries even if OS-demo-1 doesn't exist - Recommended

# # same as makedir and makedirs
os.rmdir('OS-demo-1')
os.rmdirs('OS-demo-1/Sub-dir-1')

# renaming
os.rename('original_name.txt', 'new_name.txt')

# Stats of a file - refer documetation for the stats names eg: size, modification time etc..
os.stat('file.txt')
mod_time = os.stat('file.txt').st_mtime # give modification time - non human readble

# Use case 1: Converting non readable times to readble
import datetime

print(datetime.fromtimestamp(mod_time))

# os.walk walks-over the specified path and returns three valued tuple - (dir_path, dir_names, file_names)
for dirpath, dirnames, filename in os.walk('C:/path/Desktop'):
    print('Current path: ', dirpath)
    print("Directories: ", dirnames)
    print('Files: ', filename + '\n')

# TO get all env variables
os.environ

# To get specific path
os.environ.get('HOME')

# Use Case 2: joining two paths for a new file named test.txt
file_path = os.path.join(os.environ.get('HOME'), 'text.txt')

# os.path useful methods
PATH = '/tmp/test.txt' # no worries even if path doesn't exists

os.path.basename(PATH) # returns test.txt
os.path.dirname(PATH) # returns tmp
os.path.split(PATH) # returns tuple of strings: ('/tmp', 'test.txt')
os.path.exists(PATH)  # returns boolean
os.path.splittext(PATH) # returns tuple of strings with splitting file extensions: ('/tmp/test', '.txt') 

# For further exploration
print(dir(os))