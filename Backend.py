import json
import matplotlib.pyplot as plt
import sys

def generate_graph(json_file_path, graph_type="line", output_path="output.png"):
    """
    Reads JSON data from a file, generates a specified type of graph, and saves it.

    Args:
        json_file_path (str): Path to the JSON data file.
        graph_type (str, optional): Type of graph to generate ('line', 'bar', 'scatter'). Defaults to "line".
        output_path (str, optional): Path to save the generated graph. Defaults to "output.png".
    """
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at '{json_file_path}'")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file_path}'")
        return

    if not data or not isinstance(data, list) or not all(isinstance(item, dict) and "x" in item and "y" in item for item in data):
        print("Error: JSON data should be a list of dictionaries with 'x' and 'y' keys.")
        return

    x_values = [item['x'] for item in data]
    y_values = [item['y'] for item in data]

    plt.figure(figsize=(10, 6))

    if graph_type == "line":
        plt.plot(x_values, y_values, marker='o')
    elif graph_type == "bar":
        plt.bar(x_values, y_values)
    elif graph_type == "scatter":
        plt.scatter(x_values, y_values)
    else:
        print(f"Error: Invalid graph type '{graph_type}'. Supported types are 'line', 'bar', 'scatter'.")
        return

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(f"{graph_type.capitalize()} Graph")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"{graph_type.capitalize()} graph saved to '{output_path}'")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python main.py <path_to_json_file> [graph_type]")
        print("Supported graph types: line (default), bar, scatter")
    else:
        json_file_path = sys.argv[1]
        graph_type = sys.argv[2] if len(sys.argv) == 3 else "line"
        generate_graph(json_file_path, graph_type)
