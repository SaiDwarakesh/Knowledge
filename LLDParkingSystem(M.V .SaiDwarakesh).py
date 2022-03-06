#Low Level Design Of a Parking System
import numpy as np
class ParkingSystem:
    def __init__(self):
        self.twowheelers=np.zeros((2,7),dtype="int32")
        self.fourwheelers=np.zeros((2,7),dtype="int32")
        self.list1=[]
    def showemptypositions(self,n):
        if(n==1):
            self.list1=[]
            k=0
            for i in range(0,2):
                for j in range(0,7):
                    if(self.twowheelers[i][j]==0):
                        
                        self.list1.append(k)
                    k=k+1
            print("Free Parking Slots Are ")
            l3=np.array(self.list1)+1
            print(l3)
        if(n==4):
            self.list1=[]
            k=0
            for i in range(0,2):
                for j in range(0,7):
                    if(self.fourwheelers[i][j]==0):
                        self.list1.append(k)
                    k=k+1
            print("Free Parking Slots Are ")
            l3=np.array(self.list1)+1
            print(l3)

    def v2(self):
        self.showemptypositions(1)
        if(len(self.list1)!=0):
            place=int(input("enter parking place"))
            place=place-1
            if place in self.list1:
                k=0
                for i in range(0,2):
                    for j in range(0,7):
                        if(place==k):
                            self.twowheelers[i][j]=1
                        k=k+1
                print("Your Vehicle Is Successfully Parked")
            else:
                print("Enter Correct Place")
        else:
            print("Parking Area For TwoWheelers is Fulled!!")
    def v4(self):
        self.showemptypositions(4)
        if(len(self.list1)!=0):
            place=int(input("enter parking place"))
            place=place-1
            if place in self.list1:
                k=0
                for i in range(0,2):
                    for j in range(0,7):
                        if(place==k):
                            self.fourwheelers[i][j]=1
                        k=k+1
                print("Your Vehicle Is Successfully Parked")
            else:
                print("Enter Correct Place")
        else:
            print("Parking Area For TwoWheelers is Fulled!!")
    def leaveopt2(self,vt):
        num=int(input("Enter Position"))
        num=num-1
        k=0
        for i in range(0,2):
            for j in range(0,7):
                if(vt==2):
                    if(num==k and self.twowheelers[i][j]==1):
                        self.twowheelers[i][j]=0
                        print("You Are successfully left From Parking Area")
                    elif(num==k and self.twowheelers[i][j]==0):
                        print("There Is No Vehicle In That Given Position\nGive Correct Position")
                elif(vt==4):
                    if(num==k and self.fourwheelers[i][j]==1):
                        self.twowheelers[i][j]=0
                        print("You Are successfully left From Parking Area")
                    elif(num==k and self.fourwheelers[i][j]==0):
                        print("There Is No Vehicle In That Given Position\nGive Correct Position")
                k=k+1
        
    def display(self):
        listt=[]
        listf=[]
        k=0
        for i in range(0,2):
            for j in range(0,7):
                if(self.fourwheelers[i][j]==1):
                    listf.append(k+1)
                if(self.twowheelers[i][j]==1):
                    listt.append(k+1)
                k=k+1
        print("The twowheeler Vehicles Parked positions are ",listt)
        print("The fourwheeler Vehicles Parked positions are ",listf)
                    
        
def menu():
    print("\n1.ParkVehicle")
    print("2.Display Places of Parked Vehicles")
    print("3.UnParkVehicle")
    print("4.Exit")
def vehicletype():
    print(" 1.Two wheeler")
    print(" 2.Four wheeler")

    
def main():
    ps=ParkingSystem()
    while(True):
        menu()
        opt=int(input("Enter Your Option"))
        if(opt==1):
            vehicletype()
            vehicle=int(input("Enter option"))
            if(vehicle==1):
                ps.v2()
            elif(vehicle==2):
                ps.v4()
        elif(opt==2):
            ps.display()
        elif(opt==3):
            vehicletype()
            vehicle=int(input("Enter option"))
            if(vehicle==1):
                ps.leaveopt2(2)
            elif(vehicle==2):
                ps.leaveopt2(4)
        elif(opt ==4):
            print("You Are Exiting from Parking System")
            break
        else:
            print("Select any one From above options")
    
if __name__=="__main__":
    main()