from collections import deque

graph = {
    'you': ['Bob', 'Claire', 'Alice'],
    'Bob': ['Anuj', 'Peggy'],
    'Claire': ['Thom', 'Jonny'],
    'Alice': ['Peggy'],
    'Anuj': [],
    'Peggy': [],
    'Thom': [],
    'Jonny': []
}


def person_is_seller(person):
    return person[-1:] == 'm'


def breath_first(m_graph):
    search_queue = deque()
    search_queue += m_graph['you']
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                return f'We have a Mango seller -> {person}'
            else:
                search_queue += m_graph[person]
                searched += person

    return False


print(breath_first(graph))

