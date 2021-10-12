import React, { useState, useEffect, Fragment } from 'react';

export default function Reviews(props) {

    const URL = 'http://localhost:8000/reviews/'
    const [reviews, setReviews] = useState([{}]);

    const HEADERS = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
    }

    useEffect(() => {
        fetch(URL, {
            HEADERS
        }).then(res => res.json()).then(data => setReviews(data))
    }, [])

    console.log(reviews)




    return (
        <Fragment>
            {
                reviews.map(review => (
                    <Fragment>
                        <h1>{review.name}</h1>
                        <h1>{review.age}</h1>
                        <h1>{review.school}</h1>
                        <h1>{review.description}</h1>
                    </Fragment>
                ))
            }
        </Fragment>
    )
}