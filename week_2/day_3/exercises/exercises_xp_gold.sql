-- Afficher tous les films
SELECT * FROM film;

-- ========================
-- Exercise 1
-- ========================

-- 1️⃣ Liste de tous les films loués avec durée de location et temps écoulé
SELECT 
    r.rental_id,
    f.title,
    f.rental_duration,
    (r.return_date - r.rental_date) AS rental_out
FROM rental r
INNER JOIN inventory i ON i.inventory_id = r.inventory_id
INNER JOIN film f ON f.film_id = i.film_id;

-- 2️⃣ Liste des clients et durée de location
SELECT 
    c.first_name,
    c.last_name,
    (r.return_date - r.rental_date) AS rental_out
FROM customer c
INNER JOIN rental r ON r.customer_id = c.customer_id
INNER JOIN inventory i ON i.inventory_id = r.inventory_id
INNER JOIN film f ON f.film_id = i.film_id;

-- 3️⃣ Liste de tous les films Action avec Joe Swank
SELECT 
    f.title,
    f.description,
    a.first_name || ' ' || a.last_name AS actor_name
FROM film f
INNER JOIN film_actor fa ON f.film_id = fa.film_id
INNER JOIN actor a ON a.actor_id = fa.actor_id
WHERE a.first_name = 'Joe'
  AND a.last_name = 'Swank'
  AND f.description ILIKE '%action%';

-- ========================
-- Exercise 2
-- ========================

-- 1️⃣ Nombre de magasins et leur localisation
SELECT 
    COUNT(s.store_id) AS total_stores,
    ci.city,
    co.country
FROM store s
INNER JOIN address a ON a.address_id = s.address_id
INNER JOIN city ci ON ci.city_id = a.city_id
INNER JOIN country co ON co.country_id = ci.country_id
GROUP BY ci.city, co.country;
