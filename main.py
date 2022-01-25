import start_window
import main_map
import Leshii
import Baba_ega
import fight


start_window.main()
level = main_map.main()
if level == 1:
    Leshii.main()
elif level == 2:
    Baba_ega.main()
else:
    fight.main()
