from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import random
import time
import ast
import numpy as np
from collections import Counter


def rand_cr(am):
    try:
        am = int(am)
        for _ in range(0, am):
            cr = random.randint(1000000, 9999999)
            new_dna = []
            for _ in range(0, random.randint(2, 10)):
                new_dna.append([])
            for x in range(0, len(new_dna)):
                new_dna[x].append(random.randint(0, 4))
                new_dna[x].append(random.randint(5, 26))
            exec('creat' + str(cr) + ' = Creature(game, ' + str(new_dna) + ', "creat' + str(cr) + '", ' + str(
                random.randint(200, 900)) + ', ' + str(random.randint(30, 730)) + ', [])')
            exec('game.creatures.append(' + 'creat' + str(cr) + ')')
    except ValueError:
        messagebox.showinfo("Invalid input", "Please enter valid number!")


def monster():
    cr = random.randint(1000000, 9999999)
    exec('creat' + str(cr) + ' = Creature(game, ' + str(
        [[0, 50], [1, 30], [2, 50], [3, 25], [4, 20]]) + ', "creat' + str(
        cr) + '", 550, 380' + ', [[[2,0,0,0],[0,2,0,0],[10,5,10,5],[0,0,0,0]]])')
    exec('game.creatures.append(' + 'creat' + str(cr) + ')')
    exec('creat' + str(cr) + '.happiness=9999999999999999')
    exec('creat' + str(cr) + '.energy=9999999999999999')
    exec('creat' + str(cr) + '.first_name=random.choice(game.monster_first_names)')
    exec('creat' + str(cr) + '.last_name=random.choice(game.monster_last_names)')
    exec('creat' + str(cr) + '.name_gr = 8')


def p():
    game.moving = False
    game.deleting = False
    game.info = False
    game.tk.config(cursor='arrow')
    game.canvas.itemconfig(game.move_rect, state='hidden')
    game.canvas.itemconfig(game.del_rect, state='hidden')
    game.canvas.itemconfig(game.mouse_rect, state='normal')
    game.canvas.itemconfig(game.inf_rect, state='hidden')


def m():
    game.moving = True
    game.deleting = False
    game.info = False
    game.tk.config(cursor='fleur')
    game.canvas.itemconfig(game.del_rect, state='hidden')
    game.canvas.itemconfig(game.mouse_rect, state='hidden')
    game.canvas.itemconfig(game.move_rect, state='normal')
    game.canvas.itemconfig(game.inf_rect, state='hidden')


def d():
    game.moving = False
    game.deleting = True
    game.info = False
    game.tk.config(cursor='pirate')
    game.canvas.itemconfig(game.move_rect, state='hidden')
    game.canvas.itemconfig(game.mouse_rect, state='hidden')
    game.canvas.itemconfig(game.del_rect, state='normal')
    game.canvas.itemconfig(game.inf_rect, state='hidden')


def i():
    game.moving = False
    game.deleting = False
    game.info = True
    game.tk.config(cursor='sb_down_arrow')
    game.canvas.itemconfig(game.move_rect, state='hidden')
    game.canvas.itemconfig(game.mouse_rect, state='hidden')
    game.canvas.itemconfig(game.del_rect, state='hidden')
    game.canvas.itemconfig(game.inf_rect, state='normal')


def nearest_on(event):
    for creature in game.creatures:
        cr_posx = creature.posx
        cr_posy = creature.posy
        difx = cr_posx - event.x
        dify = cr_posy - event.y
        if -25 <= difx <= 25 and -25 <= dify <= 25:
            if game.moving:
                creature.moving = True
                break
            elif game.deleting:
                creature.dying = True
                break
        if -50 <= difx <= 50 and -50 <= dify <= 50:
            if game.info:
                creature.inf_state = 'normal'
        else:
            creature.inf_state = 'hidden'


def nearest_off(event):
    if game.moving or game.deleting:
        for creature in game.creatures:
            creature.moving = False
            creature.x = 0
            creature.y = 0
            creature.inf_state = 'hidden'


def add_food(f, am):
    try:
        am = int(am)
        for _ in range(0, am):
            exec('food' + str(f) + ' = Food(game)')
            exec('game.food.append(' + 'food' + str(f) + ')')
    except ValueError:
        messagebox.showinfo("Invalid input", "Please enter valid number!")


def clear_sim():
    for creature in game.creatures:
        creature.dying = True
    while len(game.food) >= 1:
        for ind, food in enumerate(game.food):
            game.wait = 0
            game.canvas.delete(food.ID)
            del game.food[ind]


def update_clock():
    if game.time_state.get():
        game.canvas.itemconfig(game.clock, state='normal')
    else:
        game.canvas.itemconfig(game.clock, state='hidden')
    game.minutes += 1
    game.ticks += 1
    if game.minutes >= 60:
        game.minutes = 0
        game.hour += 1
    if game.hour >= 24:
        game.hour = 0
        game.day += 1
    if game.day >= 30 and game.month in [4, 5, 9, 11]:
        game.day = 1
        game.month += 1
    if game.day >= 31 and game.month in [1, 3, 5, 7, 8, 10, 12]:
        game.day = 1
        game.month += 1
    if game.day >= 28 and game.month == 2 and game.years % 4 == 0:
        game.day = 1
        game.month += 1
    if game.day >= 29 and game.month == 2 and game.years % 4 != 0:
        game.day = 1
        game.month += 1
    if game.month >= 12:
        game.month = 1
        game.year += 1


def cust_cr():
    game.tk.config(cursor='wait')
    cust_crr()


def Random(a, b):
    return random.randint(a, b)


def cust_crr():
    dia = Cust_cr_dialog(game.tk, game)
    try:
        game.tk.wait_window(dia.tk2)
    except:
        pass


