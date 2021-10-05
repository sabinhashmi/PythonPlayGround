import numpy as np
import pandas as pd
import time


def random_sequence_generator():

    sequence = []
    final_sequence = []
    unique_sequence = []

    repeting_number = np.array([1, 8, 14, 17, 19, 21, 26])
    repeting_number_1 = np.array([2, 9, 15, 18, 20, 22, 27])
    repeting_number_01 = np.array([35, 7, 13, 16, 18, 20, 25])
    repeting_number_3 = np.array([4, 11, 17, 20, 22, 24, 29])
    repeting_number_8 = np.array([9, 17, 22, 25, 27, 29, 34])
    repeting_number_10 = np.array([11, 18, 24, 27, 29, 31, 1])
    repeting_number_x10 = np.array([26, 33, 4, 7, 9, 11, 16])
    combined_number=np.array([1,3,5,8,9,10,12,15,18,20,22,25,27,29,31,33,34,35])
    subtracted_number=np.array([2,3,4,5,6,7,9,11,12,13,16,18,20,25])



    for count in range(1000):

        number_sequence = np.random.randint(1,36,7)
        number_sequence_04 = number_sequence+4

        if set(repeting_number).intersection(number_sequence) and set(repeting_number_1).intersection(number_sequence) and set(repeting_number_01).intersection(number_sequence) and set(repeting_number_3).intersection(number_sequence) and set(repeting_number_8).intersection(number_sequence) and set(repeting_number_10).intersection(number_sequence) and set(number_sequence).intersection(number_sequence_04) and set(combined_number).intersection(number_sequence) and set(subtracted_number).intersection(number_sequence) and set(repeting_number_x10).intersection(number_sequence):

            if sum(number_sequence) <= 150 and sum(number_sequence) >= 100:

                if np.count_nonzero(number_sequence % 2 == 0) == 2 or np.count_nonzero(number_sequence % 2 == 0) == 3 or np.count_nonzero(number_sequence % 2 == 0) == 4:

                    sequence.append(number_sequence)

                else:
                    pass

            else:
                pass

        else:
            pass


        for p in sequence:
            unique_sequence=[]
            for q in p:
                if q not in unique_sequence:
                    unique_sequence.append(q)

        if len(unique_sequence) == 7:
            final_sequence.append(unique_sequence)


    return final_sequence



##############################################################################################################################################################################


Lottery_Lots=random_sequence_generator()
sequence_pool=pd.DataFrame(Lottery_Lots,columns=[['Number-1','Number-2','Number-3','Number-4','Number-5','Number-6','Number-7']])
sequence_pool['Sum']=sequence_pool.sum(axis=1)

print(f'Generated Sequence Dimension : {sequence_pool.shape}')

unique=sequence_pool.drop_duplicates()
print(f'Unique Sequence Dimension : {unique.shape}')
unique.to_csv('Sequence.csv')
print('\n')
print('------------')
print('Compilation Completed!')