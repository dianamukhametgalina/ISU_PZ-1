# ISU_PZ-1
Алгоритм BFS
Обозначения:
++ - начальная точка
|| - стены
\\## - точки, по которым обязательно нужно пройти
оо – пройденные точки алгоритмом
Вывод:
Формируется матрица смежности, затем из нее создаем список смежности:
 ![image](https://user-images.githubusercontent.com/71024367/198890237-c2dcb25f-43af-46cf-a46b-c2a787381bca.png)
Список, в котором случайном образом формируются координаты особых точек: Path(oo), Start(++), End(--), Blocks(||), Goals(##):
 ![image](https://user-images.githubusercontent.com/71024367/198890245-25052524-1b11-43a1-b1b6-372e7e94661a.png)
Производим поиск в ширину и получаем результат в виде пути, пройденного агентом.
 ![image](https://user-images.githubusercontent.com/71024367/198890257-a4d42c34-186a-4ed6-a223-fccada6e7e41.png)
![image](https://user-images.githubusercontent.com/71024367/198890266-be716a4c-eacf-4a4e-8130-9f09a0aa901c.png)
![image](https://user-images.githubusercontent.com/71024367/198890274-0470b0e2-dab3-4c1d-8bc6-12b5bb37c975.png)
