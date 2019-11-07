template: slide_section
name: data_types
# Data Types

---

template: slide_normal
## Variables and Data Types - Concept

***Variables*** and ***data types*** are the building blocks of all programs.

In order to better manipulate them, two concepts must be taken into consideration:

+ **State**: The current *status* of a data type.
    True or False; 1, 2, 1000; 1.4, 1.2, etc ...
+ **Mutation**: The process of altering the *state* of a data type.

Then, we can define:

+ **Data type**: A way in which data can be arranged.
    When creating a new data type a "copy" of it is created
    (an ***object***) in memory.
     Some are ***mutable*** (are sucseptible to change) where as others are ***immutable***.
     Ex: boolean, integer, string, etc ...

---

## Data Types - Numbers

In general there are two types of representing numbers: ***integers*** and ***floats***.
You can create these variables easily in the interpreter:

```python
a=3   # integer
b=4.0 # float
```

|*Operation* | *Symbol* |
|:-|:-:|
|Addition            |          + |
|Subtraction         |          - |
|Multiplication      |          * |
|Division            |          / |
|Integer Division    |          // |
|Remainder           |          % |
|Power               |          ** |

???

Mostrar q 2e5 funciona
Mostrar q += e amigos existem

---

## Data Types - Numbers

Some notes to take into account:

+ When dividing two numbers the result is a *float*.
+ When using operators between *integers* the result is an *integer*
    (except for division).
+ When using operators between *floats* the result is a *float*.
+ When using operators between *floats* and integers the result is a *float*.

  ```python
  print(3.0 * 2) # 6.0
  print(1 / 1) # 1.0
  ```

+ Python takes operation priority into account
   (parenthesis are the highest priority, then \*\*, etc...)

---

## Data Types - Booleans

The ***boolean*** type is used to store values for ***True*** or ***False***.
Some variables can be converted to boolean by using:

```python
bool("") # False
bool("qwerty") # True
```

In general, an object that is considered to be empty (Ex: "", [  ], 0)
returns false, while an object that contains anything returns true (Ex: 5, 0.1).

True          | False
--------------|----------------
True          | False
"0"           | ""
[1, 2, "asd"] | [  ]
{4}           | {}
4             | 0
0.01          | 0.0

---

## Data Types - Strings

The ***string*** data type stores text or a sequence of characters. We can define
them by surrounding text by ', " or """.

```python
a="this is a string"
```

To define a quote inside a string, so as to not confuse the python interpreter,
a escape sequence \" can be used.

```python
print("\"This is a quote\"")
```

---

## Escape Sequences

| **Output** | **Escape Sequence** |
| :- | :-: |
| Backslash | \\\\ |
| Newline / Paragraph | \\n |
| Double quote | \\" |
| Single quote | \\' |
| Unicode character | \\Uxxxx |
| Octal character | \\o87 |
| Hexadecimal character | \\xFA |

---

## String Indexing

By convention, the indexing of the characters in a string starts at 0.  
INSERT STRING IMG HERE  

---

## String Indexing

You can use indexing to:

+ Access the nth character of a string using __**str[n]**__.
+ Retrieve the last character of a string by __**str[-1]**__.
+ Access the nth last character with __**str[-n]**__..
+ Inverse the string with __**str[::-1]**__.

```python
a="IEEE"
print(a[0])   # "I"
print(a[-2]   # "E")
print(a[::-1] # EEEI)
```

---

## String Slicing

Indexing also allows the ***slicing*** of a string. When slicing, a new substring
is always created. The starting and ending chars of that substring can be specified
(at least one of them is required). A string can be sliced using the syntax ***str[start:end]***:

```python
my_str="A beautiful morning"
my_substr=my_str[2:11]
print(my_substr) # beautiful
```

Using only one integer will yield either all contents to, or from that position.

```python
print("A beautiful morning"[12:]) # morning
print("A beautiful morning"[:12]) # A beautiful
```

???

Notice how the first integer refers to the character 'b' (inclusive) and 11
corresponds to the whitespace after 'l' (exclusive).

---

## Data Types - String Methods

One particularity of strings is that they are ***immutable***,
and as such, cannot be changed. 

```python
a="str"
a[0]="t" # ILLEGAL! - str object does not support assignment
```

As a consequence, when trying to change the content of a
string we are forced to create a new one.
So as to make this process easier the str class has a
selection of methods that take an input string and
create a new object in memory (which is usually a modified version of that string).

A method can be called using ***str.method(__args__)***.
Many methods require additional arguments and sometimes they have to be of
a specific type. Some arguments are also optional. These are
surrounded by brackets.

