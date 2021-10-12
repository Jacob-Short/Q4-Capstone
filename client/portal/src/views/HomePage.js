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
        <div>
            <h1>Have an Account</h1>
            <a href='/login/'>
            <button>Login</button>
            </a>
            <h2>Dont have an Account?</h2>
            <a href='/signup/'>
            <button>Sign Up</button>
            </a>
        </div>
    )
}