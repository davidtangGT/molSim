import os
import subprocess
from datetime import datetime
start = datetime.now()
#subprocess.call(["python",'main.py','-slab_gen',
#                 '-cif_path', 'Unitcells/gold.cif','-duplication_vector','[4,2,2]'])
# subprocess.call(["python",'ptcotest.py','-slab_gen','-cif_path','data/gold.cif',
#                  '-slab_size','15,15,5','-align_dist','1.89','-duplication_vector','2,2,2'])
#subprocess.call(["python",'ptcotest.py','-slab_gen','-cif_path','data/gold.cif',
#                 '-align_dist','1.89','-duplication_vector','[2,2,2]','-slab_size','[15,15,5]',
#                 '-align_distance_method','custom','miller_index','[1,1,1]','-align_method'])


#subprocess.call(["python",'main.py','-slab_gen','-cif_path','Unitcells/gold.cif',
#                 '-align_dist','2.7','-slab_size','[15,15,5]','-align_distance_method',
#                 'custom','-miller_index','[1,1,1]','-align_method','alignpair',
#                 '-place_on_slab','-target_molecule','/home/jp/Runs/copo.xyz','-surface_atom_type','Au',
#                 '-object_align','Co','-control_angle','40','-angle_control_partner','2',
#                 '-angle_surface_axis','[1,1]'])

#subprocess.call(["python",'main.py','-slab_gen','-cif_path','Unitcells/gold.cif',
#                 '-slab_size','[15,15,5]','-align_distance_method',
#                 'chemisorption','-miller_index','[1,1,1]','-align_method','alignpair',
#                 '-place_on_slab','-target_molecule','/home/jp/Runs/copo.xyz','-surface_atom_type','Au',
#                 '-object_align','Co','-control_angle','40','-angle_control_partner','2',
#                 '-angle_surface_axis','[1,1]'])

#subprocess.call(["python",'main.py','-slab_gen','-cif_path','Unitcells/gold.cif',
#                 '-slab_size','[15,15,5]',
#                 '-miller_index','[1,1,1]'])
#subprocess.call(["python",'main.py','-slab_gen','-cif_path','Unitcells/gold.cif',
#                 '-duplication_vector','[3,3,2]','-miller_index','[1,1,1]'])
#subprocess.call(["python",'main.py','-slab_gen','-cif_path','Unitcells/gold.cif',
#                 '-align_dist','1.89','-slab_size','[15,15,5]','-align_distance_method',
#                 'custom','-align_method','alignpair',
#                 '-place_on_slab','-target_molecule','/home/jp/Runs/copo.xyz','-surface_atom_type','Au',
 #                '-object_align','Co','-control_angle','90','-angle_control_partner','2',
  #               '-angle_surface_axis','[1,1]'])
#subprocess.call(["python",'main.py','-slab_gen','-cif_path','Unitcells/anatase_tio2.cif',
#                 '-slab_size','[12,12,8]','-miller_index','[1,1,0]','-place_on_slab','-target_molecule','/home/jp/Runs/mo5.xyz',
#                 '-align_method','alignpair','-surface_atom_type','Ti','-num_surface_atoms','4',
#                 '-object_align','2,3,4,5','-align_dist','2.5'])
#subprocess.call(["python",'main.py','-slab_gen','-cif_path','Unitcells/anatase_tio2.cif',
#                 '-slab_size','[12,12,8]','-place_on_slab','-miller_index','[1,0,1]','-target_molecule','/home/jp/Runs/mo5.xyz',
#                 '-align_method','alignpair','-surface_atom_type','Ti','-num_surface_atoms','4',
#                 '-object_align','2,3,4,5','-align_dist','2.5'])
#subprocess.call(["python",'main.py','-slab_gen','-cif_path','Unitcells/anatase_tio2.cif',
#                 '-slab_size','[12,12,8]','-miller_index','[1,0,1]','-target_molecule','/home/jp/Runs/mo5.xyz',
#                 '-align_method','alignpair','-surface_atom_type','Ti','-num_surface_atoms','4',
#                 '-object_align','2,3,4,5','-align_dist','2.5'])
#
#subprocess.call(["python",'-m','molSimplify.__main__','-slab_gen','-cif_path','Unitcells/anatase_tio2.cif',
#                 '-slab_size','[9,9,9]','-place_on_slab','-target_molecule','/home/jp/Runs/co.xyz',
#                 '-align_method','alignpair','-surface_atom_type','Ti','-num_surface_atoms','1',
#                 '-object_alignvim','C','-align_dist','2.5'])
#
#subprocess.call(["python",'molSimplify/main.py','-slab_gen','-cif_path','molSimplify/Unitcells/anatase_tio2.cif',
#                 '-slab_size','[9,9,9]','-miller_index','[1,0,0]','-freeze','1'])



#
#mol_name = "sally"
#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'6',"-lig","acac,water","-ligocc",'2,2',
#                 '-geometry','oct','-distort','0','checkdirb','True','-ligalign','False','-calccharge','yes',
#                 '-keepHs','False','-bcharge','0','-rundir','/home/jp/Runs/mpc/\n','-jobdir temp',
#                 '-oxstate','II','-spin','1','-mopac','-name',mol_name+'\n','-qccode TeraChem'])
#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'4',"-lig","diaminomethyl","-ligocc",'2',

