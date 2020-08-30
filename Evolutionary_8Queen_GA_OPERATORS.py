import random,copy

class CHROMOSOME:
    def __init__(self,length=8):
        self.genes=[None]*length
        for i in range(length):
            self.genes[i]=random.randint(1,8)
        self.EVALUATE()

    def EVALUATE(self):
        self.fitness = 0
        rows = 8
        cols = 8
        board = [[0]*cols]*rows
        for i in range(len(self.genes)):
            queen = self.genes[i]
            if board[queen-1][queen-1] == 0:
                board[queen-1][queen-1] = queen
            else:
                self.fitness+=1

class SELECTION:
    def binary_tournament(pop,return_pop,T_size):
        new_population=[]
        for i in range(return_pop):
            Tour_teams=[]
            for j in range(T_size):
                Tour_teams.append(random.choice(pop))
            new_population.append(min(Tour_teams,key=lambda item:item.fitness))
        return(new_population)

class OPERATOR:
    def one_point_crossover(parent1,parent2):

        print('parent fitness',parent1.fitness,parent2.fitness)
        child1=copy.deepcopy(parent1)
        child2=copy.deepcopy(parent2)

        crossover_point=random.randint(0,len(parent2.genes))
        print('crossover point', crossover_point)
        child1.genes[crossover_point:]=parent2.genes[crossover_point:]
        child2.genes[crossover_point:]=parent1.genes[crossover_point:]
        print('The children are :',child1.genes,child2.genes)
        child1.EVALUATE()
        child2.EVALUATE()
        print('child fitness', child1.fitness, child2.fitness)

        return child1,child2

    def two_point_crossover(parent1, parent2):
        print('parent fitness', parent1.fitness, parent2.fitness)
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        crossover_point1 = random.randint(0, len(parent2.genes))
        crossover_point2 = random.randint(0, len(parent2.genes))
        if (crossover_point1 >crossover_point2):
            crossover_point1,crossover_point2=crossover_point2,crossover_point1
        print('crossover point:', crossover_point1,crossover_point2)

        child1.genes[crossover_point1:crossover_point2] = parent2.genes[crossover_point1:crossover_point2]
        child2.genes[crossover_point1:crossover_point2] = parent1.genes[crossover_point1:crossover_point2]
        print('The children are :', child1.genes, child2.genes)
        child1.EVALUATE()
        child2.EVALUATE()
        print('parent fitness', child1.fitness, child2.fitness)

        return child1, child2

    def flip_mutation(ind):
        index=random.randint(0,len(ind.genes)-1)
        print('index is:',index)
        print('before',ind.genes)
        ind.genes[index]=random.randint(1,8)
        print('after', ind.genes)
        ind.EVALUATE()
        return ind