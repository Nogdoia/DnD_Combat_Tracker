import tkinter as tk
import os

def load_party():
    party_list = []
    if os.path.exists('party.txt'):
        with open('party.txt', mode='r') as party_doc:
            for line in party_doc:
                if len(line.strip()) > 0:
                    pair = line.split(',')
                    party_list.append(pair[0].strip())
        return party_list
    else:
        return []
def load_AC():
    ac_dict = {}
    if os.path.exists('party.txt'):
        with open('party.txt', mode='r') as party_doc:
            for line in party_doc:
                if len(line.strip()) > 0:
                    pair = line.split(',')
                    ac_dict[pair[0]] = pair[1]
        return ac_dict
    else:
        return {}



def reset(par_list_entry, num_of_par, combatants, header):
    header.destroy()
    num_of_par.destroy()
    header.reset()
    num_of_par.reset()
    combatants.reset()
    ple = par_list_entry.entries
    for p in ple:
        ple[p].destroy()
    par_list_entry.reset()
    

def create(par_list_entry, num_of_par, combatants, header):
    n_participants = int(num_of_par.get())
    num_of_par.destroy()
    header.destroy()
    header.creation()
    party = load_party()
    participants = []
    for i in range(n_participants):
        if i < len(party):
            participants.append(party[i])
        else:
            participants.append('Opponent {}'.format(i-len(party)+1))
    for j in range(len(participants)):
        par_list_entry.append(participants[j], Entry_class(participants[j], j+1))


def start(par_list_entry, num_of_par, combatants, header):
    header.destroy()
    header.start()
    participants = {}
    ple = par_list_entry.entries
    for p in ple:
        new = ple[p].load()
        participants[new[0]] = new[1]
    sort_par = sorted(participants.items(), key=lambda x: x[1], reverse=True)
    par_list_entry.reset()
    party = load_AC()
    i = 2
    for pair in sort_par:
        if pair[0] in party:
            c = Combatant_class(pair[0], pair[1], True, i, party[pair[0]])
        else:
            c = Combatant_class(pair[0], pair[1], False, i, '??')
        combatants.append(c)
        i += 1



def add(num_obj):
    number = int(num_obj.get())
    num_obj.config(state='normal')
    num_obj.delete(0, last='end')
    num_obj.insert(0, str(number+1))
    if number < 0:
        num_obj.config(state='readonly', fg='red')
    else:
        num_obj.config(state='readonly', fg='blue')
def sub(num_obj):
    number = int(num_obj.get())
    num_obj.config(state='normal')
    num_obj.delete(0, last='end')
    num_obj.insert(0, str(number-1))
    if number < 2:
        num_obj.config(state='readonly', fg='red')
    else:
        num_obj.config(state='readonly', fg='blue')


