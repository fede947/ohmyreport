import sys
class ProgressBar:

    stop=True

    def __init__(self,size):
        self.index = 1
        self.long = int(size/80)+1
        self.size = int(size/self.long)

    def mostrar(self):
        sys.stdout.write("[%s]" % ("." * self.size))
        sys.stdout.flush()
        sys.stdout.write("\b" * (self.size+1))

    def siguiente(self):
        self.index += 1
        if(int(self.index/self.long) == self.size and self.stop):
            print('#',end='',flush=True)
            self.stop=False
            print("")
        else:
            if(self.index%self.long==0 and self.stop):
                print('#',end='',flush=True)
