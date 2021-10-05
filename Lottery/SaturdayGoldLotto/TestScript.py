import numpy as np
import pandas as pd
from tqdm import tqdm
Condition=True

repeting_number = np.random.randint(1,46,6)
repeting_number_1 = np.random.randint(1,46,6)
repeting_number_01 = np.random.randint(1,46,6)
repeting_number_3 = np.random.randint(1,46,6)
repeting_number_8 = np.random.randint(1,46,6)
repeting_number_10 = np.random.randint(1,46,6)
repeting_number_x10 = np.random.randint(1,46,6)
combined_number=np.random.randint(1,46,6)
subtracted_number=np.random.randint(1,46,6)



num1=[1, 3, 4, 2, 5, 6, 7, 8, 9, 11]
num2=[10, 11, 9, 12, 13, 6, 8, 5, 7, 19]
num3=[18, 16, 20, 13, 15, 22, 24, 21, 14, 17]
num4=[29, 26, 24, 27, 32, 30, 33, 22, 25, 23]
num5=[39, 38, 37, 32, 40, 31, 42, 36, 41, 34]
num6=[45, 43, 44, 42, 41, 40, 38, 39, 34, 37]

avoid_sequence=[25,44,10,37,21,29,35,34,18,31,41,28,6,27,30,13]


def random_sequence_generator():

    sequence = []
    final_sequence = []
    unique_sequence = []



    
    for count in tqdm(range(100000)):

        number_sequence = np.random.randint(1,46,6)

        if Condition:

            if sum(number_sequence) <= 170 and sum(number_sequence) >= 100:

                if np.count_nonzero(number_sequence % 2 == 0) == 2 or np.count_nonzero(number_sequence % 2 == 0) == 3 or np.count_nonzero(number_sequence % 2 == 0) == 4:

                    number_sequence=sorted(number_sequence)
                    
                    if number_sequence[0] in num1 and number_sequence[1] in num2 and number_sequence[2] in num3 and number_sequence[3] in num4 and number_sequence[4] in num5 and number_sequence[5] in num6:

                        if not set(number_sequence).intersection(avoid_sequence):


                            sequence.append(number_sequence)
                        
                        else:
                            pass

                    else:
                        pass

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

        if len(unique_sequence) == 6:
            final_sequence.append(unique_sequence)


    return final_sequence



##############################################################################################################################################################################


Lottery_Lots=random_sequence_generator()
sequence_pool=pd.DataFrame(Lottery_Lots,columns=[['Number-1','Number-2','Number-3','Number-4','Number-5','Number-6']])
sequence_pool['Sum']=sequence_pool.sum(axis=1)

print(f'Generated Sequence Dimension : {sequence_pool.shape}')

unique=sequence_pool.drop_duplicates()
print(f'Unique Sequence Dimension : {unique.shape}')
unique.to_csv('Sequence.csv') 

print('\n')
print('------------')
print('Compilation Completed!')