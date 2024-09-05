file=input("enter file name: ")
filename=file.lower()
filename=filename.strip()
found=False
dict={'.gif':'image/gif','.jpg':'image/jpeg','.jpeg':'image/jpeg','.png':'image/png','.pdf':'application/pdf','.txt':'text/plain','.zip':'application/zip'}
for k in dict:
    if(filename.endswith(k)):
        print(dict[k])
        found=True
        break
if(not found):
    print("application/octet-stream")
