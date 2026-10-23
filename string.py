greeting = 'Hello'
name = 'Michael'

message1 = greeting + ', ' + name + '. Welcome!'
message2 = '{}, {}. Welcome!'.format(greeting, name)
message3 = f'{greeting}, {name}. Welcome!'

print(message1)
print(message2)
print(message3)


print(dir(greeting))
print(help(str))
