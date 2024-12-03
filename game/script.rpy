style screentext:
    color "#f29c2cff"
    size 16
# The game starts here.

label start:
    show screen black_screen
    with dissolve
    pause 1.0
    hide screen black_screen
    with dissolve
    stop music fadeout 1.3
    jump prolog_pertama


label prolog_pertama:
    scene envi_mom
    show larasati_kecil at left
    with fade
    larasati "[text_prolog_larasati[0]]"
    show sriyani_muda at right
    with dissolve
    sriyani "[text_prolog_sriyani[0]]"
    larasati "[text_prolog_larasati[1]]"
    sriyani "[text_prolog_sriyani[1]]"
    larasati "[text_prolog_larasati[2]]"
    sriyani "[text_prolog_sriyani[2]]"
    larasati "[text_prolog_larasati[3]]"
    sriyani "[text_prolog_sriyani[3]]"
    larasati "[text_prolog_larasati[4]]"
    sriyani "[text_prolog_sriyani[4]]"
    larasati "[text_prolog_larasati[5]]"
    sriyani "[text_prolog_sriyani[5]]"
    jump penasaran_1

label penasaran_1:
    scene envi_mom
    play sound "SFX/Kain.mp3" fadeout 1.3
    show mengamati at center
    play sound "SFX/Kain2.mp3" fadeout 1.3
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide mengamati

    show sriyani_muda at right
    with dissolve
    show larasati_kecil at left
    sriyani "[text_prolog_sriyani[6]]"

    scene envi_mom
    show berpikir at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide berpikir

    show larasati_kecil at left
    with dissolve
    show sriyani_muda at right
    larasati "[text_prolog_larasati[6]]"

    # This ends the game.
    hide larasati_kecil
    hide sriyani_muda
    jump kamar_larasati_1


label kamar_larasati_1:
    scene kamar_larasati
    show mencobaa at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide mencobaa
    show mencoba at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide mencoba

    show larasati_sma at left
    with dissolve

    larasati "[text_larasati_kamar[0]]"
    larasati "[text_larasati_kamar[1]]"

    scene kamar_larasati
    show kebingungan at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide kebingungan

    show larasati_sma at left
    larasati "[text_larasati_kamar[2]]"

    scene kamar_larasati
    show notif_pesan at center
    play sound "SFX/Notif2.mp3"
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide notif_pesan
    jump dm_dari_rani

label dm_dari_rani:
    scene kamar_larasati
    show phone at center
    with dissolve
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[0]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[0]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[1]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[1]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[2]]"
    play sound "audio/SFX/typing4.mp3" fadeout 1.5
    larasati "[text_larasati_dm[2]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[3]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[4]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[3]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[5]]"
    play sound "audio/SFX/typing2.mp3" fadeout 0.6
    larasati "[text_larasati_dm[4]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[6]]"
    play sound "audio/SFX/typing3.mp3" fadeout 0.7
    larasati "[text_larasati_dm[5]]"

    hide phone
    with dissolve
    jump kamar_larasati_2

label kamar_larasati_2:
    scene kamar_larasati
    show terdiam at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide terdiam

    show larasati_sma at center
    with dissolve

    larasati "[text_larasati_kamar[3]]"
    larasati "[text_larasati_kamar[4]]"
    jump dikafe_3


label dikafe_3:
    scene cafe
    show menunggu at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide menunggu

    scene cafe
    show rani_outfit at center
    with dissolve

    rani "[text_rani[7]]"
    rani "[text_rani[8]]"

    hide rani_outfit
    with dissolve

    scene cafe
    show ketemuan at center
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide ketemuan

    show rani_outfit at right
    with dissolve

    rani "[text_rani[9]]"

    show larasati_outfit at left
    with dissolve

    larasati "[text_larasati_kafe[0]]"
    rani "[text_rani[10]]"
    larasati "[text_larasati_kafe[1]]"
    larasati "[text_larasati_kafe[2]]"

    scene cafe
    show screen white_screen
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide screen white_screen
    scene cafe
    show screen black_screen
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide screen black_screen
    jump dunia_lain

label dunia_lain:
    show dimensi
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide dimensi
    jump story_parang

