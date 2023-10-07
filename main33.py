import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # np array
    train_set = np.array([1, 2, 3])
    test_set=np.array([[0, 1, 2], [1, 2, 3]])

    # we want Res_set 🡪 [[1, 2, 3], [0, 1, 2], [1, 2, 3]]
    res = np.vstack([train_set, test_set])
    print(res)
