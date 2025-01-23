cmds_2 = {

    "AU01": {
        "location" : "Apu",              # success - hold
        "origin" : "Apu",
        "destination" : "Apu",
        "country": "AU",
        "owner" : "Liam"
    },
    "AU02": {                       # fail - hold
        "location" : "Ser",
        "origin" : "Ser",
        "destination" : "Ser",
        "country": "AU",
        "owner" : "Liam"
    },
    "AU03": {                       # fail - hold
        "location" : "Tri",
        "origin" : "Tri",
        "destination" : "Tri",
        "country": "AU",
        "owner" : "Liam"
    },
    "UK01": {
        "location" : "Lon",              # success - support Nth's hold
        "origin" : "Nth",
        "destination" : "Nth",
        "country": "UK",
        "owner" : "Mercy"
    },
    "UK02": {                       # success - hold
        "location" : "Nth",
        "origin" : "Nth",
        "destination" : "Nth",
        "country": "UK",
        "owner" : "Mercy"
    },
    "UK03": {                       # ERROR - non-neighbor destination
        "location" : "Nwy",
        "origin" : "Nwy",
        "destination" : "Den",
        "country": "UK",
        "owner" : "Mercy"
    },
    "UK04": {                       # ERROR - illegal attack
        "location" : "Ska",
        "origin" : "Nwy",
        "destination" : "Den",
        "country": "UK",
        "owner" : "Mercy"
    },
    "GE01": {                       # success - hold
        "location" : "Den",
        "origin" : "Den",
        "destination" : "Den",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE02": {                       # success - support Den's hold
        "location" : "Hel",
        "origin" : "Den",
        "destination" : "Den",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE03": {                       # success - support Hel's hold
        "location" : "Hol",
        "origin" : "Hel",
        "destination" : "Hel",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE04": {                       # success - attack
        "location" : "Mun",
        "origin" : "Mun",
        "destination" : "Tyr",
        "country" : "GE",
        "owner" : "Will"
    },
    "GE05": {                       # success - attack
        "location" : "Ruh",
        "origin" : "Ruh",
        "destination" : "Bel",
        "country" : "GE",
        "owner" : "Will"
    },
    "IT01": {                       # success - attack PROGRAM WRONG
        "location" : "Tus",
        "origin" : "Tus",
        "destination" : "Ven",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "IT02": {                       # success - attack 
        "location" : "Ven",
        "origin" : "Ven",
        "destination" : "Tri",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "IT03": {                       # success - attack 
        "location" : "Wes",
        "origin" : "Wes",
        "destination" : "Lyo",
        "country" : "IT",
        "owner" : "Kamran"
    },
    "RU01": {                       # success - support Ven's attack
        "location" : "Bud",
        "origin" : "Ven",
        "destination" : "Tri",
        "country" : "RU",
        "owner" : "Katherine"
    },
    "TU01": {                       # success - attack serbia (occupied)
        "location" : "Gre",
        "origin" : "Gre",
        "destination" : "Ser",
        "country" : "TU",
        "owner" : "Adam"
    },
    "TU02": {                       # success - support Gre's attack to serbia
        "location" : "Bul",
        "origin" : "Gre",
        "destination" : "Ser",
        "country" : "TU",
        "owner" : "Adam"
    }

}
