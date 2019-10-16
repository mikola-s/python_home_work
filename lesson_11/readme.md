
## Домашнее задание №11

### Первый уровень ("Храню данные..."):
>Повторяем урок, создаем базу данных фильмов с таблицами актеров, фильмов, режиссеров.

создание базы данных

```sql
CREATE DATABASE movie_info;

\c movie_info
```

<details open="open">
	<summary>создание таблицы actors</summary>

```sql
CREATE TABLE actors (
	id SERIAL,
	first_name TEXT,
	second_name TEXT
	);

\d actors
                                  Table "public.actors"
   Column    |  Type   | Collation | Nullable |                 Default                  
-------------+---------+-----------+----------+------------------------------------------
 id          | integer |           | not null | nextval('actors_id_actor_seq'::regclass)
 first_name  | text    |           |          | 
 second_name | text    |           |          | 


```
</details>

<details open="open">
	<summary>создание таблицы producers</summary>

```sql
CREATE TABLE producers (
	id SERIAL,
	first_name TEXT,
	second_name TEXT
	);

\d producers
                                   Table "public.producers"
   Column    |  Type   | Collation | Nullable |                    Default                     
-------------+---------+-----------+----------+------------------------------------------------
 id          | integer |           | not null | nextval('producers_id_producer_seq'::regclass)
 first_name  | text    |           |          | 
 second_name | text    |           |          | 

```
</details>

<details open="open">
	<summary>создание таблицы films</summary>

```sql
CREATE TABLE films (
	id SERIAL,
	title_ru TEXT,
	title_en TEXT,
	release INT
	);

\d films
                                Table "public.films"
  Column  |  Type   | Collation | Nullable |                Default                 
----------+---------+-----------+----------+----------------------------------------
 id       | integer |           | not null | nextval('films_id_film_seq'::regclass)
 title_ru | text    |           |          | 
 title_en | text    |           |          | 
 release  | integer |           |          | 


```
</details>


### Второй уровень("Храню данные в табличках..."):

>Удаляем и пересоздаем таблицы, добавляем и редактирем поля в таблицах.

<details open="open">
	<summary>изменеие таблицы actors</summary> 

```sql
ALTER TABLE actors RENAME id TO id_actor;

\d actors
                                  Table "public.actors"
   Column    |  Type   | Collation | Nullable |                 Default                  
-------------+---------+-----------+----------+------------------------------------------
 id_actor    | integer |           | not null | nextval('actors_id_actor_seq'::regclass)
 first_name  | text    |           |          | 
 second_name | text    |           |          | 



ALTER TABLE actors ADD PRIMARY KEY(id_actor);

\d actors
                                  Table "public.actors"
   Column    |  Type   | Collation | Nullable |                 Default                  
-------------+---------+-----------+----------+------------------------------------------
 id_actor    | integer |           | not null | nextval('actors_id_actor_seq'::regclass)
 first_name  | text    |           |          | 
 second_name | text    |           |          | 
Indexes:
    "actors_pkey" PRIMARY KEY, btree (id_actor)

```
</details>


<details open="open">
	<summary>заполнение таблицы actors (закрытый спойлер)</summary>

