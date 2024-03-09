#myname : youssef mohamed mohmed ezzat
#id : 20200688
from hmac import new
import random
import numpy as np

def chromosome(number, length):
    chromosomes = []
    for i in range(number):
        chromosomes.append("")
        for j in range(length):
            x = random.randint(0, 1)
            chromosomes[i] += str(x)
    return chromosomes

def evaluate_fitness(chromosomes):
    fitness_scores = []
    target_chromosome = '11111'
    for chromosome in chromosomes:
        fitness = chromosome.count('1') 
        fitness_scores.append(fitness)
    return fitness_scores



def probability(fitness):
    total_fitness = sum(fitness)
    probabilities = [float(fitness[i]) / total_fitness for i in range(len(fitness))]
    return probabilities

def cumulative(probabilities):
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    return cumulative_probabilities

def select_based_on_cumulative_probabilities(chromosomes, cumulative_probabilities):
    r = random.random()
    for i in range(len(cumulative_probabilities)):
        if r <= cumulative_probabilities[i]:
            return chromosomes[i]
def select_byrouttle2(chromosomes, cumulative_probabilities):
    r = random.random()
    print(r)
    for i in range(len(cumulative_probabilities)):
        if r <= cumulative_probabilities[i]:
            return chromosomes[i]

def crossover(parent1, parent2, pCross, crossover_point):
    if random.random() < pCross:
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    else:
        offspring1 = parent1
        offspring2 = parent2
    return offspring1, offspring2

def mutation(chromosome, pMut):
    mutated_chromosome = ""
    for bit in chromosome:
        if random.random() < pMut:
            mutated_bit = '0' if bit == '1' else '1'
            mutated_chromosome += mutated_bit
        else:
            mutated_chromosome += bit
    return mutated_chromosome
def eltism(chromosome,fitness):
    el =[]
    temp=fitness.copy()
    i =temp.index(max(temp))
    el.append(chromosome[i])
    del(temp[i])
    j=temp.index(max(temp))
    el.append(chromosome[j])
    return el

def genetic_algorithm(runs, generations, ch_length, pcross, pmut):
    best_fitness_history = []
    avr_fitness_history = []
    
    for j in range(runs):
        chromosomes = chromosome(20, ch_length)
        best_fitness = []
        avr_fitness = []
        
        for i in range(generations):
            fitnesses = evaluate_fitness(chromosomes)
            best_fitness.append(max(fitnesses))
            avr_fitness.append(sum(fitnesses) / len(fitnesses))
            probabilities = probability(fitnesses)
            cummulative_prob = cumulative(probabilities)
            new_population = []
            
            while len(new_population) < len(chromosomes):
                selection = []
                selection.append(select_based_on_cumulative_probabilities(chromosomes, cummulative_prob))
                selection.append(select_based_on_cumulative_probabilities(chromosomes, cummulative_prob))
                offspring = crossover(selection[0], selection[1], pcross, int(ch_length/2))
                new_population.append(mutation(offspring[0], pmut))
                new_population.append(mutation(offspring[1], pmut))
            
            new_population = new_population[0:18]
            best = eltism(chromosomes, fitnesses)
            new_population.extend(best)
            chromosomes = new_population.copy()
            
     
      
        print(" final generation ",chromosomes, "\n")
      
        
       
        print("Best fitness history:\n", best_fitness, "\n")
        print("Average fitness history:\n", avr_fitness, "\n")
        print("\n")
       # if i == generations - 1:
             # print("Final population:\n", chromosomes, "\n")
        
        


 
        

# Input parameters
# switch case for gentic with selection , gentic with etlisim , test code 
while True:        
 print ("\t \t \t<< welcome to my application>> \n\n")    
 print ("select 1 for test all part of code :")
 print ("selcet 2 for run gentic algorthm without eltisim :")
 print ("select 3 for run gentic algorithm with eltisim:")
 print("select 4 for stop :\n\n")
 x=int(input("enter your choice : \n"))
 if x==1:
     num_of_chromose=int(input("enter number of your chromose : "))
     length=int(input("enter your length of each chromsome "))
     chromose=chromosome(num_of_chromose, length)
     print("all chromose are generated :",chromose)
     fitness =evaluate_fitness(chromose) 
     print(" fitnsess of each fitness : " ,evaluate_fitness(chromose)  )
     probality =probability(fitness)
     print (" all probablity of each chromose : ",probability(fitness))
     print ( "all cummulative of each chromose : ",cumulative( probality))
     cumulative =cumulative( probality)
     selection=[]
     for i in range(2):
       selection.append(select_byrouttle2(chromose,cumulative))

       print ("  parent ",i+1 ," for making mutation and cross over ",selection[i])
     eltisim=eltism(chromose,fitness)
     print(" you can found the best indivdual : ",eltisim)
     print (" now we can make cross over and mutation ")
     crosspoint=int(input(" enter cross over point :"))
     pcross=float(input("enter pcross")) 
     offspring_2=crossover(eltisim[0],eltisim[1],pcross,crosspoint)
     print("two childern from the best indivdula : ",offspring_2)
     offspring = crossover(selection[0], selection[1], pcross, crosspoint)
     print(" two childern from selection routlle : ",offspring)
     pMut=float(input("enter your Pmut "))
     print (" muattion of childern 1 from  best indivdula (etlism) : ",mutation(offspring_2[0], pMut))
     print("mutation of childern 2 from best indivdula (etlism) : ", mutation(offspring_2[1],pMut))
     print (" muattion of childern 1 from selection routtle : ",mutation(offspring[0], pMut))
     print("mutation of childern 2 from selection routtle  : ", mutation(offspring[1],pMut))
   

 
 if x==2 :
     runs = int(input("Enter number of runs: "))
     generation=int(input("enter number of your generation : "))
     ch_length = int(input("Enter length of chromosome: "))
     pCross = float(input("Enter pCross: "))
     pMut = float(input("Enter pMut: "))

# Run the genetic algorithm
     genetic_algorithm(runs, generation, ch_length, pCross, pMut)

    
     
            

  
     
