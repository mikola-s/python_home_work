## Домашнее задание №13

### 1. Практикуем все, пройденное на уроке.


#### CRUD data -- CREATE

<details>
    <summary>
        создание базы данных и таблицы
    </summary>



```sql

CREATE DATABASE squad;

CREATE TABLE squad_weapons(
	weapon_id SERIAL PRIMARY KEY,
	weapon_name TEXT NOT NULL,
	serial_num TEXT UNIQUE NOT NULL); 

\d squad_weapons

weapon_id   | integer |           | not null | nextval('squad_weapons_weapon_id_seq'::regclass)
weapon_name | text    |           | not null | 
serial_num  | text    |           | not null | 


```
</details>

<details>
    <summary>
        запись дашнных в таблицу (insert)
    </summary>

```sql

INSERT INTO squad_weapons(weapon_name, serial_num) 
VALUES
	('AK-74','249896'),
	('RPG-7','2381906'),
	('AK-74','123498'),
	('PKM','BN-301'),
	('AK-74','879832'),
	('GP-30','32978'),
	('AK-74','355278'),
	('GP-30','23344'),
	('AKS-74U','5761278'),
	('AKS-74U','1235561'),
	('SVD','232132'),
	('PM','1234456');

 weapon_id | weapon_name | serial_num 
-----------+-------------+------------
         1 | AK-74       | 249896
         2 | RPG-7       | 2381906
         3 | AK-74       | 123498
         4 | PKM         | BN-301
         5 | AK-74       | 879832
         6 | GP-30       | 32978
         7 | AK-74       | 355278
         8 | GP-30       | 23344
         9 | AKS-74U     | 5761278
        10 | AKS-74U     | 1235561
        11 | SVD         | 232132
        12 | PM          | 1234456
(12 rows)


```

</details>

<details>
    <summary>
        запись данных с помощью SELECT
    </summary>

```sql

INSERT INTO squad_weapons(weapon_name, serial_num) 
	SELECT weapon_name, trunc(random()*1000000) 
	FROM squad_weapons;

SELECT * FROM squad_weapons;

 weapon_id | weapon_name | serial_num 
-----------+-------------+------------
         1 | AK-74       | 249896
         2 | RPG-7       | 2381906
         3 | AK-74       | 123498
         4 | PKM         | BN-301
         5 | AK-74       | 879832
         6 | GP-30       | 32978
         7 | AK-74       | 355278
         8 | GP-30       | 23344
         9 | AKS-74U     | 5761278
        10 | AKS-74U     | 1235561
        11 | SVD         | 232132
        12 | PM          | 1234456
        26 | AK-74       | 812208
        27 | RPG-7       | 820134
        28 | AK-74       | 448275
        29 | PKM         | 971221
        30 | AK-74       | 968629
        31 | GP-30       | 405628
        32 | AK-74       | 17736
        33 | GP-30       | 765760
        34 | AKS-74U     | 362891
        35 | AKS-74U     | 316008
        36 | SVD         | 176676
        37 | PM          | 359044
(24 rows)


```

</details>

<details>
    <summary>
        добавление колонки в таблицу
    </summary>

```sql

ALTER TABLE squad_weapons ADD COLUMN ammo TEXT DEFAULT '';

SELECT * FROM squad_weapons;

 weapon_id | weapon_name | serial_num | ammo 
-----------+-------------+------------+------
         1 | AK-74       | 249896     | 
         2 | RPG-7       | 2381906    | 
         3 | AK-74       | 123498     | 
         4 | PKM         | BN-301     | 
         5 | AK-74       | 879832     | 
         6 | GP-30       | 32978      | 
         7 | AK-74       | 355278     | 
         8 | GP-30       | 23344      | 
         9 | AKS-74U     | 5761278    | 
        10 | AKS-74U     | 1235561    | 
        11 | SVD         | 232132     | 
        12 | PM          | 1234456    | 
        26 | AK-74       | 812208     | 
        27 | RPG-7       | 820134     | 
        28 | AK-74       | 448275     | 
        29 | PKM         | 971221     | 
        30 | AK-74       | 968629     | 
        31 | GP-30       | 405628     | 
        32 | AK-74       | 17736      | 
        33 | GP-30       | 765760     | 
        34 | AKS-74U     | 362891     | 
        35 | AKS-74U     | 316008     | 
        36 | SVD         | 176676     | 
        37 | PM          | 359044     | 
(24 rows)

```
</details>

#### CRUD data -- READ

<details>
    <summary>
        чтение данных (SELECT)
    </summary>

