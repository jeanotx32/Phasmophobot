import pydirectinput, pyautogui, pyscreenshot
import time
from PIL import Image
import os 
import psutil
from pywinauto import Application
import random

process_name = "Phasmophobia.exe"
list_entité_4k= 1
quatre_k = {'choix_carte' : {'h':1780 ,'l':1698},'demarrer2' : {'h':1900 ,'l':2950}, 'preuve': {'h':117,'l':2021}, 'passer' : {'h':1941,'l':790}, 'suivant' : {'h':1904,'l':2894},'pret': {'h':1930,'l':1698}, 'LVLUP': {'h':1497,'l':1917}, 'PartieSolo': {'h':660,'l':934}, 'PLACEHOLDER': {'h':20,'l':20}}
#deux_k = {'choix_carte' : {'h':1075 ,'l':2019},'demarer' : {'h':1280,'l':1977}, 'preuve': {'h':250,'l':250}, 'passer' : {'h':250,'l':250}, 'suivant' : {'h':250,'l':250},'pret': {'h':1271,'l':1271}}
list_entité_4k = {'Spirit':{'h':1100,'l':2200},'Wraith':{'h':1100,'l':2500},'Phantom':{'h':1100,'l':2700},'Poltergeist':{'h':1200,'l':2200},'Banshee':{'h':1200,'l':2500},'Jinn':{'h':1200,'l':2700},'Mare':{'h':1300,'l':2200},'Revenant':{'h':1300,'l':2500},'Shade':{'h':1300,'l':2700},'Demon':{'h':1400,'l':2200},'Yurei':{'h':1400,'l':2500},'Oni':{'h':1400,'l':2700},'Yokai':{'h':1500,'l':2200},'Hantu':{'h':1500,'l':2500},'Goryo':{'h':1500,'l':2700},'Myling':{'h':1600,'l':2200},'Onryo':{'h':1600,'l':2500},'The Twins':{'h':1600,'l':2700},'Raiju':{'h':1700,'l':2200},'Obake':{'h':1700,'l':2500},'The Mimic':{'h':1700,'l':2700},'Moroi':{'h':1800,'l':2200},'Deogen':{'h':1800,'l':2500},'Thaye':{'h':1800,'l':2700}}
cycle = 0

def click(coord=0):
    if coord != 0:
        pydirectinput.moveTo(coord['l'],coord['h'])
    if coord != 'Spirit' :
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()

def random_guess_mouse_AutoGUI_loaction():
    try:
        while True:
            x, y = pydirectinput.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def screenshot_entitee():
    # part of the screen
    im = pyscreenshot.grab(bbox=(1188, 1812, 2668, 1993))  # X1,Y1,X2,Y2

    # save image file
    im.save(r"tmp\color.png")

def start():
    resolution=100
    #while resolution not in ['1','2']:
    #    resolution = input("Quel resolution \n 1)2k \n 2)4k\n")

    #if resolution == '1':
    #    coordone_menu=deux_k
    #    coordone_entite=list_entité_2k
    #elif resolution == '2':
    coordone_menu=quatre_k
    coordone_entite=list_entité_4k
    startLoopwMain()
    return(coordone_menu, coordone_entite)
    time.sleep(5)
    #startLoopwMain()
#==========================================================================Find Process================================================================

def findProcess(name):
    procs = list()
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            if proc.name() == name and proc.status() == psutil.STATUS_RUNNING:
                pid = proc.pid
                procs.append(pid)
        except:
            pass
    return procs

#==========================================================================Restart Game================================================================
gameExe = 'T:\SteamLibrary\steamapps\common\Phasmophobia\Phasmophobia.exe'
process_name = "Phasmophobia.exe"
def restartGame(coordone_menu):
    if process_status(process_name) == True :
        PROCNAME = "Phasmophobia.exe"
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME:
                proc.kill()
                time.sleep(5)
    os.startfile(gameExe)
    time.sleep(50)
    pydirectinput.press('space')
    click(coord=coordone_menu['PartieSolo'])
    time.sleep(4)
    print("Game Restarted, In solo Game")
    return()


#==========================================================================Check Process================================================================
process_name = "Phasmophobia.exe"

def process_status(process_name):
    #phasmophobiaPID = psutil.Process.pid(process_name)
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

#==========================================================================GET COLOR================================================================

def screenshotBoucle():
    # part of the screen
    im = pyscreenshot.grab(bbox=(1188, 1812, 2668, 1993))  # X1,Y1,X2,Y2
    # save image file
    im.save(r"tmp\color.png")
    time.sleep(.3)    

def screenshotWalk():
    # part of the screen
    im = pyscreenshot.grab(bbox=(1000, 400, 1300, 450))  # X1,Y1,X2,Y2
    # save image file
    im.save(r"tmp\colorwalk.png")
    time.sleep(.1)

def screenshotStart():
    # part of the screen
    im = pyscreenshot.grab(bbox=(806, 1306, 809, 1309))  # X1,Y1,X2,Y2
    # save image file
    im.save(r"tmp\colorstart.png")
    time.sleep(.1)  


