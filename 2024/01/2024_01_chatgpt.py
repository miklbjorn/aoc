from collections import Counter


def read_input_from_file(filename):
    """
    Reads input from a file and returns two separate lists of integers.
    """
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            # Split the line into two integers
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list


def calculate_total_distance(left_list, right_list):
    """
    Calculates the total distance between two lists.
    """
    # Sort both lists
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list_sorted, right_list_sorted))

    return total_distance


def calculate_similarity_score(left_list, right_list):
    """
    Calculates the similarity score based on the frequency of numbers in the right list.
    """
    # Count the occurrences of each number in the right list
    right_count = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(num * right_count[num] for num in left_list)

    return similarity_score


# Main execution
if __name__ == "__main__":
    # Read input from file
    left_list, right_list = read_input_from_file("input")

    # Calculate the total distance (Part 1)
    total_distance = calculate_total_distance(left_list, right_list)
    print("Total distance:", total_distance)

    # Calculate the similarity score (Part 2)
    similarity_score = calculate_similarity_score(left_list, right_list)
    print("Similarity score:", similarity_score)