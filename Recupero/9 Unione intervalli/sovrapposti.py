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


    check_intervals: list[list[int]] = []
    for check in intervals:
        if len(check) != 2 \
            or not isinstance(check[0], int) \
            or not isinstance(check[1], int) \
            or check[0] > check[1]:
            continue
        check_intervals.append(check)

    order_intervals: list[list[int]] = sorted(check_intervals)
    final_list: list[int] = []

    for new_interval in order_intervals:

        if final_list == []:
            final_list.append(new_interval)

        elif new_interval[0] <= final_list[-1][1]:
            final_list[-1][1] = max(new_interval[1], final_list[-1][1])

        else:
            final_list.append(new_interval)

    return final_list

if __name__ == "__main__":
    
    intervals = [[3, 1], [4, 5]]                        # restituisce [[1, 5]]
    intervals2 = [[1, 3], [2, 6], [8, 10], [15, 18]]    # restituisce [[1, 6], [8, 10], [15,18]]
    intervals3 = [[15, 18], [2, 6], [18, 10], [1, 3], [10, 18], [15, 18, 10], [1], ["a", 4]]
    print(merge_intervals(intervals))
    print(merge_intervals(intervals2))
    print(merge_intervals(intervals3))

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