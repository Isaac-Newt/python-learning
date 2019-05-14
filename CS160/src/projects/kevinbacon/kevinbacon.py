#!/usr/bin/env python3
"""Using Breadth first search to find Kevin Bacon's number of actors"""


from pythonds3.graphs import Graph
import sys
import time


def read_file(filename):
    """Build a graph from the file"""
    # Create the graph
    kevinbacon_graph = Graph()

    # Open and read the file
    source = open(filename, "r")
    # Ignore first line
    line = source.readline() # first line
    line = source.readline()

    while line != "":
        # Clean the line
        line = line.strip()
        # Break into portions
        components = line.split("|")
        first_title = components[0]
        title = components[0]
        actor = components[1]

        actors = []
        while title == first_title and line != "":
            # Add the actor to the list
            actors.append(actor)
            # Get the next line
            line = source.readline()
            if line != "":
                line = line.strip()
                components = line.split("|")
                title = components[0]
                actor = components[1]
        # For actors in the list, make connections to other actors
        # If a source/destination doesn't exist, add_edge will add
        # a new vertex, otherwise will use the existing vertex. 
        for actor in actors:
            for other_actor in actors:
                if other_actor != actor:
                    kevinbacon_graph.add_edge(actor, other_actor, title)

    # Return the graph
    return kevinbacon_graph


def find_kevin_bacon_numbers(graph):
    """Find kevin bacon number for all actors (start at Kevin)"""
    graph.bfs(graph.get_vertex("Kevin Bacon"))


def traverse(graph, src, dst):
    """Traverse a graph"""
    path = []
    current = dst
    # Find the actor path
    while current:
        path.append(current)
        current = current.previous
    # Build the path string
    path_strings = []
    for idx in range(1, len(path)):
        string = f"{path[idx - 1].key} acted with {path[idx].key}"
        path_strings.append(string)
    print("\n".join(path_strings))
    # print(" ".join(vertex.key for vertex in (path)))


def main():
    print("---Kevin Bacon number calculator---")
    print("\nReading the file")
    b_graph = read_file("data/projects/kevinbacon/movie_actors_full.txt")
    find_kevin_bacon_numbers(b_graph)
    # Loop to find number and links for any actor entered
    actor = input("What Actor would you like to trace? (exit to quit): ")
    while actor != "exit":
        print(f"The Kevin Bacon number for {actor} is {b_graph.get_vertex(actor).get_distance()}.")

        traverse(b_graph, b_graph.get_vertex("Kevin Bacon"), b_graph.get_vertex(actor))

        actor = input("What Actor would you like to trace? (exit to quit): ")


if __name__ == "__main__":
    main()
