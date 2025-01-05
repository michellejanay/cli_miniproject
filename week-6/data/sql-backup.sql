DROP TABLE IF EXISTS "couriers";
CREATE TABLE "public"."couriers" (
    "courier_id" integer GENERATED ALWAYS AS IDENTITY NOT NULL,
    "name" character varying(20) NOT NULL,
    "phone" character varying(20) NOT NULL,
    CONSTRAINT "couriers_pkey" PRIMARY KEY ("courier_id")
) WITH (oids = false);

DROP TABLE IF EXISTS "orders";
CREATE TABLE "public"."orders" (
    "order_id" integer GENERATED ALWAYS AS IDENTITY NOT NULL,
    "customer_name" character varying(200) NOT NULL,
    "customer_address" character varying(200) NOT NULL,
    "customer_phone" character varying(20) NOT NULL,
    "courier" integer,
    "order_status" character varying(200) NOT NULL,
    "items" character varying(20) NOT NULL,
    CONSTRAINT "orders_pkey" PRIMARY KEY ("order_id")
) WITH (oids = false);


DROP TABLE IF EXISTS "products";
CREATE TABLE "public"."products" (
    "product_id" integer GENERATED ALWAYS AS IDENTITY NOT NULL,
    "name" character varying(20) NOT NULL,
    "price" numeric,
    CONSTRAINT "products_pkey" PRIMARY KEY ("product_id")
) WITH (oids = false);

INSERT INTO "couriers" ("name", "phone") VALUES
('Bob',	'07811111111'),
('John',	'07822222222'),
('Sarah',	'07807833333333'),
('Billy',	'07844444444');

INSERT INTO "orders" ("customer_name", "customer_address", "customer_phone", "courier", "order_status", "items") VALUES
('john',	'123 road name',	'07812345678',	1,	'PREPARING',	'1,2,3');

INSERT INTO "products" ("name", "price") VALUES
('White Coffee',	3.00),
('Black Coffee',	2.50),
('Latte',	3.50),
('Cappuccino',	3.50),
('Mocha',	4.00),
('White Mocha',	4.00),
('Water',	0.00);