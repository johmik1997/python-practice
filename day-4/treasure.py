print("welcome to treasury co.")
row1=['__','__','__']
row2=['__','__','__']
row3=['__','__','__']
map=[row1,row2,row3]
print(f'{row1}\n {row2}\n{row3}')
position=input("where do you want to go")
horizontal=int(position[0])
vertical=int(position[1])
map[vertical-1][horizontal-1]='x'
print(f'{row1}\n {row2}\n{row3}')