class Header_class():
    def __init__(self):
        self.pocet = tk.Label(plocha, text='Počet bojovníků:')
        self.pocet.grid(row=0, column=0)
        self.round_frame = tk.Frame(plocha)
        self.name = tk.Label(plocha, text='Jméno')
        self.initiative = tk.Label(plocha, text='Iniciativa')
        self.ac = tk.Label(plocha, text='OČ')
        self.hp = tk.Label(plocha, text='Životy')
        self.cond = tk.Label(plocha, text='Stav')
    def reset(self):
        self.pocet = tk.Label(plocha, text='Počet bojovníků:')
        self.pocet.grid(row=0, column=0)
        self.round_frame = tk.Frame(plocha)
        self.name = tk.Label(plocha, text='Jméno')
        self.initiative = tk.Label(plocha, text='Iniciativa')
        self.ac = tk.Label(plocha, text='OČ')
        self.hp = tk.Label(plocha, text='Životy')
        self.cond = tk.Label(plocha, text='Stav')
    def destroy(self):
        self.pocet.destroy()
        self.round_frame.destroy()
        self.name.destroy()
        self.initiative.destroy()
        self.ac.destroy()
        self.hp.destroy()
        self.cond.destroy()       
    def creation(self):
        self.round_frame = tk.Frame(plocha)
        self.name = tk.Label(plocha, text='Jméno')
        self.initiative = tk.Label(plocha, text='Iniciativa')
        self.name.grid(row=0, column=0)
        self.initiative.grid(row=0, column=1)
    def start(self):
        self.round_frame = tk.Frame(plocha)
        self.round_label = tk.Label(self.round_frame, text='Kolo:')
        self.round_box = tk.Entry(self.round_frame)
        self.round_box.insert(0, 1)
        self.round_box.config(state='readonly', width=2)
        self.round_add = tk.Button(self.round_frame, text='+', command=lambda: add(self.round_box))
        self.round_sub = tk.Button(self.round_frame, text='-', command=lambda: sub(self.round_box))
        self.name = tk.Label(plocha, text='Jméno')
        self.initiative = tk.Label(plocha, text='Iniciativa')
        self.ac = tk.Label(plocha, text='OČ')
        self.hp = tk.Label(plocha, text='Životy')
        self.cond = tk.Label(plocha, text='Stav')
        self.round_frame.grid(row=0, column=1, columnspan=2)
        self.round_label.pack(side='left')
        self.round_box.pack(side='left')
        self.round_add.pack(side='left')
        self.round_sub.pack(side='left')
        self.initiative.grid(row=1, column=0)
        self.name.grid(row=1, column=1)
        self.ac.grid(row=1, column=2)
        self.hp.grid(row=1, column=3)
        self.cond.grid(row=1, column=4)




class Combatants_class():
    def __init__(self):
        self.combatants = []
    def append(self, new):
        self.combatants.append(new)
    def reset(self):
        for c in self.combatants:
            c.destroy()
        self.combatants = []


class Combatant_class():
    def __init__(self, name, initiative, friend, pos, ac):
        self.basic_frame = tk.Frame(plocha)
        self.init_box = tk.Entry(self.basic_frame)
        self.init_box.insert(0, initiative)
        self.init_box.config(state='readonly', width=2, relief='flat')
        self.name_box = tk.Entry(self.basic_frame)
        self.name_box.insert(0, name)
        if friend:
            self.name_box.config(state='readonly', fg='green', width=20, relief='ridge')
        else:
            self.name_box.config(state='readonly', fg='red', width=20, relief='ridge')
        self.ac_box = tk.Entry(self.basic_frame)
        self.ac_box.insert(0, ac)
        self.ac_box.config(state='readonly', width=2, relief='raised')
        self.hp_frame = tk.Frame(plocha)
        self.hp_box = tk.Entry(self.hp_frame)
        self.hp_box.insert(0, 10)
        self.hp_box.config(state='readonly', width=2, fg='blue')
        self.hp_add = tk.Button(self.hp_frame, text='+', command=lambda: add(self.hp_box))
        self.hp_sub = tk.Button(self.hp_frame, text='-', command=lambda: sub(self.hp_box))
        self.var = tk.StringVar(plocha)
        self.var.set('Žádný')
        self.cond_box = tk.OptionMenu(plocha, self.var, 'Žádný', 'Hluchý', 'Ležící', 'Mrtvý', 'Neschopný', 'Neviditelný', 'Ochromený', 'Otrávený', 'Paralyzovaný', 'Slepý', 'Uchvácený', 'V bezvědomí', 'Vystrašený', 'Zadržený', 'Zkamenělý', 'Zmámený')
        self.basic_frame.grid(row=pos, column=0, columnspan=3)
        self.init_box.pack(side='left', padx=20)
        self.name_box.pack(side='left')
        self.ac_box.pack(side='right', padx=20)
        self.hp_frame.grid(row=pos, column=3)
        self.hp_box.pack(side='left')
        self.hp_add.pack(side='left')
        self.hp_sub.pack(side='left')
        self.cond_box.grid(row=pos, column=4, padx=20)
    def destroy(self):
        self.basic_frame.destroy()
        self.init_box.destroy()
        self.name_box.destroy()
        self.ac_box.destroy()
        self.hp_frame.destroy()
        self.hp_box.destroy()
        self.hp_add.destroy()
        self.hp_sub.destroy()
        self.cond_box.destroy()



