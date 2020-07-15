import matplotlib.pyplot as plt
import time
start_time = time.time()

n = 5 #number of iterations

carpet = 'white' #color of the carpet
background = 'black' #background color

plt.rcParams['axes.facecolor'] = background

fig = plt.figure(1,(5,5))
fig.patch.set_facecolor(background)
plt.xlim(-0.05,1.05)
plt.ylim(-0.05,1.05)
plt.tick_params(axis='both',which='both',bottom=False,top=False,labelbottom=False,right=False,left=False,labelleft=False)

square = plt.Rectangle((0,0),1,1,fc=carpet)
plt.gca().add_patch(square)

for m in range(1,n+1):
    for s in range(0,3**(m-1)+3):
        for r in range(0,3**(m-1)+3):
            if (1+3*s)/3**m < 1 and (1+3*r)/3**m < 1:
                void1 = plt.Rectangle(((1+3*s)/3**m,(1+3*r)/3**m),1/3**m,1/3**m,fc=background)
                plt.gca().add_patch(void1)

seconds = time.time()-start_time
print('%.1f seconds'%(seconds))
plt.show()



