import random

def GeneticAlgorithm(population, generations=5, mutation_prob=0.2):
    def Gen(population,mutation_prob):
        d = {}
        tot = 0
        for individual in population:
            fitness = sum(int(gene) for gene in individual)
            tot += fitness
            d[tuple(individual)] = fitness

        for key in d:
            d[key] /= tot  


        keys = list(d.keys())
        probs = [d[k] for k in keys]
        chosen1 = random.choices(keys, weights=probs, k=1)[0]

        d2 = {key: val for key, val in d.items() if key != chosen1}
        sum_d2 = sum(d2.values())
        for key in d2:
            d2[key] /= sum_d2

        keys2 = list(d2.keys())
        probs2 = [d2[k] for k in keys2]
        chosen2 = random.choices(keys2, weights=probs2, k=1)[0]

        kid=[]
        for i in range (len(chosen1)):
            if random.randint(1,2)==1:
                kid.append(chosen1[i])

            else:
                kid.append(chosen2[i])
        mutation_prob/=len(kid)
        for i in range(len(kid)):
            if random.random() < mutation_prob:
                if kid[i]==0:
                    kid[i]=1
                else:
                    kid[i]=0


        return kid
    
    for i in range(generations):
        population.append(Gen(population,mutation_prob))

    return population


# Example usage:
population = [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0,1,0,0]]
print(GeneticAlgorithm(population, 100, 0.3))
