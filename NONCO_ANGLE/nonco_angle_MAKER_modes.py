from modes import *


if __name__ == "__main__":
    
    text = "MODES"
    print(f"{text:_^20}\n0 : Magnetocrystalline anisotropy\n1 : Magnons")
    mode = int(input("\nSELECT MODE: "))
    
    N = int(input("\nNAEZ number: "))
    
    if mode == 0:
        th_start = int(input("\nTHETA angle start: "))
        th_end   = int(input("THETA angle final: "))
        if th_start != th_end:
            d_th = int(input("d_THETA: "))
        else:
            d_th = 1
        
        phi_start = int(input("\nPHI angle start: "))
        phi_end   = int(input("PHI angle final: "))
        if phi_start != phi_end:
            d_phi = int(input("d_PHI: "))
        else:
            d_phi = 1
        
        MAKE_DIRs_0(N, th_start, th_end, d_th, phi_start, phi_end, d_phi)
    
    elif mode == 1:
        th_start = int(input("\nTHETA angle: "))
        th_end   = th_start
        d_th     = 1
        
        phi_start = int(input("\nPHI angle start: "))
        phi_end   = int(input("PHI angle final: "))
        if phi_start != phi_end:
            d_phi = int(input("d_PHI: "))
        else:
            d_phi = 1
        
        MAKE_DIRs_1(N, th_start, th_end, d_th, phi_start, phi_end, d_phi)
    
    else:
        print("\nMODE NOT FOUND... :(\n")

