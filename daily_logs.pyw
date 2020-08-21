import time
import datetime
import quotes
import os.path
from plyer.utils import platform
from plyer import notification 

while True:
    path = r'C:\Users\param\Desktop\Daily_logs'
     
    #rq = quotes.random_quote()
    clock_time = time.gmtime() 
    date = datetime.datetime.now()
    name = str(clock_time.tm_mday) +"."+ str(clock_time.tm_mon)+ "." + str(clock_time.tm_year) + ".txt"
    completeName = os.path.join(path, name)
     
    
    # Writing to file 
    if os.path.isfile(completeName) == False:
        file1 = open(completeName, "a")
        file1.write(str(date))
        file1.write("\n" + str(quotes.random_quote()) + "\n\n")
        file1.write("Fill in the random works. Its all random I know.\n")
        file1.write("\nMy Daily logs:\n")
        file1.write(".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n") 
        print(str(date) + "  DONE")

        # Closing file 
        file1.close() 

        notification.notify(
        title='Daily Log Time',
        message='Go ahead write something',
        app_name= str(date),
        #app_icon='path/to/the/icon.' + ('ico' if platform == 'win' else 'png')
        )

    # using sleep() to hault execution 
    time_t  = 12*60*60
    time.sleep(time_t) 