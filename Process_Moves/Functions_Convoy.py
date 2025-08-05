import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node

def convoying_unit(cmds):
    for cmding_unit in cmds:
        cmd = cmds[cmding_unit]
        # Check if unit is army
        if cmd.unit.type == "army":
            unit_boolean = True
        else:
            unit_boolean = False
        # Check if unit moves to coasts
        if cmd.loc == cmd.origin and cmd.loc != cmd.destination:
            if cmd.loc.node_type == "Coast" and cmd.destination.node_type == "Coast":
                node_boolean = True
            else:
                node_boolean = False
        else:
            node_boolean = False
        # Check if origin and destination are not neighbors
        #print(cmd.origin.name, cmd.origin.nbrs)
        if cmd.destination in cmd.origin.nbrs.values():
                nbr_boolean = False
        else:
            nbr_boolean = True
            print("true", cmd.unit.id)
                #print("TRUE", cmd.unit.id)
        # Check if origin and destination have common sea neighbor
        for nbr in cmd.loc.nbrs:
            for other_nbr in cmd.destination.nbrs:
                    if nbr == other_nbr:
                        #print("TEST", cmd.unit.id, nbr)
                        if cmd.loc.nbrs[nbr].node_type == "Coast" or cmd.loc.nbrs[nbr].node_type == "Land":
                            sea_nbr_boolean = False
                    else:
                        sea_nbr_boolean = True
                        break
        if unit_boolean == True and node_boolean == True:
            if nbr_boolean == True and sea_nbr_boolean == True:
                print("YES", cmding_unit)
    
    
