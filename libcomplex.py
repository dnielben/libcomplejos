# Mi primera libería

def cplxsum(a, b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return (real, imag)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(cplxsum((3,5),(-2.4,6.8))) # (3 + 5i)+(-2.4 + 6.8i) = (0.6 + 11.8i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
