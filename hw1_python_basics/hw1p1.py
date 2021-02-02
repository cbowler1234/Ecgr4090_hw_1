#!/usr/bin/env python
from person import person
import numpy as np
import matplotlib.pyplot as plt

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))

new_list = [len(name) for name in list_of_names]
print(new_list)
name_dict={}

for x in range(0,len(list_of_names)):
	new_person=person(list_of_names[x],list_of_ages[x],list_of_heights_cm[x])
	name_dict[list_of_names[x]]=new_person
print(name_dict)
ages_array=np.array(list_of_ages)
heights_array=np.array(list_of_heights_cm)
average_age=np.mean(ages_array)
print(f"The average age is {average_age}")
plt.scatter(ages_array, heights_array)
plt.suptitle('Ages vs Heights')
plt.xlabel('Age')
plt.ylabel('Height in cm')
plt.grid()
plt.show()
plt.savefig("AvH.png")

  

