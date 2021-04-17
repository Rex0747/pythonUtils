import keyboard


txt = ''
v = ''
mtx = []
while v != '028187':
    events = keyboard.record('enter')
    txt = keyboard.get_typed_strings(events)
    # play these events
    #keyboard.play(events)
    v = list(txt)[0]
    v = v.replace('+','*')
    mtx.append(v)
    
print(str(mtx))
    #print(txt)