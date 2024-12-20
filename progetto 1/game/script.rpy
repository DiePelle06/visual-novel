#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define m = Character("--------", color="#0000ff")
define l = Character("locondiere", color="#ffff00")

define fadehold = Fade(0.5, 1.0, 0.5) #quanto ci mette a diventare nero, quanto resta nero, quanto ci mette a tornare come prima


# Il gioco comincia qui.

label start:

    scene black

    scene camera_locanda with fadehold
    scene camera_locanda with fadehold
    scene camera_locanda
    
    m "Yaaaaaaaawh"
    
    m "ho dormito proprio bene"
    
    show dragonide_in_piedi
    with fade
    
    m "ma ora devo andare"
    
    scene locanda_del_medioevo with fade
    
    show locandiere 
    show bancone 
    
    l "salve gentil cliente "
    
    l "ha gradito la sua stanza?"
    
    show dragonide_in_piedi at left 
    
    m "si, ho dormito molto bene"
    
    m "grazie a rivederci"

    return