class Cust_cr_dialog:
    def __init__(self, parent, game):
        self.running = True
        self.brain = False
        self.brainn = False
        self.y = 20
        self.game = game
        self.tk2 = Toplevel(parent)
        self.tk2.title('DNA Lab')
        self.tk2.resizable(0, 0)
        self.tk2.wm_attributes('-topmost', 1)
        self.tk2.protocol("WM_DELETE_WINDOW", self.destroy)

        self.tabControl2 = ttk.Notebook(self.tk2)
        self.tab21 = ttk.Frame(self.tabControl2, relief='flat')
        self.tabControl2.add(self.tab21, text='DNA Maker')
        self.tab22 = ttk.Frame(self.tabControl2, relief='flat', width=500, height=500)
        self.tabControl2.add(self.tab22, text='Extra Settings')
        self.tabControl2.pack()

        # tab1
        self.cust_canvas = Canvas(self.tab21, width=500, height=220, bd=0, highlightthickness=0)
        self.cust_canvas.pack()
        self.cust_canvas.create_line(0, 215, 500, 215, fill='gray65')
        self.frames = [PhotoImage(file='DNA.gif', format='gif -index %s' % s)
                       for s in range(0, 27)]
        self.l_frames = [
            PhotoImage(file='lines.gif', format='gif -index %s' % s) for s in
            range(0, 25)]
        self.b_img = PhotoImage(file='brain.gif')
        self.DNA_img = self.cust_canvas.create_image(0, 0, image=self.frames[0], anchor='nw')

        self.scrollbar = Scrollbar(self.tab21)  # height=310
        self.c = Canvas(self.tab21, yscrollcommand=self.scrollbar.set, width=490, height=200,
                        scrollregion=(0, 0, 1000, 1000))
        self.scrollbar.config(command=self.c.yview)
        self.scrollbar.pack(fill=Y, side=RIGHT)
        self.c.pack(side=LEFT, fill=BOTH)
        self.frame = Frame(self.c, height=1000, width=320)
        self.c.create_window((0, 0), window=self.frame, anchor='nw')

        self.ok_bt = Button(self.tab21, text='Summon Creature', command=lambda: self.add_creature(),
                            cursor='hand2').place(x=315, y=470)
        self.canc_bt = Button(self.tab21, text='Close', command=lambda: self.destroy(), cursor='hand2').place(x=435,
                                                                                                              y=470)
        self.ok_bt = Button(self.tab22, text='Summon Creature', command=lambda: self.add_creature(),
                            cursor='hand2').place(x=315, y=470)
        self.canc_bt = Button(self.tab22, text='Close', command=lambda: self.destroy(), cursor='hand2').place(x=435,
                                                                                                              y=470)

        Label(self.tab21, text='Cells:', font=('helvetica', 10, 'bold', 'underline')).place(x=15, y=180)
        self.cel_combos = []
        self.cel_sliders = []
        self.add()
        self.add_bt = Button(self.tab21, text='Add cel', command=lambda: self.add(), cursor='hand2').place(x=390, y=185)
        self.del_bt = Button(self.tab21, text='Delete cel', command=lambda: self.remove(), cursor='hand2').place(x=450,
                                                                                                                 y=185)

        # tab2
        Label(self.tab22, text='Extra Settings:', anchor='nw', font=('helvetica', 10, 'bold', 'underline')).place(x=10,
                                                                                                                  y=15)
        Label(self.tab22, text='You can set the value to "Random(x, y)" for a random number between x and y.',
              anchor='nw', font=('helvetica', 8)).place(x=12, y=35)

        self.entrys = {'Spawn posx:': 'Random(200, 900)', 'Spawn posy:': 'Random(30, 730)', 'Blood level:': 200,
                       'Energy Level:': 200, 'Happiness Level:': 100, 'First Name:': 'Random(/)',
                       'Last Name:': 'Random(/)'}
        self.yy = 65
        for ent in self.entrys:
            Label(self.tab22, text=ent, anchor='nw', font=('helvetica', 8, 'bold')).place(x=12, y=self.yy)
            exec('self.' + ent.replace(' ', '').replace(':', '') + ' = Entry(self.tab22, width=15)')
            exec('self.' + ent.replace(' ', '').replace(':', '') + '.place(x=125, y=self.yy)')
            exec('self.' + ent.replace(' ', '').replace(':', '') + '.insert(0, self.entrys[ent])')
            self.yy += 40
        Label(self.tab22, text='Age:', anchor='nw', font=('helvetica', 8, 'bold')).place(x=12, y=345)
        self.years = Entry(self.tab22, width=6)
        self.years.place(x=115, y=345)
        self.years.insert(0, '0')
        Label(self.tab22, text='Years', anchor='nw', font=('helvetica', 8)).place(x=155, y=348)
        self.months = Entry(self.tab22, width=6)
        self.months.place(x=195, y=345)
        self.months.insert(0, '0')
        Label(self.tab22, text='Months', anchor='nw', font=('helvetica', 8)).place(x=235, y=350)
        self.days = Entry(self.tab22, width=6)
        self.days.place(x=285, y=345)
        self.days.insert(0, '0')
        Label(self.tab22, text='Days', anchor='nw', font=('helvetica', 8)).place(x=325, y=350)
        self.game.tk.config(cursor='arrow')

        # DNA animation(s)
        self.current = 0
        self.sleep_time = 0.1
        fr = 23
        b = 0
        while self.running:
            try:
                self.cust_canvas.itemconfig(self.DNA_img, image=self.frames[self.current])
                time.sleep(self.sleep_time)
                self.tk2.update()
                for c in self.cel_combos:
                    if c.current() == 3 and not self.brain and not self.brainn:
                        self.brain = True
                        self.lines_img = self.cust_canvas.create_image(0, 0, image=self.l_frames[16], anchor='nw')
                if self.current >= 26:
                    self.current_add = -1
                elif self.current <= 0:
                    self.current_add = 1
                self.current += self.current_add
                if self.current >= 24:
                    self.sleep_time = 0.18
                elif self.current <= 4:
                    self.sleep_time = 0.18
                else:
                    self.sleep_time = 0.1
                if self.brain:
                    self.cust_canvas.itemconfig(self.lines_img, image=self.l_frames[fr])
                    self.sleep_time = 0.075
                    if fr == 1:
                        self.tab23 = ttk.Frame(self.tabControl2, relief='flat', width=500, height=500)
                        self.tabControl2.add(self.tab23, text='Behaviour')
                        self.ok_bt = Button(self.tab23, text='Summon Creature', command=lambda: self.add_creature(),
                                            cursor='hand2').place(x=315, y=470)
                        self.canc_bt = Button(self.tab23, text='Close', command=lambda: self.destroy(),
                                              cursor='hand2').place(x=435, y=470)
                        Label(self.tab23, text='Brain', font=('helvetica', 10, 'bold', 'underline')).place(x=25, y=250)
                        Label(self.tab23, text='Attraction to others (on a scale from -10 to 10):',
                              font=('helvetica', 8, 'bold')).place(x=34, y=285)
                        self.attr_o = Entry(self.tab23, width=15)
                        self.attr_o.place(x=320, y=285)
                        self.attr_o.insert(0, 'Random(-10, 10)')
                        Label(self.tab23, text='Attraction to food (on a scale from -10 to 10):',
                              font=('helvetica', 8, 'bold')).place(x=34, y=320)
                        self.attr_f = Entry(self.tab23, width=15)
                        self.attr_f.place(x=320, y=320)
                        self.attr_f.insert(0, 'Random(-10, 10)')

                        Label(self.tab23, text='Favourite food:', font=('helvetica', 8, 'bold')).place(x=34, y=355)
                        self.fav_f = IntVar()
                        self.f_none = Radiobutton(self.tab23, text='Nothing', value=1, variable=self.fav_f)
                        self.f_none.place(x=50, y=375)
                        self.f_cr = Radiobutton(self.tab23, text='Creatures', value=2, variable=self.fav_f)
                        self.f_cr.place(x=125, y=375)
                        self.f_f = Radiobutton(self.tab23, text='Normal Food', value=3, variable=self.fav_f)
                        self.f_f.place(x=200, y=375)
                        self.f_ev = Radiobutton(self.tab23, text='Everything', value=4, variable=self.fav_f)
                        self.f_ev.place(x=300, y=375)
                        self.f_r = Radiobutton(self.tab23, text='Random', value=5, variable=self.fav_f)
                        self.f_r.place(x=380, y=375)
                        self.fav_f.set(5)

                        Label(self.tab23, text='"Wants to mate" (on a scale from -10 to 10):',
                              font=('helvetica', 8, 'bold')).place(x=34, y=420)
                        self.mate = Entry(self.tab23, width=15)
                        self.mate.place(x=320, y=420)
                        self.mate.insert(0, 'Random(-10, 10)')
                    if fr == 0:
                        self.cust_canvas.delete(self.lines_img)
                        self.brain = False
                        self.brainn = True
                        self.custt_canvas = Canvas(self.tab23, width=500, height=220, bd=0, highlightthickness=0)
                        self.custt_canvas.pack()
                        self.brain_img = self.custt_canvas.create_image(0, 0, image=self.b_img, anchor='nw')
                    if fr > 0:
                        fr -= 1
            except:
                pass

    def destroy(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.running = False
            self.tk2.destroy()

    def add(self):
        self.cel_combo = ttk.Combobox(self.frame, width=17, font=('helvetica', 8))
        self.cel_combo['values'] = ('Heart', 'Eye', 'Mouth', 'Brain', 'Reproductive System')
        self.cel_combo.current(0)
        self.cel_combo.place(x=20, y=10 + self.y, anchor='nw')
        self.cel_combos.append(self.cel_combo)
        self.cel_sc = Scale(self.frame, from_=5, to=35, orient=HORIZONTAL, length=175, width=10, tickinterval=10,
                            fg='dark red', activebackground='midnight blue', cursor='hand2')
        self.cel_sc.set(15)
        self.cel_sc.place(x=25, y=60 + self.y, anchor='w')
        self.cel_sliders.append(self.cel_sc)
        self.y += 75

    def remove(self):
        try:
            self.cel_combos[-1].place_forget()
            self.cel_sliders[-1].place_forget()
            del self.cel_combos[-1]
            del self.cel_sliders[-1]
            self.y -= 75
        except IndexError:
            messagebox.showinfo("Action not possible", "Sorry, there is nothing to remove.")

    def add_creature(self):
        new_dna = []
        new_weights = []
        self.error = False

        for i, c in enumerate(self.cel_combos):
            new_dna.append([c.current(), self.cel_sliders[i].get()])

        try:
            if self.fav_f.get() == 1:
                self.eat = [0, 0, 0, 0]
            elif self.fav_f.get() == 2:
                self.eat = [-1, -1, 50, 50]
            elif self.fav_f.get() == 3:
                self.eat = [50, 50, -1, -1]
            elif self.fav_f.get() == 4:
                self.eat = [50, 50, 50, 50]
            else:
                self.eat = [round(random.uniform(-1, 1), 2), round(random.uniform(-1, 1), 2), round(random.uniform(-1, 1), 2), round(random.uniform(-1, 1), 2)]
            if self.attr_o.get() != 'Random(-10, 10)' or self.attr_f.get() != 'Random(-10, 10)' or \
                    self.mate.get() != 'Random(-10, 10)' or self.fav_f.get() != 5:
                new_weights.append([])
                new_weights[0].append([])
                try:
                    try:
                        new_weights[0][0].append(int(self.attr_o.get()) / 5)
                    except:
                        exec('self.real = ' + self.attr_o.get() + '/ 5')
                        new_weights[0][0].append(self.real)
                    finally:
                        new_weights[0][0].append(0)
                    try:
                        new_weights[0][0].append(int(self.attr_f.get()) / 5)
                    except:
                        exec('self.real = ' + self.attr_f.get() + '/ 5')
                        new_weights[0][0].append(self.real)
                    finally:
                        new_weights[0][0].append(0)
                    new_weights[0].append([])
                    new_weights[0][1].append(0)
                    try:
                        new_weights[0][1].append(int(self.attr_o.get()) / 5)
                    except:
                        exec('self.real = ' + self.attr_o.get() + '/ 5')
                        new_weights[0][1].append(self.real)
                    finally:
                        new_weights[0][1].append(0)
                    try:
                        new_weights[0][1].append(int(self.attr_f.get()) / 5)
                    except:
                        exec('self.real = ' + self.attr_f.get() + '/ 5')
                        new_weights[0][1].append(self.real)
                    new_weights[0].append(self.eat)
                    new_weights[0].append([])
                    for _ in range(2):
                        try:
                            new_weights[0][3].append(int(self.mate.get()) / 5)
                        except:
                            exec('self.real = ' + self.mate.get() + '/ 5')
                            new_weights[0][3].append(self.real)
                    new_weights[0][3].append(0)
                    new_weights[0][3].append(0)
                except:
                   self.error = True
        except AttributeError:
            pass

        cr = random.randint(1000000, 9999999)
        try:
            exec('creat' + str(cr) + ' = Creature(game, ' + str(new_dna) + ', "creat' + str(cr) + '", ' + str(
                self.Spawnposx.get().replace('Random', 'random.randint')) + ', ' + str(
                self.Spawnposy.get().replace('Random', 'random.randint')) + ', new_weights)')
            exec('game.creatures.append(' + 'creat' + str(cr) + ')')
            self.Spawnposx.config(highlightthickness=0)
            self.Spawnposy.config(highlightthickness=0)
        except:
            self.Spawnposx.config(highlightbackground="red", highlightthickness=1)
            self.Spawnposy.config(highlightbackground="red", highlightthickness=1)
            self.error = True

        things = {'Bloodlevel': 'blood', 'EnergyLevel': 'energy', 'HappinessLevel': 'happiness',
                  'FirstName': 'first_name', 'LastName': 'last_name'}
        for item in things:
            try:
                if item != 'FirstName' and item != 'LastName':
                    try:
                        exec('creat' + str(cr) + '.' + things[item] + ' = int(self.' + item + '.get())')
                    except ValueError:
                        exec('self.test = self.' + item + '.get()')
                        exec('self.test = ' + self.test)
                        exec('creat' + str(cr) + '.' + things[item] + ' = self.test')
                else:
                    if (self.FirstName.get() == 'Random(/)' and item == 'FirstName') or (
                            self.LastName.get() == 'Random(/)' and item == 'LastName'):
                        pass
                    else:
                        exec('creat' + str(cr) + '.' + things[item] + ' = self.' + item + '.get()')
                exec('self.' + item + '.config(highlightthickness=0)')
            except:
                exec('self.' + item + '.config(highlightbackground="red",highlightthickness=1)')
                self.error = True
        try:
            # age
            exec('creat' + str(cr) + '.years = self.game.year - int(self.years.get())')
            exec('creat' + str(cr) + '.months = self.game.month - int(self.months.get())')
            exec('creat' + str(cr) + '.days = self.game.day - int(self.days.get())')
            self.years.config(highlightthickness=0)
            self.months.config(highlightthickness=0)
            self.days.config(highlightthickness=0)
        except:
            self.years.config(highlightbackground="red", highlightthickness=1)
            self.months.config(highlightbackground="red", highlightthickness=1)
            self.days.config(highlightbackground="red", highlightthickness=1)
            self.error = True
        if self.error:
            messagebox.showinfo("Invalid input", "Please enter valid numbers!")


class Game:
    def __init__(self):
        with open('first_names.txt', 'r') as f:
            self.first_names = ast.literal_eval(f.read())
        with open('last_names.txt', 'r') as f:
            self.last_names = ast.literal_eval(f.read())
        self.monster_first_names = ['Satan', 'Hauntbeast', 'The Rotten Howler', 'Killerbunny', 'Dreamscream', 'Bigfoot',
                                    'Bowser']
        self.monster_last_names = ['From Hell', 'Glidebreaker', 'Nosethunder', 'Junior', 'Battler', 'Killer',
                                   'Helltree', 'Blooddrinker', 'Firespitter']
        self.speed = 1
        self.moving = False
        self.deleting = False
        self.info = False
        self.creatures = []
        self.food = []
        self.n_creatures = []
        self.cells = []
        self.tk = Tk()
        self.tk.title('Evolution!')
        self.tk.resizable(0, 0)
        self.canvas = Canvas(self.tk, width=900, height=730, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.back_img = PhotoImage(file='background.gif')
        self.canvas.create_image(200, 30, image=self.back_img, anchor='nw')
        self.day = 1
        self.month = 1
        self.year = 1
        self.hour = 0
        self.minutes = 0
        self.ticks = 0
        self.clock_text = str(self.day).zfill(2) + '/' + str(self.month).zfill(2) + '/' + str(self.year) + ' ' + str(
            self.hour).zfill(2) + ':' + str(self.minutes).zfill(2)
        self.clock = self.canvas.create_text(660, 40, text=self.clock_text, font=('distant galaxy', 30),
                                             fill='dark blue', state='normal', anchor='nw')
        # layout toolbar
        toolbar = self.canvas.create_rectangle(200, 0, 900, 30, fill='gray10')
        self.move_img = PhotoImage(file='move.gif')
        self.mouse_img = PhotoImage(file='mouse.gif')
        self.skull_img = PhotoImage(file='skull.gif')
        mouse_bt = Button(self.tk, image=self.mouse_img, cursor='hand2', relief=FLAT, bg='gray10',
                          command=lambda: p()).place(relx=1, x=-690, y=2, anchor='nw')
        move_bt = Button(self.tk, cursor='hand2', relief=FLAT, image=self.move_img, bg='gray10',
                         command=lambda: m()).place(relx=1, x=-650, y=2, anchor='nw')
        del_bt = Button(self.tk, image=self.skull_img, cursor='hand2', relief=FLAT, bg='gray10',
                        command=lambda: d()).place(relx=1, x=-610, y=2, anchor='nw')
        inf_bt = Button(self.tk, text='i', font=('times', 10, 'bold'), fg='white', cursor='hand2', relief=FLAT,
                        bg='gray10', command=lambda: i()).place(relx=1, x=-563, y=2, anchor='nw')
        self.mouse_rect = self.canvas.create_rectangle(209, 1, 236, 28, outline='blue')
        self.move_rect = self.canvas.create_rectangle(249, 1, 276, 28, outline='blue', state='hidden')
        self.del_rect = self.canvas.create_rectangle(289, 1, 316, 28, outline='blue', state='hidden')
        self.inf_rect = self.canvas.create_rectangle(329, 1, 356, 28, outline='blue', state='hidden')
        self.tk.bind('<ButtonPress-1>', nearest_on)
        self.tk.bind('<ButtonRelease-1>', nearest_off)
        self.mouse_x = self.tk.winfo_pointerx() - self.tk.winfo_rootx()
        self.mouse_y = self.tk.winfo_pointery() - self.tk.winfo_rooty()

        self.command = Entry(self.canvas, width=25, bg='white', fg='grey')
        self.command.place(x=740, y=6, anchor='nw')
        self.command.insert(0, 'Enter command')
        self.command.bind('<FocusIn>', self.foc_in)
        self.command.bind('<FocusOut>', self.foc_out)
        self.command.bind('<Return>', self.enter)
        # layout GUI
        self.tabControl = ttk.Notebook(self.tk)
        tab1 = ttk.Frame(self.tabControl, relief='flat')
        self.tabControl.add(tab1, text='Control Room')
        self.tab2 = ttk.Frame(self.tabControl, relief='flat', width=200, height=730)
        self.tabControl.add(self.tab2, text='Statistics')
        self.tabControl.place(relx=1, x=-900, y=0)
        # tab1 layout
        self.canvas2 = Canvas(tab1, width=201, height=700, bd=0, highlightthickness=0)
        self.canvas2.place(relx=1, x=-201, y=0)
        self.canvas2.create_line(-1, 18, 201, 18)
        self.canvas2.create_line(-1, 300, 201, 300)
        lb2 = Label(tab1, text='Summon amount:', font=('helvetica', 7)).place(relx=1, x=-155, y=55, anchor='nw')
        self.cr_amount = Spinbox(tab1, width=7, from_=1, to=100)
        self.cr_amount.place(relx=1, x=-130, y=70)
        rand_cr_bt = Button(tab1, text='Random Creature(s)', cursor='hand2', font=('helvetica', 7, 'bold'),
                            command=lambda: rand_cr(self.cr_amount.get()), bg='orange2', fg='gray93',
                            anchor='nw').place(relx=1, x=-192, y=31)
        rand_f_bt = Button(tab1, text='Random Food', cursor='hand2', font=('helvetica', 7, 'bold'),
                           command=lambda: add_food(random.randint(1000, 9999), self.cr_amount.get()), bg='orange2',
                           fg='gray93', anchor='nw').place(relx=1, x=-88, y=31)
        rand_cust_bt = Button(tab1, text='Custom Creature', cursor='hand2', font=('helvetica', 7, 'bold'),
                              command=lambda: cust_cr(), bg='orange2', fg='gray93', anchor='nw').place(relx=1, x=-191,
                                                                                                       y=110)
        monster_bt = Button(tab1, text='Summon Monster', cursor='hand2', font=('helvetica', 7, 'bold'),
                            command=lambda: monster(), bg='orange2', fg='gray93', anchor='nw').place(relx=1, x=-95,
                                                                                                     y=110)
        clear_bt = Button(tab1, text='\n Clear Simulation', cursor='hand2', height=3, font=('helvetica', 8, 'bold'),
                          command=lambda: clear_sim(), bg='red', fg='gray93', anchor='nw').place(relx=1, x=-99, y=180,
                                                                                                 anchor='center')
        lb3 = Label(tab1, text='Simulation Speed:', font=('helvetica', 8)).place(relx=1, x=-100, y=330, anchor='se')
        self.speed_sc = Scale(tab1, from_=0, to=100, orient=HORIZONTAL, length=175, width=10, tickinterval=20,
                              fg='gray65', activebackground='midnight blue', cursor='hand2')
        self.speed_sc.set(1)
        self.speed_sc.place(relx=1, x=-100, y=353, anchor='center')
        lb4 = Label(tab1, text='Food Type:', font=('helvetica', 8)).place(relx=1, x=-195, y=380, anchor='nw')
        self.food_combo = ttk.Combobox(tab1, width=10)
        self.food_combo['values'] = ('Berry', 'Pizza', 'Salad', 'Bread', 'Cookie', 'Hamburger', 'Steak')
        self.food_combo.current(random.randint(0, 6))
        self.food_combo.place(relx=1, x=-185, y=400, anchor='nw')
        self.time_state = BooleanVar()
        self.time_state.set(True)
        self.time_chk = Checkbutton(tab1, text='Show Clock', font=('helvetica', 8), var=self.time_state)
        self.time_chk.place(relx=1, x=-93, y=400, anchor='nw')
        self.name_state = BooleanVar()
        self.name_state.set(True)
        self.name_chk = Checkbutton(tab1, text='Creature Names', font=('helvetica', 8), var=self.name_state)
        self.name_chk.place(relx=1, x=-110, y=450, anchor='nw')
        self.aut_state = BooleanVar()
        self.aut_state.set(False)
        self.aut_chk = Checkbutton(tab1, text='Auto Gen*', font=('helvetica', 8), var=self.aut_state)
        self.aut_chk.place(relx=1, x=-195, y=450, anchor='nw')
        inf1 = Label(tab1, text='* Summons automatically a', font=('helvetica', 8), fg='gray55').place(relx=1, x=-190,
                                                                                                       y=470,
                                                                                                       anchor='nw')
        inf2 = Label(tab1, text='new generation of creatures', font=('helvetica', 8), fg='gray55').place(relx=1, x=-182,
                                                                                                         y=486,
                                                                                                         anchor='nw')
        inf3 = Label(tab1, text='after the current one died.', font=('helvetica', 8), fg='gray55').place(relx=1, x=-182,
                                                                                                         y=502,
                                                                                                         anchor='nw')
        lb7 = Label(tab1, text='Notifications:', font=('helvetica', 10, 'underline', 'bold'), fg='gray10').place(x=5,
                                                                                                                 y=535,
                                                                                                                 anchor='nw')
        self.birth_state = BooleanVar()
        self.birth_state.set(False)
        self.birth_chk = Checkbutton(tab1, text='Birth', font=('helvetica', 8), var=self.birth_state)
        self.birth_chk.place(x=18, y=558, anchor='nw')
        self.death_state = BooleanVar()
        self.death_state.set(False)
        self.death_chk = Checkbutton(tab1, text='Death', font=('helvetica', 8), var=self.death_state)
        self.death_chk.place(x=18, y=580, anchor='nw')
        self.evde_state = BooleanVar()
        self.evde_state.set(False)
        self.evde_chk = Checkbutton(tab1, text='Everyone Died', font=('helvetica', 8), var=self.evde_state)
        self.evde_chk.place(x=18, y=602, anchor='nw')
        self.last_notify = 0
        lb5 = Label(tab1, text='Actions').place(relx=1, x=-122, y=4, anchor='nw')
        lb6 = Label(tab1, text='Settings').place(relx=1, x=-122, y=284, anchor='nw')
        # Tab2 LayOut
        Label(self.tab2, text='There may be a drop in frame rate while this \n tab is open.', font=('helvetica', 7), \
              fg='gray55', anchor='nw').place(x=2, y=5)

        self.cr_am_data = []
        self.figure1 = Figure(figsize=(2.1, 1.6), dpi=100)
        self.ax1 = self.figure1.add_subplot(111)
        self.ax1.set_facecolor((0.94, 0.94, 0.92))
        self.figure1.patch.set_facecolor((0.94, 0.94, 0.92))
        self.line1 = FigureCanvasTkAgg(self.figure1, self.tab2)
        self.line1.get_tk_widget().place(x=110, y=110, anchor='center')
        self.ax1.set_title('Creature Amount', fontsize=9)

        self.cell_data1 = []
        self.cell_data2 = []
        self.figure2 = Figure(figsize=(2.2, 1.7), dpi=100)
        self.ax2 = self.figure2.add_subplot(111)
        self.ax2.set_facecolor((0.94, 0.94, 0.92))
        self.figure2.patch.set_facecolor((0.94, 0.94, 0.92))
        self.line2 = FigureCanvasTkAgg(self.figure2, self.tab2)
        self.line2.get_tk_widget().place(x=110, y=275, anchor='center')
        self.ax2.set_title('Cell Percentages', fontsize=9)

        Label(self.tab2, text='Most Popular Surnames', font=('helvetica', 10, 'bold', 'underline')).place(x=100, y=410, anchor='center')
        Label(self.tab2, text='Rank    Surname    %    Amount', font=('helvetica', 7), fg='gray55').place(x=95, y=430,anchor='center')
        self.first_place = Label(self.tab2, text='1.', font=('helvetica', 8, 'bold'))
        self.first_place.place(x=27, y=445, anchor='nw')
        self.second_place = Label(self.tab2, text='2.', font=('helvetica', 8, 'bold'))
        self.second_place.place(x=27, y=465, anchor='nw')
        self.third_place = Label(self.tab2, text='3.', font=('helvetica', 8, 'bold'))
        self.third_place.place(x=27, y=485, anchor='nw')
        self.fourt_place = Label(self.tab2, text='4.', font=('helvetica', 8, 'bold'))
        self.fourt_place.place(x=27, y=505, anchor='nw')
        self.fived_place = Label(self.tab2, text='5.', font=('helvetica', 8, 'bold'))
        self.fived_place.place(x=27, y=525, anchor='nw')
        # generate creatures
        self.wait = 2000
        for cr in range(0, random.randint(15, 50)):
            new_DNA = []
            for _ in range(0, random.randint(2, 10)):
                new_DNA.append([])
            for x in range(0, len(new_DNA)):
                new_DNA[x].append(random.randint(0, 4))
                new_DNA[x].append(random.randint(5, 26))
            exec('creat' + str(cr) + ' = Creature(self, ' + str(new_DNA) + ', "creat' + str(cr) + '", ' + str(
                random.randint(200, 900)) + ', ' + str(random.randint(30, 730)) + ', [])')
            exec('self.creatures.append(' + 'creat' + str(cr) + ')')
    def main_loop(self):
        while True:
            try:
                self.clock_text = str(self.day).zfill(2) + '/' + str(self.month).zfill(2) + '/' + str(
                    self.year) + ' ' + str(self.hour).zfill(2) + ':' + str(self.minutes).zfill(2)
                self.speed = self.speed_sc.get()
                self.tk.update_idletasks()
                self.tk.update()
                if len(self.creatures) == 0 and game.evde_state.get() and time.time() - self.last_notify >= 15:
                    print('Everyone has died!')
                    self.last_notify = time.time()
                self.cr_am_data.append((len(self.cr_am_data) + 1, len(self.creatures)))
                try:
                    self.cell_data1 = ['Heart', 'Eye', 'Mouth', 'Brain', 'Repr. Sys.']
                    self.cell_data2 = [self.cells.count(0)/len(self.cells)*100, self.cells.count(1)/len(self.cells)*100,
                                       self.cells.count(2)/len(self.cells)*100, self.cells.count(3)/len(self.cells)*100,
                                       self.cells.count(4)/len(self.cells)*100]
                except:
                    pass
                if self.speed != 0:
                    if self.tab2.winfo_viewable():
                        xList = []
                        yList = []
                        for t in self.cr_am_data:
                            x, y = t
                            xList.append(x)
                            yList.append(y)
                        self.ax1.clear()
                        self.figure1 = Figure(figsize=(2.1, 1.6), dpi=100)
                        self.ax1 = self.figure1.add_subplot(111)
                        self.line1 = FigureCanvasTkAgg(self.figure1, self.tab2)
                        self.line1.get_tk_widget().place(x=110, y=110, anchor='center')
                        self.ax1.plot(xList, yList, color='r')
                        self.ax1.set_facecolor((0.94, 0.94, 0.92))
                        self.figure1.patch.set_facecolor((0.94, 0.94, 0.92))
                        self.ax1.set_title('Creature Amount', fontsize=9)
                        self.figure1.canvas.draw()

                        self.ax2.clear()
                        self.figure2 = Figure(figsize=(2.2, 1.7), dpi=100)
                        self.ax2 = self.figure2.add_subplot(111)
                        self.line2 = FigureCanvasTkAgg(self.figure2, self.tab2)
                        self.line2.get_tk_widget().place(x=110, y=275, anchor='center')
                        self.ax2.bar(self.cell_data1, self.cell_data2, color='b')
                        self.ax2.set_facecolor((0.94, 0.94, 0.92))
                        self.figure2.patch.set_facecolor((0.94, 0.94, 0.92))
                        self.ax2.set_title('Cell Percentages', fontsize=9)
                        self.figure2.canvas.draw()

                        self.surnames = [cr.last_name for cr in self.creatures]
                        self.popular = [item for items, c in Counter(self.surnames).most_common()
                                      for item in [items] * c]
                        self.pop_set = list(set(self.popular))
                        for i, item in enumerate(['first', 'second', 'third', 'fourt', 'fived']):
                            exec("self." + item + "_place['text'] = '" + str(i+1) + """. %s %s %s' % (self.pop_set[i],
                                            round(self.popular.count(self.popular[i])/len(self.creatures)*100, 2),
                                            self.popular.count(self.popular[i]))""")
                    if len(self.n_creatures) > 0:
                        for index, creature in enumerate(self.n_creatures):
                            cr = random.randint(1000000, 9999999)
                            exec('creat' + str(cr) + ' = Creature(self, ' + str(creature[0]) + ', "creat' + str(
                                cr) + '", ' + str(creature[1]) + ', ' + str(creature[2]) + ', ' + str(
                                creature[3]) + ')')
                            exec('self.creatures.append(' + 'creat' + str(cr) + ')')
                            exec('creat' + str(cr) + '.last_name=creature[4].last_name')
                            del self.n_creatures[index]
                    if len(self.creatures) == 0 and self.aut_state.get():
                        rand_cr(random.randint(15, 50))
                    if self.wait >= 2000:
                        for f in range(0, random.randint(7, 12)):
                            exec('food' + str(f) + ' = Food(self)')
                            exec('self.food.append(' + 'food' + str(f) + ')')
                        self.wait = 0
                    if self.moving or self.deleting:
                        self.mouse_x = self.tk.winfo_pointerx() - self.tk.winfo_rootx()
                        self.mouse_y = self.tk.winfo_pointery() - self.tk.winfo_rooty()
                    self.wait += 1
                    time.sleep(0.01 / self.speed)
                    for creature in self.creatures:
                        creature.move()
                    update_clock()
                    if self.speed < 50 or self.ticks >= 5:
                        self.ticks = 0
                        game.canvas.itemconfig(game.clock, text=self.clock_text)
            except:
                break
    def foc_in(self, event):
        self.command.delete(0, END)
        self.command.config(fg='black')
    def foc_out(self, event):
        self.command.delete(0, END)
        self.command.config(fg='grey')
        self.command.insert(0, 'Enter command')
        self.tk.focus()
    def enter(self, event):
        try:
            exec(self.command.get())
        except Exception as error:
            messagebox.showerror('Error:', error)
        self.foc_out('x')

class Creature:
    def __init__(self, game, DNA, ID, spawn_posx, spawn_posy, weights):
        self.cells = []
        self.first_name = random.choice(game.first_names)
        self.last_name = random.choice(game.last_names)
        self.ID = ID
        self.DNA = DNA
        self.game = game
        self.energy = 200
        self.blood = 200
        self.happiness = 100
        self.weights = weights
        self.eating = False
        self.mating = False
        self.n_food_x = 0
        self.n_food_y = 0
        self.n_creature_x = 0
        self.n_creature_y = 0
        self.x = 0
        self.y = 0
        self.posx = spawn_posx
        self.posy = spawn_posy
        self.moving = False
        self.spawn_posx = spawn_posx
        self.spawn_posy = spawn_posy
        self.body = []
        self.heart_img = PhotoImage(file='heart.gif')
        self.batt_img = PhotoImage(file='low_energy.gif')
        self.b_img = PhotoImage(file='b.gif')
        self.face_img = PhotoImage(file='face.gif')
        self.batt = None
        self.b = None
        self.face = None
        self.dying = False
        self.birth = self.game.clock_text
        self.years = self.game.year
        self.months = self.game.month
        self.days = self.game.day
        self.name_gr = 10
        try:
            for c in range(0, len(DNA)):
                self.cel_ID = self.DNA[c][0]
                self.inf = self.DNA[c][1]
                self.game.cells.append(self.cel_ID)
                if self.cel_ID == 3:
                    if self.weights == []:
                        layer_sizes = [4, 4]
                        poss = -1
                        for layer in layer_sizes:
                            if poss < len(layer_sizes) - 2:
                                self.weights.append([])
                            poss += 1
                            try:
                                for w in range(0, layer_sizes[poss + 1]):
                                    self.weights[poss].append([])
                            except IndexError:
                                pass
                            pos = 0
                            for neurons in range(0, layer):
                                try:
                                    for neurons in range(0, layer):
                                        self.weights[poss][pos].append(round((random.uniform(-1, 1)), 2))
                                except IndexError:
                                    pass
                                pos += 1
                            try:
                                for neurons in range(0, layer_sizes[poss + 1]):
                                    for neurons in range(0, layer):
                                        self.weights[poss][pos].append(round((random.uniform(-5, 5)), 2))
                                    pos += 1
                            except IndexError:
                                pass
                exec('self.cel' + str(c) + ' = cel_' + str(self.cel_ID) + '(self.game, self, ' + str(self.inf) + ')')
                exec('self.cells.append(' + '"self.cel' + str(c) + '")')
                posx = self.spawn_posx + random.randint(-self.inf, self.inf)
                posy = self.spawn_posy + random.randint(-self.inf, self.inf)
                exec('self.color = ' + 'self.cel' + str(c) + '.color')
                self.body.append(
                    self.game.canvas.create_oval(posx, posy, posx + self.inf, posy + self.inf, fill=self.color))
                if c == 0:
                    self.posx = self.game.canvas.coords(self.body[0])[0]
                    self.posy = self.game.canvas.coords(self.body[0])[1]
        except:
            pass
        self.inf_state = 'hidden'
        self.inf_rect = self.game.canvas.create_rectangle(self.posx, self.posy, self.posx + 150, self.posy + 100,
                                                          fill='gray30', state=self.inf_state)
        self.inf_textt1 = self.game.canvas.create_text(self.posx + 5, self.posy + 10, fill='white',
                                                       state=self.inf_state, text='', anchor='w',
                                                       font=('helvetica', 9, 'underline'))
        self.inf_textt2 = self.game.canvas.create_text(self.posx + 5, self.posy + 18, fill='white',
                                                       state=self.inf_state, text='', anchor='w', font=('helvetica', 8))

    def move(self):
        self.age = '%s years, %s months, %s days' % (
            self.game.year - self.years, self.game.month - self.months, self.game.day - self.days)
        if game.name_state.get():
            self.full_name = self.first_name + ' ' + self.last_name
        else:
            self.full_name = self.ID
        if not self.moving:
            self.game.canvas.delete(self.inf_rect)
            self.game.canvas.delete(self.inf_textt1)
            self.game.canvas.delete(self.inf_textt2)
            self.inf_rect = self.game.canvas.create_rectangle(self.posx, self.posy, self.posx + 150, self.posy + 90,
                                                              fill='gray30', state=self.inf_state)
            self.inf_text = 'Age: %s \n Birthday: %s \n Blood level: %s \n Energy: %s \n Happiness: %s' % (
                self.age, self.birth, round(self.blood, 5), round(self.energy, 5), round(self.happiness, 5))
            self.inf_textt1 = self.game.canvas.create_text(self.posx + 5, self.posy + 10, fill='white',
                                                           state=self.inf_state, text=self.full_name, anchor='w',
                                                           font=('helvetica', self.name_gr, 'underline'))
            self.inf_textt2 = self.game.canvas.create_text(self.posx + 5, self.posy + 25, fill='white',
                                                           state=self.inf_state, text=self.inf_text, anchor='nw',
                                                           font=('helvetica', 7))
            if self.blood >= 150 and not self.dying:
                for cel in self.cells:
                    if cel == self.cells[0]:
                        try:
                            self.posx = self.game.canvas.coords(self.body[0])[0]
                            self.posy = self.game.canvas.coords(self.body[0])[1]
                        except IndexError:
                            pass
                    if self.energy >= 30:
                        exec(cel + '.function()')
                        self.energy -= 0.01
                if self.posx <= 250 and self.x < 0:
                    self.x = 0
                elif self.posx >= 850 and self.x > 0:
                    self.x = 0
                if self.posy <= 80 and self.y < 0:
                    self.y = 0
                elif self.posy >= 680 and self.y > 0:
                    self.y = 0
                for cel in self.body:
                    if (self.x != 0 or self.y != 0) and self.energy > 0:
                        self.energyy = self.energy / 100 if self.energy <= 50 else 1
                        self.happinesss = self.happiness / 100 if self.happiness <= 70 else 1
                        self.game.canvas.move(cel, self.x * (self.happinesss) * (self.energyy),
                                              self.y * (self.happinesss) * (self.energyy))
                summ = self.x + self.y
                if summ < 0:
                    summ *= -1
                if self.energy >= 0.01:
                    self.energy -= round(summ / 50, 2)
            if self.blood <= 130 or self.dying:
                for cel in self.body:
                    self.game.canvas.delete(cel)
                for cel in self.cells:
                    try:
                        exec('self.game.canvas.delete(' + str(cel) + '.heart)')
                    except AttributeError:
                        pass
                for cel in self.DNA:
                    del self.game.cells[self.game.cells.index(cel[0])]
                try:
                    self.game.canvas.delete(self.batt)
                except AttributeError:
                    pass
                try:
                    self.game.canvas.delete(self.b)
                except AttributeError:
                    pass
                try:
                    self.game.canvas.delete(self.face)
                except AttributeError:
                    pass
                del self.game.creatures[self.game.creatures.index(self)]
                self.game.canvas.delete(self.inf_rect)
                self.game.canvas.delete(self.inf_textt1)
                self.game.canvas.delete(self.inf_textt2)
                for cel in self.cells:
                    try:
                        self.game.canvas.move(cel.heart, -1000, -1000)
                    except AttributeError:
                        pass
                if game.death_state.get():
                    print('%s passed away.' % (self.full_name))
            else:
                if self.blood <= 140:
                    try:
                        self.game.canvas.delete(self.b)
                    except AttributeError:
                        pass
                    self.b = self.game.canvas.create_image(self.posx, self.posy + 10, image=self.b_img, anchor='nw')
                if self.energy <= 40:
                    try:
                        self.game.canvas.delete(self.batt)
                    except AttributeError:
                        pass
                    self.batt = self.game.canvas.create_image(self.posx + 5, self.posy - 10, image=self.batt_img,
                                                              anchor='nw')
                if self.happiness <= 40:
                    try:
                        self.game.canvas.delete(self.face)
                    except AttributeError:
                        pass
                    self.face = self.game.canvas.create_image(self.posx + 5, self.posy - 15, image=self.face_img,
                                                              anchor='nw')

        elif self.moving:
            for cel in self.cells:
                if cel == self.cells[0]:
                    self.posx = self.game.canvas.coords(self.body[0])[0]
                    self.posy = self.game.canvas.coords(self.body[0])[1]
            if self.game.mouse_x >= 200 and self.game.mouse_x <= 900:
                self.x = self.game.mouse_x - self.posx
            else:
                self.x = 0
            if self.game.mouse_y >= 40 and self.game.mouse_y <= 680:
                self.y = self.game.mouse_y - self.posy
            else:
                self.y = 0
            for cel in self.body:
                self.game.canvas.move(cel, self.x, self.y)
        self.blood -= 0.07


class Food:
    def __init__(self, game):
        self.game = game
        self.posx = random.randint(200, 900)
        self.posy = random.randint(30, 730)
        food_type = str(self.game.food_combo.get()) + '.gif'
        self.img = PhotoImage(file=food_type)
        self.ID = self.game.canvas.create_image(self.posx, self.posy, image=self.img, anchor='nw')


class cel_0:
    # heart
    def __init__(self, game, cr_ID, blood):
        self.cr = cr_ID
        self.blood = blood
        self.game = game
        self.color = 'red'
        self.wait = 100

    def function(self):
        if self.wait >= 100:
            self.cr.blood += self.blood
            self.wait = 0
        else:
            self.wait += 1


class cel_1:
    # eye
    def __init__(self, game, cr_ID, eye_range):
        self.cr = cr_ID
        self.eye_range = eye_range
        self.game = game
        self.color = 'white'

    def function(self):
        for creature in self.game.creatures:
            if creature == self.cr:
                continue
            cr_posx = creature.posx
            cr_posy = creature.posy
            difx = cr_posx - self.cr.posx
            dify = cr_posy - self.cr.posy
            rdifx = difx if difx > 0 else difx * -1
            rdify = dify if dify > 0 else dify * -1
            if rdifx + rdify < self.eye_range * 6 and rdifx + rdify > self.cr.n_creature_x + self.cr.n_creature_y:
                self.cr.n_creature_x = difx
                self.cr.n_creature_y = dify
        for food in self.game.food:
            f_posx = food.posx
            f_posy = food.posy
            difx = f_posx - self.cr.posx
            dify = f_posy - self.cr.posy
            rdifx = difx if difx > 0 else difx * -1
            rdify = dify if dify > 0 else dify * -1
            if rdifx + rdify < self.eye_range * 6 and rdifx + rdify > self.cr.n_food_x + self.cr.n_food_y:
                self.cr.n_food_x = difx
                self.cr.n_food_y = dify


class cel_2:
    # mouth
    def __init__(self, game, cr_ID, maxx):
        self.cr = cr_ID
        self.max = maxx
        self.color = 'green'
        self.game = game

    def function(self):
        if self.cr.eating:
            if self.max >= 22:
                for creature in self.game.creatures:
                    if creature == self.cr:
                        continue
                    cr_posx = creature.posx
                    cr_posy = creature.posy
                    difx = cr_posx - self.cr.posx
                    dify = cr_posy - self.cr.posy
                    rdifx = difx if difx > 0 else difx * -1
                    rdify = dify if dify > 0 else dify * -1
                    if difx == self.cr.n_creature_x and rdifx + rdify < 3 * self.max:
                        creature.dying = True
                        self.cr.energy += 30
                        self.cr.happiness -= 70
            for food in self.game.food:
                f_posx = food.posx
                f_posy = food.posy
                difx = f_posx - self.cr.posx
                dify = f_posy - self.cr.posy
                rdifx = difx if difx > 0 else difx * -1
                rdify = dify if dify > 0 else dify * -1
                if difx == self.cr.n_food_x and rdifx + rdify < 3 * self.max:
                    self.cr.energy += 5
                    self.cr.happiness += 5
                    self.game.canvas.delete(food.ID)
                    try:
                        del self.game.food[self.game.food.index(food)]
                    except ValueError:
                        pass


class cel_3:
    # brain (Neural Network)
    def __init__(self, game, cr_ID, nothing_important):
        self.cr = cr_ID
        self.color = 'orange'
        self.game = game
        self.weights = self.cr.weights[0]

    def function(self):
        inp_vec = [[self.cr.n_creature_x], [self.cr.n_creature_y], [self.cr.n_food_x], [self.cr.n_food_y]]
        outp = np.array(self.weights).dot(np.array(inp_vec))
        self.cr.x = round(int(outp[0]) / (50 / self.game.speed), 2)
        self.cr.y = round(int(outp[1]) / (50 / self.game.speed), 2)
        self.cr.eating = True if abs(outp[2]) >= 30 else False
        self.cr.mating = True if abs(outp[3]) >= 30 else False


class cel_4:
    # reproduction
    def __init__(self, game, cr_ID, maxx):
        self.cr = cr_ID
        self.max = maxx
        self.game = game
        self.color = 'hot pink'

    def function(self):
        try:
            self.time += 1
            if self.time <= 80:
                self.cr.mating = False
                self.game.canvas.move(self.heart, 0, -1)
            if self.time >= 200:
                self.game.canvas.move(self.heart, -1000, -1000)
                self.time = None
            if self.time == 50:
                self.game.n_creatures.append([self.DNA, self.cr.posx, self.cr.posy, self.weights, self.cr])
        except AttributeError:
            pass
        except TypeError:
            pass
        if self.cr.mating:
            for creature in self.game.creatures:
                if creature == self.cr:
                    continue
                cr_posx = creature.posx
                cr_posy = creature.posy
                difx = cr_posx - self.cr.posx
                dify = cr_posy - self.cr.posy
                rdifx = difx if difx > 0 else difx * -1
                rdify = dify if dify > 0 else dify * -1
                if difx == self.cr.n_creature_x and rdifx + rdify < 3 * self.max:
                    if len(self.cr.DNA) == len(creature.DNA):
                        self.DNA = [[] for x in range(0, len(self.cr.DNA))]
                    else:
                        self.DNA = [[] for x in range(0, len(self.cr.DNA))]
                    try:
                        for index in range(0, len(self.DNA)):
                            for _cel_ in range(0, len(creature.DNA)):
                                if len(self.DNA[index]) < 2:
                                    if creature.DNA[_cel_][0] == self.cr.DNA[index][0]:
                                        self.DNA[index].append(self.cr.DNA[index][0])
                                        if creature.DNA[_cel_][1] == self.cr.DNA[index][1]:
                                            self.DNA[index].append(self.cr.DNA[index][1])
                                            break
                            if len(self.DNA[index]) < 2:
                                if len(self.DNA[index]) == 0:
                                    self.DNA[index].append(random.randint(0, 4))
                                    self.DNA[index].append(self.cr.DNA[index][1] + random.randint(-6, 6))
                                else:
                                    self.DNA[index].append(self.cr.DNA[index][1] + random.randint(-6, 6))
                            if len(self.DNA[index]) > 2:
                                del self.DNA[index]
                        for _ in range(0, random.randint(1, 3)):
                            rn = random.randint(0, 2)
                            if rn == 0:
                                self.DNA.append([random.randint(0, 4), random.randint(5, 30)])
                            elif rn == 1:
                                del self.DNA[random.randint(0, len(self.DNA) - 1)]
                            else:
                                self.DNA[random.randint(0, len(self.DNA) - 1)][1] += random.randint(-5, 5)
                        self.weights = [[]]
                        for indexh, h in enumerate(self.cr.weights[0]):
                            self.weights[0].append([])
                            for indexw, w in enumerate(h):
                                if w - creature.weights[0][indexh][indexw] <= 0.75 and w - creature.weights[0][indexh][
                                    indexw] >= -0.75:
                                    self.weights[0][indexh].append(w)
                                else:
                                    self.weights[0][indexh].append(round(random.uniform(-1, 1), 2))
                        for _ in range(0, random.randint(1, 3)):
                            self.weights[0][random.randint(0, 3)][random.randint(0, 3)] += round(random.uniform(-2, 2),
                                                                                                 2)
                        self.cr.blood -= 20
                        self.cr.happiness += 40
                        self.cr.energy -= 10
                        self.heart = self.game.canvas.create_image(self.cr.posx, self.cr.posy, image=self.cr.heart_img,
                                                                   anchor='nw')
                        self.time = 0
                        self.cr.mating = False
                        if game.birth_state.get():
                            print('A new creature is born!')
                    except:
                        pass


plt.rc('xtick', labelsize=6)
plt.rc('ytick', labelsize=6)
game = Game()
game.main_loop()
