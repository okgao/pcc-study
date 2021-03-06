from dieMB import Die
import matplotlib.pyplot as plt
import pygal

# create a D6
die_1 = Die(6)
# die_2 = Die(6)

# roll die some times, and store the result in a list
results = []
for roll_number in range(1000):
    #result = die_1.roll() + die_2.roll()
    result = die_1.roll()
    results.append(result)

# analize the resultes
frequencies = []
#max_result = die_1.number_sides * die_2.number_sides
raw_result = {}
my_range = list(set(sorted(results)))
for value in my_range:
    frequencey = results.count(value)
    frequencies.append(frequencey)

    """
    print the raw results to reference
    """
    raw_result[value] = frequencey
print(raw_result)

# visualize the result
hist = pygal.Bar()

hist.title = "Results of rolling 2 D6 1000 times."
hist.x_labels = [i for i in my_range]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')



#plt.scatter(my_range, frequencies, s=15)
plt.plot(my_range, frequencies)
plt.show()