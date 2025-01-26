cmds_3a = {

    "AU01": {
        "location" : "Tri",             # success
        "origin" : "Tri",
        "destination" : "Alb",
        "country": "AU",
        "owner" : "Liam"
    },
    "AU02": {                           # success
        "location" : "Vie",
        "origin" : "Vie",
        "destination" : "Bud",
        "country": "AU",
        "owner" : "Liam"
    },
    "AU03": {                           # success
        "location" : "Bud",
        "origin" : "Bud",
        "destination" : "Ser",
        "country": "AU",
        "owner" : "Liam"
    },
    "UK01": {
        "location" : "Lon",             # success
        "origin" : "Lon",
        "destination" : "Eng",
        "country": "UK",
        "owner" : "Mercy"
    },
    "UK02": {                           # success
        "location" : "Edi",
        "origin" : "Edi",
        "destination" : "Nth",
        "country": "UK",
        "owner" : "Mercy"
    },
    "UK03": {                           # success
        "location" : "Lvp",
        "origin" : "Lvp",
        "destination" : "Yor",
        "country": "UK",
        "owner" : "Mercy"
    },
    "FR01": {
        "location" : "Bre",             # success
        "origin" : "Bre",
        "destination" : "Mao",
        "country": "AU",
        "owner" : "Sunny"
    },
    "FR02": {                           # success
        "location" : "Par",
        "origin" : "Par",
        "destination" : "Bre",
        "country": "AU",
        "owner" : "Sunny"
    },
    "FR03": {                           # success        
        "location" : "Mar",
        "origin" : "Mar",
        "destination" : "Spa",
        "country": "AU",
        "owner" : "Sunny"
    },
    "GE01": {                           # success
        "location" : "Kie",
        "origin" : "Kie",
        "destination" : "Den",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE02": {                           # success
        "location" : "Mun",
        "origin" : "Mun",
        "destination" : "Ruh",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE03": {                           # success
        "location" : "Ber",
        "origin" : "Ber",
        "destination" : "Kie",
        "country" : "GE",
        "owner" : "Will"
    },
    "IT01": {                           # success
        "location" : "Rom",
        "origin" : "Rom",
        "destination" : "Ven",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "IT02": {                           # success
        "location" : "Ven",
        "origin" : "Ven",
        "destination" : "Tyr",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "IT03": {                           # success
        "location" : "Nap",
        "origin" : "Nap",
        "destination" : "Tys",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "RU01": {                           # success
        "location" : "Stp-SC",
        "origin" : "Stp-SC",
        "destination" : "Bot",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU02": {                           # success
        "location" : "War",
        "origin" : "War",
        "destination" : "Gal",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU03": {                           # success
        "location" : "Mos",
        "origin" : "Mos",
        "destination" : "Ukr",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU04": {                           # fail - bounce with TU03
        "location" : "Sev",
        "origin" : "Sev",
        "destination" : "Bla",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "TU01": {                           # success
        "location" : "Con",
        "origin" : "Con",
        "destination" : "Bul",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU02": {                           # success
        "location" : "Smy",
        "origin" : "Smy",
        "destination" : "Con",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU03": {                           # fail - bounce with RU04
        "location" : "Ank",
        "origin" : "Ank",
        "destination" : "Bla",
        "country" : "TU",
        "owner" : "Adam"
    }

}

cmds_3b = {

    "AU01": {
        "location" : "Alb",             # success
        "origin" : "Ser",
        "destination" : "Gre",
        "country": "AU",
        "owner" : "Liam"
    },
    "AU02": {                           # fail - IT01 takes Tri
        "location" : "Bud",
        "origin" : "Bud",
        "destination" : "Tri",
        "country": "AU",
        "owner" : "Liam"
    },
    "AU03": {                           # success
        "location" : "Ser",
        "origin" : "Ser",
        "destination" : "Gre",
        "country": "AU",
        "owner" : "Liam"
    },
    "UK01": {
        "location" : "Eng",             # success
        "origin" : "Eng",
        "destination" : "Bel",
        "country": "UK",
        "owner" : "Mercy"
    },
    "UK02": {                           # fail - GE03 takes Hol
        "location" : "Nth",
        "origin" : "Nth",
        "destination" : "Hol",
        "country": "UK",
        "owner" : "Mercy"
    },
    "UK03": {                           # success
        "location" : "Yor",
        "origin" : "Yor",
        "destination" : "Yor",
        "country": "UK",
        "owner" : "Mercy"
    },
    "FR01": {
        "location" : "Mao",             # success
        "origin" : "Mao",
        "destination" : "Por",
        "country": "AU",
        "owner" : "Sunny"
    },
    "FR02": {                           # success
        "location" : "Bre",
        "origin" : "Bre",
        "destination" : "Bre",
        "country": "AU",
        "owner" : "Sunny"
    },
    "FR03": {                           # success        
        "location" : "Spa",
        "origin" : "Spa",
        "destination" : "Spa",
        "country": "AU",
        "owner" : "Sunny"
    },
    "GE01": {                           # success
        "location" : "Den",
        "origin" : "Den",
        "destination" : "Den",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE02": {                           # success
        "location" : "Ruh",
        "origin" : "Kie",
        "destination" : "Hol",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE03": {                           # success
        "location" : "Kie",
        "origin" : "Kie",
        "destination" : "Hol",
        "country" : "GE",
        "owner" : "Will"
    },
    "IT01": {                           # success
        "location" : "Ven",
        "origin" : "Ven",
        "destination" : "Tri",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "IT02": {                           # success
        "location" : "Tyr",
        "origin" : "Ven",
        "destination" : "Tri",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "IT03": {                           # success
        "location" : "Tys",
        "origin" : "Tys",
        "destination" : "Tun",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "RU01": {                           # success
        "location" : "Bot",
        "origin" : "Bot",
        "destination" : "Swe",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU02": {                           # success
        "location" : "Gal",
        "origin" : "Sev",
        "destination" : "Rum",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU03": {                           # success
        "location" : "Ukr",
        "origin" : "Sev",
        "destination" : "Rum",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU04": {                           # success
        "location" : "Sev",
        "origin" : "Sev",
        "destination" : "Rum",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "TU01": {                           # success
        "location" : "Bul",
        "origin" : "Bul",
        "destination" : "Ser",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU02": {                           # success
        "location" : "Con",
        "origin" : "Con",
        "destination" : "Bul",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU03": {                           # success
        "location" : "Ank",
        "origin" : "Ank",
        "destination" : "Bla",
        "country" : "TU",
        "owner" : "Adam"
    }

}