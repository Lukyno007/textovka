import random
import monstra
import zbrane
from inventar import Inventar
from postava import Postava

print("Ahoj, vitej ve hre STESTI")
print("Pro zacatek mi prosim rekni sve jmeno, tak ti budu rikat celou hru: ")
print("Tve jmeno:")


def vytvor_postavu_z_input():
    jmeno_hrace = input()
    nova_postava = Postava(jmeno_hrace, level=1, exp=0, hp=20, utok=10, obrana=5)
    return nova_postava


nova_postava = vytvor_postavu_z_input()
hracuv_inventar = Inventar()

print(f"Diky, {nova_postava.jmeno}, tve zakladni hodnoty jsou nasledujici:")
print(
    f"Tvuj level je: {nova_postava.level}, tve HP jsou: {nova_postava.hp}, tvoje obrana je: {nova_postava.obrana} a tvuj utok je: {nova_postava.utok}. ")

print("")

print("""Sbirej hodnotne veci, ktere ti mohou pomoci v prekonavani nastrah tohoto sveta...
Nikdy se nepoustej do akci, ktere vypadaji prilis nebezpecne...
Obcas, kdyz si spatne zvolis moznost, muze te zachranit "HOD KOSTKOU"...
K hodu kostkou  jsi vyzvan a pokud hodis:
1 az 4 - povedlo se
5 az 6 - nepovedlo se.""")

print("")

print("""Kdyz se rozhodnes pro boj s priserou, stridate se utok po utoku.
Ty s utokem vzdy zacinas, po tvem utoku utoci monster.
Tvuj utok je tvuj utok minus monster obrana a pro monster to plati stejne.
Ke kazdemu utoku si hazite s monstrem spolecne kostkou, hozene cislo se pricita ke kazdemu utoku.
Hodne stesti.""")

print("")

print("Zaciname tedy tve dobrodruzsti :).")
print("Tvuj pribeh zacina na ostrove Bolze, po ztroskotani tve lodi jsi jen zazrakem prezil.")
print("Probudil jsi se na rozpalene plazi.")
print("Kousek vedle tebe lezi truhla, ktera byla tvym majetkem na lodi.")
print("Rozhodnes se tuto truhlu otevrit?")
print("( ano / ne: )")
rozhodnuti = input()

print("")

while rozhodnuti != "ano" and rozhodnuti != "ne":
    print("Zadal jsi neplatny prikaz, zkus to znovu: ")
    rozhodnuti = input()
if rozhodnuti == "ano":
    print(f"{nova_postava.jmeno}, rozhodl jsi se otevrit svou truhlu a delas dobre :) .")
    print("Nasel si v ni svuj stary mec.")
    nova_postava.ziskat_exp(100)

    print("")

    print(f"Ziskal jsi novy predmet: {zbrane.stary_mec.jmeno}, utok: {zbrane.stary_mec.utok}.")
    hracuv_inventar.pridat_zbran(zbrane.stary_mec)
    hracuv_inventar.vypis_inventar()
    nova_postava.aktualizovat_vlastnosti(hracuv_inventar)

    print("")

    print(f"Tvuj zakladni utok se zvetsil na: {nova_postava.utok}")
    print(
        f"Tvuj level je: {nova_postava.level}, tve EXP jsou: {nova_postava.exp},\ntve HP jsou: {nova_postava.hp}, tvoje obrana je: {nova_postava.obrana} a tvuj utok je: {nova_postava.utok}. ")

    print("")

    print("Nyni se rozhodujes, co budes delat dal.")
else:
    print(
        f"{nova_postava.jmeno}, rozhodl jsi se bednu neotevrit, dobra tedy, od bedny odstupujes a rozhodujes se, co udelas dal.")

print("V dalce vidis jeskyni, nevypada teda vlidne... Vydas se k ni nebo ji radeji obejdes?")
print("( k jeskyni / obejit: )")
rozhodnuti = input()
while rozhodnuti != "k jeskyni" and rozhodnuti != "obejit":
    print("Zadal jsi neplatny prikaz, zkus to znovu: ")
    rozhodnuti = input()

