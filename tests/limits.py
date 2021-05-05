import numpy as np
import numpy.random as npr

p_d_plus = 10 / 1000
p_d_minus = 1 - p_d_plus
p_t_plus_given_d_plus = 9 / 10
p_t_minus_given_d_plus = 1 - p_t_plus_given_d_plus
p_t_plus_given_d_minus = 89 / 990
p_t_minus_given_d_minus = 1 - p_t_plus_given_d_minus

n_repeats = 100000
n_iters = 10000
results = np.zeros(n_repeats)
for r in range(n_repeats):
    diseases= npr.choice([True, False],
                         p=[p_d_plus, p_d_minus],
                         size=n_iters)
    n_disease = np.count_nonzero(diseases)
    tests = np.zeros(n_iters, dtype=bool)
    tests[diseases] = npr.choice([True, False],
                                p=[p_t_plus_given_d_plus,
                                   p_t_minus_given_d_plus],
                                size=n_disease)
    tests[~diseases] = npr.choice([True, False],
                                  p=[p_t_plus_given_d_minus,
                                     p_t_minus_given_d_minus],
                                  size=n_iters - n_disease)
    pos_diseases = diseases[tests]
    results[r] = np.count_nonzero(pos_diseases) / len(pos_diseases)

print(min(results), max(results))
