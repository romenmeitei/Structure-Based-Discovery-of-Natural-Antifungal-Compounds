from modeller import *

env = Environ()

aln = Alignment(env)

mdl = Model(
    env,
    file='template'
)

aln.append_model(
    mdl,
    align_codes='template',
    atom_files='template.pdb'
)

aln.append(
    file='target.fasta'
)

aln.salign()

aln.write(
    file='alignment.ali',
    alignment_format='PIR'
)

aln.write(
    file='alignment.pap',
    alignment_format='PAP'
)

print("Alignment completed")