CREATE Database covid;

Drop table if exists t1;
Drop table if exists t2;
Drop table if exists t3;

CREATE TABLE t1 (id VARCHAR(10), geo VARCHAR(10));
CREATE TABLE t2 (id VARCHAR(10), geo VARCHAR(10));
CREATE TABLE t3 (id VARCHAR(10), geo VARCHAR(10));

COPY t1
FROM '⁩/Users/joshua.bae/Documents/04_Code/01_AGE/02_Covid_track/t1.csv' CSV HEADER;

COPY t2
FROM '⁩/Users/joshua.bae/Documents/04_Code/01_AGE/02_Covid_track/t2.csv' CSV HEADER;

COPY t3
FROM '⁩/Users/joshua.bae/Documents/04_Code/01_AGE/02_Covid_track/t2.csv' CSV HEADER;

-- 'To list the people that stayed over 10 mins together at the same places'
WITH colo AS(
    SELECT t2.id, t2.geo
    FROM t1
    INNER JOIN t2 ON t1.id = t2.id
    WHERE t1.geo = t2.geo)
SELECT * 
FROM colo
WHERE geo IN (
        SELECT geo
        FROM colo
        GROUP BY geo
        HAVING COUNT(*) > 1)
;

-- 'Between t2 and t3 To list the people that stayed over 10 mins together at the same places'
WITH colo AS(
    SELECT t3.id, t3.geo
    FROM t2
    INNER JOIN t3 ON t2.id = t3.id
    WHERE t2.geo = t3.geo)
SELECT * 
FROM colo
WHERE geo IN (
        SELECT geo
        FROM colo
        GROUP BY geo
        HAVING COUNT(*) > 1)
;

-- 'pour data into colo_t1 table'
WITH colo_t1 AS(
    WITH colo AS(
        SELECT t2.id, t2.geo
        FROM t1
        INNER JOIN t2 ON t1.id = t2.id
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
WITH colo_t2 AS(
    WITH colo AS(
        SELECT t3.id, t3.geo
        FROM t2
        INNER JOIN t3 ON t2.id = t3.id
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
MERGE (a :person { id: row.id, geo:row.geo} );      

MATCH (a:person)
SET a.geo = NULL;

-- 'To set properties from the table colo_t1'
MATCH (a:person)
WITH a
SET a.geo = (
    SELECT geo
    FROM public.colo_t1
    WHERE to_jsonb(id) = (
        MATCH (a)
        RETURN a.id)
    );

-- 'To merge edges among people at the same locations longer than 10 mins'
DROP ELABEL IF EXISTS colo CASCADE;
CREATE ELABEL colo;

MATCH (a:person), (b:person)
WHERE a <> b
AND a.geo = b.geo
MERGE (a)-[:colo {start:'t1', end:'t2'}]->(b);

-- 'testing CASE WHEN THEN' <- not working
MATCH (a:person) 
RETURN  
CASE a.geo 
WHEN NULL    THEN  [(a)| a]
WHEN 'w03'    THEN  [(a)-[]->(b)| b]
END 
AS result;


create function tablename_variable(datepart CHAR(10))
returns table (id int, lat int, lon int)
as $$
    DECLARE
    BEGIN
    execute format('
        SELECT id, lat, lon
        FROM geo_%s
        where time > now ()- INTERVAL ''24 HOURS'';', datepart);
    end;
$$

language plpgsql;
This uses the procedural language and something called dynamic programming
https://www.postgresql.org/docs/12/ecpg-dynamic.html

select * from tablename_variable('202005011200');