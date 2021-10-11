import React, { useState, useEffect } from 'react';

export default function HomePage(props) {

    const URL = 'http://localhost:8000/games/games/'
    const [games, setGames] = useState([{}]);

    const HEADERS = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
    }

    useEffect(() => {
        fetch(URL, {
            HEADERS           
        }).then(res => res.json()).then(data => setGames(data))
    }, [])

    console.log(games)

    return (
        <div >
            {games.map(game =>(
                    <div className="card text-white bg-info mb-3" style={{"max-width": "18rem;"}}>
                    <div className="card-header">Game: {game.name}</div>
                    <div className="card-body">
                      <h5 className="card-title">Alt name: {game.slug}</h5>
                      <h6 className="card-title">Rating: {game.rating}</h6>
                      <h6 className="card-title">Platform: {game.platform}</h6>
                      <h6 className="card-title">Release Date: {game.released_at}</h6>
                      <h6 className="card-title">IMG: {game.image_background}</h6>
                      <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      </div>
                    </div>
                 ))}

        </div>
    )
}