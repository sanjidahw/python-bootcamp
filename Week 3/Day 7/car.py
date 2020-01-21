from classes import wheel, engine, body
#from classes import *

tire = wheel(18)
print(tire.size)

camry_eng = engine(180, 4) #180 horsepower and 4 cylinders
print(camry_eng.horsepower)
print(f"My car's engine has {camry_eng.n_cylinders} cylinders.") 
#call the attribute from classes.py by typing {camry_eng.____}

camry_body = body("silver")
print(camry_body.trunk_size)
