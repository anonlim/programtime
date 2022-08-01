import wmi,csv

from apscheduler.schedulers.blocking import BlockingScheduler
f=open('write4.csv','w',newline='')
f.close() # 새 파일에다가 만드는것이 아닌 기존으로 하니까 계속 오류 생김 ㅅㅂ
WMI_OBJ=wmi.WMI() 
process_list=WMI_OBJ.Win32_Process() #일단 미지수가 이거임 이걸 함수안에 넣으면 자꾸 에러뜸  


def makecsv():
    f=open('write4.csv','a',newline='') #그래서 파일 다시 쓰기용도로 만들어줌.

    wr=csv.writer(f)
    df=[]
    proces=[]
    for proc in process_list:
        proces = []
        proces.append(int(proc.Handle))
        proces.append(proc.Caption)
        proces.append(proc.CreationDate)
        df.append(proces)
    df.sort(key=lambda  x:x[2]) #일단 어차피 우리는 얼마나 사용했는지 알아야하니까 시간기준으로 바꿈
    wr.writerows(df)
    f.close()    #실행할때마다 그냥 닫아줌.이게 에러 제일 덜남
    
    
 
shed = BlockingScheduler(timezone = 'Asia/Seoul') 
shed.add_job(makecsv, 'interval', seconds = 30) #60초마다 위의 함수 실행
shed.start()
