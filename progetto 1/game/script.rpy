#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define m = Character("Mariner", color="#0000ff")
define l = Character("locondiere", color="#ffff00")
define r = Character("Rudel", color="#ffffff")
define b = Character("Billa", color="#00ff00")

define sbattiCiglia = Fade(0.5, 1.0, 0.5) #quanto ci mette a diventare nero, quanto resta nero, quanto ci mette a tornare come prima


# Il gioco comincia qui.

label start:

    scene black

    scene camera_locanda with sbattiCiglia
    scene camera_locanda with sbattiCiglia
    scene camera_locanda
    
    m "Yaaaaaaaawh"
    
    m "ho dormito proprio bene"
    
    show dragonide_in_piedi
    with fade
    
    m "ma ora devo andare"
    
    scene locanda_del_medioevo
    
    show locandiere at right
    
    show dragonide_in_piedi at left
    with fade
    
    l "salve gentil cliente "
    
    l "ha gradito la sua stanza?"
    
    m "si, ho dormito molto bene"
    
    m "grazie a rivederci"
    
    hide locandiere
    
    hide dragonide_in_piedi
    
    scene montagne_1
    
    show dragonide_in_piedi at left
    with fade
    
    m "a perfetto il cielo è limpido"
    
    m "ma non ho tempo da perdere, devo muovermi"
    
    hide dragonide_in_piedi
    
    scene sentiero_1
    
    show dragonide_in_piedi at left
    with fade
    
    m "dai ci sono quasi mancano solo due ore"
    
    show umano_in_piedi at right with fade
    
    r "hey! tu!"
    
    m "stai parlando con me?"
    
    menu:
        
        r "si, potresti accompagnarmi alla mia città natale?"
        
        "si certo":
            
            jump umanoSi
            
        "no mi dispiace vado di fretta":
            
            jump umanoNo

    
label umanoSi:
        
    m "dove sei diretto?"
    
    r "vado verso Middrasil"
    
    m "oh ma che coincidenza devo andarci pure io"
    
    play sound "passi_erba.mp3" loop volume 2.0
    
    scene pianura_1
    
    show dragonide_in_piedi at left
    
    show umano_in_piedi at right 
    with fade
    
    r "da dove vieni?"
    
    m "da Mlena"
    
    m "lavori?"
    
    r "si faccio lo jettatore"
    
    m "cosa?"
    
    r "sto scherzando stai tranquillo"
    
    r "sono un falegname, e tu?"
    
    m "da come puoi vedere faccio l'avventuriero"
    
    stop sound fadeout 1.0
    
    scene middrasil_1
    
    show dragonide_in_piedi at left
    
    show umano_in_piedi at right 
    with fade
    
    m "eccoci arrivati"
    
    r "me la ricordavo più grossa"
    
    m "sarà perché eri più piccolo te"
    
    jump citta


label umanoNo:
    
    r "ah okay"
    
    r "grazie lo stesso"
    
    r "TREEEEMOOOOONNNN"
    
    jump citta
    
label citta:
    
    scene middrasil_1
    
    show dragonide_in_piedi at left
    
    show umano_in_piedi at right 
    with fade
    
    "lololololololololololololololololo"
    
    return