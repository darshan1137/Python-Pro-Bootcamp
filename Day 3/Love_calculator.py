print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

me = name1.casefold()
you = name2.casefold()

t_count = 0
t1 = me.count("t")
t2 = you.count("t")
t_count = t1 +t2

r_count = 0
r1 = me.count("r")
r2 = you.count("r")
r_count = r1 +r2

u_count = 0
u1 = me.count("u")
u2 = you.count("u")
u_count = u1 +u2

e_count = 0
e1 = me.count("e")
e2 = you.count("e")
e_count = e1 +e2

true_count = (t_count + r_count + e_count + u_count)*10

l_count = 0
l1 = me.count("l")
l2 = you.count("l")
l_count = l1 +l2

o_count = 0
o1 = me.count("o")
o2 = you.count("o")
o_count = o1 +o2

v_count = 0
v1 = me.count("v")
v2 = you.count("v")
v_count = v1 +v2

love_count = l_count + o_count + v_count + e_count

love = (true_count + love_count)

if love<10 or love>90:
    print(f"Your score is {love}, you go together like coke and mentos")

elif love >40 and love < 50:
    print(f"Your score is {love}, you are alright together")

else:
    print(f"Your Score is {love}")