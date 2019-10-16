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
-- Name: squad_weapons; Type: TABLE; Schema: public; Owner: mikola-s
--

CREATE TABLE public.squad_weapons (
    weapon_id integer NOT NULL,
    weapon_name text NOT NULL,
    serial_num text NOT NULL,
    ammo text DEFAULT ''::text
);


ALTER TABLE public.squad_weapons OWNER TO "mikola-s";

--
-- Name: squad_weapons_weapon_id_seq; Type: SEQUENCE; Schema: public; Owner: mikola-s
--

CREATE SEQUENCE public.squad_weapons_weapon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.squad_weapons_weapon_id_seq OWNER TO "mikola-s";

--
-- Name: squad_weapons_weapon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mikola-s
--

ALTER SEQUENCE public.squad_weapons_weapon_id_seq OWNED BY public.squad_weapons.weapon_id;


--
-- Name: squad_weapons weapon_id; Type: DEFAULT; Schema: public; Owner: mikola-s
--

ALTER TABLE ONLY public.squad_weapons ALTER COLUMN weapon_id SET DEFAULT nextval('public.squad_weapons_weapon_id_seq'::regclass);


--
-- Data for Name: squad_weapons; Type: TABLE DATA; Schema: public; Owner: mikola-s
--

COPY public.squad_weapons (weapon_id, weapon_name, serial_num, ammo) FROM stdin;
6	GP-25	32978	40 mm grenade VOG-25
8	GP-25	23344	40 mm grenade VOG-25
31	GP-25	405628	40 mm grenade VOG-25
33	GP-25	765760	40 mm grenade VOG-25
2	RPG-7	2381906	overcaliber grenade 40 mm
27	RPG-7	820134	overcaliber grenade 40 mm
4	PKM	BN-301	7,62x54 mm
11	SVD	232132	7,62x54 mm
29	PKM	971221	7,62x54 mm
36	SVD	176676	7,62x54 mm
1	AK-74	249896	5,45x39 mm
3	AK-74	123498	5,45x39 mm
5	AK-74	879832	5,45x39 mm
7	AK-74	355278	5,45x39 mm
26	AK-74	812208	5,45x39 mm
28	AK-74	448275	5,45x39 mm
30	AK-74	968629	5,45x39 mm
32	AK-74	17736	5,45x39 mm
9	AKS-74U	5761278	5,45x39 mm
10	AKS-74U	1235561	5,45x39 mm
34	AKS-74U	362891	5,45x39 mm
35	AKS-74U	316008	5,45x39 mm
12	PM	1234456	9x18 mm PM
37	PM	359044	9x18 mm PM
\.


--
-- Name: squad_weapons_weapon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mikola-s
--

SELECT pg_catalog.setval('public.squad_weapons_weapon_id_seq', 37, true);


--
-- Name: squad_weapons squad_weapons_pkey; Type: CONSTRAINT; Schema: public; Owner: mikola-s
--

ALTER TABLE ONLY public.squad_weapons
    ADD CONSTRAINT squad_weapons_pkey PRIMARY KEY (weapon_id);


--
-- Name: squad_weapons squad_weapons_serial_num_key; Type: CONSTRAINT; Schema: public; Owner: mikola-s
--

ALTER TABLE ONLY public.squad_weapons
    ADD CONSTRAINT squad_weapons_serial_num_key UNIQUE (serial_num);


--
-- PostgreSQL database dump complete
--

