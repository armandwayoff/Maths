import turtle

tortue = turtle.Turtle()
DIM, L = 10, -10
courbe = [1]

# "Each iteration can be found by copying the previous iteration, then an R, then a second copy of the previous 
# iteration in reverse order with the L and R letters swapped."
# (https://en.wikipedia.org/wiki/Dragon_curve#cite_note-tabachnikov-1) 
for k in range(DIM):
    courbe += [1] + [int(not e) for e in courbe][::-1]

# initialisation de la position
tortue.right(90)
tortue.forward(L)

for dir in courbe:
    tortue.right(90) if dir == 1 else tortue.left(90)
    tortue.forward(L)
turtle.done()
