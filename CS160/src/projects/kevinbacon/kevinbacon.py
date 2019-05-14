#!/usr/bin/env python3
"""
Isaac List - CS160

Using Breadth first search to find Kevin Bacon's number of actors
"""

import sys
import time
from pythonds3.graphs import Graph


def read_file(filename):
    """Build a graph from the file"""
    # Create the graph
    kevinbacon_graph = Graph()

    # Open and read the file
    source = open(filename, "r")
    # Ignore first line
    line = source.readline()  # first line
    line = source.readline()
    # Clean the line
    line = line.strip()
    # Break into portions
    components = line.split("|")
    title = components[0]
    actor = components[1]

    while line != "":
        first_title = title
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
                    kevinbacon_graph.add_edge(actor, other_actor, first_title)

    # Return the graph
    return kevinbacon_graph


def find_kevin_bacon_numbers(graph):
    """Find kevin bacon number for all actors (start at Kevin)"""
    graph.bfs(graph.get_vertex("Kevin Bacon"))


def traverse(dst):
    """Traverse a graph, find path from dst to Kevin Bacon"""
    path = []
    current = dst
    # Find the actor path
    while current:
        path.append(current)
        current = current.previous
    # Build the path string
    path_strings = []
    for idx in range(1, len(path)):
        string = f"{path[idx - 1].key} acted with {path[idx].key} in {path[idx - 1].get_neighbor(path[idx])}"
        path_strings.append(string)
    print("\n".join(path_strings))


def main():
    """Main Function"""
    # Setup
    print("---Kevin Bacon number calculator---")
    print("\nReading the file")
    b_graph = read_file("data/projects/kevinbacon/movie_actors_full.txt")
    find_kevin_bacon_numbers(b_graph)
    # Loop to find number and links for any actor entered
    actor = input("What Actor would you like to trace? (exit to quit): ")
    while actor != "exit":
        # Print the Kevin Bacon Number
        print(
            f"The Kevin Bacon number for {actor} is {b_graph.get_vertex(actor).get_distance()}."
        )
        print()
        # Print the path from the selected actor to Kevin Bacon
        traverse(b_graph.get_vertex(actor))
        print("- - -")
        # Get a new actor from the user
        actor = input("What Actor would you like to trace? (exit to quit): ")


if __name__ == "__main__":
    main()
