import random

# value = random.random()
# value = random.uniform(1, 10)

# greetings = ['Hello', 'Hi', 'Hey', 'Greetings']
# value = random.choice(greetings)

# value = random.randint(1, 6)

# colors = ['red', 'green', 'blue', 'yellow']

# results = random.choices(colors, weights=[18, 18, 2, 2], k=10)

deck = list(range(1, 53))

# random.shuffle(deck)

hand = random.sample(deck, k=5)

print(hand)
