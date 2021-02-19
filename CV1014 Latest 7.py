#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:28:24 2020

@author: xtrology
"""


from tkinter import*
import webbrowser

root = Tk()
root.title("Test CV1014 Code with tkinter ")
root['bg'] = 'pink'

frame1 = LabelFrame(root, padx = 10, pady = 10)
frame1.grid(row = 6, column = 0)
frame2 = LabelFrame(root, padx = 10, pady = 10)
frame2.grid(row = 6, column = 0)
frame3 = LabelFrame(root, padx = 10, pady = 10)
frame3.grid(row = 6, column = 0)
frame4 = LabelFrame(root, padx = 10, pady = 10)
frame4.grid(row = 6, column = 0)

#Frames for genres
frame_action = LabelFrame(root, padx = 10, pady = 10)
frame_action.grid(row = 7, column = 0)
frame_comedy = LabelFrame(root, padx = 10, pady = 10)
frame_comedy.grid(row = 7, column = 0)
frame_horror = LabelFrame(root, padx = 10, pady = 10)
frame_horror.grid(row = 7, column = 0)
frame_romance = LabelFrame(root, padx = 10, pady = 10)
frame_romance.grid(row = 7, column = 0)

#Frames for language
frame_english = LabelFrame(root, padx = 10, pady = 10)
frame_english.grid(row = 7, column = 0)
frame_malay = LabelFrame(root, padx = 10, pady = 10)
frame_malay.grid(row = 7, column = 0)
frame_mandarin = LabelFrame(root, padx = 10, pady = 10)
frame_mandarin.grid(row = 7, column = 0)
frame_tamil = LabelFrame(root, padx = 10, pady = 10)
frame_tamil.grid(row = 7, column = 0)

#FRames for pgRating
frame_PG = LabelFrame(root, padx = 10, pady = 10)
frame_PG.grid(row = 7, column = 0)
frame_PG_13 = LabelFrame(root, padx = 10, pady = 10)
frame_PG_13.grid(row = 7, column = 0)
frame_NC_16 = LabelFrame(root, padx = 10, pady = 10)
frame_NC_16.grid(row = 7, column = 0)
frame_R_18 = LabelFrame(root, padx = 10, pady = 10)
frame_R_18.grid(row = 7, column = 0)

#Dictionaries for storing movies
m1 =	{
  "Name": "Aiden",
  "Genre": "Romance",
  "Language": "English",
  "PG Rating": "PG"
}
m2 =	{
  "Name": "Ava",
  "Genre": "Comedy",
  "Language": "Malay",
  "PG Rating": "PG-13"
}
m3 =	{
  "Name": "Bryann",
  "Genre": "Action",
  "Language": "Tamil",
  "PG Rating": "NC-16"
}
m4 =	{
  "Name": "Bryanna",
  "Genre": "Horror",
  "Language": "Mandarin",
  "PG Rating": "PG"
}
m5 =	{
  "Name": "Christopher",
  "Genre": "Romance",
  "Language": "English",
  "PG Rating": "PG"
}
m6 =	{
  "Name": "Christine",
  "Genre": "Comedy",
  "Language": "Malay",
  "PG Rating": "PG-13"
}
m7 =	{
  "Name": "Desmond",
  "Genre": "Action",
  "Language": "Tamil",
  "PG Rating": "NC-16"
}
m8 =	{
  "Name": "Desdemona",
  "Genre": "Horror",
  "Language": "Mandarin",
  "PG Rating": "R-18"
}
m9 =   {
  "Name": "Ethan",
  "Genre": "Romance",
  "Language": "English",
  "PG Rating": "PG"
}
m10 =  {
  "Name": "Emma",
  "Genre": "Comedy",
  "Language": "Malay",
  "PG Rating": "PG-13"
}
 
m11 =  {
  "Name": "Finn",
  "Genre": "Action",
  "Language": "Tamil",
  "PG Rating": "NC-16"
}
 
m12 =  {
  "Name": "Fiona",
  "Genre": "Horror",
  "Language": "Mandarin",
  "PG Rating": "R-18"
}
m13 =  {
  "Name": "George",
  "Genre": "Romance",
  "Language": "English",
  "PG Rating": "PG"
}
 
m14 = {
  "Name": "Georgia",
  "Genre": "Comedy",
  "Language": "Malay",
  "PG Rating": "PG-13"
}
 
m15 = {
  "Name": "Hugh",
  "Genre": "Action",
  "Language": "Tamil",
  "PG Rating": "NC-16"
}
m16 = {
  "Name": "Hannah",
  "Genre": "Horror",
  "Language": "Mandarin",
  "PG Rating": "R-18"
}
 
m17 = {
  "Name": "Indiana",
  "Genre": "Romance",
  "Language": "English",
  "PG Rating": "PG"
}
 
m18 = {
  "Name": "India",
  "Genre": "Comedy",
  "Language": "Malay",
  "PG Rating": "PG-13"
}
 
m19 = {
  "Name": "Joshua",
  "Genre": "Action",
  "Language": "Tamil",
  "PG Rating": "NC-16"
}
m20 = {
  "Name": "Joanna",
  "Genre": "Horror",
  "Language": "Mandarin",
  "PG Rating": "R-18"
}
 
m21 = {
  "Name": "Kelvin",
  "Genre": "Romance",
  "Language": "English",
  "PG Rating": "PG"
}
 
m22 = {
  "Name": "Katherine",
  "Genre": "Comedy",
  "Language": "Malay",
  "PG Rating": "PG-13"
}
 
m23 =  {
  "Name": "Leo",
  "Genre": "Action",
  "Language": "Tamil",
  "PG Rating": "NC-16"
}
 
m24 = {
  "Name": "Laura",
  "Genre": "Horror",
  "Language": "Mandarin",
  "PG Rating": "R-18"
}

MovieList = {
  "m1" : m1,
  "m2" : m2,
  "m3" : m3,
  "m4" : m4,
  "m5" : m5,
  "m6" : m6,
  "m9" : m9,
  "m10" : m10,
  "m11" : m11,
  "m12" : m12,
  "m13" : m13,
  "m14" : m14,
  "m15" : m15,
  "m16" : m16,
  "m17" : m17,
  "m18" : m18,
  "m19" : m19,
  "m20" : m20,
  "m21" : m21,
  "m22" : m22,
  "m23" : m23,
  "m24" : m24    
}

listOfMovies = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23, m24]


#Disabling Genre Buttons
def disable_genre_buttons():
    button_action.config(state='disabled')
    button_comedy.config(state='disabled')
    button_horror.config(state='disabled')
    button_romance.config(state='disabled')

#Methods to sort movie by genre
#Listbox and scrollbar for action
list_action = Listbox(frame_action, height=4, width=35)
scrolly_action = Scrollbar(frame_action, command = list_action.yview)
list_action.configure(yscrollcommand = scrolly_action.set)
scrollx_action = Scrollbar(frame_action, orient="horizontal", command = list_action.xview)
list_action.configure(xscrollcommand = scrollx_action.set)

listOfActionMovies = []
def sort_movies_Action():
    for num in range(len(listOfMovies)):
         if listOfMovies[num]["Genre"] == "Action":
             listOfActionMovies.append(listOfMovies[num])
    return listOfActionMovies
def print_action_movies():
    ActionMovies = sort_movies_Action()
    myLabel1 = Label(frame_action, text = "\nList Of Action Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in ActionMovies:
        list_action.insert(END, item)
        list_action.grid(row = 12, column = 0)
        scrolly_action.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_action.grid(row = 13, column = 0, sticky=(W,E))
    frame_action.grid()
    disable_genre_buttons()


#listbox and scrollbar for comedy
list_comedy = Listbox(frame_comedy, height=4, width=35)
scrolly_comedy = Scrollbar(frame_comedy, command = list_comedy.yview)
list_comedy.configure(yscrollcommand=scrolly_comedy.set)
scrollx_comedy = Scrollbar(frame_comedy, orient='horizontal', command = list_comedy.xview)
list_comedy.configure(xscrollcommand=scrollx_comedy.set)
    
listOfComedyMovies = []  
def sort_movies_Comedy():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["Genre"] == "Comedy":
            listOfComedyMovies.append(listOfMovies[num])
    return listOfComedyMovies
def print_comedy_movies():
    ComedyMovies = sort_movies_Comedy()
    myLabel1 = Label(frame_comedy, text = "\nList Of Comedy Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in ComedyMovies:
        list_comedy.insert(END, item)
        list_comedy.grid(row = 12, column = 0)
        scrolly_comedy.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_comedy.grid(row = 13, column = 0, sticky=(W,E))
    frame_comedy.grid()
    disable_genre_buttons()


#listbox and scrollbar for horror
list_horror = Listbox(frame_horror, height=4, width=35)
scrolly_horror = Scrollbar(frame_horror, command=list_horror.yview)
list_horror.configure(yscrollcommand=scrolly_horror.set)
scrollx_horror = Scrollbar(frame_horror, orient='horizontal', command = list_horror.xview)
list_horror.configure(xscrollcommand=scrollx_horror.set)  
  
listOfHorrorMovies = []
def sort_movies_Horror():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["Genre"] == "Horror":
            listOfHorrorMovies.append(listOfMovies[num])
    return listOfHorrorMovies
def print_horror_movies():
    HorrorMovies = sort_movies_Horror()
    myLabel1 = Label(frame_horror, text = "\nList Of Horror Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in HorrorMovies:
        list_horror.insert(END, item)
        list_horror.grid(row = 12, column = 0)
        scrolly_horror.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_horror.grid(row = 13, column = 0, sticky=(W,E))
    frame_horror.grid()
    disable_genre_buttons()
    

list_romance = Listbox(frame_romance, height=4, width=35)
scrolly_romance = Scrollbar(frame_romance, command=list_romance.yview)
list_romance.configure(yscrollcommand=scrolly_romance.set)
scrollx_romance = Scrollbar(frame_romance, orient='horizontal', command = list_romance.xview)
list_romance.configure(xscrollcommand=scrollx_romance.set)

listOfRomanceMovies = []
def sort_movies_Romance():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["Genre"] == "Romance":
            listOfRomanceMovies.append(listOfMovies[num])
    return listOfRomanceMovies
def print_romance_movies():
    RomanceMovies = sort_movies_Romance()
    myLabel1 = Label(frame_romance, text = "\nList Of Romance Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in RomanceMovies:
        list_romance.insert(END, item)
        list_romance.grid(row = 12, column = 0)
        scrolly_romance.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_romance.grid(row = 13, column = 0, sticky=(W,E))
    frame_romance.grid()
    disable_genre_buttons()

#Disabling language buttons
def disable_language_buttons():
    button_english.config(state='disabled')
    button_malay.config(state='disabled')
    button_mandarin.config(state='disabled')
    button_tamil.config(state='disabled')  

#Movies sorted by language
list_english = Listbox(frame_english, height=4, width=35)
scrolly_english = Scrollbar(frame_english, command=list_english.yview)
list_english.configure(yscrollcommand=scrolly_english.set)
scrollx_english = Scrollbar(frame_english, orient='horizontal', command = list_english.xview)
list_english.configure(xscrollcommand=scrollx_english.set) 
 
   
listOfEnglishMovies = []
def sort_movies_English():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["Language"] == "English":
            listOfEnglishMovies.append(listOfMovies[num])
    return listOfEnglishMovies
def print_english_movies():
    EnglishMovies = sort_movies_English()
    myLabel1 = Label(frame_english, text = "\nList Of English Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in EnglishMovies:
        list_english.insert(END, item)
        list_english.grid(row = 12, column = 0)
        scrolly_english.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_english.grid(row = 13, column = 0, sticky=(W,E))
    frame_english.grid()
    disable_language_buttons()
    

list_malay = Listbox(frame_malay, height=4, width=35)
scrolly_malay = Scrollbar(frame_malay, command=list_malay.yview)
list_malay.configure(yscrollcommand=scrolly_malay.set)
scrollx_malay = Scrollbar(frame_malay, orient='horizontal', command = list_malay.xview)
list_malay.configure(xscrollcommand=scrollx_malay.set)

listOfMalayMovies = []
def sort_movies_Malay():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["Language"] == "Malay":
            listOfMalayMovies.append(listOfMovies[num])
    return listOfMalayMovies
def print_malay_movies():
    MalayMovies = sort_movies_Malay()
    myLabel1 = Label(frame_malay, text = "\nList Of Malay Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in MalayMovies:
        list_malay.insert(END, item)
        list_malay.grid(row = 12, column = 0)
        scrolly_malay.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_malay.grid(row = 13, column = 0, sticky=(W,E))
    frame_malay.grid()
    disable_language_buttons()


list_mandarin = Listbox(frame_mandarin, height=4, width=35)
scrolly_mandarin = Scrollbar(frame_mandarin, command=list_mandarin.yview)
list_mandarin.configure(yscrollcommand=scrolly_malay.set)
scrollx_mandarin = Scrollbar(frame_mandarin, orient='horizontal', command = list_mandarin.xview)
list_mandarin.configure(xscrollcommand=scrollx_mandarin.set)
    
listOfMandarinMovies = []
def sort_movies_Mandarin():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["Language"] == "Mandarin":
            listOfMandarinMovies.append(listOfMovies[num])
    return listOfMandarinMovies
def print_mandarin_movies():
    MandarinMovies = sort_movies_Mandarin()
    myLabel1 = Label(frame_mandarin, text = "\nList Of Mandarin Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in MandarinMovies:
        list_mandarin.insert(END, item)
        list_mandarin.grid(row = 12, column = 0)
        scrolly_mandarin.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_mandarin.grid(row = 13, column = 0, sticky=(W,E))
    frame_mandarin.grid()
    disable_language_buttons()

    
list_tamil = Listbox(frame_tamil, height=4, width=35)
scrolly_tamil = Scrollbar(frame_tamil, command=list_tamil.yview)
list_tamil.configure(yscrollcommand=scrolly_tamil.set)
scrollx_tamil = Scrollbar(frame_tamil, orient='horizontal', command = list_tamil.xview)
list_tamil.configure(xscrollcommand=scrollx_tamil.set)
    
listOfTamilMovies = []
def sort_movies_Tamil():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["Language"] == "Tamil":
            listOfTamilMovies.append(listOfMovies[num])
    return listOfTamilMovies
def print_tamil_movies():
    TamilMovies = sort_movies_Tamil()
    myLabel1 = Label(frame_tamil, text = "\nList Of Tamil Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in TamilMovies:
        list_tamil.insert(END, item)
        list_tamil.grid(row = 12, column = 0)
        scrolly_tamil.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_tamil.grid(row = 13, column = 0, sticky=(W,E))
    frame_tamil.grid()
    disable_language_buttons()   

#Disable pgRating Buttons
def disable_pgRating_buttons():
    button_pg.config(state='disabled')
    button_pg_13.config(state='disabled')
    button_nc_16.config(state='disabled')
    button_r_18.config(state='disabled')

#Movies sorted by pgRating 
list_PG = Listbox(frame_PG, height=4, width=35)
scrolly_PG = Scrollbar(frame_PG, command=list_PG.yview)
list_PG.configure(yscrollcommand=scrolly_PG.set)
scrollx_PG = Scrollbar(frame_PG, orient='horizontal', command = list_PG.xview)
list_PG.configure(xscrollcommand=scrollx_PG.set)

listOfPGMovies = []
def sort_movies_PG():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["PG Rating"] == "PG":
            listOfPGMovies.append(listOfMovies[num])
    return listOfPGMovies
def print_PG_movies():
    PGMovies = sort_movies_PG()
    myLabel1 = Label(frame_PG, text = "\nList Of PG Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in PGMovies:
        list_PG.insert(END, item)
        list_PG.grid(row = 12, column = 0)
        scrolly_PG.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_PG.grid(row = 13, column = 0, sticky=(W,E))
    frame_PG.grid()
    disable_pgRating_buttons()


list_PG_13 = Listbox(frame_PG_13, height=4, width=35)
scrolly_PG_13 = Scrollbar(frame_PG_13, command=list_PG_13.yview)
list_PG_13.configure(yscrollcommand=scrolly_PG_13.set)
scrollx_PG_13 = Scrollbar(frame_PG_13, orient='horizontal', command = list_PG_13.xview)
list_PG_13.configure(xscrollcommand=scrollx_PG_13.set)    
listOfPG_13_Movies = []
def sort_movies_PG_13():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["PG Rating"] == "PG-13":
            listOfPG_13_Movies.append(listOfMovies[num])
    return listOfPG_13_Movies
def print_PG_13_movies():
    PG_13_Movies = sort_movies_PG_13()
    myLabel1 = Label(frame_PG_13, text = "\nList Of PG-13 Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in PG_13_Movies:
        list_PG_13.insert(END, item)
        list_PG_13.grid(row = 12, column = 0)
        scrolly_PG_13.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_PG_13.grid(row = 13, column = 0, sticky=(W,E))
    frame_PG_13.grid()
    disable_pgRating_buttons()


list_NC_16 = Listbox(frame_NC_16, height=4, width=35)
scrolly_NC_16 = Scrollbar(frame_NC_16, command=list_NC_16.yview)
list_NC_16.configure(yscrollcommand=scrolly_NC_16.set)
scrollx_NC_16 = Scrollbar(frame_NC_16, orient='horizontal', command = list_NC_16.xview)
list_NC_16.configure(xscrollcommand=scrollx_NC_16.set)    
listOfNC_16_Movies = []
def sort_movies_NC_16():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["PG Rating"] == "NC-16":
            listOfNC_16_Movies.append(listOfMovies[num])
    return listOfNC_16_Movies
def print_NC_16_movies():
    NC_16_Movies = sort_movies_NC_16()
    myLabel1 = Label(frame_NC_16, text = "\nList Of NC-16 Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in NC_16_Movies:
        list_NC_16.insert(END, item)
        list_NC_16.grid(row = 12, column = 0)
        scrolly_NC_16.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_NC_16.grid(row = 13, column = 0, sticky=(W,E))
    frame_NC_16.grid()
    disable_pgRating_buttons()


list_R_18 = Listbox(frame_R_18, height=4, width=35)
scrolly_R_18 = Scrollbar(frame_R_18, command=list_R_18.yview)
list_R_18.configure(yscrollcommand=scrolly_R_18.set)
scrollx_R_18 = Scrollbar(frame_R_18, orient='horizontal', command = list_R_18.xview)
list_R_18.configure(xscrollcommand=scrollx_R_18.set)
listOfR_18_Movies = []
def sort_movies_R_18():
    for num in range(len(listOfMovies)):
        if listOfMovies[num]["PG Rating"] == "R-18":
            listOfR_18_Movies.append(listOfMovies[num])
    return listOfR_18_Movies
def print_R_18_movies():
    R_18_Movies = sort_movies_R_18()
    myLabel1 = Label(frame_R_18, text = "\nList Of R-18 Movies:")
    myLabel1.grid(row = 11, column = 0)
    for item in R_18_Movies:
        list_R_18.insert(END, item)
        list_R_18.grid(row = 12, column = 0)
        scrolly_R_18.grid(row = 12, column = 1, sticky=(N,S))
        scrollx_R_18.grid(row = 13, column = 0, sticky=(W,E))
    frame_R_18.grid()
    disable_pgRating_buttons()

#Asking for User Input
def ask_for_user_input():
    Asking_User_Input = Label(root, bg= 'pink', text = "What do you wish to search?\n")
    Asking_User_Input.grid(row = 0, column = 0)
    button_name.grid(row = 1, column = 0)
    button_genre.grid(row = 2, column = 0)
    button_language.grid(row = 3, column = 0)
    button_pgRating.grid(row = 4, column = 0)
    button_refresh.grid(row = 0, column = 1)
    button_add_movie.grid(row = 1, column = 1, padx=5, pady=10)
    movie_links_label = Label(root, bg= 'pink', text = "Click on links below for movie timings:")
    movie_links_label.grid(row = 2, column = 1)
    
    link1.grid(row = 3, column = 1)
    link2.grid(row = 4, column = 1)

#Searching for name    
def disable_name_button():
        button_genre.config(state='disabled')
        button_language.config(state='disabled')
        button_pgRating.config(state='disabled')

def get_movie_name():
    frame1.grid()
    Label5 = Label(frame1, text = "Enter Name Of Movie: ")
    Label5.grid(row = 5, column = 0)
    e.grid(row = 6, column = 0)
    button_submit.grid(row = 7, column = 0)
    disable_name_button()
        
def submit_movie_name():
    search_for_name = e.get()
    string1 = search_for_name.lower()
    converted_movie = string1.capitalize()
    for num in range(len(listOfMovies)):
         if listOfMovies[num]["Name"] == converted_movie:
             myLabel3 = Label(frame1, text = "\n")
             myLabel3.grid(row = 8, column = 0)
             myLabel4 = Label(frame1, text = str(listOfMovies[num]))
             myLabel4.grid(row = 9, column = 0, columnspan = 1)
    e.delete(0, END)
    #button_submit.config(state = 'disabled')

#Method for adding a movie
def get_new_movie():
    name_label = Label(root, bg='pink', text = "Name: ")
    genre_label = Label(root, bg='pink', text = "Genre: ")
    language_label = Label(root, bg='pink', text = "Language: ")
    pgRating_label = Label(root, bg='pink', text = "PG Rating: ")
    name_label.grid(row = 1, column = 2)
    genre_label.grid(row = 2, column = 2)
    language_label.grid(row = 3, column = 2)
    pgRating_label.grid(row = 4, column = 2)
    
    e_name.grid(row = 1, column = 3)
    e_genre.grid(row = 2, column = 3)
    e_language.grid(row = 3, column = 3)
    e_pgRating.grid(row = 4, column = 3)
    button_submit2.grid( row = 5, column = 3)

    
def add_movie():
    num = 1
    dictionary_num = str(24 + int(num))
    dictionary_name = "m" + dictionary_num
    new_dictionary_name = {}
    get_movie_name = e_name.get()
    if get_movie_name != "":
        get_movie_genre = e_genre.get()
        get_movie_language = e_language.get()
        get_movie_pgRating = e_pgRating.get()
    
        new_dictionary_name["Name"] = get_movie_name  
        new_dictionary_name["Genre"] = get_movie_genre  
        new_dictionary_name["Language"] = get_movie_language
        new_dictionary_name["PG Rating"] = get_movie_pgRating
    
        num + 1
        MovieList.update(new_dictionary_name)
        listOfMovies.append(new_dictionary_name)
    
    e_name.delete(0, END)
    e_genre.delete(0, END)
    e_language.delete(0, END)
    e_pgRating.delete(0, END)
    print(listOfMovies) 

#Genre button method
def disable_genre_button():
        button_name.config(state='disabled')
        button_language.config(state='disabled')
        button_pgRating.config(state='disabled')

def search_for_genre():
    frame2.grid()
    choose_genre = Label(frame2, text = "\nChoose a genre:\n")
    choose_genre.grid(row = 6, column = 0)
    button_action.grid(row = 7, column = 0)
    button_comedy.grid(row = 8, column = 0)
    button_horror.grid(row = 9, column = 0)
    button_romance.grid(row = 10, column = 0)
    disable_genre_button()

#Language Button Method
def disable_language_button():
        button_name.config(state='disabled')
        button_genre.config(state='disabled')
        button_pgRating.config(state='disabled')

def search_for_language():
    frame3.grid()
    choose_language = Label(frame3, text ="\nChoose a language:\n")
    choose_language.grid(row = 6, column = 0)
    button_english.grid(row = 7, column = 0)
    button_malay.grid(row = 8, column = 0)
    button_mandarin.grid(row = 9, column = 0)
    button_tamil.grid(row = 10, column = 0)
    disable_language_button()

#pgRating Button Method
def disable_pgRating_button():
        button_name.config(state='disabled')
        button_genre.config(state='disabled')
        button_language.config(state='disabled')
def search_for_pgRating():
    frame4.grid()
    choose_pgRating = Label(frame4, text ="\nChoose a PG Rating:\n")
    choose_pgRating.grid(row = 6, column = 0)
    button_pg.grid(row = 7, column = 0)
    button_pg_13.grid(row = 8, column = 0)
    button_nc_16.grid(row = 9, column = 0)
    button_r_18.grid(row = 10, column = 0)
    disable_pgRating_button()

#Refresh button method
def refresh_method():
    frame1.grid_forget()
    frame2.grid_forget()
    frame3.grid_forget()
    frame4.grid_forget()
    
    frame_action.grid_remove()
    frame_comedy.grid_remove()
    frame_horror.grid_remove()
    frame_romance.grid_remove()
    
    frame_english.grid_remove()
    frame_malay.grid_remove()
    frame_mandarin.grid_remove()
    frame_tamil.grid_remove()
    
    frame_PG.grid_remove()
    frame_PG_13.grid_remove()
    frame_NC_16.grid_remove()
    frame_R_18.grid_remove()

    button_name.config(state='normal')
    button_genre.config(state='normal')
    button_language.config(state='normal')
    button_pgRating.config(state='normal')
    
    button_action.config(state='normal')
    button_comedy.config(state='normal')
    button_horror.config(state='normal')
    button_romance.config(state='normal')
    
    button_english.config(state='normal')
    button_malay.config(state='normal')
    button_mandarin.config(state='normal')
    button_tamil.config(state='normal')
    
    button_pg.config(state='normal')
    button_pg_13.config(state='normal')
    button_nc_16.config(state='normal')
    button_r_18.config(state='normal')
    
#Calling hyperlink function
def callback(url):
    webbrowser.open_new(url)
    

#Buttons 
button_name = Button(root, text = "(A) Name", command = get_movie_name)
button_genre = Button(root, text = "(B) Genre", command = search_for_genre)
button_language = Button(root, text = "(C) Language", command = search_for_language)
button_pgRating = Button(root, text = "(D) PG Rating", command = search_for_pgRating)

#Command Buttons
button_submit = Button(frame1, text = "Submit", bg='powder blue', command = submit_movie_name)
button_submit2 = Button(root, text = "Submit", bg='powder blue', command = add_movie)
button_refresh = Button(root, text = "Refresh", command = refresh_method)
button_quit = Button (root, text = "Exit")

#Buttons for genre
button_action = Button(frame2, text = "(A) Action", command = print_action_movies)
button_comedy = Button(frame2, text = "(B) Comedy", command = print_comedy_movies)
button_horror = Button(frame2, text = "(C) Horror", command = print_horror_movies)
button_romance = Button(frame2, text = "(D) Romance", command = print_romance_movies)

#Buttons for language
button_english = Button(frame3, text = "(A) English", command = print_english_movies)
button_malay = Button(frame3, text = "(B) Malay", command = print_malay_movies)
button_mandarin = Button(frame3, text = "(C) Mandarin", command = print_mandarin_movies)
button_tamil = Button(frame3, text = "(D) Tamil", command = print_tamil_movies)

#Buttons for pgRating
button_pg = Button(frame4, text = "(A) PG", command = print_PG_movies)
button_pg_13 = Button(frame4, text = "(B) PG-13", command = print_PG_13_movies)
button_nc_16 = Button(frame4, text = "(C) NC-16", command = print_NC_16_movies)
button_r_18 = Button(frame4, text = "(D) R-18", command = print_R_18_movies)

#Methods to sort by names
e = Entry(frame1, width = 20, borderwidth = 10) 


#Buttons and entry for adding movies
button_add_movie = Button(root, text="Add a Movie", bg="#A0A0A0", fg="dark blue", command = get_new_movie)
e_name = Entry(root, width = 20, borderwidth = 10)
e_genre = Entry(root, width = 20, borderwidth = 10)
e_language = Entry(root, width = 20, borderwidth = 10)
e_pgRating = Entry(root, width = 20, borderwidth = 10)

#labels for links
link1 = Label(root, text="Golden Village", bg='pink', fg="blue", cursor="hand2")
link1.bind("<Button-1>", lambda e: callback("https://www.gv.com.sg/GVCinemas"))

link2 = Label(root, text="Shaw Theatres", bg='pink', fg="blue", cursor="hand2")
link2.bind("<Button-1>", lambda e: callback("https://www.shaw.sg"))

#MainLoop
ask_for_user_input()

root.mainloop()








