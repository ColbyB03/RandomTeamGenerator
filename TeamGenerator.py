import names
import tkinter
import texttable
import random
import math

from texttable import Texttable
from random import randint

t = Texttable()

for x in range(25):

        name = names.get_full_name(gender='male')

        passing = randint(1,100)

        rushing = randint(1,100)

        speed = randint(1,100)
        
        catching = randint(1,100)
        
        blocking = randint(1,100)
        
        jumping = randint(1,100)
        
        kicking = randint(1,100)

        overall = (passing + rushing + speed + catching + blocking + jumping + kicking)/7

        overall = int(round(overall))
        
        t.add_rows([['Name', 'Overall', 'Passing', 'Rushing', 'Speed', 'Catching','Blocking','Jumping','Kicking'], [name, overall, passing, rushing, speed, catching, blocking, jumping, kicking]])
           
print (t.draw())
