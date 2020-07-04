from tkinter import*
import sqlite3
import tkinter.messagebox

x=sqlite3.connect('criminals.db') #connecting the database to sqlite3
c=x.cursor()

class Criminal:     #declaring a class 
    def __init__(self,master):      #define a constructor
        self.master=master
        self.left=Frame(master,width=1000,height=720,bg="lightgrey")
        self.left.pack()
        self.right=Frame(master,width=1000,height=720,bg="lightgrey") #frame of size
        self.right.pack()
    #GUI interface connected to  class with oop terminology
        self.heading=Label(self.left,text="OXFORD JAIL-CRIMINAL RECORDS",font=("arial 40 bold"),fg="black",bg="lightgrey")
        self.heading.place(x=0,y=0)
        self.heading=Label(self.left,text="ADD CRIMINAL RECORD",font=("arial 20 bold"),fg="blue",bg="lightgrey")
        self.heading.place(x=0,y=60)
    #Records displayed of criminals
        self.criminal_number=Label(self.left,text='Criminal Number',font=("arial 18 bold"),fg="black",bg="lightgrey")
        self.criminal_number.place(x=0,y=100)
        self.name=Label(self.left,text="Name",font=("arial 18 bold"),fg="black",bg="lightgrey")
        self.name.place(x=0,y=140)
        self.age=Label(self.left,text="Age",font=("arial 18 bold"),fg="black",bg="lightgrey")
        self.age.place(x=0,y=180)    
        self.crime=Label(self.left,text="Crime",font=("arial 18 bold"),fg="black",bg="lightgrey")
        self.crime.place(x=0,y=220)
        self.fathers_name=Label(self.left,text="Father's name",font=("arial 18 bold"),fg="black",bg="lightgrey")
        self.fathers_name.place(x=0,y=260)
        self.city=Label(self.left,text="City",font=("arial 18 bold"),fg="black",bg="lightgrey")
        self.city.place(x=0,y=300)
        self.mobile_number=Label(self.left,text="Mobile Number",font=("arial 18 bold"),fg="black",bg="lightgrey")
        self.mobile_number.place(x=0,y=340)
        self.time_of_punishment=Label(self.left,text="Time of Punishment",font=("arial 18 bold"),fg="black",bg="lightgrey")
        self.time_of_punishment.place(x=0,y=380)
    #Entry box for the Records
        self.cn_1=Entry(self.left,bd=5)
        self.cn_1.place(x=250,y=100)
        self.name_1=Entry(self.left,bd=5)
        self.name_1.place(x=250,y=140)
        self.age_1=Entry(self.left,bd=5)
        self.age_1.place(x=250,y=180)
        self.crime_1=Entry(self.left,bd=5)
        self.crime_1.place(x=250,y=220)
        self.fathers_name_1=Entry(self.left,bd=5)
        self.fathers_name_1.place(x=250,y=260)
        self.city_1=Entry(self.left,bd=5)
        self.city_1.place(x=250,y=300)
        self.mobile_number_1=Entry(self.left,bd=5)
        self.mobile_number_1.place(x=250,y=340)
        self.time_of_punishment_1=Entry(self.left,bd=5)
        self.time_of_punishment_1.place(x=250,y=380)
    #Button to add the criminals record into the database table named as criminals
        self.submit=Button(self.left,text="Add Criminal Record",bd=5,height=2,fg="white",bg="blue",command=self.add_criminal_record)
        self.submit.place(x=250,y=420)
        self.heading1=Label(self.left,text="Click on next Link",font=("arial 20 bold"),fg="blue",bg="lightgrey")
        self.heading1.place(x=150,y=480)
    #Button for the next operation
        self.submit1=Button(self.left,text="Next Operation",bd=5,height=2,fg="white",bg="blue",command=nextpage)
        self.submit1.place(x=350,y=540)
    def add_criminal_record(self): #Function that adds the criminals
        self.value1=self.cn_1.get()
        self.value2=self.name_1.get()
        self.value3=self.age_1.get()
        self.value4=self.crime_1.get()
        self.value5=self.fathers_name_1.get()
        self.value6=self.city_1.get()
        self.value7=self.mobile_number_1.get()
        self.value8=self.time_of_punishment_1.get()
        if(self.value1=='' or self.value2==''or self.value3==''or self.value4==''or self.value5==''or self.value6==''or self.value7==''or self.value8==''):
            tkinter.messagebox.showinfo("Not done","Please fill all values")
        else:
           sql="insert into Criminal_Record(criminal_number,name,age,crime,fathers_name,city,mobile_number,time_of_punishment) values(?,?,?,?,?,?,?,?)"
        #Executing the sql queries
           c.execute(sql,(self.value1,self.value2,self.value3,self.value4,self.value5,self.value6,self.value7,self.value8))
           x.commit()  #commit the task
           tkinter.messagebox.showinfo("Completed","Record has been added")
           #messagebox to show the completion of adding
           