label story_parang:
    scene hutan_parang
    show dimensi_1
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide dimensi_1

    scene hutan_parang
    with dissolve
    larasati "[larasati_story_2[0]]"

    scene hutan_parang
    show terbangun
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide terbangun
    show mengingat
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide mengingat

    show larasati_outfit at center
    with dissolve

    larasati "[larasati_story_2[1]]"
    larasati "[larasati_story_2[2]]"
    larasati "[larasati_story_2[3]]"
    larasati "[larasati_story_2[4]]"
    larasati "[larasati_story_2[5]]"
    scene hutan_parang
    show tenang
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide tenang
    show melihat
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide melihat

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[6]]"
    larasati "[larasati_story_2[7]]"
    larasati "[larasati_story_2[8]]"
    larasati "[larasati_story_2[9]]"
    larasati "[larasati_story_2[10]]"
    larasati "[larasati_story_2[11]]"

    scene hutan_parang
    show keliling
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide keliling

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[12]]"
    larasati "[larasati_story_2[13]]"
    larasati "[larasati_story_2[14]]"
    larasati "[larasati_story_2[15]]"
    larasati "[larasati_story_2[16]]"
    larasati "[larasati_story_2[17]]"
    larasati "[larasati_story_2[18]]"

    scene hutan_parang
    show keliling_1
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide keliling_1
    show keliling_2
    with dissolve
    $renpy.pause(11.0, hard=True)
    hide keliling_2

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[19]]"
    larasati "[larasati_story_2[20]]"

    scene hutan_parang
    show mencari
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide mencari

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[21]]"

    scene hutan_parang
    show pikiran
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide pikiran

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[22]]"
    scene hutan_parang
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    scene hutan_parang
    show larasati_outfit at right
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    with dissolve

    scene hutan_parang
    show tinggal
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide tinggal
    show melihat_1
    with dissolve
    $renpy.pause(7.0, hard=True)
    hide melihat_1

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[23]]"
    show misterius at right:
        zoom 1.74
        xpos 1279 ypos 524
    with dissolve
    larasati "[larasati_story_2[24]]"
    larasati "[larasati_story_2[25]]"

    scene hutan_parang
    show waspada
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide waspada
    show waspada_1
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide waspada_1

    show larasati_outfit at left
    with dissolve
    scene hutan_parang
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    scene hutan_parang
    show larasati_outfit_1 at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide misterius
    with dissolve
    scene hutan_parang
    show larasati_outfit at center
    with dissolve
    hide larasati_outfit
    with dissolve

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[26]]"

    show makara at right
    with dissolve
    makhluk "[suara_misterius[0]]"
    larasati "[larasati_story_2[27]]"
    scene hutan_parang
    show terkaget
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide terkaget

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[28]]"
    scene hutan_parang
    show penasaran
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide penasaran
    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[29]]"
    show makara at right
    with dissolve
    makhluk "[suara_misterius[1]]"
    scene hutan_parang
    show tenang_1
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide tenang_1
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    show larasati_outfit at left
    makhluk "[suara_misterius[2]]"
    makhluk "[suara_misterius[3]]"
    makhluk "[suara_misterius[4]]"
    larasati "[larasati_story_2[30]]"
    larasati "[larasati_story_2[31]]"
    makhluk "[suara_misterius[5]]"
    scene hutan_parang
    show bicara
    with dissolve
    $renpy.pause(9.0, hard=True)
    hide bicara
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk "[suara_misterius[6]]"
    larasati "[larasati_story_2[32]]"
    larasati "[larasati_story_2[33]]"
    makhluk "[suara_misterius[7]]"
    larasati "[larasati_story_2[34]]"
    makhluk "[suara_misterius[8]]"
    larasati "[larasati_story_2[35]]"
    makhluk_1 "[text_makara[0]]"
    makhluk_1 "[text_makara[1]]"
    larasati "[larasati_story_2[36]]"
    larasati "[larasati_story_2[37]]"

    scene hutan_parang
    show notis
    with dissolve
    $renpy.pause(10.0, hard=True)
    hide notis
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[2]]"
    makhluk_1 "[text_makara[3]]"
    larasati "[larasati_story_2[38]]"
    larasati "[larasati_story_2[39]]"
    makhluk_1 "[text_makara[4]]"
    makhluk_1 "[text_makara[5]]"
    larasati "[larasati_story_2[40]]"
    makhluk_1 "[text_makara[6]]"
    makhluk_1 "[text_makara[7]]"
    makhluk_1 "[text_makara[8]]"
    makhluk_1 "[text_makara[9]]"
    scene hutan_parang
    show menjelaskan
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide menjelaskan
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[10]]"
    larasati "[larasati_story_2[41]]"
    larasati "[larasati_story_2[42]]"
    makhluk_1 "[text_makara[11]]"
    makhluk_1 "[text_makara[12]]"
    makhluk_1 "[text_makara[13]]"
    larasati "[larasati_story_2[43]]"
    makhluk_1 "[text_makara[14]]"

    scene hutan_parang
    show mencari_1
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide mencari_1
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[44]]"
    larasati "[larasati_story_2[45]]"
    makhluk_1 "[text_makara[15]]"
    larasati "[larasati_story_2[46]]"
    makhluk_1 "[text_makara[16]]"
    scene hutan_parang
    show senang
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide senang
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[17]]"
    makhluk_1 "[text_makara[18]]"
    larasati "[larasati_story_2[47]]"
    scene hutan_parang
    show keliling_3
    with dissolve
    $renpy.pause(12.0, hard=True)
    hide keliling_3

    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[48]]"
    scene hutan_parang
    show tersenyum
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide tersenyum
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[19]]"
    makhluk_1 "[text_makara[20]]"
    hide makara
    show makara1 at right
    with dissolve
    hide makara1
    hide larasati_outfit
    scene hutan_parang
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    scene hutan_parang
    show larasati_outfit at right
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    with dissolve

    scene hutan_parang
    show berjalan
    with dissolve
    $renpy.pause(7.0, hard=True)
    hide berjalan

    scene hutan_parang
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[21]]"
    larasati "[larasati_story_2[49]]"
    makhluk_1 "[text_makara[22]]"
    larasati "[larasati_story_2[50]]"
    larasati "[larasati_story_2[51]]"
    makhluk_1 "[text_makara[23]]"
    larasati "[larasati_story_2[52]]"
    larasati "[larasati_story_2[53]]"
    larasati "[larasati_story_2[54]]"
    larasati "[larasati_story_2[55]]"
    larasati "[larasati_story_2[56]]"
    scene hutan_parang
    show menjelaskan_1
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide menjelaskan_1
    show memahami
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide memahami

    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[24]]"
    makhluk_1 "[text_makara[25]]"
    makhluk_1 "[text_makara[26]]"
    larasati "[larasati_story_2[57]]"
    makhluk_1 "[text_makara[27]]"
    makhluk_1 "[text_makara[28]]"
    scene hutan_parang
    show mengepakkan
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide mengepakkan
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[58]]"
    larasati "[larasati_story_2[59]]"
    makhluk_1 "[text_makara[29]]"
    larasati "[larasati_story_2[60]]"
    scene hutan_parang
    show melanjutkan
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide melanjutkan
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[61]]"
    larasati "[larasati_story_2[62]]"
    makhluk_1 "[text_makara[30]]"
    scene hutan_parang
    show melihat_2
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide melihat_2
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[31]]"
    scene hutan_parang
    show melompat
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide melompat
    show makara at right
    with dissolve
    hide makara
    show makara1 at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[32]]"
    hide makara1
    scene hutan_parang
    show larasati_outfit at left
    with dissolve
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    scene hutan_parang
    show larasati_outfit at right
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    with dissolve
    scene hutan_parang
    show melompat_1
    with dissolve
    $renpy.pause(9.0, hard=True)
    hide melompat_1
    scene hutan_parang
    show larasati_outfit at left
    with dissolve
    hide larasati_outfit
    with dissolve
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    larasati "[larasati_story_2[63]]"
    show makara at right
    with dissolve
    makhluk_1 "[text_makara[33]]"
    makhluk_1 "[text_makara[34]]"
    makhluk_1 "[text_makara[35]]"
    scene hutan_parang
    show menyadari
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide menyadari

    show larasati_outfit at center
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[64]]"
    scene hutan_parang
    show mengikuti
    with dissolve
    $renpy.pause(13.0, hard=True)
    hide mengikuti
    show melewati
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide melewati
    scene hutan_parang
    show larasati_outfit at right
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit

    scene hutan_parang
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[65]]"
    larasati "[larasati_story_2[66]]"
    makhluk_1 "[text_makara[36]]"
    makhluk_1 "[text_makara[37]]"
    makhluk_1 "[text_makara[38]]"
    makhluk_1 "[text_makara[39]]"
    scene hutan_parang
    show melihat_3
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide melihat_3
    scene hutan_parang
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[67]]"
    larasati "[larasati_story_2[68]]"
    larasati "[larasati_story_2[69]]"
    makhluk_1 "[text_makara[40]]"
    makhluk_1 "[text_makara[41]]"
    scene hutan_parang
    show makara1 at right
    with dissolve
    hide makara1
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    scene hutan_parang
    show larasati_outfit at right
    with dissolve 
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    scene hutan_parang
    show melanjutkan_1
    with dissolve
    $renpy.pause(9.0, hard=True)
    hide melanjutkan_1
    show keberanian
    with dissolve
    $renpy.pause(7.0, hard=True)
    hide keberanian

    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    makhluk_1 "[text_makara[42]]"
    makhluk_1 "[text_makara[43]]"
    scene hutan_parang
    show memahami_1
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide memahami_1
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[70]]"
    larasati "[larasati_story_2[71]]"
    larasati "[larasati_story_2[72]]"
    scene hutan_parang
    show senang_1
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide senang_1
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    makhluk_1 "[text_makara[44]]"
    scene hutan_parang
    show mengerti
    with dissolve
    $renpy.pause(10.0, hard=True)
    hide mengerti

    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[73]]"
    larasati "[larasati_story_2[74]]"
    makhluk_1 "[text_makara[45]]"
    hide makara
    scene hutan_parang
    show makara1 at right
    with dissolve
    $renpy.pause(1.0, hard=True)
    hide makara1
    scene hutan_parang
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    scene hutan_parang
    show larasati_outfit at right
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    scene hutan_parang
    show setelah
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide setelah
    scene bukit
    with dissolve
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[46]]"
    makhluk_1 "[text_makara[47]]"
    scene bukit
    show rebahan
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide rebahan
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[75]]"
    larasati "[larasati_story_2[76]]"
    makhluk_1 "[text_makara[48]]"
    scene bukit
    show rebahan_1
    with dissolve
    $renpy.pause(11.0, hard=True)
    hide rebahan_1
    show menggambar
    with dissolve
    $renpy.pause(12.0, hard=True)
    hide menggambar
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[77]]"
    larasati "[larasati_story_2[78]]"
    larasati "[larasati_story_2[79]]"



    return
