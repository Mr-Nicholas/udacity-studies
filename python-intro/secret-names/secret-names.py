import os

def rename_files():
    # get all the names from folder path
    file_directory = os.listdir("/Users/Heath/Downloads/prank")

    saved_path = os.getcwd()
    print saved_path
    
    os.chdir("/Users/Heath/Downloads/prank")

    saved_path = os.getcwd()
    print saved_path
    
    # for each file, remove the integers and save the new file
    for file_name in file_directory:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print file_name

    os.chdir(saved_path)
    print os.getcwd()       
        
    # reorder the items by letter
    
rename_files()
