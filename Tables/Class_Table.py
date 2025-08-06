from MySQLdb import _mysql

class Table ():

    def __init__ (self):
        self.db = _mysql.connect(
        user = "root",
        passwd = "password",
        host = 'localhost',
        db = 'tgdp_1'
    )

    def create_table(self):
            self.db.query("""
            USE tgdp_1;
            """)
            self.db.store_result()
            self.db.query("""
                CREATE TABLE IF NOT EXISTS game1_1901_fall (
                UNIT_ID TEXT,
                Commander TEXT,
                Location TEXT,
                Origin TEXT,
                Destination TEXT,
                Outcome TEXT
                )
                """
            )
            self.db.store_result()
            return self.db

    def save(self, cmds):
        sql = """USE tgdp_1;"""
        self.db.query(sql)
        sql = """
            DELETE FROM game1_1901_fall;
            """
        self.db.query(sql)
        for cmd_string in cmds:
            cmd = cmds[cmd_string]
            sql = """
                INSERT INTO game1_1901_fall (UNIT_ID, Commander, Location, Origin, Destination, Outcome) VALUES ("{}", "{}", "{}", "{}", "{}", "{}")
                ON DUPLICATE KEY UPDATE UNIT_ID = UNIT_ID;
                """.format(cmd.unit.id, cmd.human.human, cmd.loc.name, cmd.origin.name, cmd.destination.name, cmd.outcome_loc.name)
            self.db.query(sql)
        self.db.store_result()