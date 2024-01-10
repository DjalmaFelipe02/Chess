import os

def menu():
    continuar = 1
    while continuar:
        continuar = int(input('Aperte 0 para sair ou 1 para jogar: '))
        if continuar:
            os.system('cls')
            game()
        else:
            print('Fechando')
            
tab0 = ['Tb', 'Cb', 'Bb', 'Qb', 'Kb', 'Bb', 'Cb', 'Tb']
tab1 = ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb']
tab2 = ['--', '--', '--', '--', '--', '--', '--', '--']
tab3 = ['--', '--', '--', '--', '--', '--', '--', '--']
tab4 = ['--', '--', '--', '--', '--', '--', '--', '--']
tab5 = ['--', '--', '--', '--', '--', '--', '--', '--']
tab6 = ['Pp', 'Pp', 'Pp', 'Pp', 'Pp', 'Pp', 'Pp', 'Pp']
tab7 = ['Tp', 'Cp', 'Bp', 'Qp', 'Kp', 'Bp', 'Cp', 'Tp']
tab  = [tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7]

def game():   
    
    bra = ['Tb', 'Cb', 'Bb', 'Qb', 'Kb', 'Pb']
    pre = ['Tp', 'Cp', 'Bp', 'Qp', 'Kp', 'Pp']
    tur = 1

    while 'Kb' in tab1 or 'Kb' in tab2 or'Kb' in tab3 or 'Kb' in tab4 or 'Kb' in tab5 or 'Kb' in tab6 or 'Kb' in tab7 or 'Kb' in tab0 and 'Kp' in tab1 or 'Kp' in tab2 or'Kp' in tab3 or 'Kp' in tab4 or 'Kp' in tab5 or 'Kp' in tab6 or 'Kp' in tab7 or 'Kp' in tab0:
        print('Turno:', tur)
        print("1-",tab0)
        print("2-",tab1)
        print("3-",tab2)
        print("4-",tab3)
        print("5-",tab4)
        print("6-",tab5)
        print("7-",tab6)
        print("8-",tab7)
        ii = int(input('Digite a linha horizontal da peça: ')) - 1
        ji = int(input('Digite a linha vertical da peça: ')) - 1
        ia = int(input('Digite a linha horizontal desejada: ')) - 1
        ja = int(input('Digite a linha vertical desejada: ')) - 1
        cont = 0
        os.system('cls')

        if tur % 2 == 1:
        #Movimento do peão branco
            if tab[ii][ji] == 'Pb':
                if tab[ia][ja] == '--':
                    if ia == ii + 1 and ja == ji:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Pb'
                        tur = tur + 1
                    elif ia == ii + 2 and ja == ji and tab[1][ji] == 'Pb' and tab[2][ji] == '--':
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Pb'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                elif tab[ia][ja] in pre:
                    if ia == ii + 1 and ja == ji + 1 or ja == ji - 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Pb'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
    
        #Movimento da torre branca            
            elif tab[ii][ji] == 'Tb':
                if tab[ia][ja] in pre or tab[ia][ja] == '--':
                    if ja == ji:
                        sti = abs(ia - ii)
                        if ii > ia and ii != ia + 1:
                            for x in range(1, sti):
                                if tab[ii - x][ji] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Tb'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')
                        elif ii == ia + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Tb'
                            tur = tur + 1
                        elif ia > ii and ia != ii + 1:
                            for x in range(1, sti):
                                if tab[ia - x][ji] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Tb'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')
                        elif ia == ii + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Tb'
                            tur = tur + 1
                    elif ia == ii:
                        stj = abs(ja - ji)
                        if ji > ja and ji != ja + 1:
                            for x in range(1, stj):
                                if tab[ii][ji - x] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Tb'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')
                        elif ji == ja + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Tb'
                            tur = tur + 1
                        elif ja > ji and ja != ji + 1:
                            for x in range(1, stj):
                                if tab[ii][ja - x] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Tb'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')        
                        elif ja == ji + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Tb'
                            tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
            
        #Movimento do cavalo branco
            elif tab[ii][ji] == 'Cb':
                if tab[ia][ja] in pre or tab[ia][ja] == '--':
                    if ia + 2 == ii and ja + 1 == ji or ia + 1 == ii and ja + 2 == ji or ia - 2 == ii and ja + 1 == ji or ia - 1 == ii and ja + 2 == ji or ia + 2 == ii and ja - 1 == ji or ia + 1 == ii and ja - 2 == ji or ia - 2 == ii and ja - 1 == ji or ia - 1 == ii and ja - 2 == ji:     
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Cb'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
    
        #Movimento do bispo branco
            elif tab[ii][ji] == 'Bb':
                if tab[ia][ja] in pre or tab[ia][ja] == '--':
                    sti = abs(ia - ii)
                    if ii - ia == ji - ja > 0 and ii - ia != 1:
                        for x in range(1, sti):
                            if tab[ii - x][ji - x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Bb'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ii - ia == ji - ja == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bb'
                        tur = tur + 1
                    elif ia - ii == ji - ja > 0 and ia - ii != 1:
                        for x in range(1, sti):
                            if tab[ii + x][ji - x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Bb'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ia - ii == ji - ja == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bb'
                        tur = tur + 1
                    elif ii - ia == ja - ji > 0 and ii - ia != 1:
                        for x in range(1, sti):
                            if tab[ii - x][ji + x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Bb'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ii - ia == ja - ji == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bb'
                        tur = tur + 1
                    elif ia - ii == ja - ji > 0 and ia - ii != 1:
                        for x in range(1, sti):
                            if tab[ii + x][ji + x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Bb'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ia - ii == ja - ji == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bb'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
    
        #Movimento da rainha branca
            elif tab[ii][ji] == 'Qb':
                if tab[ia][ja] in pre or tab[ia][ja] == '--':
                    sti = abs(ia - ii)
                    if ja == ji:
                        if ii > ia and ii != ia + 1:
                            for x in range(1, sti):
                                if tab[ii - x][ji] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Qb'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')
                        elif ii == ia + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Qb'
                            tur = tur + 1
                        elif ia > ii and ia != ii + 1:
                            for x in range(1, sti):
                                if tab[ia - x][ji] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Qb'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')
                        elif ia == ii + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Qb'
                            tur = tur + 1
                    elif ia == ii:
                        stj = abs(ja - ji)
                        if ji > ja and ji != ja + 1:
                            for x in range(1, stj):
                                if tab[ii][ji - x] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Qb'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')
                        elif ji == ja + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Qb'
                            tur = tur + 1
                        elif ja > ji and ja != ji + 1:
                            for x in range(1, stj):
                                if tab[ii][ja - x] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Qb'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')       
                        elif ja == ji + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Qb'
                            tur = tur + 1
                    elif ii - ia == ji - ja > 0 and ii - ia != 1:
                        for x in range(1, sti):
                            if tab[ii - x][ji - x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Qb'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ii - ia == ji - ja == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Qb'
                        tur = tur + 1
                    elif ia - ii == ji - ja > 0 and ia - ii != 1:
                        for x in range(1, sti):
                            if tab[ii + x][ji - x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Qb'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ia - ii == ji - ja == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Qb'
                        tur = tur + 1
                    elif ii - ia == ja - ji > 0 and ii - ia != 1:
                        for x in range(1, sti):
                            if tab[ii - x][ji + x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Qb'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ii - ia == ja - ji == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Qb'
                        tur = tur + 1
                    elif ia - ii == ja - ji > 0 and ia - ii != 1:
                        for x in range(1, sti):
                            if tab[ii + x][ji + x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Qb'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ia - ii == ja - ji == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Qb'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
    
        #Movimento do rei branco
            elif tab[ii][ji] == 'Kb':
                if tab[ia][ja] in pre or tab[ia][ja] == '--':
                    if ii + 2 > ia > ii - 2 and ji + 2 > ja > ji - 2:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Kb'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')

        elif tur % 2 == 0:
        #Movimento do peão preto
            if tab[ii][ji] == 'Pp':
                if tab[ia][ja] == '--':
                    if ia == ii - 1 and ja == ji:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Pp'
                        tur = tur + 1
                    elif ia == ii - 2 and ja == ji and tab[6][ji] == 'Pp' and tab[5][ji] == '--':
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Pp'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                elif tab[ia][ja] in bra:
                    if ia == ii - 1 and ja == ji + 1 or ja == ji - 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Pp'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
        #Movimento da torre preta
            elif tab[ii][ji] == 'Bp':
                if tab[ia][ja] in bra or tab[ia][ja] == '--':
                    sti = abs(ia - ii)
                    if ii - ia == ji - ja > 0 and ii - ia != 1:
                        for x in range(1, sti):
                            if tab[ii - x][ji - x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Tp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ii - ia == ji - ja == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bp'
                        tur = tur + 1
                    elif ia - ii == ji - ja > 0 and ia - ii != 1:
                        for x in range(1, sti):
                            if tab[ii + x][ji - x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Tp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ia - ii == ji - ja == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bp'
                        tur = tur + 1
                    elif ii - ia == ja - ji > 0 and ii - ia != 1:
                        for x in range(1, sti):
                            if tab[ii - x][ji + x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Tp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ii - ia == ja - ji == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bp'
                        tur = tur + 1
                    elif ia - ii == ja - ji > 0 and ia - ii != 1:
                        for x in range(1, sti):
                            if tab[ii + x][ji + x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Tp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ia - ii == ja - ji == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bp'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
                    
        #Movimento do cavalo preto
            elif tab[ii][ji] == 'Cp':
                if tab[ia][ja] in bra or tab[ia][ja] == '--':
                    if ia + 2 == ii and ja + 1 == ji or ia + 1 == ii and ja + 2 == ji or ia - 2 == ii and ja + 1 == ji or ia - 1 == ii and ja + 2 == ji or ia + 2 == ii and ja - 1 == ji or ia + 1 == ii and ja - 2 == ji or ia - 2 == ii and ja - 1 == ji or ia - 1 == ii and ja - 2 == ji:     
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Cp'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
                    
        #Movimento do bispo preto
            elif tab[ii][ji] == 'Bp':
                if tab[ia][ja] in bra or tab[ia][ja] == '--':
                    sti = abs(ia - ii)
                    if ii - ia == ji - ja > 0 and ii - ia != 1:
                        for x in range(1, sti):
                            if tab[ii - x][ji - x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Bp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ii - ia == ji - ja == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bp'
                        tur = tur + 1
                    elif ia - ii == ji - ja > 0 and ia - ii != 1:
                        for x in range(1, sti):
                            if tab[ii + x][ji - x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Bp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ia - ii == ji - ja == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bp'
                        tur = tur + 1
                    elif ii - ia == ja - ji > 0 and ii - ia != 1:
                        for x in range(1, sti):
                            if tab[ii - x][ji + x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Bp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ii - ia == ja - ji == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bp'
                        tur = tur + 1
                    elif ia - ii == ja - ji > 0 and ia - ii != 1:
                        for x in range(1, sti):
                            if tab[ii + x][ji + x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Bp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ia - ii == ja - ji == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Bp'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
                    
        #Movimento da rainha preta
            elif tab[ii][ji] == 'Qp':
                if tab[ia][ja] in bra or tab[ia][ja] == '--':
                    sti = abs(ia - ii)
                    if ja == ji:
                        if ii > ia and ii != ia + 1:
                            for x in range(1, sti):
                                if tab[ii - x][ji] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Qp'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')
                        elif ii == ia + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Qp'
                            tur = tur + 1
                        elif ia > ii and ia != ii + 1:
                            for x in range(1, sti):
                                if tab[ia - x][ji] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Qp'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')
                        elif ia == ii + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Qp'
                            tur = tur + 1
                    elif ia == ii:
                        stj = abs(ja - ji)
                        if ji > ja and ji != ja + 1:
                            for x in range(1, stj):
                                if tab[ii][ji - x] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Qp'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')
                        elif ji == ja + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Qp'
                            tur = tur + 1
                        elif ja > ji and ja != ji + 1:
                            for x in range(1, stj):
                                if tab[ii][ja - x] == '--':
                                    cont = cont + 1
                                    if cont == sti - 1:
                                        tab[ii][ji] = '--'
                                        tab[ia][ja] = 'Qp'
                                        tur = tur + 1
                            if cont != sti + 1:
                                print('Está peça não se move dessa forma')       
                        elif ja == ji + 1:
                            tab[ii][ji] = '--'
                            tab[ia][ja] = 'Qp'
                            tur = tur + 1
                    elif ii - ia == ji - ja > 0 and ii - ia != 1:
                        for x in range(1, sti):
                            if tab[ii - x][ji - x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Qp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ii - ia == ji - ja == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Qp'
                        tur = tur + 1
                    elif ia - ii == ji - ja > 0 and ia - ii != 1:
                        for x in range(1, sti):
                            if tab[ii + x][ji - x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Qp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ia - ii == ji - ja == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Qp'
                        tur = tur + 1
                    elif ii - ia == ja - ji > 0 and ii - ia != 1:
                        for x in range(1, sti):
                            if tab[ii - x][ji + x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Qp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ii - ia == ja - ji == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Qp'
                        tur = tur + 1
                    elif ia - ii == ja - ji > 0 and ia - ii != 1:
                        for x in range(1, sti):
                            if tab[ii + x][ji + x] == '--':
                                cont = cont + 1
                                if cont == sti - 1:
                                    tab[ii][ji] = '--'
                                    tab[ia][ja] = 'Qp'
                                    tur = tur + 1
                        if cont != sti + 1:
                            print('Está peça não se move dessa forma')
                    elif ia - ii == ja - ji == 1:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Qp'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
                    
        #Movimento do rei preto
            elif tab[ii][ji] == 'Kp':
                if tab[ia][ja] in pre or tab[ia][ja] == '--':
                    if ii + 2 > ia > ii - 2 and ji + 2 > ja > ji - 2:
                        tab[ii][ji] = '--'
                        tab[ia][ja] = 'Kp'
                        tur = tur + 1
                    else:
                        print('Está peça não se move dessa forma')
                else:
                    print('Está peça não se move dessa forma')
                
    if 'Kb' in tab0 or 'Kb' in tab1 or 'Kb' in tab2 or'Kb' in tab3 or 'Kb' in tab4 or 'Kb' in tab5 or 'Kb' in tab6 or 'Kb' in tab7:
        if 'Kp' not in tab1 and 'Kp' not in tab2 and'Kp' not in tab3 and 'Kp' not in tab4 and 'Kp' not in tab5 and 'Kp' not in tab6 and 'Kp' not in tab7 and 'Kp' not in tab0:
            print('')
            print('A vitória são das peças brancas!')
    elif 'Kp' in tab1 or 'Kp' in tab2 or'Kp' in tab3 or 'Kp' in tab4 or 'Kp' in tab5 or 'Kp' in tab6 or 'Kp' in tab7 or 'Kp' in tab0:
        if 'Kb' not in tab1 and 'Kb' not in tab2 and'Kb' not in tab3 and 'Kb' not in tab4 and 'Kb' not in tab5 and 'Kb' not in tab6 and 'Kb' not in tab7 and 'Kb' not in tab0:
            print('')
            print('A vitória são das peças pretas!')   

menu()
