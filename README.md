# WeatherApp-EYWA

Automatizirano dohvaćanje i slanje meteoroloških podataka s DHMZ web stranice na EYWA platformu putem GraphQL upita.

# Kako pokrenuti aplikaciju

1. Instaliraj potrebne biblioteke:
   
   pip install selenium,  eywa
   

2. Postavi ispravnu putanju do svog `chromedriver.exe` u kodu.

3. Pokreni Python skriptu:
   
   main.py
   

# Za provjeru da su podaci uspješno poslani, možete koristiti sljedeći GraphQL upit:

     graphql

{
  searchMjerenje {
    postaja
    vjetar_smjer
    vjetar_brzina
    temperatura
    vlaznost
    tlak
    tendencija
    stanje
  }
}


## Korišteni resursi

- (https://meteo.hr/podaci.php?section=podaci_vrijeme&param=hrvatska1_n) – službeni izvor vremenskih podataka
- EYWA platforma – za modeliranje i pohranu podataka
- EYWA GraphQL konzola – za testiranje i dohvat podataka
- Selenium dokumentacija -https://selenium.dev/documentation/ – za automatizaciju preglednika
- Udemy
= GraphQL - https://graphql.org/learn/#learn-graphql - za testiranje u EYWA
- EYWA - https://www.eywaonline.com/docs/intro
