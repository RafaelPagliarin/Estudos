import time

class MatrixFibonacci:
    Q = [[1, 1],
         [1, 0]]

    def __init__(self):
        self.__memo = {}


    @staticmethod
    def __multiply_matrices(m1, m2):
        """Matrices miltiplication (the matrices are expected in the form of a list of 2x2 size)."""

        a11 = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
        a12 = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
        a21 = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
        a22 = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
        r = [[a11, a12], [a21, a22]]
        return r

    def __get_matrix_power(self, m, p):
        """Matrix exponentiation (it is expected that p that is equal to the power of 2)."""

        if p == 1:
            return m
        if p in self.__memo:
            return self.__memo[p]
        k = self.__get_matrix_power(m, int(p / 2))
        r = self.__multiply_matrices(k, k)
        self.__memo[p] = r
        return r

    def get_number(self, n):
        """Getting the nth Fibonacci number (a non-negative integer number is expected as n)."""
        if n == 0:
            return 0
        if n == 1:
            return 1
        # Factoring down the passed power into the powers that are equal to the power of 2),
        # i.e. 62 = 2^5 + 2^4 + 2^3 + 2^2 + 2^0 = 32 + 16 + 8 + 4 + 1.
        powers = [int(pow(2, b)) for (b, d) in enumerate(reversed(bin(n-1)[2:])) if d == '1']
        # The same, but less pythonic: http://pastebin.com/h8cKDkHX

        matrices = [self.__get_matrix_power(MatrixFibonacci.Q, p) for p in powers]
        while len(matrices) > 1:
            m1 = matrices.pop()
            m2 = matrices.pop()
            r = self.__multiply_matrices(m1, m2)
            matrices.append(r)
        return matrices[0][0][0]


st = time.time()
mfib = MatrixFibonacci()
fibn = mfib.get_number(100000)
et = time.time()
elapsed_time = (et - st) * 1000

print('Execution time:', elapsed_time, 'miliseconds')