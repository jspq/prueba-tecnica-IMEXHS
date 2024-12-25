def is_valid_move(source_stack, target_stack):

    if not source_stack:
        return False
    if not target_stack:
        return True

    if source_stack[-1][0] > target_stack[-1][0]:
        return False

    if source_stack[-1][1] == target_stack[-1][1]:
        return False
    return True


def hanoi(n, source, target, auxiliary, rods, moves):

    if n == 0:
        return True

    if not hanoi(n - 1, source, auxiliary, target, rods, moves):
        return False

    if is_valid_move(rods[source], rods[target]):
        disk = rods[source].pop()
        rods[target].append(disk)
        moves.append((disk[0], source, target))
    else:
        return False

    if not hanoi(n - 1, auxiliary, target, source, rods, moves):
        return False

    return True


def solve_hanoi_with_colors(n, disks):

    rods = {"A": disks, "B": [], "C": []}
    moves = []

    if not hanoi(n, "A", "C", "B", rods, moves):
        return -1

    return moves