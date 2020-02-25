import sys,ast
from time import sleep as wait

output = "song\\"

#sys.argv[1]

def OF():
    file = open(sys.argv[1])

    temp = []

    for line in file:
        temp.append(line)

    

    return temp

def CF(arr1,arr2,arr3):
    meta = open(output+"metadata.txt","w+")
    hitobjects = open(output+"hitobjects.txt","w+")
    tpoint = open(output+"timingpoints.txt","w+")

    for line in arr1:
        meta.write(str(line))

    for line in arr2:
        hitobjects.write(str(line))

    for line in arr3:
        tpoint.write(str(line))

    meta.close()
    hitobjects.close()
    tpoint.close()

def meta(arr): #grabs the metadata section and returns it in separate array
    temp1 = []
    temp2 = []

    m0 = arr.index("[Metadata]") #hardcoded but all osu files are like this
    m1 = arr.index("[Difficulty]")

    for i in range(m0+1,m1-1,1):
        temp1.append(arr[i])

    print(temp2)
    for each in temp1:
        t0 = 0
        t1 = each.find(":")
        t2 = len(each)

        p1 = str(each[t0:t1])
        p2 = str(each[t1+1:t2])

        each = [(p1,p2)]
        each = dict(each)
        temp2.append(each)

    return temp2

def hitobj(arr):
    temp = []
    temp2 = []

    h0 = arr.index("[HitObjects]")
    h1 = len(arr)

    for i in range(h0+1,h1,1):
        temp.append(arr[i])

    for each in temp:
        thing = each.replace(":",",")
        thing = thing.split(",")
        thing = thing[0]+","+thing[2]
        thing = thing.split(",")
        temp2.append(thing)
        

    return temp2

def bpmtimings(arr):
    temp = []
    temp2 = []

    h0 = arr.index("[TimingPoints]")
    h1 = arr.index("[HitObjects]")

    for i in range(h0+1,h1-2,1):
        temp.append(arr[i])

    for each in temp:
        thing = each.split(",")
        temp2.append(thing)

    return temp2

def split(arr): #Splits the array to TWO different arrays, meta_d and hitobj_d

    temp = []

    for line in arr:
        linefix = line.replace("\n","")
        temp.append(linefix)


    meta_d = meta(temp)
    hitobj_d = hitobj(temp)
    tpoint_d = bpmtimings(temp)

    

    return str(meta_d),str(hitobj_d),str(tpoint_d)


file = OF()
meta,hitobj,tpoint = split(file)

CF(meta,hitobj,tpoint)

print(meta+","+hitobj+","+tpoint)