```sql
INSERT INTO actors(first_name, second_name)
VALUES	('Уайатт', 'Олефф'),		('Доминик', 'Монаган'),		('Ричард', 'Армитидж'),
	('Джон', 'Красински'),		('Керри-Энн', 'Мосс'),		('Махершала', 'Али'),
	('Пабло', 'Шрайбер'),		('Уильям', 'Сэдлер'),		('Билл', 'Скарсгорд'),
	('Билли', 'Бойд'),		('Николас', 'Хэмилтон'),	('Фредди', 'Строма'),
	('Вигго', 'Мортенсен'),		('Тоби', 'Стивенс'),		('Наоми', 'Скотт'),
	('Джеки Эрл', 'Хейли'),		('Мартин', 'Фримен'),		('Шон', 'Бин'),
	('Эмма', 'Стоун'),		('Вуди', 'Харрельсон'),		('Сигурни', 'Уивер'),
	('Джон', 'Рис-Дэвис'),		('Чоузен', 'Джейкобс'),		('Кевин', 'Костнер'),
	('Финн', 'Вулфхард'),		('Роза', 'Салазар'),		('Лоуренс', 'Фишборн'),
	('Джоэль', 'Мур'),		('Элайджа', 'Вуд'),		('Джон Кэрролл', 'Линч'),
	('Джо', 'Пантолиано'),		('Джованни', 'Рибизи'),		('Эбигейл', 'Бреслин'),
	('Мена', 'Массуд'),		('Стивен', 'Лэнг'),		('Эд', 'Скрейн'),
	('Джек Дилан', 'Грейзер'),	('София', 'Лиллис'),		('Мишель', 'Родригес'),
	('Джеймс Бэдж', 'Дэйл'),	('Энди', 'Серкис'),		('Киан', 'Джонсон'),
	('Уилл', 'Смит'),		('Томас', 'Манн'),		('Кэти', 'Бэйтс'),
	('Иэн', 'Маккеллен'),		('Сэм', 'Уортингтон'),		('Кристофер', 'Ли'),
	('Дженнифер', 'Коннелли'),	('Зои', 'Салдана'),		('Орландо', 'Блум'),
	('Кристоф', 'Вальц'),		('Киану', 'Ривз'),		('Хьюго', 'Уивинг'),
	('Эванджелин', 'Лилли'),	('Джейден', 'Мартелл'),		('Ким', 'Диккенс'),
	('Кейт', 'Бланшетт'),		('Джесси', 'Айзенберг'),	('Шон', 'Астин'),
	('Люк', 'Эванс'),		('Джереми Рэй', 'Тейлор')
;

SELECT
	(a1.first_name || ' ' || a1.second_name) as actors_name,
	(a2.first_name || ' ' || a2.second_name) as actors_name,
	(a3.first_name || ' ' || a3.second_name) as actors_name
FROM (SELECT * FROM actors LIMIT 21) a1
FULL OUTER JOIN (SELECT * FROM actors LIMIT 21 OFFSET 21) a2 
	ON (a2.id_actor = (a1.id_actor + 21))
FULL OUTER JOIN (SELECT * FROM actors LIMIT 21 OFFSET 42) a3 
	ON (a3.id_actor = (a2.id_actor + 21));


   actors_name    |    actors_name     |    actors_name     
------------------+--------------------+--------------------
 Уайатт Олефф     | Джон Рис-Дэвис     | Уилл Смит
 Доминик Монаган  | Чоузен Джейкобс    | Томас Манн
 Ричард Армитидж  | Кевин Костнер      | Кэти Бэйтс
 Джон Красински   | Финн Вулфхард      | Иэн Маккеллен
 Керри-Энн Мосс   | Роза Салазар       | Сэм Уортингтон
 Махершала Али    | Лоуренс Фишборн    | Кристофер Ли
 Пабло Шрайбер    | Джоэль Мур         | Дженнифер Коннелли
 Уильям Сэдлер    | Элайджа Вуд        | Зои Салдана
 Билл Скарсгорд   | Джон Кэрролл Линч  | Орландо Блум
 Билли Бойд       | Джо Пантолиано     | Кристоф Вальц
 Николас Хэмилтон | Джованни Рибизи    | Киану Ривз
 Фредди Строма    | Эбигейл Бреслин    | Хьюго Уивинг
 Вигго Мортенсен  | Мена Массуд        | Эванджелин Лилли
 Тоби Стивенс     | Стивен Лэнг        | Джейден Мартелл
 Наоми Скотт      | Эд Скрейн          | Ким Диккенс
 Джеки Эрл Хейли  | Джек Дилан Грейзер | Кейт Бланшетт
 Мартин Фримен    | София Лиллис       | Джесси Айзенберг
 Шон Бин          | Мишель Родригес    | Шон Астин
 Эмма Стоун       | Джеймс Бэдж Дэйл   | Люк Эванс
 Вуди Харрельсон  | Энди Серкис        | Джереми Рэй Тейлор
 Сигурни Уивер    | Киан Джонсон       | 
(21 rows)


```
</details>

<details open="open">
	<summary>изменеие таблицы producer</summary> 

```sql

ALTER TABLE producers RENAME id TO id_producer;

\d producers
                                   Table "public.producers"
   Column    |  Type   | Collation | Nullable |                    Default                     
-------------+---------+-----------+----------+------------------------------------------------
 id_producer | integer |           | not null | nextval('producers_id_producer_seq'::regclass)
 first_name  | text    |           |          | 
 second_name | text    |           |          | 


ALTER TABLE producers ADD PRIMARY KEY(id_producer);

\d producers
                                   Table "public.producers"
   Column    |  Type   | Collation | Nullable |                    Default                     
-------------+---------+-----------+----------+------------------------------------------------
 id_producer | integer |           | not null | nextval('producers_id_producer_seq'::regclass)
 first_name  | text    |           |          | 
 second_name | text    |           |          | 
Indexes:
    "producers_pkey" PRIMARY KEY, btree (id_producer)

```