print("")

if rozhodnuti == "k jeskyni":
    print(f"""Vyrazis k jeskyni {nova_postava.jmeno}, vedle vstupu je vyrity napis:

    Kdo vstoupi, jiz nevystoupi,
    pradavne monstra uvnitr najdes.
    Jeli ti zivot mili, odvrat svou cestu hned.
    """)
    print("Co tedy udelas?")
    print("( vstoupit / odejit: )")
    choice = input()

    print("")

    while choice != "vstoupit" and choice != "odejit":
        print("Zadal jsi neplatny prikaz, zkus to znovu: ")
        choice = input()
    if choice == "vstoupit":
        print(f"Vstupujes do jeskyne, jsi odvazny {nova_postava.jmeno}.")
        print("Jdes par kroku, temer po tme a najednou slysis v dalce divne zvuky...")
        print(f"Z niceho nic se ze tmy na tebe vyritil {monstra.basilisek.jmeno}.")
        print("")
        print(
            f"Monstrum: {monstra.basilisek.jmeno}, utok: {monstra.basilisek.utok}, obrana: {monstra.basilisek.obrana}, zivot: {monstra.basilisek.zivot} ")
        print(
            f"Tve vlastnosti: {nova_postava.jmeno}, utok: {nova_postava.utok}, obrana: {nova_postava.obrana}, zivot: {nova_postava.hp}.")
        print("")
        print("Budes s Baziliskem bojovat nebo uteces?")
        print("( utok / utect: )")
        choice_boj = input()
        while choice_boj != "utok" and choice_boj != "utect":
            print("Zadal jsi neplatny prikaz, zkus to znovu: ")
            choice_boj = input()

        print("")

        if choice_boj == "utok":
            utok_basilisek = nova_postava.utok - monstra.basilisek.obrana
            utok_baziliska = monstra.basilisek.utok - nova_postava.obrana
            if nova_postava.hp >= 0:
                print(f"""Tve staty jsou: 
    utok: {nova_postava.utok},
    obrana: {nova_postava.obrana},
    zivoty: {nova_postava.hp}.""")
                print("")
                print(f"""Baziliškovi staty jsou: 
    utok: {monstra.basilisek.utok},
    obrana: {monstra.basilisek.obrana},
    zivoty: {monstra.basilisek.zivot}.""")
                print("")
                print("Zahajujes svuj prvni utok, hod si kostkou / napis hodit: ")
                hazime_ted = input()
                while hazime_ted != "hodit":
                    print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                    hazime_ted = input()
                bojovny_hod = random.randint(1, 6)
                print(f"Hodil jsi: {bojovny_hod}.")
                bojovny_utok = (bojovny_hod + nova_postava.utok) - monstra.basilisek.obrana
                monstra.basilisek.ubrat_zivot(bojovny_utok)
                if monstra.basilisek.zivot >= 0:
                    print("")
                    print("Basilisek utoci!")
                    bojovny_hod_monstra = random.randint(1, 6)
                    print(f"Monster hodil: {bojovny_hod_monstra}.")
                    bojovny_utok_monstra = (bojovny_hod_monstra + monstra.basilisek.utok) - nova_postava.obrana
                    nova_postava.ubrat_hp(bojovny_utok_monstra)
                    print("")
                    print(f"{nova_postava.jmeno}, jsi na rade, utocis.")

                    print("Zahajujes svuj druhy utok, hod si kostkou / napis hodit: ")
                    hazime_ted = input()
                    while hazime_ted != "hodit":
                        print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                        hazime_ted = input()
                    bojovny_hod = random.randint(1, 6)
                    print(f"Hodil jsi: {bojovny_hod}.")
                    bojovny_utok = (bojovny_hod + nova_postava.utok) - monstra.basilisek.obrana
                    monstra.basilisek.ubrat_zivot(bojovny_utok)
                    if monstra.basilisek.zivot >= 0:
                        print("")
                        print("Basilisek utoci!")
                        bojovny_hod_monstra = random.randint(1, 6)
                        print(f"Monster hodil: {bojovny_hod_monstra}.")
                        bojovny_utok_monstra = (bojovny_hod_monstra + monstra.basilisek.utok) - nova_postava.obrana
                        nova_postava.ubrat_hp(bojovny_utok_monstra)
                        print("")
                        print(f"{nova_postava.jmeno}, jsi na rade, utocis.")
                        print("Zahajujes svuj treti utok, hod si kostkou / napis hodit: ")
                        hazime_ted = input()
                        while hazime_ted != "hodit":
                            print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                            hazime_ted = input()
                        bojovny_hod = random.randint(1, 6)
                        print(f"Hodil jsi: {bojovny_hod}.")
                        bojovny_utok = (bojovny_hod + nova_postava.utok) - monstra.basilisek.obrana
                        monstra.basilisek.ubrat_zivot(bojovny_utok)
                        if monstra.basilisek.zivot >= 0:
                            print("")
                            print("Basilisek utoci!")
                            bojovny_hod_monstra = random.randint(1, 6)
                            print(f"Monster hodil: {bojovny_hod_monstra}.")
                            bojovny_utok_monstra = (bojovny_hod_monstra + monstra.basilisek.utok) - nova_postava.obrana
                            nova_postava.ubrat_hp(bojovny_utok_monstra)
                        else:
                            print("Vítězství")
                            nova_postava.ziskat_exp(500)
                            print("")

                            print("Za mrtvolou Baziliska vidis starou truhlu.")
                            print("Rozhodnes se ji otevrit?")
                            print("( ano / ne: )")
                            otevrit_neotevrit = input()
                            while otevrit_neotevrit != "ano" and otevrit_neotevrit != "ne":
                                print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                                otevrit_neotevrit = input()
                            if otevrit_neotevrit == "ano":
                                print(f"Vyborne, nasel jsi v truhle: {zbrane.dreveny_stit.jmeno}")
                                nova_postava.ziskat_exp(100)
                                hracuv_inventar.pridat_zbran(zbrane.dreveny_stit)
                                hracuv_inventar.vypis_inventar()
                                nova_postava.aktualizovat_vlastnosti(hracuv_inventar)
                                print(f"Tva zakladni obrana se zvetsila na: {nova_postava.obrana}")
                                print(
                                    f"Tvuj level je: {nova_postava.level}, tve EXP jsou: {nova_postava.exp},\ntve HP jsou: {nova_postava.hp}, tvoje obrana je: {nova_postava.obrana} a tvuj utok je: {nova_postava.utok}. ")

                                print("")

                                print("Odchazis s novou vybavou z jeskyne pryc.")
                            else:
                                print("Radeji truhlu neoteviras a odchazis z jekyne pryc.")




                    else:
                        print("Vítězství")
                        nova_postava.ziskat_exp(500)
                        print("")

                        print("Za mrtvolou Baziliska vidis starou truhlu.")
                        print("Rozhodnes se ji otevrit?")
                        print("( ano / ne: )")
                        otevrit_neotevrit = input()
                        while otevrit_neotevrit != "ano" and otevrit_neotevrit != "ne":
                            print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                            otevrit_neotevrit = input()
                        if otevrit_neotevrit == "ano":
                            print(f"Vyborne, nasel jsi v truhle: {zbrane.dreveny_stit.jmeno}")
                            nova_postava.ziskat_exp(100)
                            hracuv_inventar.pridat_zbran(zbrane.dreveny_stit)
                            hracuv_inventar.vypis_inventar()
                            nova_postava.aktualizovat_vlastnosti(hracuv_inventar)
                            print(f"Tva zakladni obrana se zvetsila na: {nova_postava.obrana}")
                            print(
                                f"Tvuj level je: {nova_postava.level}, tve EXP jsou: {nova_postava.exp},\ntve HP jsou: {nova_postava.hp}, tvoje obrana je: {nova_postava.obrana} a tvuj utok je: {nova_postava.utok}. ")

                            print("")

                            print("Odchazis s novou vybavou z jeskyne pryc.")
                        else:
                            print("Radeji truhlu neoteviras a odchazis z jekyne pryc.")







                else:
                    print("Vítězství")
                    nova_postava.ziskat_exp(500)
                    print("")

                    print("Za mrtvolou Baziliska vidis starou truhlu.")
                    print("Rozhodnes se ji otevrit?")
                    print("( ano / ne: )")
                    otevrit_neotevrit = input()
                    while otevrit_neotevrit != "ano" and otevrit_neotevrit != "ne":
                        print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                        otevrit_neotevrit = input()
                    if otevrit_neotevrit == "ano":
                        print(f"Vyborne, nasel jsi v truhle: {zbrane.dreveny_stit.jmeno}")
                        nova_postava.ziskat_exp(100)
                        hracuv_inventar.pridat_zbran(zbrane.dreveny_stit)
                        hracuv_inventar.vypis_inventar()
                        nova_postava.aktualizovat_vlastnosti(hracuv_inventar)
                        print(f"Tva zakladni obrana se zvetsila na: {nova_postava.obrana}")
                        print(
                            f"Tvuj level je: {nova_postava.level}, tve EXP jsou: {nova_postava.exp},\ntve HP jsou: {nova_postava.hp}, tvoje obrana je: {nova_postava.obrana} a tvuj utok je: {nova_postava.utok}. ")

                        print("")

                        print("Odchazis s novou vybavou z jeskyne pryc.")
                    else:
                        print("Radeji truhlu neoteviras a odchazis z jekyne pryc.")
            else:
                print("umrel jsi.")


        else:
            print("Zkousis sve stesti a snazis se pred Baziliskem utect.")
            print("Hod si kostkou \n( napis: hodit )")
            hodit_kostkou = input()
            while hodit_kostkou != "hodit":
                print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                hodit_kostkou = input()
            hod_kostkou = random.randint(1, 6)
            hod_kostkou_str = str(hod_kostkou)
            print(f"Hodil jsi: {hod_kostkou_str}.")

            print("")

            if hod_kostkou == 1 or hod_kostkou == 2 or hod_kostkou == 3:
                print("Vyborne, povedlo se ti utect.")
                print("Mel jsi stesti...")
                print("Utekl jsi z jeskyne a pokracujes dal.")
            else:
                nova_postava.ubrat_hp(10)
                print("Bohuzel te pri uteku Bazilisek stihl zasahnout a ubrat ti 10 z tvych HP...")
                print("")
                print("Jsi nyni mimo jeskyni a pokracujes dal.")
    else:
        print(f"{nova_postava.jmeno}, rozhodl jsi se nevstoupit do jeskyne.")
        print("Obchazis tedy jeskyni a pokracujes svou cestu dal.")
