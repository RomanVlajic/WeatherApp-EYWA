import eywa
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

putanja = "C:\\Users\\elena\\Downloads\\chromedriver-win64\\chromedriver.exe"
web_stranica = 'https://meteo.hr/podaci.php?section=podaci_vrijeme&param=hrvatska1_n'

async def posalji_podatke():
    eywa.open_pipe()

    servis = Service(putanja)
    driver = webdriver.Chrome(service=servis)
    driver.get(web_stranica)
    time.sleep(5)

    redovi = driver.find_elements(By.TAG_NAME, "tr")
    mjerenja = []

    for red in redovi:
        stupci = red.find_elements(By.TAG_NAME, "td")
        vrijednosti = [s.text.replace("\n", " ").strip() for s in stupci if s.text.strip()]
        if len(vrijednosti) == 8:
            mjerenja.append({
                "postaja": vrijednosti[0],
                "vjetar_smjer": vrijednosti[1],
                "vjetar_brzina": vrijednosti[2],
                "temperatura": vrijednosti[3],
                "vlaznost": vrijednosti[4],
                "tlak": vrijednosti[5],
                "tendencija": vrijednosti[6],
                "stanje": vrijednosti[7]
            })

    driver.quit()

    try:
        await eywa.graphql("""
        mutation($podaci:[MjerenjeInput]) {
            syncMjerenjeList(data:$podaci) {
                euuid
            }
        }
        """, {"podaci": mjerenja})
    except:
        pass

    eywa.exit()

if __name__ == "__main__":
    asyncio.run(posalji_podatke())

