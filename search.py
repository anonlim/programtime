import csv
f=open('write4.csv','r',encoding='utf-8',newline='')


def chrome_time(f):
    rdr=csv.reader(f)
    a=[]
    kimo=0 #자리수
    for line in rdr:
        if(line[1]=='chrome.exe'):
            a.append(line[2])
    print(int(a[-1][6:12])-int(a[0][6:12])) #a이 프로그램 자체가 컴퓨터를 처음 켜고 그 이후의 로그를 전부 출력하는 것이므로 굳이 여러번 실행 안해도 됨 걍 출력하면 될 듯?
    print(a[-1][6:12],a[0][6:12])
    if(int(a[-1][10:12])<int(a[0][10:12])):
        sec=str(60+int(a[-1][10:12])-int(a[0][10:12]))
        kimo=1
    else:
        sec=str(int(a[-1][10:12])-int(a[0][10:12]))
    if(int(a[-1][8:10])-kimo<int(a[0][8:10])):
        min=str(24+int(int(a[-1][8:10])-kimo-int(a[0][8:10])))
        kimo=1
    else:
        min=str(int(a[-1][8:10])-kimo-int(a[0][8:10]))
        kimo=0
    print(str(int(a[-1][6:8])-int(a[0][6:8])-kimo)+"일"+min+"시간"+sec+"분 사용하였습니다.")
#프로세스를 얼만큼 사용했는지를 생각해봐야하는데 켰던 시간만 나오는 것 같음.
#프로세스를 보니까 아마 기록을 할 때마다 컴퓨터에 로그가 찍히는 것 같음. 중간에 카트라이더 했던 기록은 안남았었고 카트라이더를 켜고 프로그램을 실행시키니까
#그제서야 기록이 남음. 주기적으로 기록을 해주는 것이 좋을 듯 함 5분 혹은 10분?
chrome_time(f)