```sql

SELECT * FROM squad_weapons WHERE weapon_name = 'AK-74';

 weapon_id | weapon_name | serial_num 
-----------+-------------+------------
         1 | AK-74       | 249896
         3 | AK-74       | 123498
         5 | AK-74       | 879832
         7 | AK-74       | 355278
        26 | AK-74       | 812208
        28 | AK-74       | 448275
        30 | AK-74       | 968629
        32 | AK-74       | 17736
(8 rows)
```

</details>

<details>
    <summary>
        чтение данных (+ GROUP BY)
    </summary>

```sql

SELECT count(*), weapon_name FROM squad_weapons GROUP BY weapon_name;

 count | weapon_name 
-------+-------------
     4 | GP-30
     4 | AKS-74U
     2 | RPG-7
     2 | PM
     2 | SVD
     2 | PKM
     8 | AK-74
(7 rows)

```
</details>


### 2. Изучаем UPDATE и DELETE для данных самостоятельно (ключевые слова соответствуют))

#### CRUD data -- UPDATE

<details>
    <summary>
        заполнение колонки данными
    </summary>

```sql

UPDATE squad_weapons SET weapon_name = 'GP-25'
	WHERE weapon_name = 'GP-30';

UPDATE squad_weapons SET ammo = '5,45x39 mm' 
	WHERE weapon_name LIKE '%-74%';

UPDATE squad_weapons SET ammo = '7,62x54 mm' 
	WHERE weapon_name SIMILAR TO '(PKM|SVD)';

UPDATE squad_weapons SET ammo = '9x18 mm PM' 
	WHERE weapon_name ~~ 'PM';

UPDATE squad_weapons SET ammo = 'overcaliber grenade 40 mm' 
	WHERE weapon_name ~~ 'RPG-7';

SELECT * FROM squad_weapons;

 weapon_id | weapon_name | serial_num |           ammo            
-----------+-------------+------------+---------------------------
         6 | GP-25       | 32978      | 40 mm grenade VOG-25
         8 | GP-25       | 23344      | 40 mm grenade VOG-25
        31 | GP-25       | 405628     | 40 mm grenade VOG-25
        33 | GP-25       | 765760     | 40 mm grenade VOG-25
         2 | RPG-7       | 2381906    | overcaliber grenade 40 mm
        27 | RPG-7       | 820134     | overcaliber grenade 40 mm
         4 | PKM         | BN-301     | 7,62x54 mm
        11 | SVD         | 232132     | 7,62x54 mm
        29 | PKM         | 971221     | 7,62x54 mm
        36 | SVD         | 176676     | 7,62x54 mm
         1 | AK-74       | 249896     | 5,45x39 mm
         3 | AK-74       | 123498     | 5,45x39 mm
         5 | AK-74       | 879832     | 5,45x39 mm
         7 | AK-74       | 355278     | 5,45x39 mm
        26 | AK-74       | 812208     | 5,45x39 mm
        28 | AK-74       | 448275     | 5,45x39 mm
        30 | AK-74       | 968629     | 5,45x39 mm
        32 | AK-74       | 17736      | 5,45x39 mm
         9 | AKS-74U     | 5761278    | 5,45x39 mm
        10 | AKS-74U     | 1235561    | 5,45x39 mm
        34 | AKS-74U     | 362891     | 5,45x39 mm
        35 | AKS-74U     | 316008     | 5,45x39 mm
        12 | PM          | 1234456    | 9x18 mm PM
        37 | PM          | 359044     | 9x18 mm PM
(24 rows)


```
</details>

#### CRUD data -- DELETE

<details>
    <summary>
        удаление строк
    </summary>

```sql 

pg_dump squad > squad.sql

DELETE FROM squad_weapons WHERE weapon_id > 12;

SELECT * FROM squad_weapons;

 weapon_id | weapon_name | serial_num |           ammo            
-----------+-------------+------------+---------------------------
         6 | GP-25       | 32978      | 40 mm grenade VOG-25
         8 | GP-25       | 23344      | 40 mm grenade VOG-25
         2 | RPG-7       | 2381906    | overcaliber grenade 40 mm
         4 | PKM         | BN-301     | 7,62x54 mm
        11 | SVD         | 232132     | 7,62x54 mm
         1 | AK-74       | 249896     | 5,45x39 mm
         3 | AK-74       | 123498     | 5,45x39 mm
         5 | AK-74       | 879832     | 5,45x39 mm
         7 | AK-74       | 355278     | 5,45x39 mm
         9 | AKS-74U     | 5761278    | 5,45x39 mm
        10 | AKS-74U     | 1235561    | 5,45x39 mm
        12 | PM          | 1234456    | 9x18 mm PM
(12 rows)


```
</details>

<details>
    <summary>
        удаление поля (колонки)
    </summary>

