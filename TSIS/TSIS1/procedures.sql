CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(
    id INTEGER,
    username VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phone VARCHAR,
    phone_type VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.username, c.email, c.birthday, g.name, p.phone, p.type
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.username ILIKE '%' || pattern || '%'
       OR c.email ILIKE '%' || pattern || '%'
       OR g.name ILIKE '%' || pattern || '%'
       OR p.phone ILIKE '%' || pattern || '%'
    ORDER BY c.id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_page(limit_count INTEGER, offset_count INTEGER)
RETURNS TABLE(
    id INTEGER,
    username VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phone VARCHAR,
    phone_type VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.username, c.email, c.birthday, g.name, p.phone, p.type
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    ORDER BY c.id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE add_phone(
    contact_username VARCHAR,
    new_phone VARCHAR,
    new_type VARCHAR
)
AS $$
DECLARE
    cid INTEGER;
BEGIN
    SELECT id INTO cid
    FROM contacts
    WHERE username = contact_username;

    IF cid IS NULL THEN
        RAISE NOTICE 'Contact not found';
        RETURN;
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES(cid, new_phone, new_type);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE move_to_group(
    contact_username VARCHAR,
    new_group VARCHAR
)
AS $$
DECLARE
    gid INTEGER;
BEGIN
    INSERT INTO groups(name)
    VALUES(new_group)
    ON CONFLICT(name) DO NOTHING;

    SELECT id INTO gid
    FROM groups
    WHERE name = new_group;

    UPDATE contacts
    SET group_id = gid
    WHERE username = contact_username;
END;
$$ LANGUAGE plpgsql;