def waitUntilNotBlack():
    screenshotBoucle()
    im = Image.open(r"tmp\color.png")
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((5, 5))
    os.remove(r"tmp\color.png")
    if (r, g, b) > (20, 20, 20) :
        print('notBlack')
        return(True)
    return(False)

def waitUntilIstBlack():
    screenshotWalk()
    im = Image.open(r"tmp\colorwalk.png")
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((150, 10))
    #os.remove(r"tmp\color.png")
    if (r, g, b) < (20, 20, 20) :
        print('IsBlack')
        print(r, g, b)
        return(True)
    return(False)

def waitUntilNotBlackStart():
    screenshotStart()
    im = Image.open(r"tmp\colorstart.png")
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((2, 2))
    os.remove(r"tmp\colorstart.png")
    if (r, g, b) > (20, 20, 20) :
        print('EndStartLoadingScreen')
        return(True)
    return(False)
#===================================================================MAIN STUFF============================================================
def main_random_guess(coordone_menu,coordone_entite, cycle):
    tottime=time.time()
    time.sleep(.1)
    print("===========NB de Cycle :")
    print(cycle)
    print("========")
    print('cycle now')
    #=============================================================Dans le Menu principal==========================================================
    pydirectinput.press('left')
    time.sleep(.2)
    click(coord=coordone_menu['choix_carte'])
    time.sleep(.2)
    pydirectinput.press('right')
    time.sleep(.2)
    click(coord=coordone_menu['pret'])
    click(coord=coordone_menu['demarrer2'])
    time.sleep(2)
    while(waitUntilNotBlackStart() == False):
        waitUntilNotBlackStart()
    
    while(waitUntilNotBlack() == False):
        waitUntilNotBlack()
    time.sleep(.1)
    #=============================================================Dans le Camion==========================================================
    
    pydirectinput.keyDown('a')
    stopWalkTrigg = time.time()
    stopwalk = False
    #while (waitUntilIstBlack() == False ) :
    #    waitUntilIstBlack()
    #    if(time.time() - stopWalkTrigg > 6 ):
    #        
    #        print("Exit Via Trigger TimeOut")
    #        break

    time.sleep(6)
    pydirectinput.keyUp('a')
    #souris 90
    #return()
    pydirectinput.moveRel(1800, 150, relative=True)
    click()
    time.sleep(.2)
    pydirectinput.press('j')
    time.sleep(.5)
    #clique sur preuve
    click(coord=coordone_menu['preuve'])
    time.sleep(.1)
    #clique sur une preuve (a def)
    #click(coord=list_entité_4k[random.choice(list(list_entité_4k))])
    click(coord=list_entité_4k['Shade'])
    time.sleep(.5)
    pydirectinput.press('j')
    time.sleep(8)
    click()
    time.sleep(10)
    while(waitUntilNotBlack() == False):
        waitUntilNotBlack()
    time.sleep(.2)
    #=============================================================Dans la fin==========================================================
    #clique sur passer
    click(coord=coordone_menu['passer'])
    time.sleep(.2)
    click(coord=coordone_menu['LVLUP'])
    time.sleep(.2)
    click(coord=coordone_menu['LVLUP'])
    time.sleep(.2)
    #=====
    click(coord=coordone_menu['passer'])
    #Screen shot pour les stats =============================
    #screenshot_entitee()
    time.sleep(.1)
    #clique sur suivant
    click(coord=coordone_menu['suivant'])
    print("finish")
    print(f'Durrée : {time.time() - tottime}\n')
    if time.time() - tottime > 50 :
        restartGame(coordone_menu=quatre_k)
        print('over 50s, restarting game')


#=============================================================Stuff et tests==========================================================
def test(value):
    time.sleep(3)
    print(f"go {value}")
    pydirectinput.moveRel(value, 150, relative=True)
def test2():
    print ("Helo")

def test_coord_entité(listcE):
    time.sleep(3)
    for i in range(len(listcE)):
        print(list(listcE.values())[i])
        click(list(listcE.values())[i])
        time.sleep(1)


process_name = "Phasmophobia.exe"
def startLoopwMain() :
    time.sleep(5)
    print('start loop main')
    phasmoPID = findProcess("Phasmophobia.exe")
    #print(phasmoPID)
    app = Application().connect(process=phasmoPID[0])
    app.top_window().set_focus()
    process_name = "Phasmophobia.exe"
    cycle = 0
    while process_status(process_name) == True :
        cycle = cycle + 1
        main_random_guess(coordone_entite=list_entité_4k, coordone_menu=quatre_k, cycle=cycle)
        
    print('Phasmophobia not running, Ending program')

#start()
#time.sleep(5)

#exit()

#test(1800)
#test_coord_entité(list_entité_4k)
#random_guess_mouse_AutoGUI_loaction()
#print(quatre_k['choix_carte']['h'])
#print(list_entité_2k['Poltergeist']['h'])

#waitUntilNotBlack()