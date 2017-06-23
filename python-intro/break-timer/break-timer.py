import time, webbrowser, os

total_breaks = 3
break_count = 0

print "This program started at " + time.ctime()
while break_count  < total_breaks:
    time.sleep(60 * 60)
    os.system('say "Break time Mr Heath!"')
    print "Break started."
    webbrowser.open("https://www.youtube.com/watch?v=kxopViU98Xo")
    time.sleep(60 * 10)
    os.system('say "Break time time is over Mr Heath!"')
    print "Break ended. " + str(total_breaks - break_count) + " remain."
    break_count = break_count + 1
