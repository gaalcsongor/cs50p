#prompts the user for a string, and calls file_type() function
def main():
    ext = input("File name: ")
    ext = ext.lower().strip()
    file_type(ext)


#this function takes a string as an argument, cuts the part before the comma,
#and determines the file type in a match-case construct
def file_type(n):
    n = n[n.find("."):]
    if n == ".gif":
        print("image/gif")
    elif n == ".jpg":
        print("image/jpeg")
    elif n == ".jpeg":
        print("image/jpeg")
    elif n == ".png":
        print("image/png")
    elif n == ".pdf":
        print("application/pdf")
    elif n == ".txt":
        print("text/plain")
    elif n == ".zip":
        print("application/zip")
    else:
        print("application/octet-stream")


main() 
    
