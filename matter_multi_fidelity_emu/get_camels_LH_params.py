from typing import List

import numpy as np

def read_IllustrisTNG(
    filename: str,
    param_names: List = [
        "Omega_m",
        "sigma_8",
        "A_SN1",
        "A_AGN1",
        "A_SN2",
        "A_AGN2",
        "seed",
    ],
    parameter_limits: List = [
        (0.1, 0.8),
        (0.6, 1.0),
        (0.25, 4.0),
        (0.5, 2.0),
        (0.25, 4.0),
        (0.5, 2.0),
    ],
):
    """
    Make a dict for the params
    """
    # only read the LH set
    size = 1000
    n_params = 6 # discard the seeds

    params_values = np.full((size, n_params), fill_value=np.nan)

    with open("data/illustris_smfs/CosmoAstroSeed_params.txt", "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "").split(" ")
            # remove empty string
            line = list(filter(lambda l : l != "", line))
            # print(line)

            if "LH" in line[0]:
                re_find = re.findall("LH_([0-9]+)", line[0])
                
                num = int(re_find[0])
                # check again the number and name of this row
                assert line[0] == "LH_{}".format(num)

                # make the numbers to be float
                values = np.array(
                    list(map(lambda l : float(l), line[1:-1]))
                )

                params_values[num, :] = values
