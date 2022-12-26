import numpy as np # Using np.arange to have float increments
import os


###############################################################################
#                              * * * MODE 0 * * *                             #
###############################################################################

def MAKE_FILE_0(path, N, th, phi):
    path = os.path.join(path, "nonco_angle.dat")
    PATH = os.path.normpath(path)
    
    try:
        f = open(PATH, "w")  
    except OSError as error: 
        print(error)
    
#    -------------------------------------------------------
    for i in range(N):
        f.write(f"  {th:.15f}E+000  {phi:.15f}E+000  F\n")
#    -------------------------------------------------------
    
    f.close()


def MAKE_DIRs_0(N, th_start, th_end, d_th, phi_start, phi_end, d_phi):
    
    for th in np.arange(th_start, th_end + d_th, d_th):
        for phi in np.arange(phi_start, phi_end + d_phi, d_phi):
            
            # File name
            directory = f"th_{th:03d}_phi_{phi:03d}"
              
            # Parent Directory path
            parent_dir = os.getcwd()
              
            # Path
            path = os.path.join(parent_dir, directory)
            
            # Normalized Path for Windows or Linux
            PATH = os.path.normpath(path)
            
            try: 
                os.mkdir(PATH) 
                print("Directory '% s' created" % directory)
            except OSError as error: 
                print(error)
            
            MAKE_FILE_0(PATH, N, th, phi)


###############################################################################
#                              * * * MODE 1 * * *                             #
###############################################################################

def MAKE_FILE_1(path, N, th, phi):
    path = os.path.join(path, "nonco_angle.dat")
    PATH = os.path.normpath(path)
    
    try:
        f = open(PATH, "w")  
    except OSError as error: 
        print(error)
    
#    -------------------------------------------------------
    PHI=0
    for i in range(N):
        f.write(f"  {th:.15f}E+000  {PHI:.15f}E+000  F\n")
        PHI += (phi/N)*360
#    -------------------------------------------------------
    
    f.close()


def MAKE_DIRs_1(N, th_start, th_end, d_th, phi_start, phi_end, d_phi):
    
    for th in np.arange(th_start, th_end + d_th, d_th):
        for phi in np.arange(phi_start, phi_end + d_phi, d_phi):
            
            # File name
            directory = f"th_{th:03d}_phi_{phi}_{N}"
              
            # Parent Directory path
            parent_dir = os.getcwd()
              
            # Path
            path = os.path.join(parent_dir, directory)
            
            # Normalized Path for Windows or Linux
            PATH = os.path.normpath(path)
            
            try: 
                os.mkdir(PATH) 
                print("Directory '% s' created" % directory)
            except OSError as error: 
                print(error)
            
            MAKE_FILE_1(PATH, N, th, phi)