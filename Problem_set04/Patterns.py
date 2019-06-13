def non_recursive(n):
    k = 2 * n - 2

    for i in range(0, n):

        for j in range(0, k):
            print ' ',

        k = k - 1

        for j in range(0, i + 1):
            print '*', ' ',

        print '\r'


def recursive(n, k):
    if k == 0:
        return;
    for i in range(0, k - 1):
        print ' ',
    for i in range(k - 1, n):
        print '*',
    m = n - k
    for i in range(n, n + m):
        print '*',
    print '\n',
    recursive(n, k - 1)


n = 5
recursive(n, n)
non_recursive(n)
