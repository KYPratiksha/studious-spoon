import time

# initial = time.time()
# for i in range (1145):
#     print("pratiksha")
#     # sleeps program for 2 seconds
#     time.sleep(2)
# print("for loop ran in ", time.time()-initial,"seconds")
#
# initial2 = time.time()
# k=0
# while(k<1145):
#     print("pratiksha")
#     k+=1
# print("while ran in ", time.time()-initial2, "seconds")

# gives local time , date
# localtime = time.asctime((time.localtime(time.time())))
# print(localtime)


initial = time.time()
local_time = time.ctime(initial)
print("local time is : ", local_time)