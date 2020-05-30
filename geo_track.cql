CREATE Database covid;

Drop table if exists t1;
Drop table if exists t2;
Drop table if exists t3;
Drop table if exists t4;
Drop table if exists t5;

CREATE TABLE t1 (name VARCHAR(10), geo VARCHAR(10));
CREATE TABLE t2 (name VARCHAR(10), geo VARCHAR(10));
CREATE TABLE t3 (name VARCHAR(10), geo VARCHAR(10));
CREATE TABLE t4 (name VARCHAR(10), geo VARCHAR(10));
CREATE TABLE t5 (name VARCHAR(10), geo VARCHAR(10));

COPY t1
FROM '⁩/Users/joshua.bae/Documents/04_Code/01_AGE/02_Covid_track/t1.csv' CSV HEADER;

COPY t2
FROM '⁩/Users/joshua.bae/Documents/04_Code/01_AGE/02_Covid_track/t2.csv' CSV HEADER;

COPY t3
FROM '⁩/Users/joshua.bae/Documents/04_Code/01_AGE/02_Covid_track/t3.csv' CSV HEADER;

COPY t4
FROM '⁩/Users/joshua.bae/Documents/04_Code/01_AGE/02_Covid_track/t4.csv' CSV HEADER;

COPY t5
FROM '⁩/Users/joshua.bae/Documents/04_Code/01_AGE/02_Covid_track/t5.csv' CSV HEADER;

-- 'To list the people that stayed over 10 mins together at the same places'
WITH colo AS(
    SELECT t2.name, t2.geo
    FROM t1
    INNER JOIN t2 ON t1.name = t2.name
    WHERE t1.geo = t2.geo)
SELECT * 
FROM colo
WHERE geo IN (
        SELECT geo
        FROM colo
        GROUP BY geo
        HAVING COUNT(*) > 1)
;

-- 'pour data into colo_t1 table'
DROP TABLE IF EXISTS colo_t1;

WITH colo_t1 AS(
    WITH colo AS(
        SELECT t2.name, t2.geo
        FROM t1
        INNER JOIN t2 ON t1.name = t2.name
        WHERE t1.geo = t2.geo)
    SELECT * 
    FROM colo
    WHERE geo IN (
            SELECT geo
            FROM colo
            GROUP BY geo
            HAVING COUNT(*) > 1))
SELECT *
INTO TABLE colo_t1
FROM colo_t1;

--' test the table colo_t1'
select * from colo_t1;

-- 'pour data into colo_t2 table'
DROP TABLE IF EXISTS colo_t2;

WITH colo_t2 AS(
    WITH colo AS(
        SELECT t3.name, t3.geo
        FROM t2
        INNER JOIN t3 ON t2.name = t3.name
        WHERE t2.geo = t3.geo)
    SELECT * 
    FROM colo
    WHERE geo IN (
            SELECT geo
            FROM colo
            GROUP BY geo
            HAVING COUNT(*) > 1))
SELECT *
INTO TABLE colo_t2
FROM colo_t2;

-- 'Create graph'
DROP GRAPH IF EXISTS covid_track CASCADE;
CREATE GRAPH covid_track;
SET GRAPH_PATH = covid_track;

-- 'Create person vertexes and populate data'
DROP VLABEL IF EXISTS person;
CREATE VLABEL person;

LOAD FROM t1 AS row            
MERGE (a :person {name: row.name, geo:row.geo} );      

-- 'To set properties from the table colo_t1'
MATCH (a:person)
SET a.geo = NULL;

MATCH (a:person)
WITH a
SET a.geo = (
    SELECT geo
    FROM public.colo_t1
    WHERE to_jsonb(name) = (
        MATCH (a)
        RETURN a.name)
    );

-- 'To merge edges among people at the same locations longer than 10 mins'
DROP ELABEL IF EXISTS colo CASCADE;
CREATE ELABEL colo;

MATCH (a:person), (b:person)
WHERE a <> b
AND a.geo = b.geo
MERGE (a)-[:colo {start:'t1', end:'t2'}]->(b);


-- 'To set properties from the table colo_t2'
MATCH (a:person)
SET a.geo = NULL;

MATCH (a:person)
WITH a
SET a.geo = (
    SELECT geo
    FROM public.colo_t2
    WHERE to_jsonb(name) = (
        MATCH (a)
        RETURN a.name)
    );

