import tkinter as tk
import os

def load_party():
    party_list = []
    if os.path.exists('party.txt'):
        with open('party.txt', mode='r') as party_doc:
            for line in party_doc:
                if len(line.strip()) > 0:
                    party_list.append(line.strip())
        return party_list
    else:
        return []


def reset(par_list_entry, num_of_par, combatants):
    num_of_par.destroy()
    num_of_par.reset()
    combatants.reset()
    ple = par_list_entry.entries
    for p in ple:
        ple[p].destroy()
    par_list_entry.reset()
    

def create(par_list_entry, num_of_par, combatants):
    n_participants = int(num_of_par.get())
    num_of_par.destroy()
    party = load_party()
    participants = []
    for i in range(n_participants):
        if i < len(party):
            participants.append(party[i])
        else:
            participants.append('Opponent {}'.format(i-len(party)+1))
    for p in participants:
        par_list_entry.append(p, Entry_class(p))


def start(par_list_entry, num_of_par, combatants):
    participants = {}
    ple = par_list_entry.entries
    for p in ple:
        new = ple[p].load()
        participants[new[0]] = new[1]
    sort_par = sorted(participants.items(), key=lambda x: x[1], reverse=True)
    par_list_entry.reset()
    party = load_party()
    for pair in sort_par:
        if pair[0] in party:
            c = Combatant_class(pair[0], pair[1], True)
        else:
            c = Combatant_class(pair[0], pair[1], False)
        combatants.append(c)



def add(num_obj):
    number = int(num_obj.get())
    num_obj.config(state='normal')
    num_obj.delete(0, last='end')
    num_obj.insert(0, str(number+1))
    num_obj.config(state='readonly')
def sub(num_obj):
    number = int(num_obj.get())
    num_obj.config(state='normal')
    num_obj.delete(0, last='end')
    num_obj.insert(0, str(number-1))
    num_obj.config(state='readonly')


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
    def __init__(self, name, initiative, friend):
        self.init_box = tk.Entry(plocha)
        self.init_box.insert(0, initiative)
        self.init_box.config(state='readonly')
        self.name_box = tk.Entry(plocha)
        self.name_box.insert(0, name)
        if friend:
            self.name_box.config(state='readonly', fg='blue')
        else:
            self.name_box.config(state='readonly', fg='red')
        self.hp_box = tk.Entry(plocha)
        self.hp_box.insert(0, 10)
        self.hp_box.config(state='readonly')
        self.hp_add = tk.Button(plocha, text='+', command=lambda: add(self.hp_box))
        self.hp_sub = tk.Button(plocha, text='-', command=lambda: sub(self.hp_box))
        self.var = tk.StringVar(plocha)
        self.var.set('None')
        self.cond_box = tk.OptionMenu(plocha, self.var, 'None', 'Poisoned', 'Prone', 'Unconscious', 'Grappled')
        self.init_box.pack()
        self.name_box.pack()
        self.hp_box.pack()
        self.hp_add.pack()
        self.hp_sub.pack()
        self.cond_box.pack()
    def destroy(self):
        self.init_box.destroy()
        self.name_box.destroy()
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
        self.num_of_par.pack()
        self.plus_par.pack()
        self.minus_par.pack()
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
        self.num_of_par.pack()
        self.plus_par.pack()
        self.minus_par.pack()
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
    def __init__(self, p):
        self.ent_par = tk.Entry(plocha)
        self.ent_par.insert(0, p)
        self.ent_par.config(state='normal')
        self.ent_init = tk.Entry(plocha)
        self.ent_init.insert(0, '10')
        self.ent_init.config(state='readonly')
        self.ent_add = tk.Button(plocha, text='+', command=lambda: add(self.ent_init))
        self.ent_sub = tk.Button(plocha, text='-', command=lambda: sub(self.ent_init))
        self.ent_par.pack()
        self.ent_init.pack()
        self.ent_add.pack()
        self.ent_sub.pack()
    def destroy(self):
        self.ent_par.destroy()
        self.ent_init.destroy()
        self.ent_add.destroy()
        self.ent_sub.destroy()
    def load(self):
        name = self.ent_par.get()
        initiative = int(self.ent_init.get())
        return [name, initiative]



root = tk.Tk()
root.geometry('400x500')


menuLista = tk.Menu(root)
menuLista.add_command(label='Reset', command=lambda: reset(par_list_entry, num_of_par, combatants))
menuLista.add_command(label='Create Combat', command=lambda: create(par_list_entry, num_of_par, combatants))
menuLista.add_command(label='Start Combat', command=lambda: start(par_list_entry, num_of_par, combatants))
menuLista.add_command(label='Exit', command=root.destroy)
root.config(menu=menuLista)


plocha = tk.Frame()
plocha.pack()


par_list_entry = Entries_class()
num_of_par = Num_of_par_class()
combatants = Combatants_class()




tk.mainloop()