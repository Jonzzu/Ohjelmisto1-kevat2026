def suorakulmion_pinta_ala(kanta, korkeus):
    return kanta * korkeus
def suorakulmion_piiri(kanta, korkeus):
    return kanta *2 + korkeus *2


kanta_syote = input("Anna suorakulmion kanta: ")
korkeus_syote = input("Anna suorakulmion korkeus: ")

kanta = float(kanta_syote)
korkeus = float(korkeus_syote)

ala = suorakulmion_pinta_ala(kanta, korkeus)
print(f"Suorakulmion pinta-ala on: {ala}")


piiri =  suorakulmion_piiri(kanta, korkeus)
print(f'suorakulmion piiri on: {piiri}')