-- 'T2~T3 To merge edges among people at the same locations longer than 10 mins'
MATCH (a:person), (b:person)
WHERE a <> b
AND a.geo = b.geo
AND NOT EXISTS ((a)-[:colo {end:'t2'}]->(b))
MERGE (a)-[:colo {start:'t2', end:'t3'}]->(b);

MATCH  ((a)-[c:colo {end:'t2'}]->(b))
WHERE a.geo = b.geo
SET c.end = 't3'
;

-- 'pour data into colo_t3 table'
DROP TABLE IF EXISTS colo_t3;

WITH colo_t3 AS(
    WITH colo AS(
        SELECT t4.name, t4.geo
        FROM t3
        INNER JOIN t4 ON t3.name = t4.name
        WHERE t3.geo = t4.geo)
    SELECT * 
    FROM colo
    WHERE geo IN (
            SELECT geo
            FROM colo
            GROUP BY geo
            HAVING COUNT(*) > 1))
SELECT *
INTO TABLE colo_t3
FROM colo_t3;

-- 'To set properties from the table colo_t3'
MATCH (a:person)
SET a.geo = NULL;

MATCH (a:person)
WITH a
SET a.geo = (
    SELECT geo
    FROM public.colo_t3
    WHERE to_jsonb(name) = (
        MATCH (a)
        RETURN a.name)
    );

-- 'T3~T4 To merge edges among people at the same locations longer than 10 mins'
MATCH (a:person), (b:person)
WHERE a <> b
AND a.geo = b.geo
AND NOT EXISTS ((a)-[:colo {end:'t3'}]->(b))
MERGE (a)-[:colo {start:'t3', end:'t4'}]->(b);

MATCH  ((a)-[c:colo {end:'t3'}]->(b))
WHERE a.geo = b.geo
SET c.end = 't4'
;

-- 'pour data into colo_t4 table'
DROP TABLE IF EXISTS colo_t4;

WITH colo_t4 AS(
    WITH colo AS(
        SELECT t5.name, t5.geo
        FROM t4
        INNER JOIN t5 ON t4.name = t5.name
        WHERE t4.geo = t5.geo)
    SELECT * 
    FROM colo
    WHERE geo IN (
            SELECT geo
            FROM colo
            GROUP BY geo
            HAVING COUNT(*) > 1))
SELECT *
INTO TABLE colo_t4
FROM colo_t4;

-- 'To set properties from the table colo_t4'
MATCH (a:person)
SET a.geo = NULL;

MATCH (a:person)
WITH a
SET a.geo = (
    SELECT geo
    FROM public.colo_t4
    WHERE to_jsonb(name) = (
        MATCH (a)
        RETURN a.name)
    );

-- 'T4~T5 To merge edges among people at the same locations longer than 10 mins'
MATCH (a:person), (b:person)
WHERE a <> b
AND a.geo = b.geo
AND NOT EXISTS ((a)-[:colo {end:'t4'}]->(b))
MERGE (a)-[:colo {start:'t4', end:'t5'}]->(b);

MATCH  ((a)-[c:colo {end:'t4'}]->(b))
WHERE a.geo = b.geo
SET c.end = 't5'
;

-- 'testing the edges'
MATCH p=(a{name: 'p219'})-[c]->()-[]->()
RETURN p;

MATCH p=(a{name: 'p219'})-[]->(b)-[]->(c)-[]->(d)
where a <> c
And a <> d
And b <> d
RETURN p; 

MATCH p=(a)-[c]->()
WHERE c.end ='t4'
RETURN p;

MATCH p=(a)-[c]->()
WHERE right(to_json(c.end), 1)+right(to_json(c.start), 1) IN ['31','42','53']
return p
limit 4;

MATCH p=(a)-[c]->()
WHERE right(to_json(c.end), 1)+right(to_json(c.start), 1) IN ['41','52']
return p
limit 4;


-- 'testing CASE WHEN THEN' <- not working
MATCH (a:person) 
RETURN  
CASE a.geo 
WHEN NULL    THEN  [(a)| a]
WHEN 'w03'    THEN  [(a)-[]->(b)| b]
END 
AS result;


create function tablename_variable(datepart CHAR(10))
returns table .name int, lat int, lon int)
as $$
    DECLARE
    BEGIN
    execute format('
        SELECT.name, lat, lon
        FROM geo_%s
        where time > now ()- INTERVAL ''24 HOURS'';', datepart);
    end;
$$

language plpgsql;
This uses the procedural language and something called dynamic programming
https://www.postgresql.org/docs/12/ecpg-dynamic.html

select * from tablename_variable('202005011200');
