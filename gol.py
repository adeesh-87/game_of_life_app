import numpy as numpy
import matplotlib.pyplot as plotter
import matplotlib.animation as animator

n_row = 40
n_col = 40

field_fig = plotter.figure()
field_padded = numpy.zeros((n_row+2, n_col+2))
starter = numpy.random.randint(2, size=[n_row, n_col])


def field_update(num):
   global n_row
   global n_col
   global field_padded
   num_alive = 0
   for x in range(1, n_row+1):
      for y in range(1, n_col+1):
            num_alive =   field_padded[x-1, y-1] \
                        + field_padded[x-1, y  ] \
                        + field_padded[x-1, y+1] \
                        + field_padded[x  , y-1] \
                        + field_padded[x  , y+1] \
                        + field_padded[x+1, y-1] \
                        + field_padded[x+1, y  ] \
                        + field_padded[x+1, y+1]
            if (num_alive < 2) or (num_alive > 3):
               field_padded[x,y] = 0
            if (num_alive == 3) and (field_padded[x,y] == 0):
               field_padded[x,y] = 1
   field = field_padded[1:-1,1:-1]
   image.set_data(field)
   return image
   



for i in range(1,n_row+1):
   field_padded[i, 1:-1] = starter[(i-1), :]

field = field_padded[1:-1,1:-1]
image = plotter.imshow(field)


game = animator.FuncAnimation(field_fig, field_update, 600, fargs=(), \
                                 interval=500, blit=False)
#print(field_update(1, field_padded, image))                                 

game.save('g1.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
plotter.show()