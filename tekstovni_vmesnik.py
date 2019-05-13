import model

def izpis_igre(igra):
    return """Napačne črke: {}
            Pravilne črke: {}
            Število napak: {}
            Pravilni del gesla: {}
            Nepravilni ugibi: {}
            """.format(igra.napacne_crke(), igra.pravilne_crke(), igra.stevilo_napak(), igra.pravilni_del_gesla(), igra.nepravilni_ugibi())

def izpis_zmage(igra):
    if igra.zmaga:
        return "Bravo kralju, zmagu si!!!!"

def izpis_poraza(igra):
    if igra.poraz:
        return """Žal ni bilo prav
                Sedaj boš na drevesu
                Visel do drugič"""

def zahtevaj_vnos():
    crka = input("Vnesite črko: ")
    return crka.upper()

def pozeni_vmesnik():
    igra = nova_igra():
    while True:
        crka = zahtevaj_vnos():
        crka.napacne_crke()
        crka.pravilne_crke()
        crka.stevilo_napak()
        if crka.zmaga() or crka.poraz():
            break
        crka.pravilni_del_gesla()
        crka.nepravilni_ugibi()
        crka.stevilo_napak() += 1
        izpis_igre(crka)