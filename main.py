import start_window
import main_map
import Leshii
import Baba_ega
import fight
import start_dialog
import end_dialog
import lose_dialog
import time

while True:
    time_start = time.time()
    start_window.main()
    start_dialog.main()
    level = main_map.main()
    if level == 1:
        text_l = ['Какой ветер тебя ко мне в лес занес? \nА не лук со стрелами нужен тебе?',
                  'Сослужи службу: колесо водяной сломалось,\n сможешь собрать отплочу чем хочешь',
                  'Начать.']
        result = Leshii.run_leshii(text_l)
        lst = open('level_pos.txt', 'r', encoding='utf-8').readline()
        while '2' not in lst:
            level = main_map.main()
            if level == 1:
                result = Leshii.run_leshii(text_l)
            lst = open('level_pos.txt', 'r', encoding='utf-8').readline()
    level = main_map.main()
    if level == 2:
        text_b = ['Что то русским духом по пахивает.\n Знаю нужны тебе доспехи,\n Помощь нужна мне, мыши одолели.',
                  'Сможешь отловить, получишь, что хочешь.\n Не успеешь справиться,\nсуп у меня вкусный будет на ужин.',
                  'Начать.']
        result = Baba_ega.baba_ege_run(text_b)
        lst = open('level_pos.txt', 'r', encoding='utf-8').readline()
        while '3' not in lst:
            level = main_map.main()
            if level == 2:
                result = Baba_ega.baba_ege_run(text_b)
            lst = open('level_pos.txt', 'r', encoding='utf-8').readline()
    level = main_map.main()
    if level == 3:
        result = fight.main()
        while not result:
            lose_dialog.main()
            level = main_map.main()
            if level == 3:
                result = fight.main()
    time_game = int(time.time() - time_start)
    if open('min_time.txt').readline() != '---':
        if int(open('min_time.txt').readline()) > time_game:
            with open('min_time.txt', 'w') as f:
                f.writelines([str(int(time_game))])
    else:
        with open('min_time.txt', 'w') as f:
            f.writelines([str(int(time_game))])
    end_dialog.main(time_game)
    with open('level_pos.txt', 'w', encoding='utf-8') as file:
        print('1', file=file, end='')
