# TLS
realization of Russian TLS 1.2
## Agreements
* Languange: python3
* Codestyle: PEP8
* Separate branch for each team
## Lectures
https://www.overleaf.com/11271867qqtctbhwksqy
## Task
I ЭТАП. Реализация криптографических примитивов и алгоритмов для TLS 1.2 с российскими криптонаборами

Реализация всех необходимых примитивов и алгоритмов распределяется между тремя группами (по 2-3 человек в группе). Интерфейс алгоритмов должен соответствовать.
### Группа 1. Алгоритмы на основе блочного шифра Кузнечик

**Состав группы:** Ибрагимов, Грамович, ...

Базовые режимы
* Режим шифрования CTR-ACPKM (см. стандарт 1)
* Режим выработки имитовставки OMAC (см. стандарт 4)

Высокоуровневые алгоритмы на основе базовых режимов
* Stateful AtE алгоритм аутентифицированного шифрования (см. стандарт 2)   
* Алгоритмы KExp15/KImp15 (см. стандарт 1)

### Группа 2. Алгоритмы на основе группы точек эллиптической кривой

**Состав группы:** Забелин, Кошкин, Печатнов

http://wwwold.tc26.ru/standard/rs/Р%2050.1.114-2016.pdf

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

### Группа 3. Алгоритмы на основе хэш-функции

**Состав группы:** Захаров, Карпачёв, ...

Примитив: хэш-функция с длиной выхода 256 и 512 (стандарт 5)
Высокоуровневые алгоритмы (стандарт 3)
* Функция KDF_TREE_GOSTR3411_2012_256 
* Функция PRF_TLS_GOSTR3411_2012_256

После получения реализации функционала работы с эллиптической кривой от группы 2:
* Алгоритм VKO_GOSTR3410_2012_256
* Алгоритм VKO_GOSTR3410_2012_256


## Необходимые стандарты

* Р 1233565.1.\_\_\_-2018 «Информационная технология. Криптографическая защита информации. Криптографические алгоритмы, сопутствующие применению алгоритмов блочного шифрования»
* Р 50. . - 20\_\_\_\_\_ «Информационная технология. Криптографическая защита информации. Использование российских криптографических алгоритмов в протоколе безопасности транспортного уровня (TLS 1.2)»
* Р 50.1.113–2016 «Информационная технология. Криптографическая защита информации. Криптографические алгоритмы, сопутствующие применению алгоритмов электронной цифровой подписи и функции хэширования»
* ГОСТ Р 34.13–2015 «Информационная технология. Криптографическая защита информации. Режимы работы блочных шифров»
* ГОСТ Р 34.11–2012 «Информационная технология. Криптографическая защита информации. Функция хэширования»
* ГОСТ Р 34.10–2012 «Информационная технология. Криптографическая защита информации. Процессы формирования и проверки электронной цифровой подписи»
