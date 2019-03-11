print("Let's practice everthing.")
print('you\'d need to know \'bout escapes with \\ that do : ')
print('\n newlinse and \t tabs . ')

poem = """
\t the lovely word
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion form intuition
and requires an explanation
\n\twhere there is none
"""

print("-------------------")
print(poem)
print("-------------------")


five = 10 - 2 + 3 - 6
print(f"this should be five : {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a srting
print("With a starting point of : {}" .format(start_point))
# .format 格式: print("something in there :{}".format(something))
# 而不是       print("something in there :{}",format(something))
# 中间不能有 ","
# it's just like with an f"" string


start_point = start_point / 10

print("We can also do that this way:")

formula = secret_formula(start_point)
# this is an easy way to applu a list to a format string
print("We'd have {} beans , {} , jars, and {} crates.".format(*formula))
