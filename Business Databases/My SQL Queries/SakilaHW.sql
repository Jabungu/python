USE SAKILA;

-- 1 --
SELECT customer.first_name, customer.last_name, customer.email, address.address, city.city, country.country, city.city_id
FROM customer
join address on customer.address_id = address.address_id
join city on address.city_id = city.city_id
join country on city.country_id = country.country_id
WHERE address.city_id=312; 

-- 2 --

SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM category
JOIN film_category on category.category_id = film_category.category_id
JOIN film on film_category.film_id = film.film_id
WHERE category.name = "Comedy";

-- 3 --

SELECT actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

-- 4 --

SELECT customer.first_name, customer.last_name, customer.email, address.address, city.city
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city on address.city_id = city.city_id
WHERE customer.store_id= 1 AND city.city_id IN (1, 42, 312, 459) ;

-- 5 --
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
WHERE film.rating= "G" AND film_actor.actor_id = 15 AND film.special_features LIKE "%behind the scenes%";

-- 6 --
SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name," ", actor.last_name) AS actor_name
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE film.film_id=369;

-- 7 --
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
Join film_category on film.film_id = film_category.film_id
Join category on film_category.category_id= category.category_id
WHERE category.name= "Drama" AND film.rental_rate= 2.99;

-- 8 --
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, CONCAT(actor.first_name, " ",  actor.last_name) AS actor_name
FROM category
JOIN film_category ON category.category_id = film_category.category_id
JOIN film ON film_category.film_id = film.film_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.last_name="KILMER" AND actor.first_name="SANDRA" AND category.name="action";
