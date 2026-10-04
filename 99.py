from multiprocessing import Process
def disp():
    print("Hello !! welcome to python tutorial")
if __name__=='__main__':
    p=Process(target=disp)
    p.start()
    p.join()