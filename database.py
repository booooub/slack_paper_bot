import sqlite3

DB_NAME = "papers.db"

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS papers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE,
        summary TEXT,
        pdf_link TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS channel_topics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel TEXT,
        topic TEXT,
        UNIQUE(channel, topic)
    )""")
    
    conn.commit()
    conn.close()

def check_duplicate(title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM papers WHERE title = ?", (title,))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def save_paper(title, summary, pdf_link):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO papers (title, summary, pdf_link) VALUES (?, ?, ?)", 
                       (title, summary, pdf_link))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def add_topic(channel, topic):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO channel_topics (channel, topic) VALUES (?, ?)", (channel, topic))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def remove_topic(channel, topic):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM channel_topics WHERE channel = ? AND topic = ?", (channel, topic))
    conn.commit()
    conn.close()

def get_topics(channel):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT topic FROM channel_topics WHERE channel = ?", (channel,))
    topics = [row[0] for row in cursor.fetchall()]
    conn.close()
    return topics
