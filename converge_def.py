from matplotlib import pyplot as plt

def discrimination(x_lim_list):
    x_new_lim_list = []
    for x_lim in x_lim_list:
        if abs(x_lim - 1) < abs(x_lim + 1):
            x_new_lim_list.append(1)
        else:
            x_new_lim_list.append(-1)
    return x_new_lim_list

def True_or_False(exact_list, predicted_list):
    correct = 0
    for exact, predicted in zip(exact_list, predicted_list):
        if exact == predicted:
            correct += 1
    return correct / len(exact_list)

def converge_plot(NN_name, name, x_start_list, x2_start_list, x_lim_list):
    plt.figure()
    plus_1_x = []
    plus_1_x2 = []
    minus_1_x = []
    minus_1_x2 = []
    for x_start, x2_start, x_lim in zip(x_start_list, x2_start_list, x_lim_list):
        if x_lim == 1:
            plus_1_x.append(x_start)
            plus_1_x2.append(x2_start)
            #plt.scatter(x_start, x2_start, color="cyan", label="1")
        else:
            minus_1_x.append(x_start)
            minus_1_x2.append(x2_start)
            #plt.scatter(x_start, x2_start, color="orange", label="-1")
    plt.scatter(plus_1_x, plus_1_x2, color="cyan", label="1")
    plt.scatter(minus_1_x, minus_1_x2, color="orange", label="-1")
    #plt.title("x1" + "_trajectory")
    plt.xlabel('x1')
    plt.ylabel("d(x1)/dt")
    #plt.legend()
    plt.tight_layout()
    plt.savefig(NN_name + "2_img/" + "converge_" + NN_name + "_" + name + ".png")
    plt.savefig(NN_name + "2_img/" + "converge_" + NN_name + "_" + name + ".eps")

#print(13626 / 62412 * 23895)
#print(62412 / 23895)
#print(15331 / 6054)