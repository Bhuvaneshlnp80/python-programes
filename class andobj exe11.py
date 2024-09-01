class teacher:
    def __init__(self,name,regno):
        self.name =name
        self.regno =regno
    def display(self):
        print("name:",self.name)
        print("reg no:",self.regno)

t1=teacher("rev","1")
t2=teacher("mal","2")


t1.display()
t2.display()
