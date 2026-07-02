# %% This is a workshop placeholder to study data types and structures in
# %%Python.
n = 6
print(type(n))
x = 1 / 2
print(x)
print(type(x))

# %%
s = "Hello world!"
print(s)
print(type(s))
print(int(n * x))

mylist = [x, n, s] * n
print(mylist + [True])

N = len(mylist)
print(f"The length of my list is {N}.")
for i in range(N):
    if isinstance(mylist[i], str):
        print(type(mylist[i]))
    else:
        print("The variable is not a string!")
