import wmi,csv
from pprint import pprint

f=open('write.csv','w',newline='')
wr=csv.writer(f)
WMI_OBJ=wmi.WMI()

process_list=WMI_OBJ.Win32_Process()
df=[]
proces=[]
for proc in process_list:
    proces = []
    proces.append(int(proc.Handle))
    proces.append(proc.Caption)
    proces.append(proc.CreationDate)
    df.append(proces)
df.sort(key=lambda  x:x[0])
wr.writerows(df)
f.close()