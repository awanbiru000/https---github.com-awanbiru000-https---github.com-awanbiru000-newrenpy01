define larasati = Character("Larasati",color ="#2674f1")
define sriyani = Character("Sriyani",color = "#ffa201")
define rani = Character("Rani",color = "#e374ffff")
define makhluk_1 = Character("Makara",color = "#000000")
define makhluk = Character("???",color = "#000000")

image bg envi mom = im.Scale("envi_mom.jpg",1280,720)

define text_prolog_larasati=[
    "Ibu....Ibu....",
    "Ibu sedang menjahit lagi ?",
    "Kali ini berapa baju bu ?",
    "Ibu sejak dulu suka sekali menjahit ?",
    "Tapi kenapa batik ?",
    "Begitu, Menjahit itu gampang tidak bu ?",
    "Aku mau"
    "coba ini....."
    "coba ini bisa gak....."
    
]


define text_prolog_sriyani=[
    "kenapa sayang ?",
    "Iya sayang",
    "Hanya 2 baju tapi harus selesai hari ini",
    "Iyaa",
    "Dulu orang tua ibu suka sekali menjahit dan ibu belajar darinya, kebetulan saat itu ibu belajar membuat batik",
    "Waktu ibu pertama kali mencoba rasanya sulit tapi semakin banyak mencoba jadi semakin mudah",
    "Kamu mau coba menjahit ?"

]

# larasati sedang pusing cari ide

define text_larasati_kamar=[
    "Hmm… apa ya ?",
    "Aku bingung mau buat yang bagaimana lagi, aku butuh ide",
    "HUAHHH, aku tidak ada ide sama sekali",
    "Padahal aku sedang mencari ide buat baju batik aku",
    "Tapi nggak ada salahnya juga untuk istirahat, siapa tau nemu ide di kafe nanti"
]

# larasati dan rani sedang DM lewat handphone

define text_larasati_dm=[
    "Tidak, memangnya kenapa ?",
    "Ohh yang harganya mahal itu",
    "Mana ada kopi harganya 21 ribu Rani",
    "Kenapa tidak di WA ini aja",
    "Yaudah jam berapa",
    "Oke"
]

define text_rani=[
    "Siang ini kamu kosong gak ?",
    "Aku mau ngajak kamu ke kafe yang kemarin aku kasih tau",
    "ENGGA MAHAL",
    "Dih, yaudah ntar aku tambahin",
    "Selain itu ada yang aku mau kasih tau lagi",
    "Nggak asik ah, enakan langsung ketemu sekalian santai dan minum kopi",
    "Aku sampai sana jam 1",
    "Laras lama juga datangnya",
    "Aku sampai beli kopi karena merasa tidak enak dengan bartendernya",
    "Datang juga kamu",
    "Kenapa lama sekali sih ?",
]

define text_larasati_kafe=[
    "Ah iya",
    "Macet tahu, jam makan siang gini orang-orang pada keluar",
    "Aku mau pesan kopi dulu"
]
screen black_screen():
    frame:
        background "#000000"

#screen mengamati1():
#    frame:
        #background "mengamati"

screen white_screen():
    frame:
        background "#ffffff"