from db import get_db


# ambil semua data news
def get_news():
    db = get_db()
    cursor = db .cursor()
    #SELECT
    query = "SELECT news_id, title, content, datetime, flag FROM tbl_news_0465"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #konversi ke dictionary
        
    return result

# ambil data news berdasarkan id
def get_news_by_id(news_id):
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT news_id, title, content, datetime, flag FROM tbl_news_0465 WHERE news_id = ?"
    cursor.execute(query, [news_id])
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    result.append(dict(zip(columns, cursor.fetchone()))) #konversi ke dictionary
        
    return result


# patch data news berdasarkan flag
def patch_news(news_id, flag):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE tbl_news_0465 SET flag = ? WHERE news_id = ?"
    cursor.execute(query, [flag, news_id])
    db.commit()
    return True

# menambahkan data news
def insert_news(title, content, datetime, flag):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO tbl_news_0465(title, content, datetime, flag) VALUES (?,?,?,?)"
    cursor.execute(query, [title, content, datetime, flag])
    db.commit()
    return True
    

# mengubah data news
def update_news(news_id, title, content, datetime, flag):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE tbl_news_0465 SET title = ?, content = ?, datetime = ?, flag = ? WHERE news_id = ?"
    cursor.execute(query, [title, content, datetime, flag, news_id])
    db.commit()
    return True

# menghapus data news
def delete_news(news_id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM tbl_news_0465 WHERE news_id = ?"
    cursor.execute(query, [news_id])
    db.commit()
    return True
