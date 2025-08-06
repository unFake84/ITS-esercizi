'''
School Grading System:

    Create a function that takes a student's name and
    their scores in different subjects as input.
    The function calculates the average score and prints the student's name,
    average, and a message indicating whether
    the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores,
    calling the function for each student.

'''

def student( name:str, score:list[ int ] ) -> None:

    average: int = sum( score ) / len( score )
    print( f"The student { name } passed an average grade of { average if average%1 != 0 else int( average ) }" \
          if average >= 60 else\
            f"The student { name } did not pass because his/her average grade '{ average if average%1 != 0 else int( average ) }' is lower than 60." )

if __name__ == "__main__":

    students: list[ tuple[ str, list[ int ] ] ] = [

        ( "Maio", [ 40, 60, 80, 57, 70 ] ),
        ( "Pino", [ 98, 17, 20, 26, 8 ] ),
        ( "Panu", [ 30, 31, 9, 100, 25 ] ),
        ( "Paio", [ 64, 60, 53, 75, 54 ] )

    ]

    for person in students:
        student( person[ 0 ], person[ 1 ] )