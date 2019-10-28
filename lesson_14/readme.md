## Домашнее задание №14

### 1. Практикуем все, пройденное на уроке.

### 2. 

>Создаем одну из трех выданных на уроке баз данных

 > - автомобили-производители-модели
 > - фильмы-актеры-режиссеры
 > - студенты-группы-преподаватели

> Заполняем таблицы и делаем большой красивый запрос, который найдет все данные со всеми связанными данными.


<details>
	<summary>создание таблицы отношений films_actors_link</summary>

```sql

CREATE TABLE films_actors_link(film_id INTEGER, actor_id INTEGER, UNIQUE(film_id, actor_id));

\d films_actors_link

          Table "public.films_actors_link"
  Column  |  Type   | Collation | Nullable | Default 
----------+---------+-----------+----------+---------
 film_id  | integer |           |          | 
 actor_id | integer |           |          | 
Indexes:
    "films_actors_link_film_id_actor_id_key" UNIQUE CONSTRAINT, btree (film_id, actor_id)

ALTER TABLE actors RENAME id_actor TO actor_id;

ALTER TABLE films RENAME id_film TO film_id;

INSERT INTO films_actors_link 
SELECT 1 as film_id, actor_id FROM actors WHERE 
(first_name || ' ' || second_name) ~ 'Роза Салазар' OR
(first_name || ' ' || second_name) ~ 'Кристоф Вальц' OR
(first_name || ' ' || second_name) ~ 'Дженнифер Коннелли' OR
(first_name || ' ' || second_name) ~ 'Махершала Али' OR
(first_name || ' ' || second_name) ~ 'Эд Скрейн' OR
(first_name || ' ' || second_name) ~ 'Джеки Эрл Хейли' OR
(first_name || ' ' || second_name) ~ 'Киан Джонсон';

INSERT INTO films_actors_link 
SELECT 2 as film_id, actor_id FROM actors WHERE 
(first_name || ' ' || second_name) ~ 'Сэм Уортингтон' OR
(first_name || ' ' || second_name) ~ 'Зои Салдана' OR
(first_name || ' ' || second_name) ~ 'Сигурни Уивер' OR
(first_name || ' ' || second_name) ~ 'Стивен Лэнг' OR
(first_name || ' ' || second_name) ~ 'Мишель Родригес' OR
(first_name || ' ' || second_name) ~ 'Джованни Рибизи' OR
(first_name || ' ' || second_name) ~ 'Джоэль Мур';

INSERT INTO films_actors_link 
SELECT 3 as film_id, actor_id FROM actors WHERE 
(first_name || ' ' || second_name) ~ 'Джеймс Бэдж Дэйл' OR
(first_name || ' ' || second_name) ~ 'Джон Красински' OR
(first_name || ' ' || second_name) ~ 'Тоби Стивенс' OR
(first_name || ' ' || second_name) ~ 'Пабло Шрайбер' OR
(first_name || ' ' || second_name) ~ 'Фредди Строма';

INSERT INTO films_actors_link 
SELECT 4 as film_id, actor_id FROM actors WHERE
(first_name || ' ' || second_name) ~ 'Джесси Айзенберг' OR
(first_name || ' ' || second_name) ~ 'Вуди Харрельсон' OR
(first_name || ' ' || second_name) ~ 'Эмма Стоун' OR
(first_name || ' ' || second_name) ~ 'Эбигейл Бреслин';

INSERT INTO films_actors_link 
SELECT 5 as film_id, actor_id FROM actors WHERE
(first_name || ' ' || second_name) ~ 'Киану Ривз' OR
(first_name || ' ' || second_name) ~ 'Лоуренс Фишборн' OR
(first_name || ' ' || second_name) ~ 'Керри-Энн Мосс' OR
(first_name || ' ' || second_name) ~ 'Хьюго Уивинг' OR
(first_name || ' ' || second_name) ~ 'Джо Пантолиано';


 film_id | actor_id 
---------+----------
       1 |        6
       1 |       16
       1 |       26
       1 |       36
       1 |       42
       1 |       49
       1 |       52
       2 |       21
       2 |       28
       2 |       32
       2 |       35
       2 |       39
       2 |       47
       2 |       50
       3 |        4
       3 |        7
       3 |       12
       3 |       14
       3 |       40
       4 |       19
       4 |       20
       4 |       33
       4 |       59
       5 |        5
       5 |       27
       5 |       31
       5 |       53
       5 |       54
       6 |        8
       6 |       20
       6 |       24
       6 |       30
       6 |       44
       6 |       45
       6 |       57
       7 |        1
       7 |        9
       7 |       11
       7 |       23
       7 |       25
       7 |       37
       7 |       38
       7 |       56
       7 |       62
       8 |        2
       8 |       10
       8 |       13
       8 |       18
       8 |       22
       8 |       29
       8 |       46
       8 |       48
       8 |       51
       8 |       60
       9 |       15
       9 |       34
       9 |       43
      10 |        3
      10 |       17
      10 |       41
      10 |       46
      10 |       48
      10 |       51
      10 |       54
      10 |       55
      10 |       58
      10 |       61
       (67 rows)

ALTER TABLE films_actors_link RENAME TO films_actors_links;

```
</details>


