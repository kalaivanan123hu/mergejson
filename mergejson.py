import glob
import json
l=[]
dy=dict()
def merge(path,bname,outname,filesize):
    file_names=glob.glob(path+bname+"[0-9].json")#for recovering all json file with specific base name
    file_names.sort()#for sorting all json file with respect to base name
    print(file_names)
    for i in file_names:
        with open(i) as f1:
            d=json.load(f1)
            for u,v in d.items():
                for j in v:
                    l.append(j)
    dy[u]=l
    with open(path+outname+".json", "w") as outfile:
        json.dump(dy,outfile)
print("Enter the folder path")
path=input()
print("Enter the input file base name")
bname=input()
print("enter the  output file base name")
outname=input()
print("enter maximum file size")
msize=int(input())
merge(path,bname,outname,34)
