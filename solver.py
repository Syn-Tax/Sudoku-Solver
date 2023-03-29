import sudoku

from collections import deque
import numpy as np
import xxhash

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0


def get_actions_in(state):
    actions = []
    temp = np.argwhere(state == 0)
    # print(temp)

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


def breadth_first_search(initial_state):
    checked = 1
    if sudoku.is_goal(initial_state):
        return initial_state

    frontier = deque()
    frontier.append(initial_state)
    frontier_hashed = deque()
    frontier_hashed.append(xxhash.xxh3_64_intdigest(bytes(initial_state)))
    explored = set()

    while True:
        if len(frontier) == 0:
            return None

        state = frontier.popleft()
        frontier_hashed.popleft()
        explored.add(xxhash.xxh3_64_intdigest(bytes(state)))

        actions = get_actions(state)

        for action in actions:
            child = sudoku.move(state, *action)
            child_hash = xxhash.xxh3_64_intdigest(bytes(child))

            if child_hash not in explored and child_hash not in frontier_hashed:
                checked += 1
                if sudoku.is_goal(child):
                    print(f"Checked {checked} states")
                    return child
                frontier.append(child)
                frontier_hashed.append(xxhash.xxh3_64_intdigest(bytes(child)))


def constrained_bfs(initial_state):
    checked = 1
    if sudoku.is_goal(initial_state):
        return initial_state

    frontier = deque()
    frontier.append(initial_state)
    explored = set()

    while True:
        if len(frontier) == 0:
            return None

        state = frontier.popleft()
        explored.add(xxhash.xxh3_64_intdigest(bytes(state)))

        actions = get_actions(state)

        for action in actions:
            child = sudoku.move(state, *action)
            child_hash = xxhash.xxh3_64_intdigest(bytes(child))
            if not sudoku.is_legal(child):
                explored.add(child_hash)
                continue

            # sudoku.display(child)
            # print()

            if child_hash not in explored:
                checked += 1
                # print(f"Checking state: {checked}")
                if sudoku.is_goal(child):
                    print(f"Checked {checked} states")
                    return child
                frontier.append(child)


def depth_first_search(initial_state):
    checked = 1
    if sudoku.is_goal(initial_state):
        return initial_state

    frontier = deque()
    frontier.append(initial_state)
    explored = set()

    while True:
        if len(frontier) == 0:
            return None

        state = frontier.pop()
        explored.add(xxhash.xxh3_64_intdigest(bytes(state)))

        actions = get_actions(state)

        for action in actions:
            child = sudoku.move(state, *action)
            child_hash = xxhash.xxh3_64_intdigest(bytes(child))

            if child_hash not in explored:
                # print(f"Checking state: {checked}")
                checked += 1
                if sudoku.is_goal(child):
                    print(f"Checked {checked} states")
                    return child
                frontier.append(child)


def constrained_dfs(initial_state):
    checked = 1
    if sudoku.is_goal(initial_state):
        return initial_state

    frontier = deque()
    frontier.append(initial_state)
    explored = set()

    while True:
        if len(frontier) == 0:
            return None

        state = frontier.pop()
        explored.add(xxhash.xxh3_64_intdigest(bytes(state)))

        actions = get_actions(state)

        for action in actions:
            child = sudoku.move(state, *action)
            child_hash = xxhash.xxh3_64_intdigest(bytes(child))
            if not sudoku.is_legal(child):
                explored.add(child_hash)
                continue

            # sudoku.display(child)
            # print()

            if child_hash not in explored:
                # print(f"Checking state: {checked}")
                checked += 1
                if sudoku.is_goal(child):
                    print(f"Checked {checked} states")
                    return child
                frontier.append(child)


def dls(initial_state, limit):
    if sudoku.is_goal(initial_state):
        return initial_state

    if limit == 0:
        return np.array([])

    cutoff = False

    actions = get_actions(initial_state)
    for action in actions:
        child = sudoku.move(initial_state, *action)
        result = dls(child, limit-1)
        if result != np.array([]):
            return result
        if result == np.array([]):
            cutoff = True

    return np.array([])


def iterative_dfs(initial_state):
    depth = 0
    while True:
        result = dls(initial_state, depth)
        if result != np.array([]):
            print(f"FINAL DEPTH: {depth}")
            return result
        depth += 1
