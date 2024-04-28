<!-- TradingViewWidget.svelte -->
<script>
    import { onMount } from "svelte";
    import Detail from "./Detail.svelte";
    import Buy from "./Buy.svelte";

    // fetch data from 
    export let data;
    const key = Object.keys(data["coinData"])[0];
    let coin = data["coinData"][key];
    console.log(data)
    let coin_dict = {
        ethereum: "ETH",
        bitcoin: "BTC",
        ripple: "XRP",
        tether: "USDT",
    };

    //key is full name of coin
    let sym = coin_dict[key];

    onMount(() => {
        const script = document.createElement("script");
        script.src =
            "https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js";
        script.async = true;
        script.innerHTML = JSON.stringify({
            autosize: false, // Set autosize to false to control size
            symbol: `CRYPTOCAP:${sym}`,
            interval: "D",
            timezone: "Etc/UTC",
            theme: "dark",
            style: "1",
            locale: "en",
            enable_publishing: false,
            allow_symbol_change: true,
            calendar: false,
            support_host: "https://www.tradingview.com",
            width: "950", // Set width
            height: "500", // Set height
        });

        document.getElementById("tradingview-widget").appendChild(script);
    });
</script>

<body class="flex flex-col">
    <div class="bg-primary h-screen">
        <div class="container mx-auto px-4 py-8">
            <!-- First row for Detail component -->
            <div class="mb-8">
                <Detail
                    name={key}
                    logo={sym}
                    usd={coin["usd"]}
                    marketCap={coin["usd_market_cap"]}
                    usd_24h_vol={coin["usd_24h_vol"]}
                />
            </div>

            <!-- Second row for TradingView widget and Buy component -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <!-- TradingView widget container -->
                <div class="md:col-span-2">
                    <div
                        id="tradingview-widget"
                        class="tradingview-widget-container__widget"
                    ></div>
                </div>

                <!-- Buy component container -->
                <div class="md:col-span-1">
                    <Buy name={key} symbol={sym} price={coin["usd"]} crypto_id={ data["coinData"]['crypto_id']} />
                </div>
            </div>
        </div>
    </div></body
>