<details>
	<summary>создание таблицы отношений films_producer_link</summary>

```sql

CREATE TABLE films_producer_link(film_id INTEGER, producer_id INTEGER, UNIQUE(film_id, producer_id));

ALTER TABLE films_producer_link RENAME TO films_producers_links;

ALTER TABLE producers RENAME id_producer TO producer_id;

INSERT INTO films_producers_links(film_id, producer_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 8);

```
</details>

<details>
	<summary>SELECTS</summary>

```sql

SELECT 
	fi.title_ru, 
	(pr.first_name || ' ' || pr.second_name) AS producer,
	(ac.first_name || ' ' || ac.second_name) AS actors
FROM films fi 
LEFT JOIN films_producers_links flnk1 USING(film_id)
LEFT JOIN producers pr USING(producer_id)
LEFT JOIN films_producers_links flnk2 USING(producer_id)
LEFT JOIN films_actors_links alnk 
	ON (alnk.film_id = flnk2.film_id)
LEFT JOIN actors ac USING(actor_id)
WHERE fi.film_id = 1;


      title_ru       |    producer     |       actors       
---------------------+-----------------+--------------------
 Алита: Боевой ангел | Роберт Родригес | Махершала Али
 Алита: Боевой ангел | Роберт Родригес | Джеки Эрл Хейли
 Алита: Боевой ангел | Роберт Родригес | Роза Салазар
 Алита: Боевой ангел | Роберт Родригес | Эд Скрейн
 Алита: Боевой ангел | Роберт Родригес | Киан Джонсон
 Алита: Боевой ангел | Роберт Родригес | Дженнифер Коннелли
 Алита: Боевой ангел | Роберт Родригес | Кристоф Вальц
(7 rows)

SELECT 
	fi.title_ru, 
	(pr.first_name || ' ' || pr.second_name) AS producer,
	(ac.first_name || ' ' || ac.second_name) AS actors
FROM films fi 
LEFT JOIN films_producers_links flnk1 USING(film_id)
LEFT JOIN producers pr USING(producer_id)
LEFT JOIN films_producers_links flnk2 USING(producer_id)
LEFT JOIN films_actors_links alnk 
	ON (alnk.film_id = flnk2.film_id)
LEFT JOIN actors ac USING(actor_id)
WHERE fi.film_id <= 5
ORDER BY fi.title_ru, actors;


             title_ru             |    producer     |       actors       
----------------------------------+-----------------+--------------------
 13 часов: Тайные солдаты Бенгази | Майкл Бэй       | Джеймс Бэдж Дэйл
 13 часов: Тайные солдаты Бенгази | Майкл Бэй       | Джон Красински
 13 часов: Тайные солдаты Бенгази | Майкл Бэй       | Пабло Шрайбер
 13 часов: Тайные солдаты Бенгази | Майкл Бэй       | Тоби Стивенс
 13 часов: Тайные солдаты Бенгази | Майкл Бэй       | Фредди Строма
 Аватар                           | Джеймс Кэмерон  | Джованни Рибизи
 Аватар                           | Джеймс Кэмерон  | Джоэль Мур
 Аватар                           | Джеймс Кэмерон  | Зои Салдана
 Аватар                           | Джеймс Кэмерон  | Мишель Родригес
 Аватар                           | Джеймс Кэмерон  | Сигурни Уивер
 Аватар                           | Джеймс Кэмерон  | Стивен Лэнг
 Аватар                           | Джеймс Кэмерон  | Сэм Уортингтон
 Алита: Боевой ангел              | Роберт Родригес | Джеки Эрл Хейли
 Алита: Боевой ангел              | Роберт Родригес | Дженнифер Коннелли
 Алита: Боевой ангел              | Роберт Родригес | Киан Джонсон
 Алита: Боевой ангел              | Роберт Родригес | Кристоф Вальц
 Алита: Боевой ангел              | Роберт Родригес | Махершала Али
 Алита: Боевой ангел              | Роберт Родригес | Роза Салазар
 Алита: Боевой ангел              | Роберт Родригес | Эд Скрейн
 Добро пожаловать в Zомбилэнд     | Рубен Флейшер   | Вуди Харрельсон
 Добро пожаловать в Zомбилэнд     | Рубен Флейшер   | Джесси Айзенберг
 Добро пожаловать в Zомбилэнд     | Рубен Флейшер   | Эбигейл Бреслин
 Добро пожаловать в Zомбилэнд     | Рубен Флейшер   | Эмма Стоун
 Матрица                          | Братья Вачовски | Джо Пантолиано
 Матрица                          | Братья Вачовски | Керри-Энн Мосс
 Матрица                          | Братья Вачовски | Киану Ривз
 Матрица                          | Братья Вачовски | Лоуренс Фишборн
 Матрица                          | Братья Вачовски | Хьюго Уивинг
(28 rows)


```
</details>

Так и не понял как красиво убрать повторения

### 3.

> Продолжаем работу с домашней базой данных, практикуем разницу между видами джоинов, дополняем базу данных новыми сущностями на свой вкус и цвет. Инфу о дополненном и найденом пишем в файле `README.md` в репозитории с этой базой данных. 

### Результаты наработок, как обычно, дампом заливаем на github или gitlab так, чтобы я легко нашел их по номеру урока.