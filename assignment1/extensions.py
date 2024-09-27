#isto definitivamente que da para fazer melhor :I

#def main():
#    file=input("File name: ").casefold().strip()
#    if file[-4:] == ".gif":
#        print ("image/gif")
#    elif file[-4:] == ".jpg" or file[-5:] == ".jpeg":
#        print ("image/jpeg")
#    elif file[-4:] == ".png":
#        print ("image/png")
#    elif file[-4:] == ".pdf":
#        print ("application/pdf")
#    elif file[-4:] == ".txt":
#        print ("text/plain")
#    elif file[-4:] == ".zip":
#        print ("application/zip")
#    else:
#        print("application/octet-stream")
#
#main()

#ok descobri dicionários e deve para resumir

def main():
    extension = {                                               #dicionário que relaciona cada extensao com o MIME type
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    file_name = input("File name: ")
    file_extension = "." + file_name.split(".")[-1]              #divide a sting pelo . e fica com a ultima parte, isolando a extensao
    file_extension = file_extension.casefold().strip()
    if file_extension in extension:                              #se a extenção esta do dicionario retorna o MIME type
    	    print (extension[file_extension])
    else:
            print ("application/octet-stream")                   #se não esta retorna o octet-stream


main()

