-- Démarrer une transaction
BEGIN;

-- 1️⃣ Supprimer les tables si elles existent pour repartir propre
DROP TABLE IF EXISTS public.items;
DROP TABLE IF EXISTS public.customers;

-- 2️⃣ Création des tables

CREATE TABLE public.items (
    id    integer PRIMARY KEY,
    name  text    NOT NULL,
    price integer NOT NULL CHECK (price >= 0)
);

CREATE TABLE public.customers (
    id         integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name  text NOT NULL
);

-- 3️⃣ Insertion des données

INSERT INTO public.items (id, name, price) VALUES
 (1, 'Small Desk', 100),
 (2, 'Large Desk', 300),
 (3, 'Fan',        80);

INSERT INTO public.customers (id, first_name, last_name) VALUES
 (1, 'Greg',    'Jones'),
 (2, 'Sandra',  'Jones'),
 (3, 'Scott',   'Scott'),
 (4, 'Trevor',  'Green'),
 (5, 'Melanie', 'Johnson');

-- ========================
-- 4️⃣ Requêtes demandées
-- ========================

-- 4.1 Tous les items
SELECT * FROM public.items
ORDER BY id;

-- 4.2 Items avec un prix strictement > 80
SELECT * FROM public.items
WHERE price > 80
ORDER BY id;

-- 4.3 Items avec un prix <= 300
SELECT * FROM public.items
WHERE price <= 300
ORDER BY id;

-- 4.4 Clients dont le nom = 'Smith' (résultat : 0 ligne)
SELECT * FROM public.customers
WHERE last_name = 'Smith';

-- 4.5 Clients dont le nom = 'Jones' (résultat : 2 lignes)
SELECT * FROM public.customers
WHERE last_name = 'Jones'
ORDER BY id;

-- 4.6 Clients dont le prénom n'est pas 'Scott' (résultat : 4 lignes)
SELECT * FROM public.customers
WHERE first_name <> 'Scott'
ORDER BY id;

-- Valider les changements
COMMIT;
