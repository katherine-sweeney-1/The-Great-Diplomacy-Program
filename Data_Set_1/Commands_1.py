cmds_1 = {
    "UK01": {
        "location" : "Lon",              # success - attack to sea
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
    "UK04": {                       # success - support attack for UK01
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
    "FR01": {                       # support - hold for FR03
        "location" : "Par",
        "origin" : "Bre",
        "destination" : "Bre",
        "country" : "FR",
        "owner" : "Mercy"
    },
    "FR02": {                       # success - army to parent node
        "location" : "Mar",                     
        "origin" : "Mar",
        "destination" : "Spa",
        "country" : "FR",
        "owner" : "Mercy"
    },
    "FR03": {                       # success - hold
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
    "FR05": {                       # success - attack from parent node
        "location" : "Spa",                     
        "origin" : "Spa",
        "destination" : "Gas",
        "country" : "FR",
        "owner" : "Mercy"
    },
    "GE01": {                       # fail - bounces with UK03 CODE WRONG BECAUSE IT CANNOT DISPLACE OWN COUNTRYS UNITS
        "location" : "Kie",
        "origin" : "Kie",
        "destination" : "Hol",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE02": {                       # fail - can't displace own unit CODE WRONG CANT DISAPLCAE UNITS        
        "location" : "Ber",
        "origin" : "Ber",
        "destination" : "Kie",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE03": {                       # success - support attack for GE02 (attack fails)
        "location" : "Mun",
        "origin" : "Ber",
        "destination" : "Kie",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE04": {                       # fail - attack supporting unit bounce with RU02
        "location" : "Lvn",
        "origin" : "Lvn",
        "destination" : "Mos",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE05": {                       # fail (hold success) - support a nonexistent move
        "location" : "Hel",
        "origin" : "Kie",
        "destination" : "Den",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "GE06": {                       # fail (hold success) - support unit not on territory
        "location" : "Sil",
        "origin" : "Boh",
        "destination" : "Boh",
        "country" : "GE",
        "owner" : "Kamran"
    },
    "RU01": {                       # success - attack 
        "location" : "Stp-SC",
        "origin" : "Stp-SC",
        "destination" : "Bot",
        "country" : "RU",
        "owner" : "Michael"
    },
    "RU02": {                       # fail - support holds support is cut by GE04
        "location" : "Mos",
        "origin" : "Sev",
        "destination" : "Sev",
        "country" : "RU",           
        "owner" : "Michael"
    },
    "RU03": {                       # fail (support success) - support for nonexistent move
        "location" : "War",
        "origin" : "Mos",
        "destination" : "Ukr",
        "country" : "RU",
        "owner" : "Michael"            
    },
    "RU04": {                       # success - hold
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