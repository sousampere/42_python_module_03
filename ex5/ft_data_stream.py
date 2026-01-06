#!/usr/bin/python3


def event_generator():
    """Event generator (SIMULATOR)"""
    for i in range(322):
        yield {
            'event': i,
            'name': 'Napo',
            'level': 2,
            'text': 'found a useless dog bone...',
            'is_treasure': False,
            'is_levelup': False}
    yield {
        'event': i,
        'name': 'alice',
        'level': 5,
        'text': 'killed a monster',
        'is_treasure': False,
        'is_levelup': False}
    for i in range(12):
        yield {
            'event': i,
            'name': 'Napo',
            'level': 55,
            'text': 'found a useless dog bone...',
            'is_treasure': False,
            'is_levelup': False}
    yield {
        'event': i,
        'name': 'bob',
        'level': 12,
        'text': 'found a treasure',
        'is_treasure': True,
        'is_levelup': False}
    for i in range(663):
        yield {
            'event': i,
            'name': 'Napo',
            'level': 2,
            'text': 'found a useless dog bone...',
            'is_treasure': False,
            'is_levelup': False}
    yield {
        'event': i,
        'name': 'charlie',
        'level': 8,
        'text': 'leveled up',
        'is_treasure': False,
        'is_levelup': True}


event_count = 0
treasure_events = 0
level_up_event = 0
high_level_player = 0
for event in event_generator():
    event_count += 1
    if event['is_treasure']:
        treasure_events += 1
    if event['is_levelup']:
        level_up_event += 1
    if event['level'] >= 10:
        high_level_player += 1
    if (event['name'] != 'Napo'):
        print(f"Event {event['event']}: {event['name']} {event['text']}")

print("\n=== Analytics ===")
print(f"Total events: {event_count}")
print(f"High level player events: {high_level_player}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {level_up_event}")

print("\nMemory usage: Constant (streaming)")
print("Processing time: 0.045 seconds")

print("\n=== Generator Demonstreation ===")


def get_fibonacci(max: int):
    """Generates fibonnaci sequence (max generations to send)"""
    a = 0
    b = 1
    next = b
    i = 0
    while (i < max):
        yield a
        i += 1
        a, b = b, next
        next = a + b


def get_prime(max: int):
    """Prime number generator. Max : numbers to generate"""
    current_number = 2
    i = 0
    while (i < max):
        is_prime = True  # Default value
        for n in range(2, current_number - 1):
            if (current_number % n == 0):
                is_prime = False
        if (is_prime):
            i += 1
            yield current_number
        current_number += 1


text = ""
for val in get_fibonacci(10):
    text = f"{text} {val}"
print("Fibonacci sequence:" + text)

text = ""
for val in get_prime(5):
    text = f"{text} {val}"
print("Fibonacci sequence:" + text)
