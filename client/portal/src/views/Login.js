import React, { useState, useEffect, Fragment } from 'react';

export default function Login(props) {

    const URL = 'http://localhost:8000/login/'
    const [user, setUser] = useState([{}]);

    const HEADERS = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
    }

    useEffect(() => {
        fetch(URL, {
            HEADERS
        }).then(res => res.json()).then(data => setUser(data))
    }, [])

    console.log(user)




    return (
        <Fragment>
            <h1>Login</h1>
        </Fragment>
    )
}