// src/routes/top-pick/+page.js
export async function load({ fetch }) {
    const url = 'http://localhost:8002/api/v1/cryptocurrencies';
    const response = await fetch(url);
    if (response.ok) {
        const coins = await response.json();
        return { props: coins } ; 
    }
    return {
        status: response.status,
        error: new Error('Could not fetch the cryptocurrencies')
    };
}
