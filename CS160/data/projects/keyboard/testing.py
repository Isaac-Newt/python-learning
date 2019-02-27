top_distances_to_q = {"q": 0, "w": 1, "e": 2, "r": 3, "t": 4, "y": 5, "u": 6, "i": 7, "o": 8, "p": 9}
    
mid_distances_to_a = {"a": 0, "s": 1, "d": 2, "f": 3, "g": 4, "h": 5, "j": 6, "k": 7, "l": 8}

low_distances_to_z = {"z": 0, "x": 1, "c": 2, "v": 3, "b": 4, "n": 5, "m": 6}

def find_distance(character_1: str, character_2: str):
    # If they are in the same row --> Simplify this garbage?
    if ((character_1 in top_distances_to_q) and (character_2 in top_distances_to_q)):
        distance = abs(top_distances_to_q[character_1] - top_distances_to_q[character_2])
    if ((character_1 in mid_distances_to_a) and (character_2 in mid_distances_to_a)):
        distance = abs(mid_distances_to_a[character_1] - mid_distances_to_a[character_2])
    if ((character_1 in low_distances_to_z) and (character_2 in low_distances_to_z)):
        distance = abs(low_distances_to_z[character_1] - low_distances_to_z[character_2])

    # If one is in top and one is in mid
    if ((character_1 in top_distances_to_q) and (character_2 in mid_distances_to_a)):
        distance = abs(top_distances_to_q[character_1] - mid_distances_to_a[character_2]) + 1
    if ((character_1 in mid_distances_to_a) and (character_2 in top_distances_to_q)):
        distance = abs(mid_distances_to_a[character_1] - top_distances_to_q[character_2]) + 1

    # If one is in top and one is in low
    if ((character_1 in top_distances_to_q) and (character_2 in low_distances_to_z)):
        distance = abs(top_distances_to_q[character_1] - low_distances_to_z[character_2]) + 2
    if ((character_1 in low_distances_to_z) and (character_2 in top_distances_to_q)):
        distance = abs(low_distances_to_z[character_1] - top_distances_to_q[character_2]) + 2

    # If one is in mid and one is in low
    if ((character_1 in mid_distances_to_a) and (character_2 in low_distances_to_z)):
        distance = abs(mid_distances_to_a[character_1] - low_distances_to_z[character_2]) + 1
    if ((character_1 in low_distances_to_z) and (character_2 in mid_distances_to_a)):
        distance = abs(low_distances_to_z[character_1] - mid_distances_to_a[character_2]) + 1

    return distance 

a_to_a = find_distance("a", "a")

s_to_q = find_distance("s", "q")
q_to_s = find_distance("q", "s")

j_to_q = find_distance("j", "q")
q_to_j = find_distance("q", "j")

m_to_g = find_distance("m", "g")
g_to_m = find_distance("g", "m")

print("same row --> 0")
print(a_to_a) # expect 0

print("top mid --> 2")
print(s_to_q) # expect 2
print(q_to_s) # expect 2

print("top low --> 7")
print(j_to_q) # expect 7
print(q_to_j) # expect 7

print("mid low --> 3")
print(m_to_g) # expect 3
print(g_to_m) # expect 3

print()
print(find_distance("m", "h")) # expect 2

p_to_z = find_distance("p", "z")
q_to_z = find_distance("m", "u")
print()
print(p_to_z) # expect 11
print(q_to_z) # expect 2