import printing_models
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
printing_models.print_models(unprinted_designs, completed_models)
printing_models.show_completed_models(completed_models)

import printing_models as Pm
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
Pm.print_models(unprinted_designs, completed_models)
Pm.show_completed_models(completed_models)



from printing_models import print_models
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)

from printing_models import print_models as Pt
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
Pt(unprinted_designs, completed_models)

from printing_models import *
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)