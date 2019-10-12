--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: mikola-s
--

CREATE TABLE public.actors (
    id_actor integer NOT NULL,
    first_name text,
    second_name text
);


ALTER TABLE public.actors OWNER TO "mikola-s";

--
-- Name: actors_id_actor_seq; Type: SEQUENCE; Schema: public; Owner: mikola-s
--

CREATE SEQUENCE public.actors_id_actor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_actor_seq OWNER TO "mikola-s";

--
-- Name: actors_id_actor_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mikola-s
--

ALTER SEQUENCE public.actors_id_actor_seq OWNED BY public.actors.id_actor;


--
-- Name: films; Type: TABLE; Schema: public; Owner: mikola-s
--

CREATE TABLE public.films (
    id_film integer NOT NULL,
    title_ru text,
    title_en text,
    release integer
);


ALTER TABLE public.films OWNER TO "mikola-s";

--
-- Name: films_id_film_seq; Type: SEQUENCE; Schema: public; Owner: mikola-s
--

CREATE SEQUENCE public.films_id_film_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_id_film_seq OWNER TO "mikola-s";

--
-- Name: films_id_film_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mikola-s
--

ALTER SEQUENCE public.films_id_film_seq OWNED BY public.films.id_film;


--
-- Name: producers; Type: TABLE; Schema: public; Owner: mikola-s
--

CREATE TABLE public.producers (
    id_producer integer NOT NULL,
    first_name text,
    second_name text
);


ALTER TABLE public.producers OWNER TO "mikola-s";

--
-- Name: producers_id_producer_seq; Type: SEQUENCE; Schema: public; Owner: mikola-s
--

CREATE SEQUENCE public.producers_id_producer_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producers_id_producer_seq OWNER TO "mikola-s";

--
-- Name: producers_id_producer_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mikola-s
--

ALTER SEQUENCE public.producers_id_producer_seq OWNED BY public.producers.id_producer;


--
-- Name: actors id_actor; Type: DEFAULT; Schema: public; Owner: mikola-s
--

ALTER TABLE ONLY public.actors ALTER COLUMN id_actor SET DEFAULT nextval('public.actors_id_actor_seq'::regclass);


--
-- Name: films id_film; Type: DEFAULT; Schema: public; Owner: mikola-s
--

ALTER TABLE ONLY public.films ALTER COLUMN id_film SET DEFAULT nextval('public.films_id_film_seq'::regclass);


--
-- Name: producers id_producer; Type: DEFAULT; Schema: public; Owner: mikola-s
--

ALTER TABLE ONLY public.producers ALTER COLUMN id_producer SET DEFAULT nextval('public.producers_id_producer_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: mikola-s
--

COPY public.actors (id_actor, first_name, second_name) FROM stdin;
1	Уайатт	Олефф
2	Доминик	Монаган
3	Ричард	Армитидж
4	Джон	Красински
5	Керри-Энн	Мосс
6	Махершала	Али
7	Пабло	Шрайбер
8	Уильям	Сэдлер
9	Билл	Скарсгорд
10	Билли	Бойд
11	Николас	Хэмилтон
12	Фредди	Строма
13	Вигго	Мортенсен
14	Тоби	Стивенс
15	Наоми	Скотт
16	Джеки Эрл	Хейли
17	Мартин	Фримен
18	Шон	Бин
19	Эмма	Стоун
20	Вуди	Харрельсон
21	Сигурни	Уивер
22	Джон	Рис-Дэвис
23	Чоузен	Джейкобс
24	Кевин	Костнер
25	Финн	Вулфхард
26	Роза	Салазар
27	Лоуренс	Фишборн
28	Джоэль	Мур
29	Элайджа	Вуд
30	Джон Кэрролл	Линч
31	Джо	Пантолиано
32	Джованни	Рибизи
33	Эбигейл	Бреслин
34	Мена	Массуд
35	Стивен	Лэнг
36	Эд	Скрейн
37	Джек Дилан	Грейзер
38	София	Лиллис
39	Мишель	Родригес
40	Джеймс Бэдж	Дэйл
41	Энди	Серкис
42	Киан	Джонсон
43	Уилл	Смит
44	Томас	Манн
45	Кэти	Бэйтс
46	Иэн	Маккеллен
47	Сэм	Уортингтон
48	Кристофер	Ли
49	Дженнифер	Коннелли
50	Зои	Салдана
51	Орландо	Блум
52	Кристоф	Вальц
53	Киану	Ривз
54	Хьюго	Уивинг
55	Эванджелин	Лилли
56	Джейден	Мартелл
57	Ким	Диккенс
58	Кейт	Бланшетт
59	Джесси	Айзенберг
60	Шон	Астин
61	Люк	Эванс
62	Джереми Рэй	Тейлор
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: mikola-s
--

COPY public.films (id_film, title_ru, title_en, release) FROM stdin;
1	Алита: Боевой ангел	Alita: Battle Angel	2019
2	Аватар	Avatar	2009
3	13 часов: Тайные солдаты Бенгази	13 Hours: The Secret Soldiers of Benghazi	2016
4	Добро пожаловать в Zомбилэнд	Zombieland	2009
5	Матрица	Matrix	1999
6	В погоне за Бонни и Клайдом	The Highwaymen	2019
7	Оно	It	2017
8	Властелин колец: Братство Кольца	The Lord of the Rings: The Fellowship of the Ring	2001
9	Аладдин	Aladdin	2019
10	Хоббит: Нежданное путешествие	The Hobbit: An Unexpected Journey	2012
\.


--
-- Data for Name: producers; Type: TABLE DATA; Schema: public; Owner: mikola-s
--

COPY public.producers (id_producer, first_name, second_name) FROM stdin;
1	Роберт	Родригес
2	Джеймс	Кэмерон
3	Майкл	Бэй
4	Рубен	Флейшер
5	Братья	Вачовски
6	Джон Ли	Хэнкок
7	Энди	Мускетти
8	Питер	Джексон
9	Гай	Ричи
\.


--
-- Name: actors_id_actor_seq; Type: SEQUENCE SET; Schema: public; Owner: mikola-s
--

SELECT pg_catalog.setval('public.actors_id_actor_seq', 62, true);


--
-- Name: films_id_film_seq; Type: SEQUENCE SET; Schema: public; Owner: mikola-s
--

SELECT pg_catalog.setval('public.films_id_film_seq', 10, true);


--
-- Name: producers_id_producer_seq; Type: SEQUENCE SET; Schema: public; Owner: mikola-s
--

SELECT pg_catalog.setval('public.producers_id_producer_seq', 9, true);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: mikola-s
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id_actor);


--
-- Name: films films_pkey; Type: CONSTRAINT; Schema: public; Owner: mikola-s
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT films_pkey PRIMARY KEY (id_film);


--
-- Name: producers producers_pkey; Type: CONSTRAINT; Schema: public; Owner: mikola-s
--

ALTER TABLE ONLY public.producers
    ADD CONSTRAINT producers_pkey PRIMARY KEY (id_producer);


--
-- PostgreSQL database dump complete
--

