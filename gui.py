from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import random

import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from opencage.geocoder import OpenCageGeocode




class OTP:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Information Finder By-Pavi")
        self.root.geometry("450x450+280+50")
        self.root.config(bg='#1c2841')

        self.timezone = StringVar()
        self.company = StringVar()
        self.region = StringVar()
        self.location = StringVar()
        self.text_address = StringVar()





        title = Label(self.root, text="Phone Info.", font=('times new roman', 30, "bold"), bg='#6495ed', fg='#1c2841').place(x=0,
                                                                                                               y=0,relwidth=1)

        self.ph_ = StringVar()

        ph_ = Label(self.root, text="Phone NO.", font=('times new roman', 16, "bold"), bg='#1c2841',fg='white').place(x=0,y=70)
        find = Button(self.root, text='Find', bd=3, cursor='hand2',font=('', 10, "bold"), bg='#1c2841',command=self.find, fg='#e5e4e2', activebackground='#1c2841').place(x=160,y=120,width=120)


        self.ph_txt = ttk.Combobox(self.root, font=('', 15),textvariable=self.ph_, justify=CENTER)
        self.ph_txt['values'] = ('Select', '+91', '+61', '+44', '+1', '+55', '+81', '+977')
        self.ph_txt.place(x=130, y=70, width=200,height=30)
        self.ph_txt.current(0)

        image = Image.open("map.jpg")
        resize_image = image.resize((460, 450))

        img = ImageTk.PhotoImage(resize_image)

        label1 = Label(image=img)
        label1.image = img
        label1.place(x=0, y=150, width=460, height=380)





    def find(self):
            if self.ph_.get() == "Select" or self.ph_.get() == "+91" or self.ph_.get() == '+61' or self.ph_.get() == '+44' or self.ph_.get() == '+1' or self.ph_.get() == '+55' or self.ph_.get() == '+81' or self.ph_.get() == '+977':
                messagebox.showerror("Error", "Enter A Valid Number")
            else:
                ####################### variable ##############################

                self.title2 = LabelFrame(self.root, bg='#6495ed').place(x=0, y=150, relwidth=1, relheight=1)



                code_ = Label(self.root, text="Country Code ", font=('', 15, "bold"), bg='#6495ed',fg='#1c2841').place(x=0, y=180)

                text_address= Entry(self.root, font=('', 13,'bold'), bg='#f5f5f5',textvariable=self.text_address, fg='green').place(
                    x=150,
                    y=170,
                    width=250,
                    height=35)

                time_ = Label(self.root, text="Time Zone ", font=('', 15, "bold"), bg='#6495ed', fg='#1c2841').place(
                    x=0, y=235)
                time_txt = Entry(self.root, font=('times new roman', 13, "bold"), textvariable=self.timezone,
                                 bg='#f5f5f5',
                                 fg='green').place(x=150, y=235, width=250, height=30)

                cmp_ = Label(self.root, text="Company", font=('', 15, "bold"), bg='#6495ed', fg='#1c2841').place(x=0,
                                                                                                                 y=275)
                cmp_txt = Entry(self.root, font=('times new roman', 13, "bold"), textvariable=self.company,
                                bg='#f5f5f5',
                                fg='green').place(x=150, y=275, width=250, height=30)

                Reg = Label(self.root, text="Region", font=('', 15, "bold"), bg='#6495ed', fg='#1c2841').place(x=0,
                                                                                                               y=315)
                reg_txt = Entry(self.root, font=('times new roman', 13, "bold"), textvariable=self.region, bg='#f5f5f5',
                                fg='green').place(x=150, y=315, width=250, height=30)

                loc = Label(self.root, text="Location", font=('', 15, "bold"), bg='#6495ed', fg='#1c2841').place(x=0,
                                                                                                                 y=355)
                loc_txt = Entry(self.root, font=('times new roman', 13, "bold"), textvariable=self.location,
                                bg='#f5f5f5',
                                fg='green').place(x=150, y=355, width=250, height=30)

                clear = Button(self.root, text='Clear', bd=3, cursor='hand2', font=('', 10, "bold"),command=self.clear1, bg='#1c2841',
                               fg='#e5e4e2',
                               activebackground='#1c2841').place(x=310, y=405, width=90)



                self.number = self.ph_.get()
                code = phonenumbers.parse(self.number)
                time = timezone.time_zones_for_number(code)
                company = carrier.name_for_number(code, "en")
                region = geocoder.description_for_number(code, "en")

                key = '350d897f29594b83842dca3eda66dd26'
                geo = OpenCageGeocode(key)
                query = str(region)
                result = geo.geocode(query)
                # print(result)
                lat = result[0]['geometry']['lat']
                lng = result[0]['geometry']['lng']
                get=(lat,"",lng)

                self.timezone.set(time)
                self.company.set(company)
                self.region.set(region)
                self.text_address.set(code)
                self.location.set(get)


                #print(code)
                #print(time)
                #print(company)
                #print(region)




    def clear1(self):
        self.timezone.set("")
        self.company.set("")
        self.region.set("")
        self.text_address.set("")
        self.location.set("")
        self.ph_txt.current(0)
        image = Image.open("map.jpg")
        resize_image = image.resize((460, 450))

        img = ImageTk.PhotoImage(resize_image)

        label1 = Label(image=img)
        label1.image = img
        label1.place(x=0, y=150, width=460, height=380)


root = Tk()
ob = OTP(root)
root.mainloop()
