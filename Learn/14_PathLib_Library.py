#File Directory!! #Important
from pathlib import Path
path=Path('Python Tutorial/Modules')
print(path.exists())

"""
path=Path('New Folder')
path.mkdir()
"""

#To see all the files:
path=Path('Python Tutorial')
for files in path.glob('*.py'): #wildcard and the extension
    print(files)

