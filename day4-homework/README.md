 # qbb2022 Day 4 homework
 
 #Exercise a
 
 # numpy.around(numpy.arrange(0.55, 1.05, 0.05), decimals=2)[::-1] is making an array of 0.55, 0.60, 0.65, ... 1.00. decimals = 2 ensures that each float only has 2 decimals. the ::-1 reverses the order of the array. 0.55 serves as the start point, 1.05 is the excluded end point, and 0.05 is the separation between the numbers.
 
 #Exercise b
 
 probabilities = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
 tosses = numpy.array([10, 50, 100, 250, 500, 1000])

 new_twodim_arr = numpy.zeros((len(probabilities), len(tosses)))
 for i, prob in enumerate(probabilities):
     for j,toss in enumerate(tosses):
         power = run_experiment(prob, toss)
         new_twodim_arr[i,j] = power
 print(new_twodim_arr)

 new_twodim_arr1 = numpy.zeros((len(probabilities), len(tosses)))
 for i, prob in enumerate(probabilities):
     for j,toss in enumerate(tosses):
         power = run_experiment(prob, toss, correct_the_pvalues = True)
         new_twodim_arr1[i,j] = power
 print(new_twodim_arr1)
 
 #Exercise C
 
 fig, ax = plt.subplots()
 color = sns.color_palette("viridis", as_cmap = True)
 ax = sns.heatmap(new_twodim_arr, vmin = 0, vmax = 1, xticklabels = tosses, yticklabels = probabilities, cmap = color)
 plt.xlabel("Number of Tosses")
 plt.ylabel("Probability of Heads")
 plt.title("Coin Flip Simulations")
 plt.savefig("PowerHeatmapUncorrected.png")
 plt.show()

 fig, ax = plt.subplots()
 color = sns.color_palette("viridis", as_cmap = True)
 ax = sns.heatmap(new_twodim_arr1, vmin = 0, vmax = 1, xticklabels = tosses, yticklabels = probabilities, cmap = color)
 plt.xlabel("Number of Tosses")
 plt.ylabel("Probability of Heads")
 plt.title("Coin Flip Simulations")
 plt.savefig("PowerHeatmapCorrected.png")
 plt.show()
 
 #The more tosses there are, the more power the simulation has. The closer to 0.5 the probability is, the less power it has.
 
 #Exercise D
 
 #This relates to the preprint in that it is trying to determine if there is a bias in certain genes based on sperm survivability; so one gene may have a .60 chance and another may have .40. The issue with proving this is that families are generally small, so sample sizes of ~5 are difficult for determining how powerful the effect is/if the effect is real. This function addresses the probability and the power issue.
 
 