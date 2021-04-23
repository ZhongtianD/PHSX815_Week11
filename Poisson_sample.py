from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt


def main(L: float, Ns: int, Ne:int ):
    Samples = np.random.poisson(lam=L, size=(Ne,Ns) )
    Mean = np.mean(Samples,axis=1)
    
    count, bins, ignored = plt.hist(G1, 20, density=True)
    plt.title(str(Ne)+' experiments of '+str(Ns)+' samples')
    plt.show()
    plt.savefig('Poisson_mean.png')
    
    


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument("-L", "--lambda", type=float, default=2.0,
                        help="lambda parameter of poisson distribution")

    parser.add_argument("-Ns", "--Nsample", type=int, default=10,
                        help="Number of samples for each experiment.")
    
    parser.add_argument("-Ne", "--Nexperiment", type=int, default=1000,
                        help="Number of experiment.")


    main(**parser.parse_args().__dict__)
   
