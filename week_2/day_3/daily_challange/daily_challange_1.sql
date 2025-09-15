-- Nettoyage si relance du script
DROP TABLE IF EXISTS customer_profile CASCADE;
DROP TABLE IF EXISTS customer CASCADE;

-- 1️⃣ Création des tables
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id INT UNIQUE REFERENCES customer(id) ON DELETE CASCADE
);

-- 2️⃣ Insertion des customers
INSERT INTO customer (first_name, last_name)
VALUES ('John', 'Doe'),
       ('Jerome', 'Lalu'),
       ('Lea', 'Rive');

-- 3️⃣ Insertion des profiles avec sous-requêtes
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES 
    (TRUE, (SELECT id FROM customer WHERE first_name = 'John')),
    (FALSE, (SELECT id FROM customer WHERE first_name = 'Jerome'));
-- Lea n'a pas de profil

-- 4️⃣ Requêtes demandées

-- 🔹 a) Les first_name des clients connectés
SELECT c.first_name
FROM customer c
JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = TRUE;

-- 🔹 b) Tous les customers, même sans profil
SELECT c.first_name,
       COALESCE(cp.isLoggedIn, FALSE) AS isLoggedIn
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id
ORDER BY c.id;

-- 🔹 c) Nombre de customers NON connectés
SELECT COUNT(*) AS not_logged_in_count
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id
WHERE COALESCE(cp.isLoggedIn, FALSE) = FALSE;


-- part 2

-- Nettoyage si relance
DROP TABLE IF EXISTS library CASCADE;
DROP TABLE IF EXISTS student CASCADE;
DROP TABLE IF EXISTS book CASCADE;

-- 1️⃣ Table Book
CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL
);

INSERT INTO book (title, author)
VALUES ('Alice In Wonderland', 'Lewis Carroll'),
       ('Harry Potter', 'J.K Rowling'),
       ('To kill a mockingbird', 'Harper Lee');

-- 2️⃣ Table Student
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    age INT NOT NULL CHECK (age <= 15) -- contrainte pour l'âge
);

INSERT INTO student (name, age)
VALUES ('John', 12),
       ('Lera', 11),
       ('Patrick', 10),
       ('Bob', 14);

-- 3️⃣ Table Library (Junction Table)
CREATE TABLE library (
    book_fk_id INT REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INT REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE NOT NULL,
    PRIMARY KEY (book_fk_id, student_fk_id, borrowed_date) -- clé composite
);

-- 4️⃣ Ajout des enregistrements avec sous-requêtes
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES
    ((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
     (SELECT student_id FROM student WHERE name = 'John'),
     '2022-02-15'),

    ((SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
     (SELECT student_id FROM student WHERE name = 'Bob'),
     '2021-03-03'),

    ((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
     (SELECT student_id FROM student WHERE name = 'Lera'),
     '2021-05-23'),

    ((SELECT book_id FROM book WHERE title = 'Harry Potter'),
     (SELECT student_id FROM student WHERE name = 'Bob'),
     '2021-08-12');

-- 5️⃣ Requêtes demandées

-- 🔹 a) Toutes les colonnes de la table Library
SELECT * FROM library;

-- 🔹 b) Nom des étudiants et titres des livres empruntés
SELECT s.name, b.title, l.borrowed_date
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id
ORDER BY s.name;

-- 🔹 c) Âge moyen des enfants ayant emprunté "Alice in Wonderland"
SELECT AVG(s.age)::NUMERIC(5,2) AS avg_age_alice
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

-- 🔹 d) Suppression d'un étudiant et observation de la table library
DELETE FROM student WHERE name = 'Bob';

-- Vérifier les effets (les emprunts de Bob doivent être supprimés automatiquement)
SELECT * FROM library;
