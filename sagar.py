# # class demo:
# #     def config(self):
# #         print("hello")
# # a = 8
# # print(type(a))
# # hello = demo()
# # print(type(hello))



# class com:     
#     def config(self):
#         for i in "hello":
#             print(i)
# com1 = com()
# # com2 = com()

# com.config(com1)
# # com.config(com2)

num = int(input("enter the number: "))
for i in range(2,num):
    if num % i == 0:
        print("not peime number")
        continue
    else:
        print("prime number")