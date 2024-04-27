// /** @type {import('./$types').LayoutLoad} */
export async function load({ fetch, params, parent }) {
    function getCryptoIdByName(data, cryptoName) {
        const cryptoMap = new Map(
            data.map((item) => [item.name.toLowerCase(), item.crypto_id])
        );

        // Check if the lowercase crypto name exists in the map
        const lowerCaseName = cryptoName.toLowerCase();
        if (cryptoMap.has(lowerCaseName)) {
            return cryptoMap.get(lowerCaseName);
        } else {
            // Handle the case where the name is not found (optional)
            console.warn(
                `Cryptocurrency name "${cryptoName}" not found in the data.`
            );
            return null; // Or return a default value if desired
        }
    }
    //  full name data fron 
    const { coinId } = params;
    // data from aoi
    const { props } = await parent();
    const cryptoId = getCryptoIdByName(props, coinId);
    // console.log(coinId,cryptoID)
    const url = `https://api.coingecko.com/api/v3/simple/price?ids=${coinId}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true`;
    const options = {
        method: "GET",
        headers: {
            accept: "application/json",
            "x-cg-demo-api-key": "CG-6cdnYZr2LkWBLWcoNhTwtPne	",
        },
    };
    const res = await fetch(url, options);

    if (res.ok) {
        //contain price market cap
        const data = await res.json();
        data['crypto_id'] = cryptoId
        return { coinData: data }; // Use dynamic key based on coinId
    } else {
        // Handle errors, perhaps by returning an error prop, or by throwing an error to display a custom error page
        throw new Error(`Could not fetch data for coin ${coinId}`);
    }
}
