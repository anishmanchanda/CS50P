monthl=["January","February","March","April","May","June","July","August",
        "September","October","November","December"]
while True:
    try:
        datein=input("Date: ")
        if '/' in datein:
            nl=datein.split('/')
            month=nl[0]
            date=nl[1]
            year=nl[2]
            month=month.strip()
            date=date.strip()
            year=year.strip()
            try:
                if int(date)>31 or int(month)>12:
                    continue
                if len(nl)==3:
                    if len(month)==1:
                        month='0'+month
                    if len(date)==1:
                        date='0'+date
                    print(year,month,date,sep='-',end='')
                    break
            except:
                continue
        elif ' ' in datein:
            nl=datein.split()
            month=nl[0]
            month=month.title()
            date=nl[1]
            if not(date.endswith(',')):
                continue
            year=nl[2]
            date=date.rstrip(',')
            month=month.strip()
            date=date.strip()
            year=year.strip()
            try:
                if int(date)>31:
                    continue

                if len(nl)==3:
                    if int(date) in range (1,32):
                        if len(date)==1:
                            date='0'+date
                        month=monthl.index(month)+1
                        month=str(month)
                        if len(month)==1:
                            month='0'+month
                        print(year,month,date,sep='-',end='')
                        break
                    else:
                        continue
                else:
                    continue
            except:
                continue

        else:
            print('hello world')
            continue
    except(EOFError,NameError):
        break

