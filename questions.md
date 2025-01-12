
Commander Class

    Where to create the function/property of adding new units to a commander's unit members?
        => Create new unit => unit class
        => Add unit to commander => commander class property add_member


Need to eventually figure out how to check what territories people own, lost, occupy, etc. make that it's own thing and not part of the commander class


Legal Check

    Will use passwords to make sure the person is submitting moves for the correct country


Node


    have subclass for special coast scenarios 
        -   have "main" node and each coast nodes for three nodes total
        -   when one of the three nodes is occupied then all three return a node occupied of true
        -   e.g. fleet occupied south coast => node proptery for NC and "main" node are True (not the unit id)

    Player ONLY specifies coasts for fleet attacks to Bul and Spa
        -   constantinople => Bul-EC/SC 
        -   MAO => Spa-NC/SC
        
    Create occupied property that lists the unit that occupies the territory

    Figure out node subclass


Eventually (do not forget)

    Storing moves in SQL table 

    Graph bullshit

    Check google doc

Notes on Rules

    units can trade places with a convoy

    support can be given without consent and cannot be refused

    Cannot let fleets move from Stp-SC to Stp-NC
    fleets can move from Bul-EC to Bul-SC and Spa-SC to Spa-NC

    Diagram 13 in rulebook is the tricky one to implement
        -   if an attack from origin 1 dislodges unit X, and unit X and unit Y attack origin 1, then 
            unit Y gains origin 1 
        -   This is instead of it being a stalemate between unit X and unit Y
        -   Issue: an attack is invalid if another attack succeeds' on the unit's origin
        -   this is where recursion happened last time

    Take note of diagram 17


Unit Class

    - Have a commander property

    - Every property between two objects is bidirectional


Fucked up with making new objects instead of using ones I already created
- they're different objects


COMPLETED

    => edit the node input so it takes the name and the nested info (nodes dictionary key and value)

    => make own_dots be territory objects

    => make unit_members be unit objects