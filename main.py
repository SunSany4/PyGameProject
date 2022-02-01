import start_window
import main_map
import Leshii
import Baba_ega
import fight
import start_dialog
import end_dialog
import lose_dialog


def write2file(string):
    with open('level_pos.txt', 'a', encoding='utf-8') as file:
        print(f' {string}', file=file)


start_window.main()
start_dialog.main()
level = main_map.main()
if level == 1:
    Leshii.main()
write2file('2')
level = main_map.main()
if level == 2:
    Baba_ega.main()
write2file('3')
level = main_map.main()
if level == 3:
    result = fight.main()
    while not result:
        lose_dialog.main()
        level = main_map.main()
        if level == 3:
            result = fight.main()
end_dialog.main()
