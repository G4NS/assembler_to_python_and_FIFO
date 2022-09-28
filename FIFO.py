import time

def main_FIFO():
    global sec
    global buffer
    global allsec

    allsec = 0
    buffer = True
    sec = 0

    def a():
        global sec
        global buffer
        global allsec

        while buffer == True:

            if sec == 3:
                sec = 0
                b()
            else:
                print(f"[A] - process | sec = {sec+1} | all sec = {allsec+1}")
                sec += 1
                allsec +=1
            time.sleep(1)

    def b():
        print("[-----------------------------------]")
        global sec
        global buffer
        global allsec

        while buffer == True:
            if sec == 6:
                sec = 0
                c()
            else:
                print(f"[B] - process | sec = {sec+1} | all sec = {allsec+1}")
                sec += 1
                allsec +=1
            time.sleep(1)

    def c():
        print("[-----------------------------------]")
        global sec
        global buffer
        global allsec

        while buffer == True:

            if sec == 4:
                sec = 0
                d()
            else:
                print(f"[C] - process | sec = {sec+1} | all sec = {allsec+1}")
                sec += 1
                allsec +=1
            time.sleep(1)

    def d():
        print("[-----------------------------------]")
        global sec
        global buffer
        global allsec

        while buffer == True:
            if sec == 5:
                sec = 0
                e()
            else:
                print(f"[D] - process | sec = {sec+1} | all sec = {allsec+1}")
                sec += 1
                allsec +=1
            time.sleep(1)

    def e():
        print("[-----------------------------------]")
        global sec
        global buffer
        global allsec

        while buffer == True:
            if sec == 2:
                sec = 0
                print("[*] all process end")
                buffer = False
            else:
                print(f"[E] - process | sec = {sec+1} | all sec = {allsec+1}")
                sec += 1
                allsec +=1
            time.sleep(1)
    a()


#FIFO()