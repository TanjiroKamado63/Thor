# Practical 2: Eight Puzzle using Breadth-First Search
from collections import deque


class EightPuzzleBFS:
    def __init__(self, start_state, goal_state):
        self.start_state = tuple(start_state)
        self.goal_state = tuple(goal_state)
        self.moves = {
            'Up': (-3, 'Up'),
            'Down': (3, 'Down'),
            'Left': (-1, 'Left'),
            'Right': (1, 'Right'),
        }

    def get_neighbors(self, state):
        neighbors = []
        zero_idx = state.index(0)
        row, col = zero_idx // 3, zero_idx % 3

        for move_name, (delta, direction) in self.moves.items():
            new_idx = zero_idx + delta
            if direction == 'Up' and row == 0:
                continue
            if direction == 'Down' and row == 2:
                continue
            if direction == 'Left' and col == 0:
                continue
            if direction == 'Right' and col == 2:
                continue

            state_list = list(state)
            state_list[zero_idx], state_list[new_idx] = state_list[new_idx], state_list[zero_idx]
            neighbors.append((tuple(state_list), move_name))

        return neighbors

    def solve(self):
        if self.start_state == self.goal_state:
            return []

        queue = deque([(self.start_state, [])])
        visited = {self.start_state}

        while queue:
            current_state, path = queue.popleft()
            for next_state, action in self.get_neighbors(current_state):
                if next_state == self.goal_state:
                    return path + [action]
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [action]))

        return None


def print_board(state):
    for i in range(0, 9, 3):
        print(f" {state[i]} {state[i + 1]} {state[i + 2]} ")
    print("-" * 11)


if __name__ == "__main__":
    initial_configuration = (1, 2, 3, 4, 0, 5, 7, 8, 6)
    goal_configuration = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    print("Initial State:")
    print_board(initial_configuration)

    solver = EightPuzzleBFS(initial_configuration, goal_configuration)
    solution = solver.solve()

    if solution is not None:
        print(f"Success! Shortest path found in {len(solution)} moves.")
        print(f"Sequence of moves: {solution}")
    else:
        print("This configuration is unsolvable.")
