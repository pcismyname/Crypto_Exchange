<script>
    import bitcoin_img from "$lib/images/bitcoin.png";
    import etheruem_img from "$lib/images/etheruem.png";
    import usdt_img from "$lib/images/usdt.png";
    import xrp_img from "$lib/images/xrp.png";

    import Card from "../Card.svelte";

    /** @type {import('./$types').PageData} */
    export let data;
    let coins = data['props'];


    const images = {
        btc: bitcoin_img,
        eth: etheruem_img,
        usdt: usdt_img,
        xrp: xrp_img,
    };


    if (coins && coins.length > 0) {
        coins = coins.map((coin) => ({
            ...coin,
            image: images[coin.symbol],
        }));
    } else {
        console.log("Coins is undefined or empty.");
    }
    // console.log('after process')
    // console.log(coins)
</script>

<!-- <body class="flex flex-col h-dvh"> -->
<div class="bg-primary pt-5 h-full pb-40">
    <p class="text-4xl mb-10 font-bold text-base-100 text-center">Top Pick</p>
    <div
        class="flex flex-wrap bg-primary justify-center items-center gap-4"
    >
        {#each coins as coin}
            <Card
                image={coin.image}
                name={coin.name}
                coinId={coin.coinId}
                cryptoId={coin.crypto_id}
            />
        {/each}
    </div>
</div>

<!-- </body> -->
