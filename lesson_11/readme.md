
## Домашнее задание №11

#### Первый уровень ("Храню данные..."):
>Повторяем урок, создаем базу данных фильмов с таблицами актеров, фильмов, режиссеров.

создание базы данных

```sql
CREATE DATABASE movie_info;

\c movie_info

CREATE TABLE actors (
	id_actor INT,
	first_name TEXT,
	second_name TEXT,
	PRIMARY KEY (id_actor)
	);

\d actors
                 Table "public.actors"
   Column    |  Type   | Collation | Nullable | Default 
-------------+---------+-----------+----------+---------
 id_actor    | numeric |           | not null | 
 first_name  | text    |           |          | 
 second_name | text    |           |          | 
Indexes:
    "actors_pkey" PRIMARY KEY, btree (id_actor)

========================================================

CREATE TABLE producers (
	id_producer INT,
	first_name TEXT,
	second_name TEXT,
	PRIMARY KEY (id_producer)
	);

\d producers

                Table "public.producers"
   Column    |  Type   | Collation | Nullable | Default 
-------------+---------+-----------+----------+---------
 id_producer | integer |           | not null | 
 first_name  | text    |           |          | 
 second_name | text    |           |          | 
Indexes:
    "producers_pkey" PRIMARY KEY, btree (id_producer)

========================================================

CREATE TABLE films (
	id_film INT,
	title_ru TEXT,
	title_en TEXT,
	release INT,
	PRIMARY KEY (id_film)
	);

\d films

                Table "public.films"
  Column  |  Type   | Collation | Nullable | Default 
----------+---------+-----------+----------+---------
 id_film  | integer |           | not null | 
 title_ru | text    |           |          | 
 title_en | text    |           |          | 
 release  | integer |           |          | 
Indexes:
    "films_pkey" PRIMARY KEY, btree (id_film)

```


#### Второй уровень("Храню данные в табличках..."):

>Удаляем и пересоздаем таблицы, добавляем и редактирем поля в таблицах.

#### Третий уровень ("Храню данные в табличках правильно и красиво!"):

>Создаем дамп базы данных и скидываем ссылку на выложенный в git дамп. Как создавать дамп - google that question.
