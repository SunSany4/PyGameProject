import start_window
import main_map
import Leshii
import Baba_ega
import fight
import start_dialog
import end_dialog
import lose_dialog
import time

time_start = time.time()
start_window.main()
start_dialog.main()
level = main_map.main()
if level == 1:
    result = Leshii.run_leshii(['Какой ветер тебя ко мне в лес занес? \nА не лук со стрелами нужен тебе?',
                                'Сослужи службу: колесо водяной сломалось,\n сможешь собрать отплочу чем хочешь',
                                'Начать.'])
    lst = open('level_pos.txt', 'r', encoding='utf-8').readline()
    while '2' not in lst:
        level = main_map.main()
        if level == 1:
            result = Leshii.run_leshii(['Какой ветер тебя ко мне в лес занес? \nА не лук со стрелами нужен тебе?',
                                        'Сослужи службу: колесо водяной сломалось,\n сможешь собрать отплочу чем хочешь',
                                        'Начать.'])
level = main_map.main()
if level == 2:
    text = ['Что то русским духом по пахивает.\n Знаю нужны тебе доспехи,\n Помощь нужна мне, мыши одолели.',
            'Сможешь отловить, получишь, что хочешь.\n Не успеешь справиться,\nсуп у меня вкусный будет на ужин.',
            'Начать.']
    result = Baba_ega.baba_ege_run(text)
    lst = open('level_pos.txt', 'r', encoding='utf-8').readline()
    while '3' not in lst:
        level = main_map.main()
        if level == 2:
            result = Baba_ega.baba_ege_run(text)
level = main_map.main()
if level == 3:
    result = fight.main()
    while not result:
        lose_dialog.main()
        level = main_map.main()
        if level == 3:
            result = fight.main()
time_end = time.time()
time_game = int(time_end - time_start)
end_dialog.main(time_game)