def nextpage():
  class Criminal1:            #another class for searching,updating and deleting
       def __init__(self,master):  #define a constructor
          self.master=master
          self.left1=Frame(master,width=1000,height=720,bg="lightgrey")
          self.left1.pack()
          self.right1=Frame(master,width=1000,height=720,bg="lightgrey")
          self.right1.pack()
          self.heading=Label(self.right1,text="SEARCH RECORD",font=("arial 20 bold"),fg="blue",bg="lightgrey")
          self.heading.place(x=550,y=0) 
          self.name=Label(master,text="Enter Criminal Name",font=("arial 18 bold"),bg="lightgrey")
          self.name.place(x=550,y=100)
          self.namenet=Entry(master,bd=5)
          self.namenet.place(x=850,y=100)
        #button to search criminal
          self.search=Button(master,text="Search Criminal Record",bd=5,height=2,fg="white",bg="blue",command=self.search_criminal_record)
          self.search.place(x=750,y=160)
       def search_criminal_record(self):
          self.input=self.namenet.get()
          if(self.input==''):
              tkinter.messagebox.showinfo("Not done","Please enter the name")
          else:
              sql="SELECT*FROM Criminal_Record WHERE name LIKE ?"
              self.res=c.execute(sql,(self.input,))
              for self.row in self.res:
                 self.criminal_number=self.row[0]
                 self.name=self.row[1]
                 self.age=self.row[2]
                 self.crime=self.row[3]
                 self.fathers_name=self.row[4]
                 self.city=self.row[5]
                 self.mobile_number=self.row[6]
                 self.time_of_punishment=self.row[7]
                 #Taking all input in a row after search operation executed
              self.u_criminal_number=Label(self.master,text="Criminal Number",font=("arial 18 bold"),bg="lightgrey")
              self.u_criminal_number.place(x=550,y=220)
              self.u_name=Label(self.master,text="Name",font=("arial 18 bold"),bg="lightgrey")
              self.u_name.place(x=550,y=260)
              self.u_age=Label(self.master,text="Age",font=("arial 18 bold"),bg="lightgrey")
              self.u_age.place(x=550,y=300)
              self.u_crime=Label(self.master,text="Crime",font=("arial 18 bold"),bg="lightgrey")
              self.u_crime.place(x=550,y=340)
              self.u_fathers_name=Label(self.master,text="Father's Name",font=("arial 18 bold"),bg="lightgrey")
              self.u_fathers_name.place(x=550,y=380)
              self.u_city=Label(self.master,text="City",font=("arial 18 bold"),bg="lightgrey")
              self.u_city.place(x=550,y=420)
              self.u_mobile_number=Label(self.master,text="Mobile Number",font=("arial 18 bold"),bg="lightgrey")
              self.u_mobile_number.place(x=550,y=460)
              self.u_time_of_punishment=Label(self.master,text="Time of punishment",font=("arial 18 bold"),bg="lightgrey")
              self.u_time_of_punishment.place(x=550,y=500)
            #Entry for the data
              self.ent1=Entry(self.master,bd=5)
              self.ent1.place(x=850,y=220)
              self.ent1.insert(END,str(self.criminal_number))
              self.ent2=Entry(self.master,bd=5)
              self.ent2.place(x=850,y=260)
              self.ent2.insert(END,str(self.name))
              self.ent3=Entry(self.master,bd=5)
              self.ent3.place(x=850,y=300)
              self.ent3.insert(END,str(self.age))
              self.ent4=Entry(self.master,bd=5)
              self.ent4.place(x=850,y=340)
              self.ent4.insert(END,str(self.crime))
              self.ent5=Entry(self.master,bd=5)
              self.ent5.place(x=850,y=380)
              self.ent5.insert(END,str(self.fathers_name))
              self.ent6=Entry(self.master,bd=5)
              self.ent6.place(x=850,y=420)
              self.ent6.insert(END,str(self.city))
              self.ent7=Entry(self.master,bd=5)
              self.ent7.place(x=850,y=460)
              self.ent7.insert(END,str(self.mobile_number))
              self.ent8=Entry(self.master,bd=5)
              self.ent8.place(x=850,y=500)
              self.ent8.insert(END,str(self.time_of_punishment))
              self.update=Button(self.master,text="UPDATE RECORD" ,bd=5,height=2,fg="white",bg="blue",command=self.update_criminal_record)
              self.update.place(x=650,y=580)
              self.update=Button(self.master,text="DELETE RECORD" ,bd=5,height=2,fg="white",bg="red",command=self.delete_criminal_record)
              self.update.place(x=920,y=580)
       def update_criminal_record(self): #Update the record of a table 
              self.variable1=self.ent1.get()
              self.variable2=self.ent2.get()
              self.variable3=self.ent3.get()
              self.variable4=self.ent4.get()
              self.variable5=self.ent5.get()
              self.variable6=self.ent6.get()
              self.variable7=self.ent7.get()
              self.variable8=self.ent8.get()
              sql2="UPDATE Criminal_Record SET criminal_number=?,name=?,age=?,crime=?,fathers_name=?,city=?,mobile_number=?,time_of_punishment=? WHERE name LIKE ?"
              c.execute(sql2,(self.variable1,self.variable2,self.variable3,self.variable4,self.variable5,self.variable6,self.variable7,self.variable8,self.namenet.get()))
              x.commit()
              tkinter.messagebox.showinfo("Updated","Successfully updated the values")
       def delete_criminal_record(self):    #delete the record of the table
              sql3="DELETE from Criminal_Record WHERE name LIKE ?"
              c.execute(sql3,(self.namenet.get(),))
              x.commit()
              tkinter.messagebox.showinfo("Deleted","Record is deleted")
              self.ent1.destroy()
              self.ent2.destroy()
              self.ent3.destroy()
              self.ent4.destroy()
              self.ent5.destroy()
              self.ent6.destroy()
              self.ent7.destroy()
              self.ent8.destroy()    # Destroy all  elements after deleting a record
  obj2=Criminal1(root)  #object of class criminal1 takes root as a argument
  root.geometry("1200x900") #geometry for the project
root=Tk()   #GUI part
root.title(" Criminal Record Project") #title for project
obj1=Criminal(root)    #object of class criminal takes root as a argument
root.geometry("1200x900")  #geometry for the project
