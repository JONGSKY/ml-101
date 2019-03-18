def vector_size_check(*vector_variables):
    result = len(set([len(vector) for vector in vector_variables])) == 1
    return result


def vector_addition(*vector_variables):
    result = [sum(vector) for vector in zip(*vector_variables)]
    return result



def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    else:
        result = [2*vector[0]-sum(vector) for vector in zip(*vector_variables)]
    return result


def scalar_vector_product(alpha, vector_variable):
    result = [alpha*vector for vector in vector_variable]
    return result


def matrix_size_check(*matrix_variables):
    result = len(set([len(a) for a in (matrix_variables)]))==1 and len(set([len(matrix[0]) for matrix in matrix_variables]))==1
    return result


def is_matrix_equal(*matrix_variables):
    result = all([ all([len(set(k))==1 for k in zip(*i)]) for i in zip(*matrix_variables)])
    return result


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    else:
        result = [[sum(row) for row in zip(*t)] for t in zip(*matrix_variables)]
    return result


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    else:
        result = [[2*k[0]-sum(k) for k in zip(*i)]for i in zip(*matrix_variables)]
    return result


def matrix_transpose(matrix_variable):
    result = [[k for k in i] for i in zip(*matrix_variable)]
    return result


def scalar_matrix_product(alpha, matrix_variable):
    result = [[ alpha*k for k in i]for i in matrix_variable]
    return result


def is_product_availability_matrix(matrix_a, matrix_b):
    result = len(matrix_a[0])==len(matrix_b)
    return result


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return None
