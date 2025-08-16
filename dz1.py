print("My homework")

text = [1,12,3,123,1,23,12,3,123,12,3,2,2,2,23,12,312,3,123,12,3,123,12,312,312312,3123123,5,5,5,5,5,5,5]


elements_to_remove = [5, 2]

res = []
exp_set = set(elements_to_remove)
for i in text:
    if i in exp_set:
        continue
    res.append(i)

print(res)