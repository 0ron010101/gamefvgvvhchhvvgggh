def menu():
    pleyer =y('бояошник эволар')
    print("1-гулять")
    print("2-жрать")
    print("3-занематся фигнёй")
    print("4-спать")
    print("5-cрать")
    deictvie=int(input())
    if deictvie==1:
        pleyer.gylya()
    elif deictvie==2:
        pleyer.jrat()
    elif deictvie==3:
        pleyer.figna()
    elif deictvie==4:
        pleyer.spiii()
    elif deictvie==5:
        pleyer.sriii()
    else:
        print(" не то")
    pleyer.print_info()
    menu()
class y:
    eda=10
    energiya=100
    goda=0
    dney=0
    dosyg=99
    zdarovya=100
    kihka=0
    def print_info(self):
        print("вы сыты на {}%".format(self.eda))
        print()
        print("вы енергичны на {}%".format(self.energiya))
        print()
        print("вам {} лет".format(self.goda))
        print()
        print("вы прожили {} дней".format(self.dney))
        print()
        print("вы веселы на {}%".format(self.dosyg))
        print()
        print("ваше здоровье ровно {}".format(self.zdarovya))
        print()
        print("ты хочешь на {}% срать".format(self.kihka))
    def __init__(self,NAME):
        self.name=NAME
    def kiihka(self):
        if self.kihka>=100:
            print(f'{self.name} ты сново обосрался')
            self.kihka=0
    def dniiiiii(self):
        self.dney+=1
        if self.dney==365:
            self.goda+=1
            self.dney=0
        elif self.zdarovya <= 0:
            import jopa_osla
            jopa_osla.tvoy_menu()
        elif self.eda<=0:
            self.zdarovya-=20
        elif self.energiya<=0:
            print('ты вырубился (ы)')
            self.spiii()
            self.dney+=1
        self.kiihka()
    def gylya(self):
        print('ты гуууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууляешь')
        self.energiya-=30
        self.dosyg+=30
        self.kihka+=20
        self.dniiiiii()
    def jrat(self):
        print('ты жрёшь')
        if self.eda>=100:
            print("игрок ты совсем в меня не лезет")
        else:
            self.eda+=50
            self.dosyg-=10
            self.kihka+=20
            self.dniiiiii()
    def figna(self):
        print('ты занемаешься фигнёй')
        self.energiya-=30
        self.eda-=20
        self.dosyg+=30
        self.kihka+=20
        self.dniiiiii()
    def spiii(self):
        print('ты спишь')
        self.energiya+=40
        self.eda-=50
        self.dosyg+=5
        self.kihka+=20
        self.dniiiiii()
    def sriii(self):
        print('ты cрёёёёёёёёёёооооооооош')
        self.energiya-=20
        self.eda-=20
        self.kihka=0
        self.dniiiiii()
