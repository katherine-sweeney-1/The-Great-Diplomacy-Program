
def is_convoy(cmd):
    if cmd.loc == cmd.origin and cmd.loc != cmd.destination:
        if cmd.loc.type == "Coast" and cmd.destination.type == "Coast":
            return True
