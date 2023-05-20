import random
class Cat:
    def __init__(self,name):
        self.name=name
        self.gladness=20
        self.food=0
        self.alive=True
    def to_run(self):
        print("час бігати!")
        self.food+=0.12
        self.gladness+=3
    def to_chill(self):
        print("час відпочити!")
        self.gladness+=2
        self.food-=0.1
    def to_sleep(self):
        print("час спати")
    def is_alive(self):
        if self.food<-0.5:
            print("втікли...")
            self.alive=False
        elif self.gladness<=0:
            print("скучно...")
            self.alive=False
        elif self.food>5:
            print("ви щясливі!")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"food - {round(self.food,2)}")
    def live(self,day):
        day="Day" + str(day) + "of" + self.name +"life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_run()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()
nick=Cat(name="nono")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
