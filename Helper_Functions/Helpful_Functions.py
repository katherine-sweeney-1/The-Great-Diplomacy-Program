"""
CVS File Line List - Elements:
    0 => Abbreviated name (e.g. Mun, Sev)
    1 => Full name (e.g. Munich, Sevestapol)
    2 => Type (land, sea, or coast)
    3 => Neighbors (terrritory abbreviations separated by spaces)
    4 => Country (e.g. Neutral, Fra, Aus)
    5 => Dot (True or False)
    6 => Home SupCenter (True or False)
"""

"""
Want
- Abbreviated name => 0 => line[0]
- Type             => 2 => line[2]

Steps
- have node functions parse_file parse the csv nodes_data file
- 
    for line in given_file
        create neighbor and its weight as a (nbr, wgt) tuple
        add that tuple to the territory:neighbor dictionary 
    
"""

import sys
sys.path.append("Territories\\Nodes_Functions.py")
import parse_file


