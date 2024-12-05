# '''
# Part 1
# Name : Polok Poddar
# Id : 21301644
# '''


import random

def random_binary(n):
    return ''.join(random.choice('01') for i in range(n))


def get_chromosomes(num_ch, size):
    return [random_binary(size) for i in range(num_ch)]


def fitness(chromo, step, slots):
    new_lst = [chromo[i * step:(i + 1) * step] for i in range(slots)]
    penalty = overlap(new_lst, step, slots) + const_panalty(new_lst, step, slots)
    return -penalty


def overlap(s_chromo, step, slots):
    return sum(sum(int(bit) for bit in s_chromo[i]) - 1 for i in range(slots) if sum(int(bit) for bit in s_chromo[i]) != 0)


def const_panalty(s_chromo, step, slots):
    return sum(
        sum(int(s_chromo[j][i]) for j in range(slots)) - 1 for i in range(step)
        if sum(int(s_chromo[j][i]) for j in range(slots)) != 0
    )


def select_parent(chrom_lst):
    x = random.randrange(len(chrom_lst))
    y = random.randrange(len(chrom_lst))
    while y == x:
        y = random.randrange(len(chrom_lst))
    return x, y


def crossover(child_lst, ch1, ch2):
    a = random.randint(0, len(ch1) - 1)
    b = random.randint(a, len(ch1))
    ch_1 = ch1[:a] + ch2[a:b] + ch1[b:]
    ch_2 = ch2[:a] + ch1[a:b] + ch2[b:]
    if fitness(ch_1, 3, 3) >= fitness(ch_2, 3, 3):
        child_lst.append(ch_1)
    else:
        child_lst.append(ch_2)


def mutation(child_list):
    count_mutation = random.randint(1, len(child_list))
    for i in range(count_mutation):
        idx = random.randint(0, len(child_list) - 1)
        gene_idx = random.randint(0, len(child_list[idx]) - 1)
        child_list[idx] = (
            child_list[idx][:gene_idx] +
            ('1' if child_list[idx][gene_idx] == '0' else '0') +
            child_list[idx][gene_idx + 1:]
        )
    return child_list


def zero_check(child):
    return sum(int(bit) for bit in child) == 0


def genetic_algorithm(chrom_lst, step, slots):
    child_lst = new_generation(chrom_lst)
    for i in range(1000):
        for child in child_lst:
            if fitness(child, step, slots) == 0 and not zero_check(child):
                print("chromosome : ", child)
                print("Fitness :", 0)
                return
        child_lst = new_generation(child_lst)
    best = max(child_lst, key=lambda chromo: fitness(chromo, step, slots))
    print("Chromosome:", best)
    print("Fitness value:", fitness(best, step, slots))


def new_generation(chrom_lst):
    child_lst = []
    for i in range(10):
        x, y = select_parent(chrom_lst)
        crossover(child_lst, chrom_lst[x], chrom_lst[y])
    return mutation(child_lst)


try:
    with open('E:\\All Search Algorithm\\Genetic.txt', 'r') as file:
        first_line = file.readline().strip().split(" ")
        n, l = int(first_line[0]), int(first_line[1])
        g_list = [file.readline().strip() for i in range(n)]
except FileNotFoundError:
    print("File not found.")
    exit()
except ValueError:
    print("Invalid file.")
    exit()

chrom_lst = get_chromosomes(10, n * l)
genetic_algorithm(chrom_lst, n, l)

###########################################
# Part 2

import random

def cross_over(parent1, parent2):
    if len(parent1) != len(parent2):
        
        raise ValueError("Parents have to be the same size")
    
    a = random.randint(1, len(parent1) - 2)
    b = random.randint(a + 1, len(parent1) - 1)

    ch_1 = parent1[:a] + parent2[a:b] + parent1[b:]

    ch_2 = parent2[:a] + parent1[a:b] + parent2[b:]
    return ch_1, ch_2, a, b

parent1 = "000111000"

parent2 = "111000111"

offspring1, offspring2, prnt_1, prant_2 = cross_over(parent1, parent2)

print("Parent 1: ", parent1)

print("Parent 2: ", parent2)

print(f"1st point: between index {prnt_1} and {prnt_1 + 1}")

print(f"2nd point: between index {prant_2} and {prant_2 + 1}")

# print("Offspring 1: ", offspring1)
# print("Offspring 2: ", offspring2)
#####################################################