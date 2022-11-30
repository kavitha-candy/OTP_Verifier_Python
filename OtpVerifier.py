from twilio.rest import Client
import random
import time
from tkinter import *
from tkinter import messagebox

class OtpVerifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x580+200+80")
        self.configure(bg='#FFFFFF')
        self.resizable(False, False)
        self.n = str(self.otp())
        self.client = Client("AC5d5cee88799f24c094271089d4ab751d", "1dc9aeecdc7751516ba76be4a551dkke")
        self.client.messages.create(to=("+91-7878777555"),
                                    from_ = "+19705141555",
                                    body =  self.n)

        self.minuteString = StringVar()
        self.secondsString = StringVar()

        self.minuteString.set("10")
        self.secondsString.set("00")
    def otp(self):
        return random.randrange(1000,10000)

    def labels(self):
        self.c = Canvas(self, bg = "#EEE8AA", width = 400, height =280 )
        self.c.place(x = 290, y =200)

        self.minuteTextbox = Entry (self, bg = "#EEE8AA", font = ("calibr", 20, ""), textvariable = self.minuteString, width =2)
        self.secondsTextbox = Entry (self, bg = "#EEE8AA", font = ("calibri", 20, ""), textvariable = self.secondsString, width =2)

        self.minuteTextbox.place(x = 460, y =280)
        self.secondsTextbox.place(x = 500, y = 280)

        self.upper_frame = Frame(self, bg = "#DDA0DD", width = 1500, height = 140)
        self.upper_frame.place(x=0, y=0)

        self.picture = PhotoImage(file = "password1.png")
        self.k = Label(self.upper_frame, image = self.picture, bg = "#DDA0DD").place(x = 220, y=35)

        self.j = Label(self.upper_frame, text = "Verify OTP", font = "TimesNewRoman 35 bold", bg = "#DDA0DD", fg = "White").place(x = 350, y =35)

    def entry(self):
        self.otpNumber = Text(self, font = "calibri 20", borderwidth = 2, wrap = WORD, width = 23, height = 1)
        self.otpNumber.place(x = 330, y = 230)
    
    def buttons(self):
        self.submitButtonImage = PhotoImage(file = "submit.png")
        self.submitButton = Button ( self, image = self.submitButtonImage, command = lambda: [self.checkOtp(), self.runTimer()], border= 2)
        self.submitButton.place(x = 440, y = 330)

        self.resendOtpImage = PhotoImage(file = "resendotp.png")
        self.resendOtp = Button (self, image = self.resendOtpImage, command = self.resendOtp , border = 2)
        self.resendOtp.place(x = 420, y = 430)

    def resendOtp(self):
        self.n = str(self.otp())
        self.client = Client("AC5d5cee88799f24c094271089d4ab751d", "1dc9aeecdc7751516ba76be4a551dkke")
        self.client.messages.create(to=("+91-7878777555"),
                                    from_ = "+19705141555",
                                    body =  self.n)
        messagebox.showinfo("showinfo","")

    def checkOtp(self):
        try:
            self.userInput = int(self.otpNumber.get(1.0, "end -1c"))
            if self.userInput == int(self.n):
                messagebox.showinfo("showinfo", "Verification Successful")
                self.n = "done"
            elif self.n == "done":
                messagebox.showinfo("showinfo", " OTP Entered Already")
            else:
                messagebox.showinfo("showinfo", "Wrong OTP")
        except:
            messagebox.showinfo("showinfo", "Invalid OTP")

    def runTimer(self):
        self.clockTime = int(self.minuteString.get())*60 + int(self.secondsString.get())

        while (self.clockTime > -1):
            totalMinutes, totalSeconds = divmod(self.clockTime, 60)

            self.minuteString.set("{0:2d}".format(totalMinutes))
            self.secondsString.set("{0:2d}".format(totalSeconds))

            self.update()
            time.sleep(1)

            if(self.clockTime == 0):
                messagebox.showinfo("", "Your Time has Expired!!!")
            
            self.clockTime -= 1



if __name__ == "__main__" :
    window = OtpVerifier()
    window.labels()
    window.entry()
    window.buttons()
    window.update()
    window.mainloop()