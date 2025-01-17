cmds_data_1 = {
    "UK01": {
        "location" : "Lon",              # attack
        "origin" : "Lon",
        "destination" : "Nth",
        "country": "UK",
        "owner" : "Katherine"
    },
    "UK02": {                       # support
        "location" : "Edi",
        "origin" : "Lon",
        "destination" : "Nth",
        "country": "UK",
        "owner" : "Katherine"
    },
    "UK03": {                       # ERROR attack  test for non neighbor destination
        "location" : "Lvp",
        "origin" : "Lvp",
        "destination" : "Lon",
        "country": "UK",
        "owner" : "Katherine"
    },
    "UK04": {                       # ERROR attack  test fleet to inland
        "location" : "Hol",
        "origin" : "Hol",
        "destination" : "Ruh",
        "country": "UK",
        "owner" : "Katherine"
    },
    "FR01": {                       # attack 
        "location" : "Par",
        "origin" : "Bre",
        "destination" : "Bre",
        "country" : "FR",
        "owner" : "Mercy"
    },
    "FR02": {                       # attack
        "location" : "Mar",                     
        "origin" : "Mar",
        "destination" : "Spa-SC",
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
    "GE01": {                       # attack
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
    "GE03": {                       # support
        "location" : "Mun",
        "origin" : "Ber",
        "destination" : "Kie",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE04": {                       # support
        "location" : "Ruh",
        "origin" : "Ruh",
        "destination" : "Ruh",
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
    "RU02": {                       # ERROR wrong owner 
        "location" : "Mos",
        "origin" : "Mos",
        "destination" : "Ukr",
        "country" : "RU",           
        "owner" : "Kamran"
    },
    "RU03": {                       # support 
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
    "RU05": {                       # ERROR neighbor involving special coasts
        "location" : "Aeg",
        "origin" : "Aeg",
        "destination" : "Bul-EC",
        "country" : "RU",
        "owner" : "Michael"
    }

}

# test  unit is at the right/wrong location