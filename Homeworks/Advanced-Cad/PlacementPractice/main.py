from BasicCodes.parser import parsing
from BasicCodes.visualization import *
import math

def getHPWL(net_list, cell_list, pad_list):
    # Enter your code here to get the HPWL
    return 0


def simulatedAnnealing(net_list, cell_list, pad_list):
    # Enter your code here to do SA
    snap_iter = 0  # iteration number for snapshot
    frozen = False
    Temperature = 0.8

    HPWL_list = []
    HPWL_list.append(getHPWL(net_list, cell_list, pad_list))  # get initial HPWL
    HPWL_min = math.inf

    while(not frozen):
        M = 5  # M is how many swaps per gate. This is hyper parameter
        HPWL_before = getHPWL(net_list, cell_list, pad_list)

        # swap 2 random gates Gi adn Gj

        # compute delta HPWL
        HPWL_after = getHPWL(net_list, cell_list, pad_list)
        HPWL_delta = HPWL_after - HPWL_before

        if HPWL_delta < 0:
            # accept this swap
            pass
        else:
            uniform_random = random.randint(0, 1000) / 10000
            if uniform_random < math.exp(-HPWL_delta/Temperature):
                # accept this swap
                pass
            else:
                # undo this uphill swap
                pass

        # visualization
        if HPWL_after < HPWL_min:
            HPWL_min = HPWL_after
            information = []
            information.append(Temperature)
            information.append(HPWL_after)
            draw_window(pad_list, cell_list, net_list, ver="SA", remark=snap_iter, information=information)
            snap_iter += 1

        # if HPWL still decreasing over teh last few temperatures
            # then T = 0.9 * T
            # else frozen = True

    # Recommend: plot HPWL list using csv file
    return HPWL_list


if __name__ == '__main__':
    filename = "benchmarks/toy1"
    net_list, cell_list, pad_list = parsing(filename)

    draw_window(pad_list, cell_list, net_list, ver="visualization")
    HPWL = getHPWL(net_list, cell_list, pad_list)
    print("Initial HPWL:", HPWL)

    HPWL_list = simulatedAnnealing(net_list, cell_list, pad_list)
    for i in range(len(HPWL_list)):
        print(HPWL_list[i])

