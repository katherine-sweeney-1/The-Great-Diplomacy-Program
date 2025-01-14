
Commander Class

    Completed

        => Create commander objects (1)

        => Add unit objects to commander's members (4a)

        => Add node_objects to commander's dots_owned (4b)

    To Do

        => Dots owned can only work for nodes with a dot on it

        => Add commander.orders to give all of a commander's commands for a turn?


Node

    Completed

        => Create node object (2a)

        => Create special case coastal node object subclass with parent and sibling node functions (2b)

    To Do

        => is occupied function if a unit occupies a node

        => is occupied for node subclass so if one of subclass family nodes is occupied then 
        all three in the family are occupied
    

UNIT CLASS

    Completed

        => Create unit objects (3a)

        => Assign location (node object) to unit object (3b)

        => Assign commander to unit object (3c)

    To Do

        => Add unit.command function? 


Eventually (do not forget)

    Storing moves in SQL table 

    Graph bullshit

    Check what territories people own, lost, occupy, etc. (make that it's own thing and not part of the commander class)


NOTES

    Every property between two objects is bidirectional


    Fucked up with making new objects instead of using ones I already created


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