class Num_of_par_class():
    def __init__(self):
        self.def_num_of_par = len(load_party())
        self.num = self.def_num_of_par
        self.num_of_par = tk.Entry(plocha)
        self.num_of_par.insert(0, str(self.def_num_of_par))
        self.num_of_par.config(state='readonly', width=2)
        self.plus_par = tk.Button(plocha, text='+', command=lambda: add(self.num_of_par))
        self.minus_par = tk.Button(plocha, text='-', command=lambda: sub(self.num_of_par))
        self.num_of_par.grid(row=0, column=1)
        self.plus_par.grid(row=0, column=2)
        self.minus_par.grid(row=0, column=3)
    def destroy(self):
        self.num_of_par.destroy()
        self.plus_par.destroy()
        self.minus_par.destroy()
    def reset(self):
        self.def_num_of_par = len(load_party())
        self.num = self.def_num_of_par
        self.num_of_par = tk.Entry(plocha)
        self.num_of_par.insert(0, str(self.def_num_of_par))
        self.num_of_par.config(state='readonly', width=2)
        self.plus_par = tk.Button(plocha, text='+', command=lambda: add(self.num_of_par))
        self.minus_par = tk.Button(plocha, text='-', command=lambda: sub(self.num_of_par))
        self.num_of_par.grid(row=1, column=0)
        self.plus_par.grid(row=1, column=1)
        self.minus_par.grid(row=1, column=2)
    def get(self):
        return self.num_of_par.get()


class Entries_class():
    def __init__(self):
        self.entries = {}
    def reset(self):
        for ent in self.entries:
            self.entries[ent].destroy()
        self.entries = {}
    def append(self, new_key, new_val):
        self.entries[new_key] = new_val



class Entry_class():
    def __init__(self, p, pos):
        self.ent_par = tk.Entry(plocha)
        self.ent_par.insert(0, p)
        self.ent_par.config(state='normal')
        self.init_frame = tk.Frame(plocha)
        self.ent_init = tk.Entry(self.init_frame)
        self.ent_init.insert(0, '10')
        self.ent_init.config(state='readonly', width=2)
        self.ent_add = tk.Button(self.init_frame, text='+', command=lambda: add(self.ent_init))
        self.ent_sub = tk.Button(self.init_frame, text='-', command=lambda: sub(self.ent_init))
        self.ent_par.grid(row=pos, column=0)
        self.init_frame.grid(row=pos, column=1)
        self.ent_init.pack(side='left')
        self.ent_add.pack(side='left')
        self.ent_sub.pack(side='left')
    def destroy(self):
        self.ent_par.destroy()
        self.init_frame.destroy()
        self.ent_init.destroy()
        self.ent_add.destroy()
        self.ent_sub.destroy()
    def load(self):
        name = self.ent_par.get()
        initiative = int(self.ent_init.get())
        return [name, initiative]



root = tk.Tk()
root.geometry('430x300')
root.title('Combat Tracker')


menuLista = tk.Menu(root)
menuLista.add_command(label='Reset', command=lambda: reset(par_list_entry, num_of_par, combatants, header))
menuLista.add_command(label='Založit', command=lambda: create(par_list_entry, num_of_par, combatants, header))
menuLista.add_command(label='Začít souboj', command=lambda: start(par_list_entry, num_of_par, combatants, header))
menuLista.add_command(label='Exit', command=root.destroy)
root.config(menu=menuLista)


plocha = tk.Frame()
plocha.pack()


par_list_entry = Entries_class()
num_of_par = Num_of_par_class()
combatants = Combatants_class()
header = Header_class()




tk.mainloop()