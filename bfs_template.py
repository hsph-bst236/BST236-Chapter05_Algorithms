from collections import deque

def bfs_template(start_state, is_goal_state: callable, get_next_states: callable, compute_result: callable):
    # Initialize queue
    result = []
    queue = deque([(start_state, result)]) 
    # Initialize visited set
    visited = []
    while queue:
        # Get the current state
        current_state, current_result = queue.popleft() 

        # Check if current state is the goal
        if is_goal_state(current_state):
            return current_result

        # Explore next possible states
        for next_state in get_next_states(current_state):
            if next_state in visited:
                continue
            visited.append(next_state)
            # Compute new result based on current result and next state
            next_result = compute_result(current_result, next_state)
            queue.append((next_state, next_result))

    return None # No goal state found