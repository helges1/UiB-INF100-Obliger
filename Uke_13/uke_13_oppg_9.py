import numpy as np
arr = np.arange(42,59)

oddetall=np.where(arr % 2 == 1, 1, 0)

arr[oddetall==1]=1
print(arr)