<details open="open">
	<summary>заполнение таблицы producers</summary>

```sql

INSERT INTO producers(first_name, second_name)
VALUES 
('Роберт', 'Родригес'),
('Джеймс', 'Кэмерон'),
('Майкл', 'Бэй'),
('Рубен', 'Флейшер'),
('Братья', 'Вачовски'),
('Джон Ли', 'Хэнкок'),
('Энди', 'Мускетти'),
('Питер', 'Джексон'),
('Гай', 'Ричи')
;

TABLE producers;

 id_producer | first_name | second_name 
-------------+------------+-------------
           1 | Роберт     | Родригес
           2 | Джеймс     | Кэмерон
           3 | Майкл      | Бэй
           4 | Рубен      | Флейшер
           5 | Братья     | Вачовски
           6 | Джон Ли    | Хэнкок
           7 | Энди       | Мускетти
           8 | Питер      | Джексон
           9 | Гай        | Ричи
(9 rows)

```
</details>

<details open="open">
	<summary>измение таблицы films</summary>

```sql

ALTER TABLE films RENAME id TO id_film;

\d films
                                Table "public.films"
  Column  |  Type   | Collation | Nullable |                Default                 
----------+---------+-----------+----------+----------------------------------------
 id_film  | integer |           | not null | nextval('films_id_film_seq'::regclass)
 title_ru | text    |           |          | 
 title_en | text    |           |          | 
 release  | integer |           |          | 

ALTER TABLE films ADD PRIMARY KEY(id_film);

\d films
                                Table "public.films"
  Column  |  Type   | Collation | Nullable |                Default                 
----------+---------+-----------+----------+----------------------------------------
 id_film  | integer |           | not null | nextval('films_id_film_seq'::regclass)
 title_ru | text    |           |          | 
 title_en | text    |           |          | 
 release  | integer |           |          | 
Indexes:
    "films_pkey" PRIMARY KEY, btree (id_film)

```
</details>

<details open="open">
	<summary>заполнение таблицы films</summary>

```sql

insert into films(title_ru, title_en, release)
values
('Алита: Боевой ангел', 'Alita: Battle Angel', '2019'),
('Аватар', 'Avatar', '2009'),
('13 часов: Тайные солдаты Бенгази', '13 Hours: The Secret Soldiers of Benghazi', '2016'),
('Добро пожаловать в Zомбилэнд', 'Zombieland', '2009'),
('Матрица', 'Matrix', '1999'),
('В погоне за Бонни и Клайдом', 'The Highwaymen', '2019'),
('Оно', 'It', '2017'),
('Властелин колец: Братство Кольца', 'The Lord of the Rings: The Fellowship of the Ring', '2001'),
('Аладдин', 'Aladdin', '2019'),
('Хоббит: Нежданное путешествие', 'The Hobbit: An Unexpected Journey', '2012');

table films;

 id_film |             title_ru             |                     title_en                      | release 
---------+----------------------------------+---------------------------------------------------+---------
       1 | Алита: Боевой ангел              | Alita: Battle Angel                               |    2019
       2 | Аватар                           | Avatar                                            |    2009
       3 | 13 часов: Тайные солдаты Бенгази | 13 Hours: The Secret Soldiers of Benghazi         |    2016
       4 | Добро пожаловать в Zомбилэнд     | Zombieland                                        |    2009
       5 | Матрица                          | Matrix                                            |    1999
       6 | В погоне за Бонни и Клайдом      | The Highwaymen                                    |    2019
       7 | Оно                              | It                                                |    2017
       8 | Властелин колец: Братство Кольца | The Lord of the Rings: The Fellowship of the Ring |    2001
       9 | Аладдин                          | Aladdin                                           |    2019
      10 | Хоббит: Нежданное путешествие    | The Hobbit: An Unexpected Journey                 |    2012
(10 rows)


```

</details>

### Третий уровень ("Храню данные в табличках правильно и красиво!"):

>Создаем дамп базы данных и скидываем ссылку на выложенный в git дамп. Как создавать дамп - google that question.

Дамп базы данных [movie_info_dump.sql](https://github.com/mikola-s/python_home_work/blob/master/lesson_11/)
