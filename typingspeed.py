from time import time

def tperror(prompt):
    global inwords

    words=prompt.split()
    errors=0

    for i in range(len(inwords)):
        if i in (0,len(inwords)-1):
            if inwords[i]==words[i]:
                continue
            else:
                errors=errors+1
        else:
            if inwords[i]==words[i]:
                if (inwords[i+1]==words[i+1]) & (inwords[i-1]== words[i-1]):
                    continue
                else:
                    errors+=1
            else:
                errors+=1
    return errors
def speed(inprompt,stime,etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords=len(inwords)
    speed = twords/time

    return speed

def elapsedtime(stime,etime):
    time = etime -stime
    return time     

if __name__=='__main__':
    prompt="Python is commonly used for developing websites and software" 
    print("Type this:",prompt) 

    input("enter here")

    stime =time()
    inprompt=input()
    etime=time()

    time = round(elapsedtime(stime,etime),2)
    speed = speed(inprompt,stime,etime)
    errors = tperror(prompt)

    print("total time elapsed: ",time,"seconds")
    print("your average typing speed was ",speed,"words per minute(w/n)")
    print("with the total of ",errors,"errors ")