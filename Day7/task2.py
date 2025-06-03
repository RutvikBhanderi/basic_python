import os

def get_filename(path):
    return os.path.basename(path)

print(get_filename("/user/documents/report.pdf"))  
print(get_filename("C:\\Users\\admin\\file.txt"))    

