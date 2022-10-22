from tkinter import *

master = Tk()
master.title('Combine')
master.geometry('504x520')

c = Canvas(master,
                   width = 500,
                   height = 250,
                   bg = "#6088e6")

c.place(x=0, y=0)
Label(c, text='Top Frame', bg='#6088e6', fg='white').place(x=225, y=2)
c.create_oval(50,40,230,210,fill="#fcba03", outline="")
c.create_oval(50,40,200,180,fill="#6088e6", outline="")


points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
c.create_polygon(points, outline="", fill="#fcba03")



c1 = Canvas(master,
                    width = 200,
                    height = 200,
                    bg = "#e66960")
c1.place(x=0, y=252)
Label(c1, text='Frame One', bg='#e66960', fg='white').place(x=2, y=2)
points1 = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
c1.create_polygon(points1, outline="", fill="#fcba03")


c2 = Canvas(master,
                    width = 298,
                    height = 99,
                    bg = "#914646")
c2.place(x=202, y=252)
Label(c2, text='Frame Two', bg='#914646', fg='white').place(x=2, y=2)


c3 = Canvas(master,
                    width = 298,
                    height = 98,
                    bg = "#464f91")
c3.place(x=202, y=354)
Label(c3, text='Frame Three', bg='#464f91', fg='white').place(x=2, y=2)


c4 = Canvas(master,
                    width = 500,
                    height = 65,
                    bg = "#6088e6")
c4.place(x=0, y=450)
Label(c4, text='Bottom Frame', bg='#6088e6', fg='white').place(x=2, y=2)
Label(c4, text='Nazareno Bianca', bg='#6088e6', fg='white').place(x=200, y=25)


master.mainloop()
