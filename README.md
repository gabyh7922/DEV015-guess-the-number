# Adivina el Número - Guess the Number

## 1. Resumen del Proyecto

_Guess The Number_ es un juego interactivo que se desarrolla en el terminal,
donde la jugadora y el ordenador se turnan para intentar adivinar un número
aleatorio entre 1 y 100. Deben tener en cuenta la tentativa anterior, si fue
"muy alta" o "muy baja".
![Demostración animada de sesión de juego](https://firebasestorage.googleapis.com/v0/b/laboratoria-945ea.appspot.com/o/guess-the-number-demo.gif?alt=media)


**Elementos del juego**

- player 1
- Computadora
- Numero aleatorio con random
- Random que virifca y guarda dos numeros para crear el limite de consulta segun el Rango que computadora indique

**En este proyecto trabaje todo desde una solo archivo Python ya que lo veo mas practico, la distribucion fue la siguiente:**
- Main.py : en este archivo cree la importacion de dos librerias una llamada random y la otra llamada time (manejo y usos se los dejare abajo)
- El objetivo principal era crear una variable Random que creara un numero aleatorio para que pueda ser adivinado. 
- Llegamos a la creacion de una funcion llamada  **Comparation_result** con su argumento **consult**, 
este esta verifica si el numero que generamos en random es mayor o menor.

**Ìngresamos al area del** **Ciclo o Bucle**
 - En el bucle verificamos con un input el ingreso del valor de uno de los jugadores **player** una vez tengamos el numero de **player**
 lo comparamos con :
 - Numero correcto.
 - Numero mernor.
 - Numero mayor.
 **Creamos una variable llamada **computadora_numero** donde con un random genera su numero para ser comparado y lograr la interaccion de player y "computadora"**
 donde dicho numero es tambien verificado con:
  - Numero correcto.
  - Numero mernor.
  - Numero mayor.
  **En este while utilizamos la declaracion break para romper el ciclo y no crear ciclos infinitos o con errores que dificulten el proceso del while.**

**Utilizo  la funcion **time.sleep(1)** para pausar la ejecucion 1 segundo , esto lo hago para tener una mejor experiencia en el juego.**

**Ingresando al modo Hacker**
- en esta seccion transformamos la interaccion de **computadora_numero** con la creacion de un random.randint(MIN_NUM, MAX_NUM) que guarde el ultimo valor de dicha variable bien sea por arriba o por abajo del numero random principal, esto genera un nuevo rango con el cual aseguramos que **computadora_numero** tenga una "ventaja" y aseguremos menor rango de numeros repetidos.

  <details><summary>Links de Consulta </summary><p>

  * [MSTest V2 - GitHub](https://github.com/microsoft/testfx?tab=readme-ov-file)
  * [Prueba unitaria de C# con MSTest y .NET](https://learn.microsoft.com/es-es/dotnet/core/testing/unit-testing-with-mstest)
</p></details>

### Python

- [ ] **Variables (declaración, asignación, ámbito)**

  <details><summary>Links</summary><p>

  * [Variables in Python – Real Python (en inglés)](https://realpython.com/python-variables/)
  * [Variables in Python - GeeksforGeeks (en inglés)](https://www.geeksforgeeks.org/python-variables/)
</p></details>

- [ ] **Uso de condicionales (if, elif, ternario)**

  <details><summary>Links</summary><p>

  * [Conditional Statements in Python – Real Python (en inglés)](https://realpython.com/python-conditional-statements/)
</p></details>

- [ ] **Operadores (identidad, aritméticos, comparación etc)**

  <details><summary>Links</summary><p>

  * [Python Operators - GeeksforGeeks (en inglés)](https://www.geeksforgeeks.org/python-operators/)
</p></details>

- [ ] **Docstrings (y su diferencia de comentarios)**

  <details><summary>Links</summary><p>

  * [Docstrings - Python Docs (en inglés)](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)
</p></details>

- [ ] **Linting (pylint)**

  <details><summary>Links</summary><p>

  * [Pylint - Documentación oficial](https://pylint.pycqa.org/en/latest/)
  * [Linting Python in Visual Studio Code - Visual Studio Code Docs (en inglés)](https://code.visualstudio.com/docs/python/linting)
</p></details>

#### Tipos de datos

- [ ] **Tipos de datos primitivos (int, float, str, bool)**

  <details><summary>Links</summary><p>

  * [Data Types - Python Docs (en inglés)](https://docs.python.org/3/library/datatypes.html)
  * [Data types in Python (en inglés)](https://www.educative.io/answers/data-types-in-python)
</p></details>

- [ ] **Listas (arrays)**

  <details><summary>Links</summary><p>

  * [Lists - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
  * [Lists and Tuples in Python - Real Python (en inglés)](https://realpython.com/python-lists-tuples/)
</p></details>

- [ ] **Tuples**

  <details><summary>Links</summary><p>

  * [Tuples - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
  * [Lists and Tuples in Python - Real Python (en inglés)](https://realpython.com/python-lists-tuples/)
</p></details>

- [ ] **Dictionaries (Dicts)**

  <details><summary>Links</summary><p>

  * [Dictionaries - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
  * [Dictionaries in Python - Real Python (en inglés)](https://realpython.com/python-dicts/)
</p></details>

- [ ] **Sets**

  <details><summary>Links</summary><p>

  * [Sets - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#sets)
  * [Sets in Python - Real Python (en inglés)](https://realpython.com/python-sets/)
</p></details>

#### Funciones

- [ ] **Conceptos basicos (params, args, default values, return)**

  <details><summary>Links</summary><p>

  * [Python Functions - GeeksforGeeks (en ingles)](https://www.geeksforgeeks.org/python-functions/)
</p></details>

#### Iteración

- [ ] **Uso de bucles/ciclos (while, for..in)**

  <details><summary>Links</summary><p>

  * [Loops in Python - For, While and Nested Loops - GeeksforGeeks](https://www.geeksforgeeks.org/loops-in-python/)
  * [Loops - Learn Python - Free Interactive Python Tutorial](https://www.learnpython.org/en/Loops)
</p></details>

#### Testing en Python

- [ ] **Pruebas unitarias (unit tests, unittest, pytest)**

  <details><summary>Links</summary><p>

  * [unittest - Python Docs (en inglés)](https://docs.python.org/3/library/unittest.html)
  * [pytest - Documentación oficial](https://docs.pytest.org/en/6.2.x/)
</p></details>

- [ ] **Uso de mocks (y patch)**

  <details><summary>Links</summary><p>

  * [unittest.mock - Python Docs (en inglés)](https://docs.python.org/3/library/unittest.mock.html)
  * [Python Mock Library - Real Python (en inglés)](https://realpython.com/python-mock-library/)
</p></details>

- [ ] **Uso de fixtures**

  <details><summary>Links</summary><p>

  * [pytest fixtures - Documentación oficial](https://docs.pytest.org/en/6.2.x/fixture.html)
</p></details>

#### Modularización

- [ ] **Módulos**

  <details><summary>Links</summary><p>

  * [Módulos - Python Docs (en inglés)](https://docs.python.org/3/tutorial/modules.html)
</p></details>

#### Manejo de dependencias

- [ ] **pip (instalación y uso de paquetes)**

  <details><summary>Links</summary><p>

  * [pip - Python Docs (en inglés)](https://docs.python.org/3/installing/index.html)
</p></details>

- [ ] **Virtual Environment (ambientes virtuales, virtualenv)**

  <details><summary>Links</summary><p>

  * [venv — Creation of virtual environments — Python 3.12.2 documentation (en inglés)](https://docs.python.org/3/library/venv.html)
  * [Python Virtual Environments: A Primer – Real Python (en inglés)](https://realpython.com/python-virtual-environments-a-primer/)
</p></details>

- [ ] **requirements.txt**

  <details><summary>Links</summary><p>

  * [requirements.txt - Documentación oficial](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
</p></details>

### C#

- [ ] **Variables**

  <details><summary>Links</summary><p>

  * [Variables (en inglés) - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/language-specification/variables)
  * [C# | Variables](https://www.geeksforgeeks.org/c-sharp-variables/)
  * [Variables y Tipos en C#](https://desarrolloweb.com/articulos/variables-tipos-csharp)
</p></details>

- [ ] **Condicionales**

  <details><summary>Links</summary><p>

  * [Instrucciones de selección - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/statements/selection-statements)
</p></details>

- [ ] **Bucles/Ciclos**

  <details><summary>Links</summary><p>

  * [Instrucciones de iteración - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/statements/iteration-statements)
</p></details>

- [ ] **Operadores**

  <details><summary>Links</summary><p>

  * [Operadores y expresiones de C# (referencia de C#) - Microsoft Docs](https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/operators/)
</p></details>

- [ ] **Modificadores de Acceso**

  <details><summary>Links</summary><p>

  * [Modificadores de acceso (Guía de programación de C#) - Microsoft Docs](https://docs.microsoft.com/es-es/dotnet/csharp/programming-guide/classes-and-structs/access-modifiers)
</p></details>

- [ ] **Espacios de Nombres (namespaces)**

  <details><summary>Links</summary><p>

  * [Declaración de espacios de nombres para organizar los tipos - Microsoft Docs](https://docs.microsoft.com/es-es/dotnet/csharp/programming-guide/namespaces/)
</p></details>

#### Tipos de datos

- [ ] **Tipos de datos primitivos**

  <details><summary>Links</summary><p>

  * [Tipos integrados (referencia de C#) - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/built-in-types)
  * [C# | Data Types (en inglés)](https://www.geeksforgeeks.org/c-sharp-data-types/)
</p></details>

- [ ] **Tipos de datos no primitivos**

  <details><summary>Links</summary><p>

  * [Common Type System - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/csharp/fundamentals/types/#the-common-type-system)
</p></details>

#### Colecciones

- [ ] **Listas**

  <details><summary>Links</summary><p>

  * [List<T> Clase - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/api/system.collections.generic.list-1?view=net-8.0)
  * [Aprenda a administrar colecciones de datos mediante List<T> en C# - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/csharp/tour-of-csharp/tutorials/arrays-and-collections)
</p></details>

- [ ] **Arreglos**

  <details><summary>Links</summary><p>

  * [Matrices - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/arrays)
</p></details>

- [ ] **Conjuntos (Sets)**

  <details><summary>Links</summary><p>

  * [HashSet<T> Clase - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/api/system.collections.generic.hashset-1?view=net-8.0)
  * [HashSet in C# with Examples (en inglés)](https://www.geeksforgeeks.org/hashset-in-c-sharp-with-examples/)
</p></details>

#### Funciones

- [ ] **Funciones Lambda**

  <details><summary>Links</summary><p>

  * [Expresiones lambda y funciones anónimas (referencia de C#) - Microsoft Docs](https://docs.microsoft.com/es-es/dotnet/csharp/programming-guide/statements-expressions-operators/lambda-expressions)
</p></details>

- [ ] **Decoradores (Atributos)**

  <details><summary>Links</summary><p>

  * [Atributos (en Inglés) - Microsoft Docs](https://docs.microsoft.com/es-es/dotnet/csharp/programming-guide/concepts/attributes/)
  * [Definición y lectura de atributos personalizados - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/csharp/advanced-topics/reflection-and-attributes/attribute-tutorial)
</p></details>

#### Pruebas

- [ ] **xUnit**

  <details><summary>Links</summary><p>

  * [xUnit.net Documentación - xUnit.net](https://xunit.net/#documentation)
  * [Prueba unitaria de C# en .NET Core mediante pruebas de dotnet y xUnit - Microsoft Docs](https://learn.microsoft.com/es-es/dotnet/core/testing/unit-testing-with-dotnet-test)
</p></details>

- [ ] **MSTest**

  <details><summary>Links</summary><p>

  * [MSTest V2 - GitHub](https://github.com/microsoft/testfx?tab=readme-ov-file)
  * [Prueba unitaria de C# con MSTest y .NET](https://learn.microsoft.com/es-es/dotnet/core/testing/unit-testing-with-mstest)
</p></details>


