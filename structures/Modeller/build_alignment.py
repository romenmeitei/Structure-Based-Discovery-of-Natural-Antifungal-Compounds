from modeller import *

env = Environ()

aln = Alignment(env)

mdl = Model(env, file='template_clean')

aln.append_model(
    mdl,
    align_codes='template_clean',
    atom_files='template_clean.pdb'
)

aln.append(
    file='target.ali'
)

aln.align2d()

aln.write(
    file='alignment.ali',
    alignment_format='PIR'
)

aln.write(
    file='alignment.pap',
    alignment_format='PAP'
)

print("Alignment done")