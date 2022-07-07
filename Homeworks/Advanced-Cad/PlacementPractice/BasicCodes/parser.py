## CSDL, POSTECH, Korea Summer Internship 2022
## Original file created by Minjae Kim
## kmj0824@postech.ac.kr

if __name__ == '__main__':
    from dataStructures import *
else:
    from BasicCodes.dataStructures import *

def parsing(filename: str):
    # parse the txt file
    file = open(filename)
    file_lines = file.readlines()
    file.close()

    file_info = []
    for line in file_lines:
        line = line.strip()
        line = line.split()
        for i in range(len(line)):
            line[i] = float(line[i])

        file_info.append(line)
    del line, file_lines, file

    # parse the info of cells and nets
    ## get cell # and net #
    cell_number = int(file_info[0][0])
    net_number = int(file_info[0][1])
    cell_list = []
    file_info.pop(0)

    ## get cell data
    for i in range(cell_number):
        cell_info = file_info.pop(0)
        theCell = Cell(cell_info[0], cell_info[1])
        for j in range(theCell.degree):
            theCell.connected_nets.append(int(cell_info.pop(2)) - 1)
        cell_list.append(theCell)

    del cell_info, i, j, theCell

    ## get pads data
    pad_number = int(file_info.pop(0)[0])
    pad_list = []
    for i in range(pad_number):
        pad_info = file_info.pop(0)
        thePad = Pad(pad_info[0], pad_info[1], pad_info[2], pad_info[3])
        pad_list.append(thePad)
    del i, thePad, pad_info, file_info

    ## make the net data
    ### make the net list
    net_list = []
    for i in range(net_number):
        net_list.append(Net(i))
    ### enter the cell list data to the net list
    for i in range(cell_number):
        theCell = cell_list[i]
        for j in range(theCell.degree):
            net_list[theCell.connected_nets[j]].connected_cells.append(theCell.id)
    del theCell, i, j
    ### enter the pad list data to the net list
    for i in range(pad_number):
        thePad = pad_list[i]
        net_list[thePad.connected_net].connected_pad.append(thePad.pad_id)
    del thePad, i

    return net_list, cell_list, pad_list


if __name__ == '__main__':
    net_list, cell_list, pad_list = parsing("../benchmarks/toy1")
    print("parsing test")
