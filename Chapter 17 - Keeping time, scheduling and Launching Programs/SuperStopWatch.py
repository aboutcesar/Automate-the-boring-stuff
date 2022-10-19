import time

def stopwatch():
    print("Press enter to start the stop watch, and press enter to 'click' the stopwatch. Press Ctl + C to quit. ")
    input()
    print("Time has Started")
    starttime = time.time()
    lasttime = starttime  #last time tracked for the lap
    lapnum = 1

    #Tracking lap times
    try:
        while True: 
            input()
            laptime = round(time.time() - lasttime, 2)
            totaltime = round(time.time() - starttime, 2)
            print('Lap #%s: %s (%s)' % (lapnum, totaltime, laptime), end = '')
            lapnum += 1
            lasttime = time.time()  # Need time to reset to keep track of the time between laps
           
    except KeyboardInterrupt:
        #Handles the Ctl-C button and finishes the program.
        print('\nDone')

stopwatch()




