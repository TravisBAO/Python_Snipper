import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

# data source
TestRounds = ['1', '2', '3', '4']

# fill in test result data here
One_round_effort_manual_test = 9
One_round_effort_automatic_test = 1
test_script_creation = 15
test_case_count = 150
graph_doc_name = 'AutoRabbit Efficiency - ABT interface - AX100'

graph_title = graph_doc_name + ' (TC:' + str(test_case_count) + ')'

first_M_e = One_round_effort_manual_test * 1
second_M_e = One_round_effort_manual_test * 2
third_M_e = One_round_effort_manual_test * 3
forth_M_e = One_round_effort_manual_test * 4

first_A_e = test_script_creation + One_round_effort_automatic_test * 1
second_A_e = test_script_creation + One_round_effort_automatic_test * 2
third_A_e = test_script_creation + One_round_effort_automatic_test * 3
forth_A_e = test_script_creation + One_round_effort_automatic_test * 4

eff_ratio_1 = 100 * (first_M_e - first_A_e)/first_M_e
eff_ratio_2 = 100 * (second_M_e - second_A_e)/second_M_e
eff_ratio_3 = 100 * (third_M_e - third_A_e)/third_M_e
eff_ratio_4 = 100 * (forth_M_e - forth_A_e)/forth_M_e

ManualTest = [first_M_e, second_M_e, third_M_e, forth_M_e]  # fillin the test effort of manual test
AutomaticTest = [first_A_e, second_A_e, third_A_e, forth_A_e]  # fillin the test effort of automatic test
Efficiency = [eff_ratio_1, eff_ratio_2, eff_ratio_3, eff_ratio_4]  # fillin the efficiency: (manual - automatic)/manual

size = 4

x = np.arange(size)

a = ManualTest
b = AutomaticTest
c = Efficiency


pyplot.xlabel('TestRounds')  # display label on x, y and title
pyplot.ylabel('Test Effort in Days')
pyplot.title(graph_title)

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

first = pyplot.bar(x, a,  width=width, label='ManualTest')
second = pyplot.bar(x + width, b, width=width, label='AutomaticTest')
third = pyplot.bar(x + 2 * width, c, width=width, label='Speedup')

plt.xticks(x + width, TestRounds)  # 显示x坐标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置

for aa, bb in zip(x, ManualTest):  # 显示 sendcount
    pyplot.text(aa - 0.1, bb + 0.1, '%.0f' % bb)
for aa, bb in zip(x, AutomaticTest):  # 显示RPM Response count
    pyplot.text(aa + 0.2, bb + 0.1, '%.2f' % bb)
for aa, bb in zip(x, Efficiency):  # 显示 WP Response count
    # pyplot.text(aa + 0.45, bb + 0.1, '%i' % bb)
    pyplot.text(aa + 0.45, bb + 0.1, '%i' % bb + '%')

pyplot.legend()
# pyplot.show()

pyplot.savefig(graph_doc_name + ".png")

