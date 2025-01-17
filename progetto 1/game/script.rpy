#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define m = Character("Mariner", color="#0000ff") #protagonista
define l = Character("locondiere", color="#ffff00") #locandiere1
define r = Character("Rudel", color="#ffffff") #umano
define b = Character("Billa", color="#00ff00") #elfa

define sbattiCiglia = Fade(0.5, 0.5 ,0.5) #quanto ci mette a diventare nero, quanto resta nero, quanto ci mette a tornare come prima

default vitaPro = 35
default vitaProMax = 35
default vitaUmano = 28
default vitaUmanoMax = 28
default vitaElfa = 20
default vitaElfaMax = 20
default spada = 5
default mostroVita1 = 10000000000 
default mostroDanno1 = 10000000000 
#cinghiale vita-> 18
#cinghiale danno-> 4
default nCura = 0
default turno = 0

# Il gioco comincia qui.

label start:

    jump umanoNo
    
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
    
    m "perfetto il cielo è limpido"
    
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
    
    m "..."
    
    m "io sono Mariner, e tu?"
    
    r "io sono Rudel piacere"
    
    stop sound fadeout 1.0
    
    scene middrasil_1
    
    show dragonide_in_piedi at left
    
    show umano_in_piedi at right 
    with fade
    
    m "eccoci arrivati"
    
    r "me la ricordavo più grossa"
    
    m "sarà perché eri più piccolo te"
    
    m "comunque laggiu vedo una locanda"
    
    r "non sembra così piena"
    
    r "menomale avevo paura di non riuscire a trovare dove dormire"
    
    m "dai entriamo"
    
    jump citta


label umanoNo:
    
    r "ah okay"
    
    r "grazie lo stesso"
    
    "mi dispiace ma non so neache dove deve andare"
    
    play sound "passi_erba.mp3" loop volume 2.0
    
    scene pianura_1
    
    show dragonide_in_piedi at left
    with fade
    
    "spero che arrivi sano e salvo alla sua città natale"
    
    "va be comunque devo muovermi"
    
    play sound "ruggito.mp3" volume 2.0
    
    m "MA!"
    
    m "COSA E' STATO!"
    
    scene pianura_1
    
    show mostro_1 at right 
    
    show dragonide_in_piedi at left
    with fade
    
    $mostroVita1 = 18
    $mostroDanno1 = 4
    $nCura = 1
    
    menu comb1:
        
        "Tu-> vita: [vitaPro] | danno: [spada] \n mostro-> vita: [mostroVita1] | danno: [mostroDanno1]"
        
        "attacca":
            
            $mostroVita1 = mostroVita1 - spada
            
        "curati":
            
            if nCura > 0:
                $vitaPro = vitaPro + 8
                if vitaPro > vitaProMax:
                    $vitaPro = vitaProMax
                $nCura = 0
            else:
                "serve ancora un turno per curarsi"
                jump comb1
    
    if mostroVita1 > 0:
        if turno % 2 == 0:
            $vitaPro = vitaPro - mostroDanno1
        $nCura = nCura + 1
        $turno = turno + 1
        with fade
        jump comb1
    
    jump citta
    
label citta:
    
    scene locanda_del_medioevo_middrasil
    
    show locandiere
    
    show dragonide_in_piedi at left
    
    show umano_in_piedi at right 
    with fade
    
    m "salve quante stanza sono rimaste"
    
    return