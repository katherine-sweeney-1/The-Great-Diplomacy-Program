from Class_Table import Table

def yield_table (commands):
    db_table = Table()
    db_table.create_table()
    db_table.save(commands)
    return db_table