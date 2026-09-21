def find_duplicates(nums):
    """Problema: encontrar todos los valores repetidos.

    Solución: guardar los valores vistos y añadir al resultado los que vuelven
    a aparecer. Precondición: ``nums`` debe ser iterable. Complejidad: O(n).
    Nota: el resultado no conserva un orden garantizado porque usa un set.
    """
    seen = set()
    vistos = set()
    # return all numbers that appear more than once
    for x in nums:
       if x in seen:
           vistos.add(x)
       else:
           seen.add(x)
    return list(vistos)


def two_sum(nums, target): # nums = [2,7,11,12] target = 9
    """Problema: localizar dos índices cuya suma sea ``target``.

    Solución: complementar cada número con ``target - num`` y consultar los
    índices ya vistos. Complejidad: O(n). Si no hay solución, retorna None.
    """
    seen = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen.keys():
            return [seen[needed], i]
        else:
            seen[num] = i


def first_unique_char(s):
    """Problema: obtener el índice del primer carácter no repetido.

    Solución: contar frecuencias en una primera pasada y buscar el primero con
    frecuencia uno en una segunda. Si no existe, retorna -1. Complejidad: O(n).
    """
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for i, char in enumerate(s):
        if freq[char] == 1:
            return i

    return -1


def has_pair_sum(nums, target):
    """Problema: comprobar si existe una pareja con suma ``target``.

    Solución: consultar en un set el complemento de cada número ya recorrido.
    No requiere que ``nums`` esté ordenada. Complejidad: O(n).
    """
    seen = set()
    for x in nums:
        needed= target- x
        if needed in seen:
            return True
        else:
            seen.add(x)

            

def has_pair_sum_2(nums, target):
    """Problema: comprobar una pareja con suma ``target`` usando dos punteros.

    Solución: mover los punteros según la suma actual. Precondición crítica:
    ``nums`` debe estar ordenada de menor a mayor. Complejidad: O(n).
    """
    left = 0
    right = len(nums)-1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return True
        elif total < target:
            left +=1
        else:
            right -=1     
    return False
            


