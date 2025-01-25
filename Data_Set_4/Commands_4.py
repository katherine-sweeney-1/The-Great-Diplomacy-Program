cmds_4a = {

    "AU01": {
        "location" : "Alb",             # success
        "origin" : "Bud",
        "destination" : "Tri",
        "country": "AU",
        "owner" : "Liam"
    },
    "AU02": {                           # fail - IT01 takes Tri CODE WRONG  
        "location" : "Bud",
        "origin" : "Bud",
        "destination" : "Tri",
        "country": "AU",
        "owner" : "Liam"
    },
    "AU03": {                           # success doesn't count strength for AU01
        "location" : "Gre",
        "origin" : "Alb",
        "destination" : "Alb",
        "country": "AU",
        "owner" : "Liam"
    },
    "UK01": {
        "location" : "Bel",             # fail
        "origin" : "Nth",
        "destination" : "Hol",
        "country": "UK",
        "owner" : "Mercy"
    },
    "UK02": {                           # fail
        "location" : "Nth",
        "origin" : "Nth",
        "destination" : "Hol",
        "country": "UK",
        "owner" : "Mercy"
    },
    "UK03": {                           # success
        "location" : "Lon",
        "origin" : "Lon",
        "destination" : "Lon",
        "country": "UK",
        "owner" : "Mercy"
    },
    "UK04": {                           # fails - Nth is occupied due to failed attack
        "location" : "Edi",
        "origin" : "Edi",
        "destination" : "Nth",
        "country": "UK",
        "owner" : "Mercy"
    },
    "FR01": {
        "location" : "Por",             # success
        "origin" : "Por",
        "destination" : "Mao",
        "country": "FR",
        "owner" : "Sunny"
    },
    "FR02": {                           # success
        "location" : "Bre",
        "origin" : "Bre",
        "destination" : "Pic",
        "country": "FR",
        "owner" : "Sunny"
    },
    "FR03": {                           # success        
        "location" : "Spa",
        "origin" : "Spa",
        "destination" : "Gas",
        "country": "FR",
        "owner" : "Sunny"
    },
    "FR04": {                           # success        
        "location" : "Par",
        "origin" : "Par",
        "destination" : "Bur",
        "country": "FR",
        "owner" : "Sunny"
    },
    "FR05": {                           # success        
        "location" : "Mar",
        "origin" : "Mar",
        "destination" : "Spa-SC",
        "country": "FR",
        "owner" : "Sunny"
    },
    "GE01": {                           # fail - Nth is occupied due to failed attack 
        "location" : "Den",
        "origin" : "Den",
        "destination" : "Nth",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE02": {                           # success
        "location" : "Ruh",
        "origin" : "Hol",
        "destination" : "Bel",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE03": {                           # success
        "location" : "Hol",
        "origin" : "Hol",
        "destination" : "Bel",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE04": {                           # fail CODE SAYS TRUE
        "location" : "Kie",
        "origin" : "Kie",
        "destination" : "Hol",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE05": {                           # fail CODE SAYS TRUE
        "location" : "Ber",
        "origin" : "Ber",
        "destination" : "Kie",
        "country" : "GE",
        "owner" : "Will"
    },
    "IT01": {                           # success
        "location" : "Tri",
        "origin" : "Tri",
        "destination" : "Vie",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "IT02": {                           # success
        "location" : "Tyr",
        "origin" : "Tri",
        "destination" : "Vie",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "IT03": {                           # success
        "location" : "Tun",
        "origin" : "Nap",
        "destination" : "Ion",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "IT04": {                           # success
        "location" : "Nap",
        "origin" : "Nap",
        "destination" : "Ion",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "IT05": {                           # fail - bounce CODE SAYS TRUE
        "location" : "Ven",
        "origin" : "Ven",
        "destination" : "Tri",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "RU01": {                           # success
        "location" : "Swe",
        "origin" : "Stp-NC",
        "destination" : "Nwy",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU02": {                           # success
        "location" : "Gal",
        "origin" : "Rum",
        "destination" : "Rum",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU03": {                           # fail issue with counting support holds
        "location" : "Rum",
        "origin" : "Gal",
        "destination" : "Gal",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU04": {                           # fail
        "location" : "Sev",
        "origin" : "Rum",
        "destination" : "Rum",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU05": {                           # success
        "location" : "Stp-NC",
        "origin" : "Stp-NC",
        "destination" : "Nwy",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "RU06": {                           # success
        "location" : "War",
        "origin" : "War",
        "destination" : "Sil",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "TU01": {                           # success
        "location" : "Ser",
        "origin" : "Bul",
        "destination" : "Rum",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU02": {                           # fail CODE SAYS TRUE
        "location" : "Bul",
        "origin" : "Bul",
        "destination" : "Rum",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU03": {                           # fail
        "location" : "Bla",
        "origin" : "Bla",
        "destination" : "Sev",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU04": {                           # fail CODE SAYS TRUE
        "location" : "Con",
        "origin" : "Con",
        "destination" : "Bul-EC",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU05": {                           # success
        "location" : "Smy",
        "origin" : "Smy",
        "destination" : "Aeg",
        "country" : "TU",
        "owner" : "Adam"
    }

}