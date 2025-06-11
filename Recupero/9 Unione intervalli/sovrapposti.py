'''
Unione di Intervalli Sovrapposti
Data una lista di intervalli chiusi rappresentati come liste di due elementi [start, end],
scrivi una funzione merge_intervals(intervals) che restituisce una nuova lista di
intervalli in cui tutti quelli sovrapposti sono stati fusi. Ogni intervallo soddisfa start <=
end. La lista risultante deve essere ordinata per inizio intervallo e non devono esserci
sovrapposizioni.

                Requisiti:

● Input: una lista di liste, ad esempio [[1, 4], [2, 6], [8, 10], [15, 18]].
● Se due intervalli si sovrappongono o si toccano (es. [1,4] e [4,5]), unirli in
[1,5].

● Restituisci una lista di intervalli fusi, ordinata per il valore di inizio.
● Casi limite:
    ○ Se l’input è vuoto, restituisci una lista vuota.
    ○ Se è presente un solo intervallo, restituiscilo così com’è.

Esempi:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals) # restituisce [[1, 6], [8, 10], [15,
18]]
intervals = [[1, 4], [4, 5]]
merge_intervals(intervals) # restituisce [[1, 5]]
'''

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    pass

if __name__ == "__main__":
    
    intervals = [[1, 4], [4, 5]]                        # restituisce [[1, 5]]
    intervals2 = [[1, 3], [2, 6], [8, 10], [10, 18]]    # restituisce [[1, 6], [8, 10], [15,18]]
    print(merge_intervals(intervals))
    print(merge_intervals(intervals2))

# #-----------------------------------------------------------------------------------------------------------------

#     ordered_intervals: list[list[int]] = []
#     last_interval: list[list[int]] = []
#     iter: int = 0

#     for numbers in intervals:
#         last_interval.append(numbers)
        

#         print(numbers)
#         if iter > 1:
#             ordered_intervals.append(numbers) if numbers[0] >= ordered_intervals[0][1] else print("banana")

#         if not ordered_intervals:
#             ordered_intervals.append(numbers)
#         if numbers[0] == last_interval[0][1]:
#             ordered_intervals[0][1] = numbers[1]
#             print("banana")

#         iter += 1
# #-----------------------------------------------------------------------------------------------------------------

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # #------------------------------------------
        # ordered_intervals.append(numbers)
        # if numbers[0] == ordered_intervals[0][1]:
        #     ordered_intervals[0][1] = numbers[1]
        #     ordered_intervals.pop()
        # if numbers[0] <= ordered_intervals[0][1]:
        #     ordered_intervals[0][1] = numbers[1]
        # #------------------------------------------