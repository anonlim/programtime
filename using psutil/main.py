import psutil,csv,os,time
from pprint import pprint

f=open('write.csv','w',newline='')
wr=csv.writer(f)
df=[]
proces=[]
for proc in psutil.process_iter():
    proces=[]
    proces.append(proc.pid)
    proces.append(proc.name())
    p=psutil.Process(os.getpid())
    p.create_time()
    t=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(p.create_time()))
    proces.append(t)
    t=0
    df.append(proces)
wr.writerows(df)
f.close()