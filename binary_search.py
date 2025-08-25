# Binary Search, buscar un elemento en un arreglo ordenado
def binary_search(arr, target):
    #arr = sorted(arr)
    numMin = 0
    numMax = len(arr) - 1
    
    while numMin <= numMax:
        mid = (numMin + numMax) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            numMin = mid + 1
        else:
            numMax = mid - 1
    return -1

# inputs
print("Letra a buscar: ")
target = input()
arr = ['a', 'b', 'f', 'h', 'c', 'g']

try:
    posicion = arr.index(target)
    print(f'La letra {target} está en la posición: {posicion}')
except ValueError:
    print(f'La letra {target} no está en el arreglo')