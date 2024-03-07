

# Introducción a Python

## Semana 11
<!-- .element style="text-align:center" -->

![alt text](./img/logo2.png) <!-- .element style="margin-left: auto; margin-right: auto; display: block" -->

---

# Tipos de datos

- En los ordenadores, sólo tenemos unos y ceros
- El significado de los unos y los ceros se lo damos nosotros
- Ejemplo: ¿cómo representaríais una frase? ¿y una imágen?

---

# Tipos de datos en python

Tipos simples:
  - None:	`NoneType`
  - Texto:	`str` (*Here There Be Dragons*)
  - Numericos:	`int`, `float`, `complex`
  - Booleanos: `bool`

Tipos compuestos (tienen más de un valor):
- Secuencia:	`list`, `tuple`, `range`
- Diccionario:	`dict`
- Conjunto:	`set`, `frozenset`
- Binarios:	`bytes`, `bytearray`, `memoryview` (*Here There Be Dragons*)

Se puede consultar el tipo de una variable con `type(variable)`, aunque no suele ser necesario
---

# Tipos numéricos

- `int`:
  - No tiene límite
  - Se pueden usar números hexadecimales y octales: `0x2a`, `0o52`
- `float`:
  - Usa 64 bits
  - Tiene ~ 16 digitos de precisión.
  - De `1.7*10^(-308)` hasta `1.7*10^(308)` (se calcula que hay unos 10^82 átomos en el universo)
  - Tiene +∞ y -∞ (`float("inf")`, `float("-inf")`)
- `complex`:
  - `5+7j`
  - Parte real e imaginaria: `x.real`, `x.imag`
  - Se pueden multiplicar, dividir...

¿Cómo representaríais una cantidad monetaria?

---

# Tipos Booleanos

- Por defecto todo es `True`
- Excepto:
  - `False`
  - Ceros (`0`, `0.0`, `0j`)
  - `None`
  - Listas vacías `[]`
  - Tuplas vacías `()`
  - Diccionarios vacíos `{}`
  - Conjuntos vaćios `()`
  - Cadenas vacías `""`
  - Rangos vacíos `range(0)`
- `True` vale `1`, `False` `0`. **Usar con cuidado**

---

# Operadores booleanos

- Se aplican los operadores `and`, `not`, `or`
- Una comparación devuelve booleano (`3 > 5` => `False`, `2+1 == 3` => `True`)
- Las comparaciones se pueden encadenar: `1 > 2 > 3` ==> `(1 > 2) and (2 > 3)`


Expresión que devuelva `True` si son los dos mayor de edad y el hombre no es mayor que la mujer, o bien si están los dos jubilados.
```python
edad_hombre = ...
edad_mujer = ...
<expresión aquí>
```
---

# Custom truthy y falsy

- Puedes decidir cuando quieres que tus clases sean `True` o `False` con dos métodos:
  - `__bool__`
  - `__len__`: si devuelve 0, es False

```python
class Account:
	def __init__(self, balance):
		self.balance = balance

	def __bool__(self):
		return self.balance > 0
```



---

# Listas

- Literales de listas
- Acceso a listas
- Métodos de listas
- List comprehension


---

# Rangos


---

# Tuplas

https://realpython.com/python-tuple/
fixed and unchangeable series of values
puede contener múltiples tipos
cero index





---


# Diccionarios



---

# ¿Cómo de buena eres realmente?

Había un examen en tu clase y lo has aprobado. ¡Enhorabuena!

Pero eres una persona ambiciosa. Quieres saber si eres mejor que el alumno medio de tu clase.

Recibes las puntuaciones de los exámenes de tus compañeros. Ahora calcula la media y compara tu puntuación.
Devuelve `True` si eres mejor, si no, `False`.

<div></div> <!-- .element style="height: 200px" -->

[Enlace Kata](https://www.codewars.com/kata/5601409514fc93442500010b)

---

# Ordenamiento pseudoalfabético

> He preparado un programa que ordena los números del 1 al 100 en orden alfabético
> es decir: primero los que empiezan por 1, luego por 2, etc. Los que empiezan
> por el mismo dígito los reordena por el dígito que viene a continuación. Así,
> los números quedarían: 1, 10, 100, 11, 12...

¿En qué números coincide el orden numérico con el alfabético?

