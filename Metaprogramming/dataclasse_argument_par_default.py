from dataclasses import dataclass, field

@dataclass
class Menu:
    prix_menu : int 
    list_menu : list = field(default_factory=list)

menu1 = Menu(60)
menu1.list_menu.append("Crevette")
print(menu1)

menu2 = Menu(120)
menu2.list_menu.append("Moule")
print(menu2)
