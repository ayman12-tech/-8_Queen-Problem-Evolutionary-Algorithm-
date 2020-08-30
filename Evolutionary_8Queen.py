import Evolutionary_8Queen_GA_OPERATORS,random
pop=[_ for _ in range(8)]

#random solution generations
for i in range(len(pop)):
    pop[i]=Evolutionary_8Queen_GA_OPERATORS.CHROMOSOME(8)
    print(pop[i].genes,pop[i].fitness)

print('******************************************************************************')

for g in range(0,50): #generation loop
    children=[]
    print('Starting a new generation')
    for i in range(0,len(pop),2):
        parents=Evolutionary_8Queen_GA_OPERATORS.SELECTION.binary_tournament(pop,2,2) #10 individual mn se 2 ko utha rh hun

        for ind in parents:
            print(ind.genes,ind.fitness)
        off1,off2=Evolutionary_8Queen_GA_OPERATORS.OPERATOR.one_point_crossover(parents[0],parents[1])


        if random.random()<0.2:
            print('MUTATING')
            off1=Evolutionary_8Queen_GA_OPERATORS.OPERATOR.flip_mutation(off1)
            print('After mutation fitness of offspring1:',off1.fitness)

        if random.random()<0.2:
            print('MUTATING')
            off2=Evolutionary_8Queen_GA_OPERATORS.OPERATOR.flip_mutation(off2)
            print('After mutation fitness of offspring1:',off2.fitness)
        children.append(off1)
        children.append(off2)
    print('******************************************************************************')
    pop=Evolutionary_8Queen_GA_OPERATORS.SELECTION.binary_tournament(pop+children,len(pop),10) #survival selection

print('best solution found so far',sorted(pop,key=lambda x:x.fitness,reverse=False)[0].fitness, 'Board is:', sorted(pop,key=lambda x:x.fitness,reverse=False)[0].genes)