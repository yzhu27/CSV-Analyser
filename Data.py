import math

from Cols import Cols, push
from Row import Row
from read_csv import Csv, csv

def rnd(x,places):
    mult = pow(10,(places or 2))
    return math.floor(x * mult +0.5)/mult

class Data:
    def add(self,xs):
        if self.cols == None:
            value_list = list(xs.values())
            self.cols = Cols(value_list)
        else:
            row = Row(xs)
            row = push(self.rows,row)
            # need to be fixed
            for _, todo in enumerate([self.cols.x,self.cols.y]):
                print(type(todo))
                for _, col in enumerate(todo):
                    col.add(row.cells[col.at])

    #  not sure where to find the 'row' parameter.
    def __init__(self, src):
        self.cols = None
        self.rows = {}
        if type(src)==type('string'):
            csv(src,lambda row:self.add(row))
        else:
            for _,row in enumerate(src or {}):
                self.add(row)


    def stats(self,places,showCols, fun):
        showCols , fun = showCols or self.cols.y, fun or "mid"
        t = {};
        for _, col in enumerate(showCols):
            v = fun(col)
            v = type(v) == type(0) and rnd(v,places) or v
            t[col.name] = v
        return  t

if __name__ == '__main__':
    data = Data(r"C:\Users\Pinxiang Wang\Documents\PythonFileTransfer.csv")
    print(data.csv_obj.titles)
    print(data.cols.x)
    print(data.cols.y)