else:
    print("Obchazis tedy jeskyni a pokracujes svou cestu dal.")

print("")

print("Kdyz jdes podel hory, ve ktere byl vstup do jeskyne, zacinas pocitovat priznaky hladu.")
print("Premyslis, co budes delat, jak si obstaras jidlo...")

print("")

print("Jelikoz jsi nepozorny, hladovy a nekoukas na cestu, slapl jsi na ostri kamen, ktery lezel v pisku.")
print("Hod si kostkou, jestli ti kamen zpusobil poskozeni nebo ne. \n( napis: hodit )")
hodit_kostkou = input()
while hodit_kostkou != "hodit":
    print("Zadal jsi neplatny prikaz, zkus to znovu: ")
    hodit_kostkou = input()
hod_kostkou = random.randint(1, 6)
hod_kostkou_str = str(hod_kostkou)
print(f"Hodil jsi: {hod_kostkou_str}.")

print("")

if hod_kostkou == 2 or hod_kostkou == 3 or hod_kostkou == 1:
    print("Vyborne, kamen ti nezpusobil zadna zraneni, jen to trochu zabolelo.")
    print("Mel jsi stesti...")

    print("")

    print("Pokracujes dal.")
else:
    nova_postava.ubrat_hp(4)
    print("Bohuzel te kamen poranil a ubral ti 4 z tvych HP...")
    print(f"Tvuj zivot je nyni: {nova_postava.hp}.")
    print("I pres tve zraneni ale pokracujes dal.")

