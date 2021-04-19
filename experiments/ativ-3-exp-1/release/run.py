import os

n_runs = 50 # number of runs

# Initialize simulation #
os.system("wget https://www.ic.unicamp.br/~edson/disciplinas/mo833/2021-1s/anexos/6LVN.pdb")
os.system("wget https://www.ic.unicamp.br/~edson/disciplinas/mo833/2021-1s/anexos/ions.mdp")
os.system("printf '15' | gmx pdb2gmx -f 6LVN.pdb -o 6LVN_processed.gro -water spce")
os.system("gmx editconf -f 6LVN_processed.gro -o 6LVN_newbox.gro -c -d 1.0 -bt cubic")
os.system("gmx solvate -cp 6LVN_newbox.gro -cs spc216.gro -o 6LVN_solv.gro -p topol.top")
os.system("gmx grompp -f ions.mdp -c 6LVN_solv.gro -p topol.top -o ions.tpr")
os.system("printf '13' | gmx genion -s ions.tpr -o 6LVN_solv_ions.gro -p topol.top -pname NA -nname CL -neutral")
os.system("gmx grompp -f ions.mdp -c 6LVN_solv_ions.gro -p topol.top -o em.tpr")

# Run the experiments #
for i in range(n_runs):
    os.system("gmx mdrun -v -deffnm em")
