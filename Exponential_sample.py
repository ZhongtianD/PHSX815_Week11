from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt


def main(lamb: float, Nsample: int, Nexperiment:int ):
    Samples = np.random.exponential(scale=1/lamb, size=(Nexperiment,Nsample) )
    Mean = np.mean(Samples,axis=1)
    
    count, bins, ignored = plt.hist(Mean, 50, density=True)
    plt.title(str(Nexperiment)+' experiments of '+str(Nsample)+' samples')
    plt.show()
    plt.savefig('Exponential_mean.png')
    
    


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument("-L", "--lamb", type=float, default=2.0,
                        help="lambda parameter of exponential distribution")

    parser.add_argument("-Ns", "--Nsample", type=int, default=10,
                        help="Number of samples for each experiment.")
    
    parser.add_argument("-Ne", "--Nexperiment", type=int, default=1000,
                        help="Number of experiment.")


    main(**parser.parse_args().__dict__)
   
