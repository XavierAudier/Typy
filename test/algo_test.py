from algo import algo

my_algo = algo.TrainingAlgorithm()
my_algo.build_from_textfile("text\\plain_english.txt")

print(my_algo.get_next_example())