print("")

print("Prichazis ke stromu, ktere nese zahadne, leč chutne vypadajici druh ovoce.")
print("Trhas jedno ovoce ze stromu a premyslis, jestli ho snist nebo radeji ne.")
print("( snist / zahodit: )")
vyhodit_nebo_snist = input()
print("")
while vyhodit_nebo_snist != "snist" and vyhodit_nebo_snist != "zahodit":
    print("Zadal jsi neplatny prikaz, zkus to znovu: ")
    vyhodit_nebo_snist = input()
if vyhodit_nebo_snist == "snist":
    print("Rozhodl jsi se snist chutne vypadajici ovoce a delas dobre. Ovoce ti pridalo 5 HP")
    # tady pridat exp , to jeste nevim jak, aby prislusny pocet expu zvysoval automaticky level...
    if nova_postava.hp <= 15:
        nova_postava.hp = nova_postava.hp + 5
        print(f"Tvuj zivot je nyni: {nova_postava.hp}")
    elif nova_postava.hp == 16:
        nova_postava.hp = nova_postava.hp + 4
        print(f"Tvuj zivot je nyni: {nova_postava.hp}")
    elif nova_postava.hp == 17:
        nova_postava.hp = nova_postava.hp + 3
        print(f"Tvuj zivot je nyni: {nova_postava.hp}")
    elif nova_postava.hp == 18:
        nova_postava.hp = nova_postava.hp + 2
        print(f"Tvuj zivot je nyni: {nova_postava.hp}")
    elif nova_postava.hp == 19:
        nova_postava.hp = nova_postava.hp + 1
        print(f"Tvuj zivot je nyni: {nova_postava.hp}")
    else:
        print(f"Tva postava ma plny zivot, ovoce ti nic nepridalo.")