```sql

ALTER TABLE squad_weapons DROP COLUMN ammo;

 weapon_id | weapon_name | serial_num 
-----------+-------------+------------
         6 | GP-25       | 32978
         8 | GP-25       | 23344
         2 | RPG-7       | 2381906
         4 | PKM         | BN-301
        11 | SVD         | 232132
         1 | AK-74       | 249896
         3 | AK-74       | 123498
         5 | AK-74       | 879832
         7 | AK-74       | 355278
         9 | AKS-74U     | 5761278
        10 | AKS-74U     | 1235561
        12 | PM          | 1234456
(12 rows)


```
</details>

<details>
    <summary>
        удаление таблицы из базы данных
    </summary>

```sql

DROP TABLE squad_weapons;

SELECT * FROM squad_weapons;

ERROR:  relation "squad_weapons" does not exist
LINE 1: SELECT * FROM squad_weapons;
                      ^

```
</details>

### 3. Дополнительно знакомимся с FETCH (аналог LIMIT) и TRUNCATE (аналог DROP TABLE + CREATE TABLE)


#### FETCH

<details>
    <summary>восстановление таблицы squad_weapons </summary>

```sql 

psql squad < squad.sql

SELECT * FROM squad_weapons ORDER BY weapon_id;

 weapon_id | weapon_name | serial_num |           ammo            
-----------+-------------+------------+---------------------------
         1 | AK-74       | 249896     | 5,45x39 mm
         2 | RPG-7       | 2381906    | overcaliber grenade 40 mm
         3 | AK-74       | 123498     | 5,45x39 mm
         4 | PKM         | BN-301     | 7,62x54 mm
         5 | AK-74       | 879832     | 5,45x39 mm
         6 | GP-25       | 32978      | 40 mm grenade VOG-25
         7 | AK-74       | 355278     | 5,45x39 mm
         8 | GP-25       | 23344      | 40 mm grenade VOG-25
         9 | AKS-74U     | 5761278    | 5,45x39 mm
        10 | AKS-74U     | 1235561    | 5,45x39 mm
        11 | SVD         | 232132     | 7,62x54 mm
        12 | PM          | 1234456    | 9x18 mm PM
        26 | AK-74       | 812208     | 5,45x39 mm
        27 | RPG-7       | 820134     | overcaliber grenade 40 mm
        28 | AK-74       | 448275     | 5,45x39 mm
        29 | PKM         | 971221     | 7,62x54 mm
        30 | AK-74       | 968629     | 5,45x39 mm
        31 | GP-25       | 405628     | 40 mm grenade VOG-25
        32 | AK-74       | 17736      | 5,45x39 mm
        33 | GP-25       | 765760     | 40 mm grenade VOG-25
        34 | AKS-74U     | 362891     | 5,45x39 mm
        35 | AKS-74U     | 316008     | 5,45x39 mm
        36 | SVD         | 176676     | 7,62x54 mm
        37 | PM          | 359044     | 9x18 mm PM
(24 rows)

```
</details>

<details>
    <summary>
        применение FETCH
    </summary>


```sql

SELECT * FROM squad_weapons ORDER BY weapon_id FETCH NEXT 5 ROW ONLY;

 weapon_id | weapon_name | serial_num |           ammo            
-----------+-------------+------------+---------------------------
         1 | AK-74       | 249896     | 5,45x39 mm
         2 | RPG-7       | 2381906    | overcaliber grenade 40 mm
         3 | AK-74       | 123498     | 5,45x39 mm
         4 | PKM         | BN-301     | 7,62x54 mm
         5 | AK-74       | 879832     | 5,45x39 mm
(5 rows)

```
</details>


ссылка на источник по [FETCH](https://postgrespro.ru/docs/postgresql/10/sql-select#SQL-LIMIT)

в источнике сказано что для FETCH 

> Слова ROW и ROWS, а также FIRST и NEXT являются незначащими и не влияют на поведение этих предложений.

но без них запрос не работает, поэтому LIMIT удобнее.


#### Truncate удаление данных (очистка) из таблицы


<details>
    <summary>
        применение TRUNCATE
    </summary>

```sql

TRUNCATE TABLE squad_weapons;

SELECT * FROM squad_weapons;
 weapon_id | weapon_name | serial_num 
-----------+-------------+------------
(0 rows)

```

</details>

ссылка на источник по [TRUNCATE](https://postgrespro.ru/docs/postgrespro/10/sql-truncate)


### Результаты наработок, как обычно, дампом заливаем на github или gitlab так, чтобы я легко нашел их по номеру урока.

[результаты наработок \)\)](https://github.com/mikola-s/python_home_work/tree/master/lesson_13)