def max_subarray_sum(nums, k):
    """Problema: encontrar la mayor suma de una ventana de tamaño ``k``.

    Solución: mantener una ventana deslizante, restando el elemento que sale y
    sumando el que entra. ``k`` debe estar entre 1 y ``len(nums)``. O(n).
    """
    window_sum = sum(nums[0:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


def is_valid(s):
    """Problema: validar que los delimitadores estén correctamente anidados.

    Solución: usar una pila y comparar cada cierre con su apertura. Esta primera
    versión debe terminar verificando que la pila quede vacía; está duplicada
    más abajo y la segunda definición es la que Python utiliza. Complejidad: O(n).
    """
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    for char in s:
        if char in pairs:  # es un cierre
            if len(stack)==0:
                return False
            if stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:  # es una apertura
            stack.append(char)
    return True
        
            
def binary_search(nums, target):
    """Problema: buscar ``target`` en una lista ordenada.

    Solución: descartar la mitad imposible en cada iteración. ``nums`` debe estar
    ordenada. Retorna el índice o -1. Complejidad: O(log n).
    """
    left = 0
    right = len(nums) -1
    while left <= right:
        puntero = (left + right) // 2
        if nums[puntero] == target:
            return puntero
        elif nums[puntero] > target:
            right = puntero - 1
        else:
            left = puntero + 1

    return -1


def has_pair_difference(nums, k):
    """Problema: comprobar si dos valores tienen diferencia absoluta ``k``.

    Solución: buscar ``num + k`` o ``num - k`` entre los valores ya vistos.
    Complejidad: O(n). Para k=0 se necesitan dos apariciones del mismo valor.
    """

    seen = set()

    for num in nums:
        if num + k in seen or num - k in seen:
            return True
        seen.add(num)

    return False


def longest_unique_substring(s):
    """Problema: hallar la longitud de la mayor subcadena sin repetidos.

    Solución: mantener una ventana y encogerla mientras el carácter se repita.
    Complejidad: O(n), con memoria O(n).
    """
    window = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]

        # Mientras haya un repetido, encogemos la ventana
        while char in window:
            window.remove(s[left])
            left += 1

        # Añadimos el nuevo carácter
        window.add(char)

        # Calculamos el tamaño de la ventana
        max_length = max(max_length, right - left + 1)

    return max_length


def longest_consecutive(nums):
    """Problema: encontrar la secuencia consecutiva más larga.

    Solución: iniciar una cuenta solo cuando no existe el predecesor en un set.
    Los duplicados no amplían la secuencia. Complejidad: O(n) promedio.
    """
    seen = set(nums)
    longest = 0

    for num in seen:
        if num - 1 not in seen:
            current = num
            count = 1

            while current + 1 in seen:
                current += 1
                count += 1

            longest = max(count, longest)

    return longest


def max_distinct_in_window(nums, k):
    """Problema: obtener el máximo de valores distintos en una ventana de k.

    Solución: mantener frecuencias al deslizar la ventana. ``k`` debe ser válido
    y positivo; conviene validarlo antes de crear la primera ventana. O(n).
    """
    counts = {}

    # Primera ventana
    for num in nums[:k]:
        counts[num] = counts.get(num, 0) + 1

    max_distinct = len(counts)

    # Deslizar
    for i in range(k, len(nums)):
        # Sale nums[i-k]
        if counts.get(nums[i-k]) > 1:
            counts[nums[i-k]] = counts.get(nums[i-k]) -1 # o counts[nums[i-k]] -= 1
        else:
            del counts[nums[i-k]]   

        counts[nums[i]] = counts.get(nums[i], 0) + 1


        max_distinct = max(max_distinct, len(counts)) 

    return max_distinct


def merge_intervals(intervals):
    """Problema: unir intervalos que se solapan.

    Solución: ordenar por inicio y extender el último intervalo fusionado.
    La función modifica ``intervals`` al ordenarlo y asume [inicio, fin] válido.
    Complejidad: O(n log n).
    """
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

def can_attend_all(meetings):
    """Problema: comprobar si todas las reuniones pueden atenderse.

    Solución: ordenar por hora de inicio y comparar cada inicio con el fin
    anterior. La lista de entrada se ordena in-place; se recomienda documentar
    o cambiar ese comportamiento. Complejidad: O(n log n).
    """
    meetings.sort(key = lambda x: x[0])
    anterior = 0
    for meet in meetings:
        if anterior == 0:
            anterior = meet[1]
        else:
            if meet[0] >= anterior:
                anterior = meet[1]
            else:
                return False

    return True



class ListNode:
    """Nodo de una lista enlazada; ``next`` apunta al nodo siguiente o None."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node3  # ← aquí creamos el ciclo

head = node1

def has_cycle(head):
    """Problema: detectar un ciclo en una lista enlazada.

    Solución: algoritmo de Floyd con puntero lento y rápido. Complejidad: O(n)
    y memoria O(1).
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def remove_duplicates(nums):
    """Problema: quitar duplicados de una lista ordenada in-place.

    Solución: ``pointer`` marca la última posición única y ``next`` recorre la
    lista. Precondición: lista ordenada. Atención: el retorno debe usar
    ``nums[:pointer + 1]`` para no perder el último elemento único.
    Complejidad: O(n).
    """
    pointer = 0
    next = 1

    while next < len(nums):
        if nums[pointer] == nums[next]:
            next += 1
        else:
            pointer += 1
            nums[pointer] = nums[next]
            next += 1

    return pointer + 1, nums[:pointer]


def product_except_self(nums):
    """Problema: producto de todos los valores salvo el de cada índice.

    Solución: combinar productos acumulados desde la izquierda y desde la
    derecha, sin división y soportando ceros. Complejidad: O(n), memoria O(1)
    adicional aparte del resultado.
    """
    result = [1] * len(nums)

    # Primera pasada: izquierda → derecha
    left_product = 1

    for i in range(len(nums)):
        result[i] = left_product
        left_product = left_product * nums[i]

    # Segunda pasada: derecha → izquierda
    right_product = 1

    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * right_product
        right_product = right_product * nums[i]

    return result


def count_positive(nums):
    """Problema: contar valores estrictamente mayores que cero. O(n)."""
    count = 0

    for num in nums:
        if num>0:
            count+=1

    return count


def count_frequencies(nums):
    """Problema: contar cuántas veces aparece cada valor. Solución: diccionario
    de frecuencias. Complejidad: O(n).
    """
    count={}
    for num in nums:
        if num in count:
            count[num] = count.get(num, 0) + 1
        else:
            count[num] = 1

    return count


def count_unique_numbers(nums):
    """Problema: contar valores cuya frecuencia exacta es uno. Complejidad: O(n)."""
    count ={}
    unique = 0
    for num in nums:
        if num in count:
            count[num] = count.get(num, 0) +1
        else:
            count[num] = 1

    for num in count:
        if count[num] == 1:
            unique += 1

    return unique


def first_duplicate(nums):
    """Problema: encontrar el primer valor que vuelve a aparecer.

    Solución: devolver el primer elemento cuyo valor ya está en ``seen``. Si no
    hay duplicados, retorna -1. Complejidad: O(n).
    """
    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return num
    return -1


def longest_consecutive_streak(nums):
    """Problema: obtener la mayor racha consecutiva.

    Solución: usar un set para iniciar solo en valores sin predecesor. Conviene
    recorrer ``seen`` y no ``nums`` para no repetir trabajo con duplicados. O(n)
    promedio.
    """
    max_count = 0
    seen = set(nums)

    for num in nums:
        if num-1 not in seen:
            current = num
            count=1
            while current+1 in seen:
                count +=1
                current +=1
            max_count= max(max_count, count)
        
            
    return max_count


def max_profit(prices):
    """Problema: maximizar el beneficio de una compra y una venta.

    Solución: conservar el precio mínimo visto y el mejor beneficio posterior.
    Si no hay beneficio, retorna 0. Complejidad: O(n).
    """
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if min_price > price:
           min_price = price
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


def max_subarray(nums):
    """Problema: encontrar la suma máxima de un subarreglo contiguo.

    Solución: algoritmo de Kadane, eligiendo entre iniciar una suma nueva o
    continuar la actual. Requiere una lista no vacía. Complejidad: O(n).
    """
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def length_of_longest_substring(s):
    """Problema: medir la mayor subcadena sin caracteres repetidos.

    Solución: ventana deslizante con conjunto. Esta función está duplicada; la
    segunda definición del archivo reemplaza a esta. Complejidad: O(n).
    """
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        max_length = max(max_length, right - left + 1)

    return max_length


def is_anagram(s, t):
    """Problema: comprobar si dos textos son anagramas.

    Solución: incrementar frecuencias con ``s`` y reducirlas con ``t``. La
    comparación es exacta: no elimina espacios ni normaliza mayúsculas. O(n).
    """
    if len(s) != len(t):
        return False
    contador = {}
    for letras in s:
        contador[letras] = contador.get(letras, 0) + 1
    for letras in t:
        contador[letras] = contador.get(letras, 0) - 1
    for letr in contador:
        if contador[letr] != 0:
            return False
    return True

def length_of_longest_substring(s):
    """Problema: medir la mayor subcadena sin repetidos.

    Solución: mantener una ventana válida y desplazar su límite izquierdo hasta
    quitar el carácter repetido. Esta es la segunda definición efectiva. O(n).
    """
    left = 0
    seen = set()
    maximo = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left +=1

        seen.add(s[right])
        maximo = max(maximo, right - left +1)

    return maximo

def binary_search(nums, target):
    """Problema: localizar un valor en una lista ordenada.

    Solución: búsqueda binaria reduciendo el intervalo a la mitad. Esta segunda
    definición reemplaza a la anterior. Retorna índice o -1. O(log n).
    """
    left = 0
    right = len(nums) - 1

    while left <= right:

        obj = (left + right) // 2

        if nums[obj] == target:
            return obj
        elif nums[obj] < target:
            left = obj + 1
        else:
            right = obj - 1
    return -1


def is_valid(s):
    """Problema: validar delimitadores balanceados y anidados.

    Solución: pila de aperturas y mapa de cierres; el resultado final exige que
    no queden aperturas pendientes. Esta es la implementación efectiva. O(n).
    """
    matches = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []

    for par in s:
        if par in matches:
            if not stack:
                return False
            if stack[-1] != matches[par]:
                return False
            stack.pop()
        else:
            stack.append(par)
    return len(stack) == 0


def num_islands(grid):
    """Problema: contar islas formadas por celdas ``'1'`` conectadas.

    Solución: DFS desde cada celda no visitada y marcarla como ``'0'``.
    Atención: modifica ``grid`` y asume una matriz rectangular. Complejidad:
    O(filas * columnas).
    """

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    def dfs(i, j):

        if i < 0 or i >= rows or j < 0 or j >= cols:
            return

        if grid[i][j] == "0":
            return

        grid[i][j] = "0"

        dfs(i+1, j) # abajo
        dfs(i-1, j) # arriba
        dfs(i, j+1) # derecha
        dfs(i, j-1) # izquierda


    islands = 0

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == "1":
                islands += 1
                dfs(i,j)

    return islands



from collections import deque

def can_finish(numCourses, prerequisites):
    """Problema: decidir si todos los cursos pueden completarse.

    Solución: construir el grafo de prerrequisitos y aplicar orden topológico de
    Kahn. Cada pareja debe ser ``[curso, prerrequisito]`` y usar índices válidos.
    Un ciclo impide completar todos los cursos. Complejidad: O(V + E).
    """

    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    queue = deque()

    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    completed = 0

    while queue:

        current = queue.popleft()
        completed += 1

        for neighbor in graph[current]:

            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)


    return completed == numCourses



