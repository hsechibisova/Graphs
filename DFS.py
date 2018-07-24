# Поиск в глубину
'''Функция создания нового графа пользователем
   Входные параметры: graph-список вершин'''
def new_graph(graph):
    print('Введите количество вершин графа')
    n = int(input()) #количество вершин
    for i in range(n):
        print('Введите количество ребер', i+1,'вершины')
        r = int(input()) #количество ребер вершины
        print('Введите ребра')
        graph += [[int(input()) for j in range(r)]]
    return graph
'''Функция проверяет и отмечает посещенность вершин
   Входные параметры: v-вершина'''
def dfs(v):
    ok[v] = True #помечаем вершину как пройденную
    for unit in graph[v]:
        print(graph[v])
        if not ok[unit]: #если вершина не посещена
            dfs(unit)

graph=[]
new_graph(graph)
print(graph)
ok = [False for i in range(len(graph))]  #список пройденных вершин

for c in range(len(graph )): #проход по всем вершинам
    if not ok[c]: #если вершина не посещена
        dfs(c)
print(ok) #всe значения True - проверены все проходы по всем вершинам
