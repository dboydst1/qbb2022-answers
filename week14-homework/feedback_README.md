This is all really great Darren! Just a few very minor comments:
1. When you're calculating the sizes of the different bins/assembly, you probably want to remove the new line characters before counting the number of characters. You can do this really easily by piping the output of your `grep` command to `tr -d '\n'`, which will delete any new line charcters. (no points deducted)
2. For step 3, you probably want to check more than just the first contig in each bin. How could you systematically (i.e. with code) check the taxonomy of all contigs in a single bin? (-0.25)

Otherwise, this is a really excellent effort.

(9.75/10)
