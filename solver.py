import sudoku

from collections import deque
import numpy as np

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0

def get_actions_in(state):
    actions = []
    temp = np.argwhere(state == 0)
    #print(temp)

    for point in temp:
        for val in values:
            actions.append([*point, val])

    return actions

def get_actions(state):
    actions = []
    for r in range(len(state)):
        for c in range(len(state[r])):
            if state[r][c] == 0:
                for val in values:
                    actions.append([r, c, val])
    return actions

def depth_first_search(initial_state):
    if sudoku.is_goal(initial_state): return initial_state

    frontier = deque()
    frontier.append(initial_state)
    frontier_hashed = deque()
    frontier_hashed.append(hash(bytes(initial_state)))
    print(len(frontier_hashed))
    explored = deque()

    while True:
        if len(frontier_hashed) == 0:
            return None

        state = frontier.pop()
        frontier_hashed.pop()
        explored.append(hash(bytes(state)))

        actions = get_actions(state)

        for action in actions:
            child = sudoku.move(state, *action)
            child_hash = hash(bytes(child))

            if child_hash not in frontier_hashed and child_hash not in explored:
                if sudoku.is_goal(child):
                    return child
                frontier.append(child)
                frontier_hashed.append(child_hash)

def constrained_dfs(initial_state):
    if sudoku.is_goal(initial_state): return initial_state

    frontier = deque()
    frontier.append(initial_state)
    frontier_hashed = deque()
    frontier_hashed.append(hash(bytes(initial_state)))
    explored = deque()

    while True:
        if len(frontier_hashed) == 0:
            return None

        state = frontier.pop()
        frontier_hashed.pop()
        explored.append(hash(bytes(state)))

        actions = get_actions(state)

        for action in actions:
            child = sudoku.move(state, *action)
            child_hash = hash(bytes(child))
            if not sudoku.is_legal(child):
                explored.append(child_hash)
                continue

            #sudoku.display(child)
            #print()

            if child_hash not in frontier_hashed and child_hash not in explored:
                if sudoku.is_goal(child):
                    return child
                frontier.append(child)
                frontier_hashed.append(child_hash)

