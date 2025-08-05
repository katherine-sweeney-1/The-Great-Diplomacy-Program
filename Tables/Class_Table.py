class Table ():

    def __init__ (self, turn_count):
        self.turn_string = str(turn_count)

    def create_table(self, db):
            db.query("""
                CREATE TABLE IF NOT EXISTS game1_{} (
                UNIT_ID TEXT,
                Commander TEXT,
                Location TEXT,
                Origin TEXT,
                Destination TEXT,
                Outcome TEXT
                )
                """.format(self.turn_string)
            )
            db.store_result()
            return db

    def drop_table(self, db):
        db.query("""   
            DROP TABLE IF EXISTS game1_{};
        """.format(self.turn_string)
        )
        db.store_result()

    def save(self,db, cmds):
        for cmd_string in cmds:
            cmd = cmds[cmd_string]
            sql = """
                INSERT INTO game1_{} (UNIT_ID, Commander, Location, Origin, Destination, Outcome) VALUES ("{}", "{}", "{}", "{}", "{}", "{}")
                ON DUPLICATE KEY UPDATE UNIT_ID = UNIT_ID;
                """.format(self.turn_string, cmd.unit.id, cmd.human.human, cmd.loc.name, cmd.origin.name, cmd.destination.name, cmd.outcome_loc.name)
            db.query(sql)
            db.store_result()