SELECT * FROM actor;

INSERT INTO actor (first_name, last_name) 
VALUES('job_oti', 'bi_oder');

UPDATE sakila.actor SET last_name = 'datnicca', first_name='chope' WHERE actor_id=5;


DELETE FROM country WHERE id = 5;