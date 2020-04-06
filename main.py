import tkinter as tk
import os
import time

def load_party():
    party_list = []
    if os.path.exists('party.txt'):
        with open('party.txt', mode='r') as party_doc:
            for line in party_doc:
                if len(line.strip()) > 0:
                    member = line.split(',')
                    party_list.append([member[0].strip(), member[1].strip()])
        return party_list
    else:
        return []


def reset(combatant_entries, num_of_comb, combatants):
    num_of_comb.destroy()
    num_of_comb.reset()
    combatants.reset()
    for c in combatant_entries.entries:
        combatant_entries.entries[c].destroy()
    combatant_entries.reset()
    

def create(combatant_entries, num_of_comb, combatants):
    n_combatants = int(num_of_comb.get())
    num_of_comb.destroy()
    party = load_party()
    all_combatants = []
    for i in range(n_combatants):
        if i < len(party):
            all_combatants.append(party[i])
        else:
            all_combatants.append(['Opponent {}'.format(i-len(party)+1), '??'])
    for c in all_combatants:
        combatant_entries.append(c[0], Combatant_entry_class(c[0]))


def start(combatant_entries, num_of_comb, combatants):
    all_combatants = {}
    for c in combatant_entries.entries:
        new = combatant_entries.entries[c].load()
        all_combatants[new[0]] = new[1]
    sort_comb = sorted(all_combatants.items(), key=lambda x: x[1], reverse=True)
    print(sort_comb)
    combatant_entries.reset()
    time.sleep(10)
    party = load_party()
    for pair in (sort_comb):
        for member in party:
            if pair[0] == member[0]:
                print('rovna se')
                c = Combatant_class(pair[0], pair[1], True, member[1])
            else:
                print('nerovna se')
                c = Combatant_class(pair[0], pair[1], False, member[1])
            combatants.append(pair[0], c)



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


#class Combatants_class():
#    def __init__(self):
#        self.combatants = []
#    def append(self, new):
#        self.combatants.append(new)
#    def reset(self):
#        for c in self.combatants:
#            c.destroy()
#        self.combatants = []


class Combatant_class():
    def __init__(self, name, initiative, friend, ac):
        self.init_box = tk.Entry(plocha)
        self.init_box.insert(0, initiative)
        self.init_box.config(state='readonly')
        self.name_box = tk.Entry(plocha)
        self.name_box.insert(0, name)
        if friend:
            self.name_box.config(state='readonly', fg='blue')
        else:
            self.name_box.config(state='readonly', fg='red')
        self.ac_box = tk.Entry(plocha)
        self.ac_box.insert(0, ac)
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
        self.ac_box.pack()
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



class Num_edit_class():
    def __init__(self):
        self.num = 10
        self.num_entry = tk.Entry(plocha)
        self.num_entry.insert(0, str(self.num))
        self.num_entry.config(state='readonly', width=2)
        self.plus = tk.Button(plocha, text='+', command=lambda: add(self.num_entry))
        self.minus = tk.Button(plocha, text='-', command=lambda: sub(self.num_entry))
        self.num_entry.pack()
        self.plus.pack()
        self.minus.pack()
    def destroy(self):
        self.num_entry.destroy()
        self.plus.destroy()
        self.minus.destroy()
    def reset(self):
        self.num = 10
        self.num_entry = tk.Entry(plocha)
        self.num_entry.insert(0, str(self.num))
        self.num_entry.config(state='readonly', width=2)
        self.plus = tk.Button(plocha, text='+', command=lambda: add(self.num_entry))
        self.minus = tk.Button(plocha, text='-', command=lambda: sub(self.num_entry))
        self.num_entry.pack()
        self.plus.pack()
        self.minus.pack()
    def get(self):
        return self.num_entry.get()


class Entries_holder():
    def __init__(self):
        self.entries = {}
    def reset(self):
        for ent in self.entries:
            self.entries[ent].destroy()
        self.entries = {}
    def append(self, new_key, new_val):
        self.entries[new_key] = new_val



class Combatant_entry_class():
    def __init__(self, comb_name):
        self.ent_comb = tk.Entry(plocha)
        self.ent_comb.insert(0, comb_name)
        self.ent_comb.config(state='normal')
        self.ent_comb.pack()
        self.ent_init = Num_edit_class()
    def destroy(self):
        self.ent_comb.destroy()
        self.ent_init.destroy()
    def load(self):
        name = self.ent_comb.get()
        initiative = int(self.ent_init.get())
        return [name, initiative]



root = tk.Tk()
root.geometry('400x500')


menuLista = tk.Menu(root)
menuLista.add_command(label='Reset', command=lambda: reset(combatant_entries, num_of_comb, combatants))
menuLista.add_command(label='Create Combat', command=lambda: create(combatant_entries, num_of_comb, combatants))
menuLista.add_command(label='Start Combat', command=lambda: start(combatant_entries, num_of_comb, combatants))
menuLista.add_command(label='Exit', command=root.destroy)
root.config(menu=menuLista)


plocha = tk.Frame()
plocha.pack()


combatant_entries = Entries_holder()
num_of_comb = Num_edit_class()
combatants = Entries_holder()




tk.mainloop()