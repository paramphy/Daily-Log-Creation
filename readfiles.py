import os

path = r'C:\Users\param\Desktop\Daily_logs'
d = 1
while d < 20:
    try:
        date = str(d) + ".8.2020.txt"
        completepath = os.path.join(path, date)
        f = open(completepath,'r')
        massage = f.readlines()
        f.close()
        
        f1 = open(os.path.join(path,"demofile3.txt"), "a")
        f1.close()
        print(massage)            
        
        d += 1
    except: 
        pass
        d += 1
    