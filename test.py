import sys
import itertools

import numpy as np

from subroutineVQE import solve_VQE
from subroutineGUI import retrive_VQE_options
from subroutineJSON import retrive_json_options, write_json
from subroutineMAIN import iterator_item_to_string, from_item_iter_to_option

if __name__ == '__main__':
    options = retrive_VQE_options(sys.argv)

    iteratore = list(itertools.product(options['molecule']['basis'],
                                       options['varforms'],
                                       options['quantum_instance'],
                                       options['optimizer'],
                                       options['lagrange']['active'],
                                       options['lagrange']['operators'],
                                       options['series']['itermax'],
                                       options['series']['step'],
                                       options['series']['lamb']
                                       )
                     )

    results = {}
    names = []
    newiteratore = []

    for idx, item in enumerate(iteratore):
        name = iteratorItemToString(item)
        if name not in names:
            names.append(name)
            results[name] = []
            newiteratore.append(item)
    iteratore = newiteratore

    for i, geometry in enumerate(options['geometries']):
        options['molecule']['geometry'] = geometry
        print("D = ", np.round(options['dists'][i], 2))
        for item in iteratore:
            name = iteratorItemToString(item)
            option = fromItemIterToOption(options, item)

            result_tot = solve_VQE(option)
            results[name].append(result_tot)

            energy = result_tot.total_energies[0]
            print("\t", name, "\tE = ", energy)

    JsonOptions = retriveJSONOptions(__file__,
                                     options,
                                     results)

    writeJson(JsonOptions)
