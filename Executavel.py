import time

import pyautogui as pa

opcoes = pa.confirm(text="Escolha o programa", title="Opções",
            buttons=["Excel", "Word","Notepad"])

if  opcoes == "Excel":
    pa.sleep(2)
    pa.hotkey('win', 'r')
    pa.sleep(1)
    pa.write("Excel")
    pa.sleep(1)
    pa.press('Enter')
    pa.click(x=775, y=343)
    pa.sleep(2.5)
    pa.click(x=1553, y=771)
    pa.sleep(1)
    pa.click(x=775, y=343)
    pa.sleep(1)
    pa.click(x=563, y=374)
    pa.sleep(1)
    pa.write("Ola Mundo")


elif opcoes == "Word":
    pa.sleep(2)
    pa.hotkey('win', 'r')
    pa.sleep(1)
    pa.write("WINWORD.EXE")
    pa.sleep(1)
    pa.press('Enter')
    pa.sleep(2)
    pa.click(x=1278, y=777)
    pa.PAUSE(1)
    pa.click(x=514, y=229)
    pa.write("Ola Mundo")

else:
    pa.sleep(2)
    pa.hotkey('win', 'r')
    pa.sleep(1)
    pa.write("notepad.exe")
    pa.sleep(1)
    pa.press('Enter')
    pa.sleep(1)
    pa.write("Ola Mundo")


