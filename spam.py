import pyautogui as pt
import time

limit = input("Inserisci la quantita': ")
message = input("Messaggio: ")
i = 0
time.sleep(5)

while i < int(limit):
    pt.typewrite(message)
    # ti puzza er culo.

    pt.press("enter")

    i+=1