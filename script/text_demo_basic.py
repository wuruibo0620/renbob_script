# class Feibo:
#     def __init__(self,num):
#         self.pre = 0
#         self.curr = 1
#         self.num = num
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count < self.num:
#             self.count += 1
#             temp = self.curr
#             self.curr = self.curr + self.pre
#             self.pre = temp
#             return temp
#         else:
#             raise StopIteration
#
# myfeibo = Feibo(5)
# for i in myfeibo:
#     print(i)
#

s = 'abcd'
l = {val:i*4 for val,i in zip(s,[[1],[2],[3],[4]])}
list = {val:[index+1]*4 for index,val in enumerate(s)}
print(list)

dick = enumerate(s)
print()
