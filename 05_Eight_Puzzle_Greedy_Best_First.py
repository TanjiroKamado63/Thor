# Practical 5: Greedy Best-First Search for the Eight Puzzle
import heapq

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
GOAL_POSITIONS = {tile: (i // 3, i % 3) for i, tile in enumerate(GOAL_STATE)}


def get_manhattan_distance(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            current_row, current_col = i // 3, i % 3
            goal_row, goal_col = GOAL_POSITIONS[tile]
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance


def get_neighbors(state):
    neighbors = []
    blank_idx = state.index(0)
    row, col = blank_idx // 3, blank_idx % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_idx], new_state[new_blank_idx] = new_state[new_blank_idx], new_state[blank_idx]
            neighbors.append(tuple(new_state))

    return neighbors


def greedy_best_first_search(start_state):
    open_list = []
    heapq.heappush(open_list, (get_manhattan_distance(start_state), start_state, [start_state]))
    visited = {start_state}

    while open_list:
        _, current_state, path = heapq.heappop(open_list)

        if current_state == GOAL_STATE:
            return path

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                h_value = get_manhattan_distance(neighbor)
                heapq.heappush(open_list, (h_value, neighbor, path + [neighbor]))

    return None


def print_state(state):
    for i in range(0, 9, 3):
        print(list(state[i:i + 3]))
    print()


if __name__ == "__main__":
    initial_configuration = (1, 2, 3, 0, 4, 6, 7, 5, 8)
    print("Initial State:")
    print_state(initial_configuration)

    solution_path = greedy_best_first_search(initial_configuration)
    if solution_path:
        print(f"Solution found in {len(solution_path) - 1} moves!\n")
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            print_state(state)
    else:
        print("No solution could be found.")
