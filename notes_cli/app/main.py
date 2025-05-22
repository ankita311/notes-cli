from typing import List
from fastapi import FastAPI, Response, status, HTTPException
import sqlite3
import schemas


# Create table
conn = sqlite3.connect("notes.db")  # Connects to the DB file
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT
)
""")
conn.close()

app = FastAPI()

@app.post("/create")
def add_notes(note: schemas.NotesIn):
    conn = sqlite3.connect("notes.db")  # Connects to the DB file
    cursor = conn.cursor()

    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (note.title, note.content))
    conn.commit()
    cursor.execute("SELECT * FROM notes where title = ? AND content = ?", (note.title, note.content))
    row = cursor.fetchone()

    conn.close()
    
    return {'note': row}

@app.get("/list", response_model=List[schemas.NotesOut])
def get_notes():
    conn = sqlite3.connect("notes.db")  # Connects to the DB file
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()
    conn.close()

    notes = [
        {"id": row[0], "title": row[1], "content": row[2]}
        for row in rows
    ]
    
    return notes

@app.get("/get/{id}", response_model=schemas.NotesOut)
def get_one_note(id: int):
    conn = sqlite3.connect("notes.db")  # Connects to the DB file
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes where id = ?", (id,))
    note = cursor.fetchone()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Note doesn't exist")
    conn.close()

    return {"id": note[0],
            "title": note[1],
            "content": note[2]
    }



@app.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(id: int):
    conn = sqlite3.connect("notes.db")  # Connects to the DB file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes where id = ?", (id,))
    note = cursor.fetchone()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Note doesn't exist")

    cursor.execute("DELETE FROM notes WHERE id = ?", (id,))
    conn.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
