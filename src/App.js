import React from "react"
import "./App.css"
import Card from "./Card.js"
import {data} from "./Data.js"


export default function App() {
 
    const cards = data.map(item => {
        return(
            <Card 
            item = {item}
            />
        )    
    })
    const [showFavourites, setShowFavourites] = React.useState(false)
    const favourites = data.filter(item => item.isFavourite === true)
    .map(item => 
        <Card 
            item={item} 
            />)

   const toggleFavourites = () => {
    setShowFavourites(!showFavourites)
    console.log(favourites)
    return favourites
  }   

    
    
    return(
        <div>
            <input     
                placeholder = "Search"
            />
            <button
                className = "button--fav"
                onClick = {toggleFavourites}
            >{showFavourites ? "Show All" : "Favourites"}
            </button>
            
            <main className="main--body">
                
                {showFavourites ? favourites : cards}
            
            </main>
            
        </div>
    )    
}

