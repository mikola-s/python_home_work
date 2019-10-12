
## Домашнее задание №11

#### Первый уровень ("Храню данные..."):
>Повторяем урок, создаем базу данных фильмов с таблицами актеров, фильмов, режиссеров.

создание базы данных

```sql
CREATE DATABASE movie_info;

\c movie_info
```

<details>
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

<details>
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

<details>
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


#### Второй уровень("Храню данные в табличках..."):

>Удаляем и пересоздаем таблицы, добавляем и редактирем поля в таблицах.

изменеие таблицы actors

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


<details>
	<summary>заполнение таблицы actors</summary>

```sql
INSERT INTO actors(first_name, second_name)
VALUES
	('Уайатт', 'Олефф'),		('Доминик', 'Монаган'),		('Ричард', 'Армитидж'),
	('Джон', 'Красински'),		('Керри-Энн', 'Мосс'),		('Махершала', 'Али'),
	('Пабло', 'Шрайбер'),		('Уильям', 'Сэдлер'),		('Билл', 'Скарсгорд'),
	('Билли', 'Бойд'),			('Николас', 'Хэмилтон'),	('Фредди', 'Строма'),
	('Вигго', 'Мортенсен'),		('Тоби', 'Стивенс'),		('Наоми', 'Скотт'),
	('Джеки Эрл', 'Хейли'),		('Мартин', 'Фримен'),		('Шон', 'Бин'),
	('Эмма', 'Стоун'),			('Вуди', 'Харрельсон'),		('Сигурни', 'Уивер'),
	('Джон', 'Рис-Дэвис'),		('Чоузен', 'Джейкобс'),		('Кевин', 'Костнер'),
	('Финн', 'Вулфхард'),		('Роза', 'Салазар'),		('Лоуренс', 'Фишборн'),
	('Джоэль', 'Мур'),			('Элайджа', 'Вуд'),			('Джон Кэрролл', 'Линч'),
	('Джо', 'Пантолиано'),		('Джованни', 'Рибизи'),		('Эбигейл', 'Бреслин'),
	('Мена', 'Массуд'),			('Стивен', 'Лэнг'),			('Эд', 'Скрейн'),
	('Джек Дилан', 'Грейзер'),	('София', 'Лиллис'),		('Мишель', 'Родригес'),
	('Джеймс Бэдж', 'Дэйл'),	('Энди', 'Серкис'),			('Киан', 'Джонсон'),
	('Уилл', 'Смит'),			('Томас', 'Манн'),			('Кэти', 'Бэйтс'),
	('Иэн', 'Маккеллен'),		('Сэм', 'Уортингтон'),		('Кристофер', 'Ли'),
	('Дженнифер', 'Коннелли'),	('Зои', 'Салдана'),			('Орландо', 'Блум'),
	('Кристоф', 'Вальц'),		('Киану', 'Ривз'),			('Хьюго', 'Уивинг'),
	('Эванджелин', 'Лилли'),	('Джейден', 'Мартелл'),		('Ким', 'Диккенс'),
	('Кейт', 'Бланшетт'),		('Джесси', 'Айзенберг'),	('Шон', 'Астин'),
	('Люк', 'Эванс'),			('Джереми Рэй', 'Тейлор')
;
```
</details>


#### Третий уровень ("Храню данные в табличках правильно и красиво!"):

>Создаем дамп базы данных и скидываем ссылку на выложенный в git дамп. Как создавать дамп - google that question.
