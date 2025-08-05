cmds_1a = {

    "AU01": {
        "location" : "Tri",             # success
        "origin" : "Tri",
        "destination" : "Adr",
        "country": "AU",
        "owner" : "Kamran"
    },
    "AU02": {                           # success
        "location" : "Vie",
        "origin" : "Vie",
        "destination" : "Boh",
        "country": "AU",
        "owner" : "Kamran"
    },
    "AU03": {                           # success
        "location" : "Bud",
        "origin" : "Bud",
        "destination" : "Ser",
        "country": "AU",
        "owner" : "Kamran"
    },
    "UK01": {
        "location" : "Lon",             # success
        "origin" : "Lon",
        "destination" : "Nth",
        "country": "UK",
        "owner" : "Will"
    },
    "UK02": {                           # success
        "location" : "Edi",
        "origin" : "Edi",
        "destination" : "Nwg",
        "country": "UK",
        "owner" : "Will"
    },
    "UK03": {                           # success
        "location" : "Lvp",
        "origin" : "Lvp",
        "destination" : "Yor",
        "country": "UK",
        "owner" : "Will"
    },
    "FR01": {
        "location" : "Bre",             # success
        "origin" : "Bre",
        "destination" : "Eng",
        "country": "FR",
        "owner" : "Mercy"
    },
    "FR02": {                           # success
        "location" : "Par",
        "origin" : "Par",
        "destination" : "Pic",
        "country": "FR",
        "owner" : "Mercy"
    },
    "FR03": {                           # success        
        "location" : "Mar",
        "origin" : "Mar",
        "destination" : "Spa",
        "country": "FR",
        "owner" : "Mercy"
    },
    "GE01": {                           # success
        "location" : "Kie",
        "origin" : "Kie",
        "destination" : "Hol",
        "country" : "GE",
        "owner" : "Keaton"
    },
    "GE02": {                           # success
        "location" : "Mun",
        "origin" : "Mun",
        "destination" : "Ruh",
        "country" : "GE",
        "owner" : "Keaton"
    },
    "GE03": {                           # success
        "location" : "Ber",
        "origin" : "Ber",
        "destination" : "Kie",
        "country" : "GE",
        "owner" : "Keaton"
    },
    "IT01": {                           # success
        "location" : "Rom",
        "origin" : "Rom",
        "destination" : "Ven",
        "country" : "IT",
        "owner" : "Katherine"
    },
    "IT02": {                           # success
        "location" : "Ven",
        "origin" : "Ven",
        "destination" : "Tyr",
        "country" : "IT",
        "owner" : "Katherine"
    },
    "IT03": {                           # success
        "location" : "Nap",
        "origin" : "Nap",
        "destination" : "Ion",
        "country" : "IT",
        "owner" : "Katherine"
    },
    "RU01": {                           # success
        "location" : "Stp-SC",
        "origin" : "Stp-SC",
        "destination" : "Bot",
        "country" : "RU",
        "owner" : "Michael"
    },
    "RU02": {                           # success
        "location" : "War",
        "origin" : "War",
        "destination" : "Gal",
        "country" : "RU",
        "owner" : "Michael"
    },
    "RU03": {                           # success
        "location" : "Mos",
        "origin" : "Mos",
        "destination" : "Sev",
        "country" : "RU",
        "owner" : "Michael"
    },
    "RU04": {                           # fail - bounce with TU03
        "location" : "Sev",
        "origin" : "Sev",
        "destination" : "Rum",
        "country" : "RU",
        "owner" : "Michael"
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
        "destination" : "Arm",
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

cmds_1b = {

    "AU01": {
        "location" : "Adr",             # success
        "origin" : "Adr",
        "destination" : "Apu",
        "country": "AU",
        "owner" : "Kamran"
    },
    "AU02": {                           # fail
        "location" : "Boh",
        "origin" : "Boh",
        "destination" : "Mun",
        "country": "AU",
        "owner" : "Kamran"
    },
    "AU03": {                           # success
        "location" : "Ser",
        "origin" : "Bul",
        "destination" : "Gre",
        "country": "AU",
        "owner" : "Kamran"
    },
    "UK01": {
        "location" : "Nth",             # success
        "origin" : "Nth",
        "destination" : "Den",
        "country": "UK",
        "owner" : "Will"
    },
    "UK02": {                           # success
        "location" : "Nwg",
        "origin" : "Nwg",
        "destination" : "Nwy",
        "country": "UK",
        "owner" : "Will"
    },
    "UK03": {                           # fail
        "location" : "Yor",
        "origin" : "Yor",
        "destination" : "Lon",
        "country": "UK",
        "owner" : "Will"
    },
    "FR01": {
        "location" : "Eng",             # fail
        "origin" : "Eng",
        "destination" : "Lon",
        "country": "FR",
        "owner" : "Mercy"
    },
    "FR02": {                           # fail
        "location" : "Pic",
        "origin" : "Pic",
        "destination" : "Bel",
        "country": "FR",
        "owner" : "Mercy"
    },
    "FR03": {                           # success        
        "location" : "Spa",
        "origin" : "Spa",
        "destination" : "Por",
        "country": "FR",
        "owner" : "Mercy"
    },
    "GE01": {                           # success
        "location" : "Hol",
        "origin" : "Ruh",
        "destination" : "Bel",
        "country" : "GE",
        "owner" : "Keaton"
    },
    "GE02": {                           # success
        "location" : "Ruh",
        "origin" : "Ruh",
        "destination" : "Bel",
        "country" : "GE",
        "owner" : "Keaton"
    },
    "GE03": {                           # fail
        "location" : "Kie",
        "origin" : "Kie",
        "destination" : "Mun",
        "country" : "GE",
        "owner" : "Keaton"
    },
    "IT01": {                           # success
        "location" : "Ven",
        "origin" : "Tyr",
        "destination" : "Tri",
        "country" : "IT",
        "owner" : "Katherine"
    },
    "IT02": {                           # success
        "location" : "Tyr",
        "origin" : "Tyr",
        "destination" : "Tri",
        "country" : "IT",
        "owner" : "Katherine"
    },
    "IT03": {                           # fail
        "location" : "Ion",
        "origin" : "Ion",
        "destination" : "Gre",
        "country" : "IT",
        "owner" : "Katherine"
    },
    "RU01": {                           # success
        "location" : "Bot",
        "origin" : "Bot",
        "destination" : "Swe",
        "country" : "RU",
        "owner" : "Michael"
    },
    "RU02": {                           # success
        "location" : "Gal",
        "origin" : "Gal",
        "destination" : "Sil",
        "country" : "RU",
        "owner" : "Michael"
    },
    "RU03": {                           # success
        "location" : "Sev",
        "origin" : "Sev",
        "destination" : "Ukr",
        "country" : "RU",
        "owner" : "Michael"
    },
    "RU04": {                           # fsuccess
        "location" : "Rum",
        "origin" : "Rum",
        "destination" : "Rum",
        "country" : "RU",
        "owner" : "Michael"
    },
    "TU01": {                           # success
        "location" : "Bul",
        "origin" : "Bul",
        "destination" : "Gre",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU02": {                           # fail with no convoy function
        "location" : "Arm",
        "origin" : "Arm",
        "destination" : "Bul",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU03": {                           # fail with no convoy function
        "location" : "Bla",
        "origin" : "Arm",
        "destination" : "Bul",
        "country" : "TU",
        "owner" : "Adam"
    }

}