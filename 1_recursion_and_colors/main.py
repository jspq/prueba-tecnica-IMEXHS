from recursion_colors import solve_hanoi_with_colors

def main():
    try:
        n = int(input("Enter the number of disks (1 - 8): "))
        if not (1 <= n <= 8):
            print("Invalid number of disks. It must be between 1 and 8.")
            return

        disks = []
        for _ in range(n):
            input_data = input("Enter the size and color for example '2 blue': ").split()
            if len(input_data) != 2:
                print("Invalid input format. Please use: <size> <color>")
                return
            size, color = input_data
            disks.append((int(size), color))

        if sorted(disks, key=lambda x: x[0], reverse=True) != disks:
            print("Disks must be sorted in descending order of size.")
            return

        result = solve_hanoi_with_colors(n, disks)
        if result == -1:
            print("-1  # Impossible to complete the transfer")
        else:
            for move in result:
                print(move)

    except ValueError as ve:
        print(f"Invalid input: {ve}")


if __name__ == "__main__":
    main()