#'-geometry','sqp','-distort','0','checkdirb','True','-ligalign','False','-calccharge','yes',
#                 '-keepHs','False','-bcharge','0','-rundir','/home/jp/Runs/\n','-jobdir consti','-debug True',
#                 '-oxstate','II','-spin','5','-name',mol_name+'\n','-qccode TeraChem'])
#mol_name = "frank"
#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'6',"-lig","n1c(noc1N)c1ncccc1","-ligocc",'3','-smicat','8,1',
#                '-geometry','oct','-distort','0','checkdirb','True','-ligalign','False','-calccharge','yes',
#                 '-keepHs','Auto','-bcharge','0','-rundir','/home/jp/Runs/\n',
#                '-oxstate','II','-spin','5'])
print('**********************************************')
subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'6',"-lig","water","-ligocc",'6','-keepHs','yes',
               '-geometry','oct','/home/jp/Runs/','-oxstate','II','-spin','5'])
 
#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'4',"-lig","water","-ligocc",'4','-keepHs','yes',
#                '/home/jp/Runs/','-oxstate','II','-spin','1'])

#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'6',"-lig","c12c(c(cc3c1nccc3)Cl)cccn2","-ligocc",'3','-keepHs','yes','-debug',
#                '-geometry','oct','-rundir','/home/jp/Runs/\n','-oxstate','II','-spin','1','-smicat',"7,15",'-name','long','-MLbonds','2.4'])
                
#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'6',"-lig","water","-ligocc",'6',
#                '-geometry','oct','-distort','0','checkdirb','True','-ligalign','False','-calccharge','yes',
#                 '-keepHs','False','-bcharge','0','-rundir','/home/jp/Runs/',
#                 '-oxstate','III','-spin','6','-qccode TeraChem'])
 #                   subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'6',"-lig","smitest.smi","-ligocc",'3',
#                    '-geometry','oct','-distort','0','checkdirb','True','-ligalign','False','-calccharge','yes',
 #                    '-keepHs','Auto','-bcharge','0','-rundir',this_path,
 #                   '-oxstate','II','-spin','1'])

#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'6',"-lig","acac,water","-ligocc",'2 2',
#                '-geometry','oct','-debug','-ligloc','yes',
#                 '-keepHs','Yes','-rundir','/home/jp/Runs/rootdir','-jobdir fancyfolder',
#                 '-oxstate','II','-spin','1','-name','fancymol'])
                 
                 
#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'6',"-lig","tbutylcyclen, furan","-ligocc",'1 2',
#                 '-geometry','oct','-calccharge','yes',
#                '-keepHs','False','-oxstate','II','-spin','1 5'])

#subprocess.call(["python","molSimplify/main.py","-dbcatoms","1 3","-dbbase","chembl_22_1","-dbresults","100",'-rundir','/home/jp/Runs/rootdir\n','-dboutput', "list.smi","-dbsmarts","[O-]C(=O)"])
if False:
    base_call =["python","molSimplify/main.py","-core","Fe","-coord",'6', '-geometry','oct','-ligalign','False','-calccharge','yes',
                '-keepHs','Auto','-qccode','TeraChem','-jsched','SGE','-method','UDFT']
    list_of_runs = ['bidentate1','bidentate2','monodentate']
    list_of_smis = {'bidentate1':'screenresults.smi','bidentate2':'dissimres.smi','monodentate':"mono.smi"}
    spin_dictionary = {'Fe':{'II':[1,5],'III':[2,6]}}
    for ANN_tags in ['ANN','Database']:
        for runs in list_of_runs:
            this_lig_tag = list_of_smis[runs]
            if runs == 'monodentate':
                this_occ = 6;
            else:
                this_occ = 3;
            for ox in ['II','III']:
                for spin in spin_dictionary['Fe'][ox]:
                    this_path = '/home/jp/Runs/'+ANN_tags+'/'+runs + '/'+'ox'+ ox + '_spin' + str(spin)
                    if not os.path.exists(this_path):
                        os.makedirs(this_path)
                    this_call = list(base_call)
                    this_call += ['-lig',this_lig_tag,'-ligocc',str(this_occ),'-spin',str(spin),'-oxstate',ox,'-rundir',this_path]
                    if ANN_tags == 'Database':
                        this_call += ['-skipANN']
                    subprocess.call(this_call)
#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'6',"-lig","smitest.smi","-ligocc",'3',
#                '-geometry','oct','-distort','0','checkdirb','True','-ligalign','False','-calccharge','yes',
#                 '-keepHs','Auto','-bcharge','0','-rundir','/home/jp/Runs/ICER/ANN/o2s1',
#                '-oxstate','II','-spin','1'])
#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'6',"-lig","smitest.smi","-ligocc",'3',
#                '-geometry','oct','-distort','0','checkdirb','True','-ligalign','False','-calccharge','yes',
#                 '-keepHs','Auto','-bcharge','0','-rundir','/home/jp/Runs/ICER/ANN/o2s5',
#                '-oxstate','II','-spin','5'])

#subprocess.call(["python","molSimplify/main.py","-core","Fe","-coord",'4',"-lig","cyclam, water","-ligocc",'1',
#                 '-geometry','sqp','-distort','0','checkdirb','True','-ligalign','False','-calccharge','yes',
#                 '-keepHs','False','-bcharge','0','-rundir','/home/jp/Runs/\n','-jobdir consti','-debug True',
#                 '-oxstate','II','-spin','5','-name',mol_name+'\n','-qccode TeraChem'])


print(datetime.now() - start)
