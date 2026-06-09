from modeller import *
from modeller.automodel import *

env = Environ()

a = AutoModel(
    env,
    alnfile='alignment.ali',
    knowns='template_clean',
    sequence='target'
)

a.starting_model = 1
a.ending_model = 5

a.make()