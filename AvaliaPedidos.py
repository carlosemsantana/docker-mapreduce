from mrjob.job import MRJob

class MRAvaliaPedidos(MRJob):
    def mapper(self, key, line):
        (x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, status_pedido_codigo) = line.split(',')
        yield status_pedido_codigo, 1

    def reducer(self, status_pedido_codigo, occurences):
        yield status_pedido_codigo, sum(occurences)

if __name__ == '__main__':
    MRAvaliaPedidos.run()


