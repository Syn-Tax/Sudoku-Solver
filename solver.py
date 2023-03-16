import sudoku

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0

def get_actions(state):
    actions = []
    count = 0
    for r in range(len(state)):
        for c in range(len(state[r])):
            if state[r][c] == 0:
                count += 1
                for val in values:
                    actions.append([r, c, val])

    return actions

def depth_first_search(initial_state):
    if sudoku.is_goal(initial_state): return initial_state

    frontier = [initial_state]
    explored = []

    while True:
        if len(frontier) == 0:
            return None

        state = frontier.pop()
        explored.append(state)

        actions = get_actions(state)

        for action in actions:
            child = sudoku.move(state, *action)

            if frontier.count(child) == 0 and explored.count(child) == 0:
                if sudoku.is_goal(child):
                    return child
                frontier.append(child)

def constrained_dfs(initial_state):
    if sudoku.is_goal(initial_state): return initial_state

    frontier = [initial_state]
    explored = []

    while True:
        if len(frontier) == 0:
            return None

        state = frontier.pop()
        explored.append(state)

        actions = get_actions(state)

        for action in actions:
            child = sudoku.move(state, *action)
            if not sudoku.is_legal(child):
                explored.append(child)
                continue

            #sudoku.display(child)
            #print()

            if frontier.count(child) == 0 and explored.count(child) == 0:
                if sudoku.is_goal(child):
                    return child
                frontier.append(child)

