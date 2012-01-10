class Ppm:
    """Represents PPM files as a multidimensional list
    Caveat 1: any line of less than 3 elements is treated as header data.
    Caveat 2: the output is uniformly formatted with 2 spaces, 
    2 or 3 character datapoints offset the visibly in text"""
    def __init__(self, filename=None):
         self.data =[]
         self.headers = []
         self.comments = []
         if filename:
             self.loc = filename
             self.parse_ppm(filename)

    def parse_ppm(self, filename):
        f = open(filename, 'r')
        if f.readline().strip() not in ['P1', 'P2', 'P3']:
            raise NotImplementedError
        f.seek(0)
        for l in f:
            d = l.split()
            # "x"[0][0] = "x", handles comments without space after #
            if d[0][0] == '#':
                self.comments.append(d)
            elif len(d) < 3:
                self.headers.append(d)
            else:
                self.data.append(d)
        f.close()
    
    def write(self, filename=None):
        if filename is None:
            filename = self.loc
        def betterwritelines(f, iterable):
            for x in iterable:
                f.writelines('  '.join(x + ['\n']))
        with open(filename, 'w') as f:
            betterwritelines(f, self.headers)
            betterwritelines(f, self.comments)
            betterwritelines(f, self.data)

if __name__ == '__main__':
    #Demo of my test.
    x = ppm.Ppm("example.ppm")
    x.write(filename="new.ppm")