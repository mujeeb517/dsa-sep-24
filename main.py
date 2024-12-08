from arrays.PrefixSum import PrefixSum


def main():
    ds = PrefixSum([10, 1, 8, 2, 3, 5, 6])
    
    print(ds.query(1, 4))
    print(ds.query(2, 4))
    print(ds.query(0, 4))


if __name__ == '__main__':
    main()
