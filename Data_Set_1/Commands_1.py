cmds_1 = {
    "UK01": {
        "location" : "Lon",              # attack to sea
        "origin" : "Lon",
        "destination" : "Nth",
        "country": "UK",
        "owner" : "Katherine"
    },
    "UK02": {                       # ERROR attack  test for non neighbor destination
        "location" : "Lvp",
        "origin" : "Lvp",
        "destination" : "Lon",
        "country": "UK",
        "owner" : "Katherine"
    },
    "UK03": {                       # ERROR attack  test fleet to inland
        "location" : "Hol",
        "origin" : "Hol",
        "destination" : "Ruh",
        "country": "UK",
        "owner" : "Katherine"
    },
    "UK04": {                       # support attack for UK01
        "location" : "Edi",
        "origin" : "Lon",
        "destination" : "Nth",
        "country": "UK",
        "owner" : "Katherine"
    },
    "UK05": {                       # ERROR army on coast supports sea move
        "location" : "Den",
        "origin" : "Lon",
        "destination" : "Nth",
        "country": "UK",
        "owner" : "Katherine"
    },
    "FR01": {                       # support hold for FR03
        "location" : "Par",
        "origin" : "Bre",
        "destination" : "Bre",
        "country" : "FR",
        "owner" : "Mercy"
    },
    "FR02": {                       # CHECK army to coast case
        "location" : "Mar",                     
        "origin" : "Mar",
        "destination" : "Spa",
        "country" : "FR",
        "owner" : "Mercy"
    },
    "FR03": {                       # hold
        "location" : "Bre",
        "origin" : "Bre",
        "destination" : "Bre",
        "country" : "FR",
        "owner" : "Mercy"
    },
    "FR04": {                       # ERROR army to sea
        "location" : "Pic",
        "origin" : "Pic",
        "destination" : "Eng",
        "country" : "FR",
        "owner" : "Mercy"
    },
    "FR05": {                       # CHECK army on south/north coast
        "location" : "Spa",                     
        "origin" : "Spa",
        "destination" : "Gas",
        "country" : "FR",
        "owner" : "Mercy"
    },
    "GE01": {                       # attack - bounce
        "location" : "Kie",
        "origin" : "Kie",
        "destination" : "Hol",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE02": {                       # attack
        "location" : "Ber",
        "origin" : "Ber",
        "destination" : "Kie",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE03": {                       # support attack for GE02
        "location" : "Mun",
        "origin" : "Ber",
        "destination" : "Kie",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE04": {                       # attack supporting unit - bounce
        "location" : "Lvn",
        "origin" : "Lvn",
        "destination" : "Mos",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE05": {                       # support a nonexistent move, GE01 moves to holland instead
        "location" : "Hel",
        "origin" : "Kie",
        "destination" : "Den",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE06": {                       # support a nonexistent move, no unit exists on Boh
        "location" : "Sil",
        "origin" : "Boh",
        "destination" : "Boh",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "RU01": {                       # attack 
        "location" : "Stp-SC",
        "origin" : "Stp-SC",
        "destination" : "Bot",
        "country" : "RU",
        "owner" : "Michael"
    },
    "RU02": {                       # CHECK support holds support is cut by GE04
        "location" : "Mos",
        "origin" : "Sev",
        "destination" : "Sev",
        "country" : "RU",           
        "owner" : "Michael"
    },
    "RU03": {                       # support  for RU04
        "location" : "War",
        "origin" : "Mos",
        "destination" : "Ukr",
        "country" : "RU",
        "owner" : "Michael"            
    },
    "RU04": {                       # hold
        "location" : "Sev",
        "origin" : "Sev",
        "destination" : "Sev",
        "country" : "RU",
        "owner" : "Michael"
    },
    "RU05": {                       # ERROR wrong owner
        "location" : "Aeg",
        "origin" : "Aeg",
        "destination" : "Bul-SC",
        "country" : "RU",
        "owner" : "Kamran"
    }

}

# test  unit is at the right/wrong location