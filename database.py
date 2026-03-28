import sqlite3

DB_FILE = "mistakes.db"

class Database:
    def __init__(self, db_name=DB_FILE):
        self.conn = sqlite3.connect(db_name)
        self.create_table()
        self._migrate_columns()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mistakes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                subject TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def _migrate_columns(self):
        cursor = self.conn.cursor()
        cursor.execute("PRAGMA table_info(mistakes)")
        cols = [row[1] for row in cursor.fetchall()]
        if "subject" not in cols:
            cursor.execute("ALTER TABLE mistakes ADD COLUMN subject TEXT NOT NULL DEFAULT '未分类'")
            self.conn.commit()

    def add_mistake(self, title, question, answer, subject):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO mistakes (title, question, answer, subject) VALUES (?, ?, ?, ?)', (title, question, answer, subject))
        self.conn.commit()

    def update_mistake(self, mistake_id, title, question, answer, subject):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE mistakes SET title=?, question=?, answer=?, subject=? WHERE id=?', (title, question, answer, subject, mistake_id))
        self.conn.commit()

    def delete_mistake(self, mistake_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM mistakes WHERE id=?', (mistake_id,))
        self.conn.commit()

    def get_all_mistakes(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, title, question, answer, subject FROM mistakes')
        return cursor.fetchall()