The command ***help(__method__)*** can be used to see the official
documentation, which has information on how to use the method and what it does.
The official documentation can also be accessed by this [***link***](https://docs.python.org/3/index.html).

The following list contains the most common string methods. All of their
descriptions are either adapted or copied from the official python documentation.

+ ***str.capitalize()*** - Makes first character upper case and the rest lower

    ```python
    "ferNANdo caRVALho".capitalize() # Fernando carvalho
    ```

+ ***str.count(sub[, start[, end]])*** - Return the number of non-overlapping
  occurrences of substring sub in the range [start, end].
  Optional arguments start and end are interpreted as in slice notation.

  ```python
  "ananas".count("an") # 2
  "ananas".count("an", 2) # 1
  ```

+ ***str.endswith(suffix)*** - Returns True if the string ends with the specified
    suffix. False otherwise.

   ```python
   "test.pdf".endswith("pdf") # True
   ```

+ ***str.find(sub[, start[, end]])*** - Return the lowest index in the string where
    substring sub is found within the slice s[start:end]. Optional arguments start
    and end are interpreted as in slice notation. Return -1 if sub is not found.

    ```python
    "Dory_Nemo".find("Nemo") # 5
    ```

    **Note:** Don't use when trying to check if sub is a substring. Use the in operator
    (much more efficient)

    ```python
    "Nemo" in "Dory_Nemo" # True
    ```

+ ***str.isdigit()*** - Return true if all characters in the string are digits
    and there is at least one character, false otherwise.

    ```python
    "1234".isdigit() # True
    "123f".isdigit() # False
    ```

+ ***str.isupper*** - Returns true only if all characters of the string are
    uppercased. False otherwise.

    ```python
    "QWERTY_".isupper() # True
    "QWeRTY_".isupper() # False
    ```

+ ***str.join(iter)*** - Concatenates str between every member of iter.

    ```python
    ", ".join("123") # "1, 2, 3"
    "_".join(["1", "2", "3"]) # 1_2_3
    ```

    Note: The last example is a list, which we will discuss later.

+ ***str.lower*** - Return a copy of the string with all the cased characters
    converted to lowercase.

    ```python
    "FeRNaNDo".lower() # "fernando"
    ```

+ ***str.replace(old, new[, count])*** - Return a copy of the string with all
    occurrences of substring old replaced by new. If the optional argument
    count is given, only the first count occurrences are replaced.

    ```python
    "I3E".replace("3", "EE") # IEEE
    "IEEE".replace("E", "_", 2) # I__E
    ```

+ ***str.split*** - Return a **list** of the words in the string, using sep
    as the delimiter string. If maxsplit is given, at most maxsplit splits are done

    ```python
    "1, 2, 3".split(", ") # ["1", "2", "3"]
    "1,2,3".split(',', maxsplit=1) # ["1", "2,3"]
    ```

+ ***str.strip([chars])*** - Returns a copy of a string with the leading and trailing
    characters removed. The chars argument specifies which characters are
    to be removed from the begining and end of the string. Characters are
    removed from the leading end until reaching a string character that is
    not contained in the set of characters in chars. If chars is omitted then
    only whitespaces are removed.

    ```python
    "   big and spacious     ".strip() # "big and spacious"
    "www,archlinux.org".strip("gw.or") # "archlinux"
    ```

+ ***format*** - The format method is one of the most extensive formats in the
    str class. It is designed to help string output formatting. It formats
    strings that are identified with the {} (braces) placeholder. The
    placeholders will then be replaced by the arguments given in format.

    ```python
    name="Fernando"
    print("My name is {}".format(name))
    ```

    It is possible to specify the order in which the strings are substitute
    by inserting an integer into the braces.

    ```python
    print("1st:{3};2nd:{0};3rd:{1};4th:{2}".format("Second", "Third", "Forth", "First"))
    # 1st:First;2nd:Second;3rd:Third;4th:Forth
    ```

    There is a whole portefolio of different options that can be used inside braces
    to format strings. Due to time restrictions we will only mention a few. For more
    information be sure to check [**the official documentation**](https://docs.python.org/3/library/string.html#formatstrings).

    These are the most commmon formatting modifiers:
  + **align** - Specifies the alignment of the string. A width can be give to
      define the minimum field width. If width isn't given, the field width will
      be determined by the content:

    1. **<** - Left align.
    2. **\>** - Right align.
    3. **=** - Forces the padding to be placed after the sign (if any) but before.
      the digits. Only valid for numeric types.
    4. **^** - Centered

    ```python
    print("{:>30}".format("IEEE"))
    #                IEEE
    ```

  + **sign** - Specifies the sign of numerical data.
    1. **+** \- Sign is used for both positive as negative numbers.
    2. **--** \- Only negative numbers have a minus sign.
    3. **space** - Space is used on positive numbers.
    Minus sign on negative numbers.

  + **#** - Specifies how numbers are displayed.
    For integers:
    1. **b** - Binary.
    2. **c** - Unicode character.
    3. **d** - Decimal integer.
    4. **o** - Octal format.
    5. **x** - Hex Format. Lower-case for a-f.
    6. **X** - Hex Format. Upper cas for A-F.

    ```python
    print("{:b}\n{:x}\n{:X}\n".format(8, 13, 13))
    # 1000
    # d
    # D
    ```

    For floats:
    1. **e** - Exponent notation.
    2. **g** - General format. Can be specified to a specific precision. Default
    precision is 6.
    3. **%** - Percentage format. Multiplies the number by 100 followed by a
    percent sign.
    4. __.precision__ - Set number precision. Must be
    inserted befor the format type (if specified).

    ```python
    print("{:.3e}\n{:.2g}\n{:%}".format(3.14, 1.26, 0.666))
    # 3.140e00
    # 1.3
    # 66.600000%

    ```
