# Slunečnice.cz list obrázků

Vytvoří minimalistickou html stránku s obrázky všech programů v zadané kategorii z webu [Slunečnice.cz](https://www.slunecnice.cz/).

Pomůže pokud chcete vyhledat konkrétní program a pamatujete si obrázek.

Kliknutí na obrázek přesměruje na daný program.


## Použití:
Kategorie je zadána pomocí URL, například:
```
python slunecnice.py "/zabava-a-volny-cas/hry/hry-ke-stazeni/oddechovky-skakacky" | tee oddechovky.html
```

Grabování může trvat i několik minut, v závislosti na velikosti kategorie.
