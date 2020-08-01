import time
import quotes
import os.path 

while True:
    path = r'C:\Users\param\Desktop\Daily_logs'
     
    #rq = quotes.random_quote()
    clock_time = time.gmtime() 
    date = time.asctime(clock_time)
    name = str(clock_time.tm_mday) +"."+ str(clock_time.tm_mon)+ "." + str(clock_time.tm_year) + ".txt"
    completeName = os.path.join(path, name)
    file1 = open(completeName, "a") 
    
    # Writing to file 
    file1.write(date)
    file1.write("\n" + str(quotes.random_quote()) + "\n\n")
    file1.write("Fill in the random works. Its all random I know.\n")
    file1.write("\nMy Daily logs:\n")
    file1.write(".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n") 
    print(date + "  DONE")

    # Closing file 
    file1.close() 

    # using sleep() to hault execution 
    time.sleep(24*60*60) 