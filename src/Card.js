import React from "react";
import "./App.css";
import star1 from "./images/blank star.png";
import star2 from "./images/yellow star.png";


export default function Card(props) {
    
    const [contact, setContact] = React.useState({
        id: props.item.id,
        title: props.item.title,
        author: props.item.author,
        chapter: props.item.chapter,
        img: props.item.img,
        link: props.item.link,
        isFavourite: props.item.isFavourite,
        isCompleted: props.item.isCompleted
      })
      
    
    let starIcon = contact.isFavourite ? star2 : star1
    
    function toggleFavourite() {
        setContact((prevContact) => ({
          ...prevContact,
          isFavourite: !prevContact.isFavourite
        }));
      }
    
    return (
        <main>
            <article className="card">
                <img src ={props.item.img} className="card--image" />
                <div className="card--info">
                
                    <img 
                        src={starIcon} 
                        className="card--favourite"
                        onClick={toggleFavourite}
                    />
                    <h2 className="card--title">
                        {props.item.title} 
                    </h2>
                    <p className="card--contact">Chapter {props.item.chapter}</p>
                    <a className="card--contact" href ={props.item.link}>Link</a>
                </div>
                
            </article>
        </main>
    )
}
