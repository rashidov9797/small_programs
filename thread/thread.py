import threading
import time 

#thread - 코드를 실행하는 하나의 동작이다. 


# 다수이 쓰레드를 동작시키는 프로그램 

def sum(name,value): 
    # name과 value 입력 받아 value의 회수만큼 반복한다
    for i in range(0,value):
        print(f"{name} : {i}")


t1 = threading.Thread(target=sum, args=('thread_1', 7))
t2 = threading.Thread(target=sum, args=('thread_2', 10))



t1.start()
t2.start()

print('Main thread')
            
    