# TLS
realization of Russian TLS 1.2

* [Agreements](#agreements)
* [Lectures](#lectures)
* [Task (part 1)](#task-part-1)
  * [Группа 1](#group-1)
  * [Группа 2](#group-2)
  * [Группа 3](#group-3)
* [Task (part 2)](#task-part-2)
  * [Группа 1](#1-group)
  * [Группа 2](#2-group)
  * [Группа 3](#3-group)

## Agreements
* Languange: python3
* Codestyle: PEP8
* Separate branch for each team
## Lectures
https://www.overleaf.com/11271867qqtctbhwksqy
## Task part 1
I ЭТАП. Реализация криптографических примитивов и алгоритмов для TLS 1.2 с российскими криптонаборами

Реализация всех необходимых примитивов и алгоритмов распределяется между тремя группами (по 2-3 человек в группе). Интерфейс алгоритмов должен соответствовать.
### Group 1

**Состав группы:** Ибрагимов, Грамович, ...

Базовые режимы
* Режим шифрования CTR-ACPKM (см. стандарт 1)
* Режим выработки имитовставки OMAC (см. стандарт 4)

Высокоуровневые алгоритмы на основе базовых режимов
* Stateful AtE алгоритм аутентифицированного шифрования (см. стандарт 2)   
* Алгоритмы KExp15/KImp15 (см. стандарт 1)

### Group 2

**Состав группы:** Забелин, Кошкин, Печатнов

http://wwwold.tc26.ru/standard/rs/Р%2050.1.114-2016.pdf - стандарт 2, эллиптические кривые
http://kaf401.rloc.ru/Criptfiles/GOST_R_34.10-2001.pdf - стандарт 6, электронная подпись

Базовый функционал работы с эллиптической кривой (класс с методами)
* Инициализация объекта класса с помощью id кривой (p,m,q,P,a,b)
* Метод сложения точек
* Метод удвоения точки
* Метод вычисления кратной точки
* Метод проверки принадлежности точки кривой

Необходимо поддержать работу с двумя кривыми, используемыми для контрольных примеров стандарта 2:
* id-tc26-gost-3410-2012-256-paramSetA, «1.2.643.7.1.2.1.1.1».
* id-tc26-gost-3410-2012-512-paramSetC, «1.2.643.7.1.2.1.2.3».

Высокоуровневые алгоритмы: алгоритмы подписи и проверки подписи (см. стандарт 6) после получения реализации хэш-функции от 3 группы.

### Group 3

**Состав группы:** Захаров, Дмитриев

Примитив: хэш-функция с длиной выхода 256 и 512 (стандарт 5)
Высокоуровневые алгоритмы (стандарт 3)
* Функция KDF_TREE_GOSTR3411_2012_256 
* Функция PRF_TLS_GOSTR3411_2012_256

После получения реализации функционала работы с эллиптической кривой от группы 2:
* Алгоритм VKO_GOSTR3410_2012_256
* Алгоритм VKO_GOSTR3410_2012_256

## Task part 2
Как вы могли заметить, в первой части задании от вас требовалось реализовать все примитивы, алгоритмы и схемы, необходимые для работы протокола TLS 1.2 с российскими криптонаборами. Во второй части вам предстоит реализовать уже сам протокол и на его базе организовать мини-чат в рамках своей группы. На экзамене у вас будут проверять как наличие и корректность функционирования данного чата на вашей машине, так и код реализованной именно вами части ПО.

Нас интересует протокол TLS 1.2 только с одним c криптонабором TLS_GOSTR341112_256_WITH_KUZNYECHIK_CTR_OMAC (так как Кузнечик вы реализовывали в прошлом семестре). Основной документ, которым вам предстоит пользоваться, можно найти здесь http://wwwold.tc26.ru/standard/draft/%D0%A2%D0%9A26_TLS_2015.pdf. В качестве кривой предлагается использовать кривую id-tc26-gost-3410-12-512-paramSetC (http://wwwold.tc26.ru/methods/recommendation/CPECC14-TC26.pdf) в форме Вейерштрасса. 

Вам необходимо реализовать установление сессии и в ее рамках одного (!) соединения с помощью полного протокола Рукопожатия (Handshake) с двухсторонней аутентификацией и последующую защиту канала с помощью протокола Записи (Record). Отметим, что соблюдение форматов сообщений протоколов Handshake и Record (заголовки, длины) является обязательным (см. 6.2 и 5.2 документа). Разобраться с форматами вам также поможет приложение в конце документа (Приложение B2), где все сообщения разобраны по полям и прокомментированы. Также можете пользоваться ASN1 coder/encoder. 

Процедуры неполного Handshake, session resumption, renegotiation реализовывать не нужно. Протокол Alert можно реализовать в усеченном виде, где на ошибку любого типа (или при закрытии сессии) будет возвращаться сообщение протокола Alert уровня fatal с любым значением поля description. 

Проверять пересылаемые сертификаты на действительность также не нужно. Вместо сертификата разрешается передавать идентификатор и открытый долговременный ключ.

То есть в поле body сообщений Certificate протокола Рукопожатия достаточно передать строку, состоящую из идентификатора (вашей группе хватит одного байта)  и ключа в формате (x,y) (128 байт для указанной кривой).

К каждому человеку, выполняющему данный практикум, должны быть привязаны идентификатор и долговременная ключевая пара. Так как сертификатами разрешено не пользоваться, взамен стоит, например, организовать следующее. Совместно составить таблицу соответствия идентификаторов и открытых ключей и распространить ее между машинами, тогда валидность долговременного ключа в протоколе может проверяться по данной таблице.

### 1 group.
Организация сети между машинами и реализация протокола Record. 

Можно реализовывать в виде класса, полями которого являются ключевой материал и текущий номер записи, а методами – <сформировать запись>, <распарсить запись>, <обновить ключевой материал>.

Таким образом, для записи и чтения вам понадобятся два класса.   

### 2 group.
Реализация функционала серверной части протокола Handshake.

Функционал Handshake лучше реализовывать в виде функций-обработчиков классов Client и Server: <обработать сообщение>, <сформировать сообщение>.

### 3 group.
Реализация функционала клиентской части протокола Handshake.

Функционал Handshake лучше реализовывать в виде функций-обработчиков классов Client и Server: <обработать сообщение>, <сформировать сообщение>.

## Необходимые стандарты

* Р 1233565.1.\_\_\_-2018 «Информационная технология. Криптографическая защита информации. Криптографические алгоритмы, сопутствующие применению алгоритмов блочного шифрования»
* Р 50. . - 20\_\_\_\_\_ «Информационная технология. Криптографическая защита информации. Использование российских криптографических алгоритмов в протоколе безопасности транспортного уровня (TLS 1.2)»
* Р 50.1.113–2016 «Информационная технология. Криптографическая защита информации. Криптографические алгоритмы, сопутствующие применению алгоритмов электронной цифровой подписи и функции хэширования»
* ГОСТ Р 34.13–2015 «Информационная технология. Криптографическая защита информации. Режимы работы блочных шифров»
* ГОСТ Р 34.11–2012 «Информационная технология. Криптографическая защита информации. Функция хэширования»
* ГОСТ Р 34.10–2012 «Информационная технология. Криптографическая защита информации. Процессы формирования и проверки электронной цифровой подписи»
