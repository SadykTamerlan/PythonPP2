from connect import get_connection

conn = get_connection()
cur = conn.cursor()

# 1. CALL procedure (upsert)
cur.execute("CALL upsert_contact(%s, %s)", ("Alice", "7771234567"))

# 2. SELECT function
cur.execute("SELECT * FROM search_contacts(%s)", ("Ali",))
print(cur.fetchall())

# 3. Pagination
cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (5, 0))
print(cur.fetchall())

# 4. Delete
cur.execute("CALL delete_contact(%s)", ("Alice",))

conn.commit()
cur.close()
conn.close()