else:
    print("Zahazujes jablko.")

print("")

print("Pokracujeme dal.")

print("")

print("Prosel si dalsi kus ostrova, prichazis k opustene chatrci, ktera uz ma sva nejlepsi leta zasebou.")
print("Mas na vyber, jestli se podivas do vnitr nebo ji proste mines.")
print("( dovnitr / odejit: )")
chatrc = input()

print("")

while chatrc != "dovnitr" and chatrc != "odejit":
    print("Zadal jsi neplatny prikaz, zkus to znovu: ")
    chatrc = input()
if chatrc == "dovnitr":
    print("Vstupujes tedy do chatrce. Vidis zde starou osobu, zahalenou v kapi s krasnou zdobenou dykou za opaskem.")
    print("""Postava: "Co je, mrdko??!" """)
    print("( odejit / mluvit: )")
    zvolit_postava_v_chatrci = input()

    print("")

    while zvolit_postava_v_chatrci != "odejit" and zvolit_postava_v_chatrci != "mluvit":
        print("Zadal jsi neplatny prikaz, zkus to znovu: ")
        zvolit_postava_v_chatrci = input()
    if zvolit_postava_v_chatrci == "mluvit":
        print("Ty: JAA, jaa, no chtel jsem se jen podivat, jestli bych tu nenasel neco k jidlu...")
        print("Postava: Vypada to tady snad do prdele jako nejakej zasranej Zupermarket?")
        print("Ty: Nee to ne, ja jen ...")
        print("Postava: Neee, ty jen co? Blbecku? Chces ranu?")
        print("( ano / ne: )")
        ano_ne_osobe_chatrc = input()

        print("")

        while ano_ne_osobe_chatrc != "ano" and ano_ne_osobe_chatrc != "ne":
            print("Zadal jsi neplatny prikaz, zkus to znovu: ")
            ano_ne_osobe_chatrc = input()
        if ano_ne_osobe_chatrc == "ano":
            print("Ty: Tak to zkus ty mocale, zabiju te, pojd!!!")
            print("Postava: AAhahhaaa dobre ty, klidek vokurko, jen jsem te zkousel, pičko...")

            print("")

            print("Postava: Rikaji mi Bohuta.")
            print("Postava: Mam pro tebe tri hadanky, kdyz je uhadnes, dam ti mou dyku, chces?")
            print("Ty: A co kdyz neuhadnu?")
            print("Postava: Tak mi das svuj mec nebo stit a pokud nemas, vykouris me, koste, AHAHAH.")
            print("( hrat / nehrat: )")
            hrat_nehrat = input()

            print("")

            while hrat_nehrat != "hrat" and hrat_nehrat != "nehrat":
                print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                hrat_nehrat = input()
            if hrat_nehrat == "hrat":
                print("Ty: Ok, to beru, jaky jsou pravidla?")
                print(
                    "Postava: CO? ty jsi uplne blbej, uhadni tri moje hadanky, dam ti dyku, poser to a das mi tu vec nebo me vykouris!!!...aHAHHA.")
                print("Ty: Ok, jdeme na to!")

                print("")

                print("""Postava: prvni hadanka: Vcera vecer jsem vojel Marenu, Terezu a Olgu. 
                        Byl jsem jak kara, a tak jsem voprcal i Terezy fenu Matyldu.
                        Pak jsem na chvili usnul, vis jak, bolel me curak...
                        Ale po hodine to na me zas prislo, a voprcal jsem Olgu znova i s jejim starym.
                        Kolik jsem vcera vojel zenskych?""")

                print("")

                print("Zamyslis se...")
                print("( 3 / 4 / 5: )")
                vyber_cisla = input()
                while vyber_cisla != "3" and vyber_cisla != "4" and vyber_cisla != "5":
                    print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                    vyber_cisla = input()
                if vyber_cisla == "3":
                    print(f"Ty: Ma odpoved je: {vyber_cisla}")
                    print("Postava: Kundo pochcana, ok, mel si stesti...dame tedy druhou hadanku...!")

                    print("")

                    print("""Postava: Co nasleduje po 69?""")

                    print("")

                    print("Chvili premyslis...")
                    print("( 70 / vyplach ust: )")
                    odpoved_na_otazku_dva = input()
                    while odpoved_na_otazku_dva != "70" and odpoved_na_otazku_dva != "vyplach ust":
                        print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                        odpoved_na_otazku_dva = input()
                    print(f"Ty: Ma odpoved je: {odpoved_na_otazku_dva}")
                    print("Postava: Kurva uz, sa citis co? No pojdme na posledni, nejtezsi, hulibrku.")

                    print("")

                    print("""Postava: TY jeden pindoure, rekni mi, co ma spolecneho
                                VIAGRA a KRESTANSTVI? """)
                    print("( Napis: odpoved: )")
                    odpoved_treti_otazka = input()
                    while odpoved_treti_otazka != "odpoved":
                        print("Zadal jsi neplatny prikaz, zkus to znovu: ")
                        odpoved_treti_otazka = input()
                    odpoved_spravna_treti_otazka = "Zmrtvýchvstání"
                    print("")

                    print(f"Ty: Ma odpovded je: {odpoved_spravna_treti_otazka}.")

                    print("")

                    print("Postava: Vyjebance, buzno, kurvaaaaaa, no to je v pejci...")
                    print("Postava: Vem si tu posranou dyku a vypadni odsad krysoooo!!!")
                    nova_postava.ziskat_exp(700)

                    print("")

                    if any(zbran.jmeno == "Starý meč" for zbran in hracuv_inventar.zbrane):
                        hracuv_inventar.pridat_zbran(zbrane.zdobena_dyka)
                        print(
                            f"Ziskal si silnejsi zbran: {zbrane.zdobena_dyka.jmeno}, vyhazujes slabsi zbran: {zbrane.stary_mec.jmeno}")
                        hracuv_inventar.odebrat_zbran(zbrane.stary_mec)
                    else:
                        print(f"Ziskal si novou zbran: {zbrane.zdobena_dyka.jmeno}")
                        hracuv_inventar.pridat_zbran(zbrane.zdobena_dyka)
                    hracuv_inventar.vypis_inventar()
                    nova_postava.aktualizovat_vlastnosti(hracuv_inventar)
                    print(f"Tvuj zakladni utok se zvetsil na: {nova_postava.utok}")
                    print(f"Tvuj level je: {nova_postava.level}, tve EXP jsou: {nova_postava.exp}.")


                elif vyber_cisla == "4":
                    print(f"Ty: Ma odpoved je: {vyber_cisla}")
                    print("""Postava: Aahahhaah, hlupacku, spravne bylo 3...aAHAHAHH,
                            Kdyz jsem asi prcal jen Marenu, Terezu a Olgu,
                            fena Matylda neni zenska, starej od Olgy neni zenska,
                            a Olgu jsem voprcal sice dvakrat, ale stale to je jen jedna,
                            tak jsem musel mit pouze tri zensky, picko ne? NAVAL MEC!!!""")

                    print("")

                    print(f"Ztracis z inventare svuj: {zbrane.stary_mec.jmeno}. ")
                    nova_postava.utok = nova_postava.utok - 15
                    print(f"Tvuj utok je nyni: {nova_postava.utok}")

                    print("")

                    print("Postava: AHahahah padej chcipacku, papa!!!")
                    print("Odchazis znicenej pryc z chatrce...")
                else:
                    print(f"Ty: Ma odpoved je: {vyber_cisla}")
                    print("""Postava: Aahahhaah, hlupacku, spravne bylo 3...aAHAHAHH,
                                                Kdyz jsem asi prcal jen Marenu, Terezu a Olgu,
                                                fena Matylda neni zenska, starej od Olgy neni zenska,
                                                a Olgu jsem voprcal sice dvakrat, ale stale to je jen jedna,
                                                tak jsem musel mit pouze tri zensky, picko ne? NAVAL MEC!!!""")

                    print("")

                    print(f"Ztracis z inventare svuj: {zbrane.stary_mec.jmeno}. ")
                    nova_postava.utok = nova_postava.utok - zbrane.stary_mec.utok
                    print(f"Tvuj utok je nyni: {nova_postava.utok}")

                    print("")

                    print("Postava: AHahahah padej chcipacku, papa!!!")
                    print("Odchazis znicenej pryc z chatrce...")

            else:
                print("Ty: Nebudu hrat, seru na tebe trosko!")
                print("Postava: Dobry, mrdko, vypadni...!!!)")
                print("Odchazis z chatrce pryc...")

        else:
            print("Postava: Copak, jsi posranej? aahahah")
            print("Ty: Ano pane, posral jsem se, celej.")
            print("Postava: AhahahaAHAH! ")
            print("Postava: Jdi se umejt a vypadni, kundo!")

            print("")

            print("Neni teda nejvlidnejsi, pomyslis si a radsi zhrzen a ponizen odchazis z chatrce pryc...")

            print("")

    else:
        print("Odchazis z chatrce bez jedineho slova radsi pryc.")
        print("Zahadne osobe to je zrejmne uplne putna.")
        print("""Jen ti jeste popreje stastnou cestu, Osoba: "To jsem si myslel, utec sracko !!! AAHAHAHA" """)

else:
    print("Do chatrce jsi se rozhodl nevstoupit a pokracujes v ceste dal.")

print("")

print("Pokracujeme tedy dal..")











